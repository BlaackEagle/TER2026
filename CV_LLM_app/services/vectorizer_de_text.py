from sentence_transformers import SentenceTransformer


model = SentenceTransformer('all-MiniLM-L6-v2')


def vectoriser_text(texte) :
    vecteur_cv = model.encode(texte)
    return vecteur_cv

