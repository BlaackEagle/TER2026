import os
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

from services.pdf_parser import extraire_intelligent
from services.vectorizer_de_text import vectoriser_text
from services.cosinus_similarity import pertinence

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
    files = request.files.getlist('cv')
    vecteur_prompt = vectoriser_text(user_prompt)
    stockés = 0
    text_extrait = ""
    liste_donne_cv = list()
    for file in files:

        if file.filename == '':
            continue

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        stockés += 1
        text_extrait = extraire_intelligent(file_path)
        if text_extrait :
            vecteur_texte = vectoriser_text(text_extrait)
            score_de_pertinence = int(pertinence(vecteur_prompt, vecteur_texte))
            fichier_CV = {
                'texte' : text_extrait,
                'nom_fichier' : filename,
                'texte_fichier' : text_extrait,
                'vecteur' : vecteur_texte.tolist(),
                'forme_vecteur' : list(vecteur_texte.shape),
                'pertinence' : score_de_pertinence
            }
            liste_donne_cv.append(fichier_CV)
        else :
            print("Le parser ne récupère aucun texte")

    return jsonify({
        'message': 'Succès',
        'count': stockés,
        'info': f'{stockés} fichier stocké!',
        'prompt' : user_prompt,
        'data' : liste_donne_cv
    })



if __name__ == '__main__':
    app.run(debug=True)