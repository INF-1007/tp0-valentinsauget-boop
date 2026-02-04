# Exercice 02 – Ambiance autour du stade (sections A a H) (gabarit)
"""
Objectif :
- Lire 8 entiers (un par ligne) : personnes dans les sections A, B, C, D, E, F, G, H (dans cet ordre)
- Valider : chaque valeur est un entier >= 0
    -> sinon afficher EXACTEMENT : "Erreur - donnees invalides."
- Calculer l'intensite brute par section : intensite = personnes * facteur
- Normaliser sur 0..10 avec un arrondi half-up :
    - maxI = max(intensites)
    - si maxI == 0 : niveaux = [0]*8
    - sinon : niveau = int((intensite / maxI) * 10 + 0.5), borne dans [0,10]
- Afficher une grille verticale :
    - lignes 10 a 1
    - colonnes A a H
    - afficher "❚" si niveau_section >= niveau_ligne sinon "."
    - un espace entre chaque cellule
    - format de ligne : "{ligne:2} | <8 cellules>"
    - derniere ligne : "     A B C D E F G H"
"""

FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]

n = 8
personnes = []
# TODO: Lire 8 entiers (un par ligne) dans une liste personnes
#       En cas d'erreur de conversion ou valeur negative -> afficher le message d'erreur et quitter

i = 0
print("Entrer le nombre de spectateurs selon la section")
while i < n :
    try :
        value = int(input(chr(65 + i) + " : "))
        if value < 0 :
            print("Erreur - donnees invalides.")
            exit()
        else :
            personnes.append(value)
            i += 1
    except ValueError :
        print("Erreur - donnees invalides.")
        exit()

# TODO: Calculer les intensites brutes (liste de 8 floats)
intensite = []

for i in range(n) :
    intensite.append(float(personnes[i]) * FACTEURS[i])
    
# TODO: Calculer les niveaux normalisés (liste de 8 entiers dans [0,10])
niveaux = []

maxI = max(intensite)

if(maxI == 0) : niveaux = [0]*8
else :
    for i in range(n) :
        niveaux.append(int((intensite[i] / maxI) * 10 + 0.5))

# TODO: Afficher la grille (10 lignes) puis la ligne des labels
lgn = 10 
col = n

for i in range(lgn, 0, -1) :
    print(f"{i:2} | ", end = "")
    for j in range(col) :
        if(niveaux[j] >= i) : print("❚", end = " ")
        else : print(".", end = " ")
    print("\n", end = "")
    
print(" " * 5, end = "")
for i in range(col) : print(chr(65 + i), end = " ")
