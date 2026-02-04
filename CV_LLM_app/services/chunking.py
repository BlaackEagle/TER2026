import re

def fct_de_chunk(texte, taille=50, mode="mots", tag=""):
    if not texte:
        return []

    elements = []

    if mode == "lignes":
        # on coupe aux sauts de ligne
        lignes_brutes = re.split(r"\r?\n+", texte.strip())
        elements = [re.sub(r"\s+", " ", l).strip() for l in lignes_brutes if l.strip()]
    elif mode == "mots":
        # on coupe à chaque espace
        elements = texte.split()
    else:
        print(f"Mode '{mode}' inconnu, passage en mode mots par défaut")
        elements = texte.split()

    resultat_final = []    

    for i in range(0, len(elements), taille):
        groupe = elements[i : i + taille]
        #espaces pour coller les mots
        bloc_texte = " ".join(groupe)
        
        if tag:
            bloc_texte = f"{tag} {bloc_texte}"   

        resultat_final.append(bloc_texte)

    return resultat_final  