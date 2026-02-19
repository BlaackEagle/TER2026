from transformers import AutoTokenizer

def fct_de_chunk(texte, taille=50, tag="", modele_name="sentence-transformers/all-MiniLM-L6-v2"):
    if not texte:
        return []

    # 1. Charger le tokenizer du modèle MiniLM
    tokenizer = AutoTokenizer.from_pretrained(modele_name)
    
    # 2. Transformer le texte en tokens (IDs numériques)
    # On désactive l'ajout des tokens spéciaux [CLS] et [SEP] ici pour le découpage
    tokens = tokenizer.encode(texte, add_special_tokens=False)
    
    resultat_final = []    

    # 3. Découper la liste d'IDs selon la taille souhaitée
    for i in range(0, len(tokens), taille):
        groupe_tokens = tokens[i : i + taille]
        
        # 4. Reconvertir les IDs en texte lisible
        bloc_texte = tokenizer.decode(groupe_tokens, skip_special_tokens=True)
        
        if tag:
            bloc_texte = f"{tag} {bloc_texte}"   

        resultat_final.append(bloc_texte)

    return resultat_final