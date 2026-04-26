# ProjetTER-S6_2026


## Analyse de CV LLM


Pour récupérer le projet, et que tout s'execute correctement, suivre ces étapes : 


## 1 - Cloner le projet
(git clone git@gitlab.etu.umontpellier.fr:e20200004120/projetter-s6_2026.git)

## 2 - Activer l'environnement virtuel (venv) : 


### Sur Windows

python -m venv venv  


venv\Scripts\activate  

Si cette commande passe pas, c'est peut etre car l’exécution de scripts est désactivée sur votre système dans ce cas taper cette commande avant:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process


### Sur Linux
python3 -m venv venv  

source venv/bin/activate  


## 3 - Installer les dépendances
pip install -r requirements.txt

## 4 - Lancer l'app
python CV_LLM_app/app.py

### PS : Quand vous ajoutez des dépendances (après un pip install+import d'une libraire faites les commandes suivantes)

pip freeze > requirements.txt

### Utiliser le générateur de cv

## 1 - Prérequis
Il faut la commande "pdflatex" pour utiliser le générateur
Pour l'installer via Windows : https://miktex.org/download (lancer l'exécuteur)
Pour l'installer via Linux :   sudo apt install texlive-base (commande terminal)
Pour l'installer via MacOS :   https://www.tug.org/mactex/morepackages.html (BasicTeX.pkg)

## 2 - Commande pour l'utiliser

python .\CV_LLM_app\services\data_generator.py

ou bien avec l'option --nb (pour le nombre de cv) et --type (pour le type btp,dev...)
utiliser -h pour voir tous les types disponibles

python .\CV_LLM_app\services\data_generator.py --nb 10 --type dev

*en gros c'est juste pour que je puisse récupérer vos ajouts vu que je travail sur ma machine personel*



