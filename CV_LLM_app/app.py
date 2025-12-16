import os
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'base_de_donnees_cv'

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
    
    for file in files:
        if file.filename == '':
            continue

        filename = secure_filename(file.filename)
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            file.save(file_path)
            stockés += 1
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de {filename}: {e}")

    return jsonify({
        'message': 'Succès',
        'count': stockés,
        'info': f'{stockés} fichier stocké!'
    })
if __name__ == '__main__':
    app.run(debug=True)