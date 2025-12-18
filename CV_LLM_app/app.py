import os
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
from services.pdf_parser import extraire_intelligent
from services.vectorizer_de_text import vectoriser_text
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MEMOIRE_CVS = []

@app.route('/')
def accueil():
    return render_template("accueil.html")



@app.route('/analyse', methods=['POST'])
def analyse_cv():
    
    global MEMOIRE_CVS
    MEMOIRE_CVS = []

    if 'cv' not in request.files:
        return jsonify({'error': 'Aucun fichier envoyé', 'info': 'Erreur: Pas de fichier'}), 400

    files = request.files.getlist('cv')
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
            fichier_CV = {
                'texte' : text_extrait,
                'nom_fichier' : filename,
                'texte_fichier' : text_extrait,
                'vecteur' : vecteur_texte.tolist(),
                'forme_vecteur' : list(vecteur_texte.shape)
            }
            liste_donne_cv.append(fichier_CV)
            MEMOIRE_CVS.append(fichier_CV)
        else :
            print("Le parser ne récupère aucun texte")

    return jsonify({
        'message': 'Succès',
        'count': stockés,
        'info': f'{stockés} fichier stocké!',
        'data' : liste_donne_cv
    })

@app.route('/chat', methods=['POST'])
def chat_avec_cv():
    data = request.json
    question = data.get('prompt')
    
    if not question:
        return jsonify({'reponse': "pas de question recu"}), 400
        
    
    vecteur_question = vectoriser_text(question)

    
    return jsonify({
        'reponse': "vecteur genere avec succès",
        'extrait': None, 
        'source': None,
        'prompt_utilisateur': question,   
        'vecteur_prompt': vecteur_question.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)