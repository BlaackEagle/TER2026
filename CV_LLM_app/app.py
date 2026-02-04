import os
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

from services.pdf_parser import extraire_intelligent
from services.vectorizer_de_text import vectoriser_text
from services.cosinus_similarity import pertinence
from services.chunking import fct_de_chunk

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def accueil():
    return render_template("accueil.html")


@app.route('/analyse', methods=['POST'])
def analyse_cv():

    if 'cv' not in request.files:
        return jsonify({'error': 'Aucun fichier envoyé', 'info': 'Erreur: Pas de fichier'}), 400

    files = request.files.getlist('cv')
    user_prompt = request.form.get('prompt', '')
    print(f"Prompt reçu : {user_prompt}")

    vecteur_prompt = vectoriser_text(user_prompt)

    liste_donne_cv = list()

    for file in files:
        if file.filename == '': continue

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        text_extrait = extraire_intelligent(file_path)
        
        if text_extrait:
            # DEBUT CHUNKING
            chunks = fct_de_chunk(text_extrait, taille=40, mode="mots", tag="[CV]")
            print(f"--> {filename} : {len(chunks)} chunks obtenus(mots)")

            meilleur_score = -1
            meilleur_passage = ""
            
            # On teste tt les morceaux et on retourne le meilleur
            for chunk in chunks:
                vecteur_chunk = vectoriser_text(chunk)
                score_chunk = int(pertinence(vecteur_prompt, vecteur_chunk))
                
                if score_chunk > meilleur_score:
                    meilleur_score = score_chunk
                    meilleur_passage = chunk

            print(f"--> {filename} Score Max : {meilleur_score}%")
            
            fichier_CV = {
                'nom_fichier': filename,
                'texte_fichier': text_extrait,     
                'meilleur_extrait': meilleur_passage, 
                'pertinence': meilleur_score       
            }

            liste_donne_cv.append(fichier_CV)
        else:
            print(f"Erreur extraction pour {filename}")

    return jsonify({
        'message': 'Analyse terminée',
        'count': len(liste_donne_cv),
        'data': liste_donne_cv
    })


if __name__ == '__main__':
    app.run(debug=True)