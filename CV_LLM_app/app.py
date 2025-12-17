import os
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

from services.pdf_parser import extraire_intelligent
from services.pdf_parser import extraire_text_pdf


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
    stockés = 0
    text_extrait = ""
    for file in files:
        if file.filename == '':
            continue

        filename = secure_filename(file.filename)
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            file.save(file_path)
            stockés += 1
            text_extrait += extraire_intelligent(file_path)

            if text_extrait :
                txt_path = file_path.replace('.pdf', '.txt')
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write(text_extrait)
            else :
                print("Le pareser ne récupère aucun texte")

        except Exception as e:
            print(f"Erreur lors de la sauvegarde de {filename}: {e}")

    return jsonify({
        'message': 'Succès',
        'count': stockés,
        'info': f'{stockés} fichier stocké!',
        'text_extrait' : text_extrait
    })
if __name__ == '__main__':
    app.run(debug=True)