import numpy as np
import matplotlib.pyplot as plt

# Configuration des données
L = np.arange(1, 81)
# Formule pour la longueur des phrases (English corpus) [cite: 252, 263]
f_exp = 1.1 * L * (0.90 ** L)
cdf = np.cumsum(f_exp)

# Paramètres de visibilité (ajustés pour LaTeX)
limit = 40
coverage = cdf[limit-1]

# On augmente globalement la taille des polices
plt.rcParams.update({
    "font.family": "serif",
    "axes.titlesize": 18,    # Titres plus imposants
    "axes.labelsize": 14,    # Labels d'axes clairs
    "xtick.labelsize": 12,   # Chiffres des axes
    "ytick.labelsize": 12,
    "legend.fontsize": 12,
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7)) # Figure plus large

# --- PLOT 1 : Distribution de masse (Discrete) ---
ax1.bar(L, f_exp, color='#4A90E2', alpha=0.7, edgecolor='#2A5D9E', linewidth=0.8)
ax1.axvline(x=limit, color='#D0021B', linestyle='--', lw=2.5, label=f'Limite Chunk ({limit} mots)')

ax1.set_title("Fréquence par longueur exacte", pad=20)
ax1.set_xlabel("Longueur de la phrase L (mots)")
ax1.set_ylabel("Fréquence d'apparition (%)")
ax1.grid(True, axis='y', linestyle=':', alpha=0.6)
ax1.legend(loc='upper right', frameon=True, fontsize=13)

# --- PLOT 2 : Fonction de répartition (Step plot) ---
ax2.step(L, cdf, where='mid', color='#F5A623', lw=3) # Trait plus épais
ax2.fill_between(L, cdf, step="mid", color='#F5A623', alpha=0.15)

# Annotation de couverture massive et claire
ax2.scatter(limit, coverage, color='#D0021B', s=100, zorder=5) # Point plus gros
ax2.annotate(f'COUVERTURE : {coverage:.1f}%\nà L = {limit} mots', 
             xy=(limit, coverage), 
             xytext=(limit-5, coverage-25), # Positionnée pour ne pas être coupée
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", color='black', lw=1.5),
             fontsize=16,          # Taille augmentée significativement
             fontweight='bold', 
             color='#D0021B',
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#D0021B", alpha=0.8))

ax2.axvline(x=limit, color='#D0021B', linestyle='--', lw=2, alpha=0.5)

ax2.set_title("Probabilité cumulée (Répartition)", pad=20)
ax2.set_xlabel("Longueur de la phrase L (mots)")
ax2.set_ylabel("Pourcentage cumulé du corpus (%)")
ax2.set_ylim(0, 105)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout(pad=3.0) # Plus d'espace entre les subplots
plt.show()