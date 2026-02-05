from sentence_transformers import SentenceTransformer
from services.cosinus_similarity import pertinence

model = SentenceTransformer('all-MiniLM-L6-v2')


def vectoriser_text(texte) :
    vecteur_cv = model.encode(texte)
    return vecteur_cv

def vectoriser_liste_text(chunks, nom_fichier, base_de_donnees) :
    liste_vecteurs = [vectoriser_text(chunk) for chunk in chunks]
    for chunk, vecteur in zip(chunks, liste_vecteurs) :
        donnee = {
            "nomFichier" : nom_fichier,
            "texte" : chunk,
            "vecteur" : vecteur
        }
        base_de_donnees.append(donnee)
    return base_de_donnees

def calculer_scores_bdd(base_de_donnee, prompt_vecteur) :
    for ligne in base_de_donnee :
        ligne['score'] = int(pertinence(prompt_vecteur, ligne['vecteur']))
    base_de_donnee.sort(key=lambda x : x['score'], reverse = True)

def filtrer_meilleurs_resultats(base_triee):
    resultats_finaux = []
    fichiers_vus = set()

    for ligne in base_triee:
        nom = ligne['nomFichier']

        if nom not in fichiers_vus:
            resultat_propre = {
                'nom_fichier': nom,
                'meilleur_extrait': ligne['texte'],
                'pertinence': ligne['score']
            }
            resultats_finaux.append(resultat_propre)
            fichiers_vus.add(nom)

    return resultats_finaux