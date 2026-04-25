import os
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

from services.vectorizer_de_text import vectorizer_de_text
from services.pdf_parser import extraire_intelligent
from services.cosinus_similarity import pertinence
from services.chunking import fct_de_chunk

import chromadb

app = Flask(__name__)
client = chromadb.EphemeralClient()
collection = client.create_collection(name="session_active")
TEXTES_COMPLETS_GLOBAUX = {}
vdt = vectorizer_de_text()

@app.route('/')
def accueil():
    return render_template("accueil.html")

@app.route('/reset', methods=['POST'])
def reset_memoire():
    global collection, client, TEXTES_COMPLETS_GLOBAUX
    TEXTES_COMPLETS_GLOBAUX = {}
    client.delete_collection(name="session_active")
    collection = client.create_collection(name="session_active", metadata={"hnsw:space": "cosine"})
    print("Mémoire vidée !")
    return jsonify({'message': 'Mémoire vidée'})

@app.route('/analyse', methods=['POST'])
def analyse_cv():
    global collection, TEXTES_COMPLETS_GLOBAUX
    user_prompt = request.form.get('prompt', '')
    vecteur_prompt = vdt.vectoriser_text(user_prompt)
    files = request.files.getlist('cv')
    nouveaux_fichiers_traites = 0

    for file in files:
        if file.filename == '' : continue
        filename = secure_filename(file.filename)
        if filename in TEXTES_COMPLETS_GLOBAUX:
            continue
        text_extrait = extraire_intelligent(file)
        if text_extrait:
            TEXTES_COMPLETS_GLOBAUX[filename] = text_extrait
            chunks = fct_de_chunk(text_extrait, taille=30, mode="mots", tag="", overlap=5)
            vdt.vectoriser_liste_text(chunks, filename, collection)
            nouveaux_fichiers_traites += 1
        else:
            continue
    if collection.count() == 0 :
        return jsonify({'error': 'Aucun fichier en mémoire. Envoyez des CVs !'}), 400
    bdd_score = vdt.calculer_scores_bdd(collection, vecteur_prompt)
    vdt.note_final_bdd(bdd_score)
    data_pour_le_front = []
    vus = set()
    for ligne in bdd_score :
        nom = ligne['nomFichier']
        if nom not in vus:
            texte_entier = TEXTES_COMPLETS_GLOBAUX.get(nom, 'null')
            data_pour_le_front.append({
                'nom_fichier': ligne['nomFichier'],
                'meilleur_extrait': ligne['texte'],
                'pertinence': ligne['score'],
                'texte_fichier': texte_entier
            })
            vus.add(ligne['nomFichier'])

    return jsonify({
        'message': 'Analyse terminée',
        'count' : len(data_pour_le_front),
        'data' : data_pour_le_front
    })

if __name__ == '__main__':
    app.run(debug=True)