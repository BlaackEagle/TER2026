import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def tracer_influence_chunk_points(cibles_rouges, fichiers_csv, labels_tailles):
    dfs = []
    
    # 1. Chargement des données
    for fichier, taille in zip(fichiers_csv, labels_tailles):
        df = pd.read_csv(fichier)
        df['Taille_Chunk'] = taille
        
        def assigner_categorie(nom_fichier):
            if nom_fichier in cibles_rouges:
                return nom_fichier.split('_')[-1].replace('.pdf', '')
            return "Autres profils (Bruit)"
        
        df['Catégorie'] = df['nom_fichier'].apply(assigner_categorie)
        dfs.append(df)
        
    df_final = pd.concat(dfs, ignore_index=True)
    
    # 2. Configuration esthétique
    plt.figure(figsize=(12, 7))
    sns.set_theme(style="whitegrid")
    
    # Création de la palette de couleurs
    noms_cibles = [nom.split('_')[-1].replace('.pdf', '') for nom in cibles_rouges]
    couleurs_vives = sns.color_palette("Set1", len(cibles_rouges))
    palette_couleurs = {nom: couleur for nom, couleur in zip(noms_cibles, couleurs_vives)}
    
    # 3. Traçage en deux étapes pour bien gérer les calques
    
    # A. La masse du "bruit" : on la rend plus sombre et bien visible
    df_bruit = df_final[df_final['Catégorie'] == "Autres profils (Bruit)"]
    sns.swarmplot(data=df_bruit, x="Taille_Chunk", y="score", color="#5c6a79", 
                  alpha=0.85, size=6)
    
    # B. Les cibles par-dessus : gros points, avec bordure noire (edgecolor) pour contraster
    df_cibles = df_final[df_final['Catégorie'] != "Autres profils (Bruit)"]
    sns.swarmplot(data=df_cibles, x="Taille_Chunk", y="score", hue="Catégorie", 
                  palette=palette_couleurs, size=10, alpha=1.0, 
                  linewidth=1.5, edgecolor="black")
    
    # 4. Finitions
    plt.title("Distribution des scores BTP vs Bruit selon la taille de l'overlap", fontsize=16, fontweight='bold')
    plt.xlabel("Hyper-paramètre : Taille de l'overlap (en mots)", fontsize=13)
    plt.ylabel("Score de pertinence final (%)", fontsize=13)
    
    # Nettoyage de la légende (pour ne pas avoir les points en double)
    handles, labels = plt.gca().get_legend_handles_labels()
    # On ajoute manuellement le "bruit" à la légende si besoin, ou on garde juste les cibles
    plt.legend(handles=handles, labels=labels, title="Profils BTP (Cibles)", 
               bbox_to_anchor=(1.02, 1), loc='upper left')
    
    plt.tight_layout()
    plt.savefig("distribution_overlap.png", dpi=300, bbox_inches='tight')
    print("Graphique sauvegardé : distribution_overlap.png")

# --- EXÉCUTION ---
mes_5_cibles = [
    "CV_ChefdeChantier_Clement.pdf", 
    "CV_ChefdeChantier_Fontaine.pdf", 
    "CV_ConducteurdeTravauxPrincipal_Roux.pdf", 
    "CV_DirecteurdeProjetConstruction_Petit.pdf", 
    "CV_DirecteurdeProjetConstruction_Lefebvre.pdf"
]

mes_fichiers_csv = [
    "resultats_1.csv", 
    "resultats_3.csv", 
    "resultats_5.csv", 
    "resultats_7.csv",
    "resultats_10.csv"
]

mes_labels = ["1 mot", "3 mots", "5 mots", "7 mots", "10 mots"]

tracer_influence_chunk_points(mes_5_cibles, mes_fichiers_csv, mes_labels)