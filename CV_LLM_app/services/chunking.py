import re

def fct_de_chunk(texte, taille=1, tag=""):
    if not texte:
        return []

    lignes_brutes = re.split(r"\r?\n+", texte.strip()) # \r?\n+ <=> n'importe quel saut de ligne (cf TP2 HAI923I)
    lignes_propres = [re.sub(r"\s+", " ", l).strip() for l in lignes_brutes if l.strip()] #enleve les espaces de trop dans chaque ligne

    resultat_final = []

    for i in range(0, len(lignes_propres), taille):
        groupe = lignes_propres[i : i + taille]
        bloc_texte = " ".join(groupe)
        
        if tag:
            bloc_texte = f"{tag} {bloc_texte}"   

        resultat_final.append(bloc_texte)

    return resultat_final
    
    # Test : Je veux des paquets de 2 lignes avec le tag [CV]

    # print(fct_de_chunk(nom_cv, taille=2, tag="[CV]"))
    

