import uuid
from sentence_transformers import SentenceTransformer
from services.cosinus_similarity import pertinence

class vectorizer_de_text :
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def vectoriser_text(self, texte):
        return self.model.encode(texte).tolist()

    def vectoriser_liste_text(self, chunks, nom_fichier, collection):
        liste_vecteurs = [self.vectoriser_text(chunk) for chunk in chunks]
        identifiants = []
        noms_fichier = []
        
        for chunk in chunks:
            identifiants.append(str(uuid.uuid4()))
            noms_fichier.append({"nomFichier": nom_fichier})
            
        collection.add(
            ids=identifiants, 
            embeddings=liste_vecteurs,  
            documents=chunks,
            metadatas=noms_fichier
        )

    def calculer_scores_bdd(self, collection, prompt_vecteur):
        nombre_total = collection.count()
        if nombre_total == 0:
            return []

        resultats = collection.query(
            query_embeddings=[prompt_vecteur],
            n_results=nombre_total,
            include=["documents", "metadatas", "embeddings"]
        )
        
        bdd_reconstruite = []
        textes = resultats['documents'][0]
        metas = resultats['metadatas'][0]
        vecteurs_stockes = resultats['embeddings'][0]
        
        for i in range(nombre_total):
            var_pertinence = int(pertinence(prompt_vecteur, vecteurs_stockes[i]))
            
            ligne = {
                "nomFichier": metas[i]["nomFichier"],
                "texte": textes[i],
                "score": var_pertinence
            }
            bdd_reconstruite.append(ligne)
            
        return bdd_reconstruite

    def note_final_bdd(self, base_de_donnee):
        compteur_pertinence = {}
        compteur_chunk = {}
        
        for ligne in base_de_donnee:
            nom_fichier = ligne['nomFichier']
            if ligne['score'] > 55:
                compteur_pertinence[nom_fichier] = compteur_pertinence.get(nom_fichier, 0) + 1
            compteur_chunk[nom_fichier] = compteur_chunk.get(nom_fichier, 0) + 1

        for ligne in base_de_donnee:
            nom_fichier = ligne['nomFichier']
            nb_passage_pertinent = compteur_pertinence.get(nom_fichier, 0)
            facteur_boost = min(0.9, nb_passage_pertinent * 0.10)
            ligne['score'] = int(ligne['score'] + (100 - ligne['score']) * facteur_boost)
            
        base_de_donnee.sort(key=lambda x: x['score'], reverse=True)
        return base_de_donnee