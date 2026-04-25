from sentence_transformers import SentenceTransformer
from services.cosinus_similarity import pertinence
import chromadb
import uuid

model = SentenceTransformer('all-MiniLM-L6-v2')


def vectoriser_text(texte) :
    vecteur_cv = model.encode(texte)
    return vecteur_cv

def vectoriser_liste_text(chunks, nom_fichier, base_de_donnees) :
    liste_vecteurs = [vectoriser_text(chunk) for chunk in chunks]
    identifiants = list()
    noms_fichier = list()
    textes = list()
    for chunk, vecteur in zip(chunks, liste_vecteurs) :
        identifiants.append(str(uuid.uuid4()))
        noms_fichier.append({"nomFichier" : nom_fichier})
        textes.append(chunk)
    base_de_donnees.add(
        ids = identifiants, 
        embeddings = liste_vecteurs,  
        documents = textes,
        metadatas = noms_fichier,

    )
    return base_de_donnees

def calculer_scores_bdd(collection, prompt_vecteur):
    nombre_total = collection.count()
    resultats = collection.query(
        query_embeddings=[prompt_vecteur],
        n_results=nombre_total 
    )
    
    bdd = []
    textes = resultats['documents'][0]
    metas = resultats['metadatas'][0]
    distances = resultats['distances'][0]

    for i in range(nombre_total):
        score = int((1 - distances[i]) * 100)
        
        ligne = {
            "nomFichier": metas[i]["nomFichier"],
            "texte": textes[i],
            "score": max(0, score) 
        }
        bdd.append(ligne)
        
    return bdd

def note_final_bdd(base_de_donnee) :
    compteur_pertinence = {}
    compteur_chunk = {}
    for ligne in base_de_donnee :
        nom_fichier = ligne['nomFichier']
        if ligne['score'] > 50 :
            compteur_pertinence[nom_fichier] = compteur_pertinence.get(nom_fichier, 0) + 1
        compteur_chunk[nom_fichier] = compteur_chunk.get(nom_fichier, 0) + 1

    for ligne in base_de_donnee :
        nom_fichier = ligne['nomFichier']
        nb_passage_pertinent = compteur_pertinence.get(nom_fichier, 0)
        #nb_passage = compteur_chunk.get(nom_fichier, 0)
        facteur_boost = min(0.9, nb_passage_pertinent*0.10)
        ligne['score'] = ligne['score'] + (100 - ligne['score']) * facteur_boost
    base_de_donnee.sort(key=lambda x : x['score'], reverse = True)