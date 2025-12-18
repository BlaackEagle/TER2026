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
        return jsonify({'reponse': "Je n'ai pas compris la question."}), 400
        
    if not MEMOIRE_CVS:
        return jsonify({'reponse': "Aucun CV n'est chargé. Veuillez uploader des documents d'abord."}), 400

    vecteur_question = vectoriser_text(question)

    meilleur_score = -1
    meilleur_cv = None

    for cv in MEMOIRE_CVS:
        score = cosine_similarity([vecteur_question], [cv['vecteur']])[0][0]
        if score > meilleur_score:
            meilleur_score = score
            meilleur_cv = cv

    if meilleur_score < 0.2:
        return jsonify({
            'reponse': "Désolé, je ne trouve pas d'information pertinente dans les CVs pour cette question.",
            'source': None
        })

    
    reponse_systeme = f"J'ai trouvé une réponse pertinente dans le fichier **{meilleur_cv['nom_fichier']}** (Pertinence: {meilleur_score:.2f})."
    
    return jsonify({
        'reponse': reponse_systeme,
        'extrait': meilleur_cv['texte'][:500] + "...", 
        'source': meilleur_cv['nom_fichier']
    })



if __name__ == '__main__':
    app.run(debug=True)