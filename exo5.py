# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut etudiant (O/N)
- Options :
    24 billets : 66.00$
    12 billets : 36.00$
     5 billets : 15.75$
     1 billet  :  3.60$
- Reduction : si etudiant = O, appliquer 12% de reduction sur le cout des forfaits uniquement.
  Les billets unitaires ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets unitaires

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 24 billets - A
    Forfaits de 12 billets - B
    Forfaits de 5 billets - C
    Billets unitaires - D
    Total billets - T
    Prix total - PPP.PP$

    3
    1
    2

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut etudiant (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""
NA = 24
NB = 12
NC = 5
ND = 1
REDUCTION = 1 - 0.12

etudiant = False

# TODO: Lire n (int) et statut (str)
while True :
    try :
        n = int(input("Entrez le nombre de billets necessaires : "))
        if n < 0 :
            print("Erreur - donnees invalides.")
            exit()
        else :
            break
    except ValueError :
        print("Erreur - donnees invalides.")
        exit()

while True :
    choix = input("Entrez le statut etudiant (O/N) : ")
    if choix == "O" or choix == "o" :
        etudiant = True
        break
    if choix == "N" or choix == "n" :
        etudiant = False
        break
    else :
        print("Erreur - donnees invalides.")
        exit()
if etudiant :
    PA = 66.00*REDUCTION
    PB = 36.00*REDUCTION
    PC = 15.75*REDUCTION
    PD = 3.60
else :
    PA = 66.00
    PB = 36.00
    PC = 15.75
    PD = 3.60

# TODO: Validation (n >= 0 et statut dans {O, N})
# validation inclue dans les boucles 

# TODO: Chercher la meilleure combinaison (A, B, C, D)
MAX_A = (n + NA - 1) // NA

finalA = finalB = finalC = finalD = 0
finalBillets = float("inf")
finalPrix = float("inf")

for a in range(0, MAX_A + 1) :
    reste1 = max(0, n - a*NA)
    maxB = (reste1 + NB - 1) // NB 

    for b in range(0, maxB + 1) :
        reste2 = max(0, reste1 - b*NB)
        maxC = (reste2 + NC - 1) // NC
        
        for c in range(0, maxC + 1) :
            billets = a*NA + b*NB + c*NC

            # Max pour éviter une valeur négative si déjà + de billets que n
            d = max(0, n - billets)
            billets += d*ND

            prix = a*PA + b*PB + c*PC + d*PD

            if prix < finalPrix :
                finalPrix = prix
                finalA = a
                finalB = b
                finalC = c
                finalD = d   
                finalBillets = billets         
            elif prix == finalPrix :
                if billets < finalBillets :
                    finalA = a
                    finalB = b
                    finalC = c
                    finalD = d  
                    finalBillets = billets
                elif billets == finalBillets and d < finalD :
                    finalA = a
                    finalB = b
                    finalC = c
                    finalD = d

# TODO: Calculer et afficher le resultat exact (6 lignes)
print("Forfaits de 24 billets -", finalA,
      "\nForfaits de 12 billets -", finalB,
      "\nForfaits de 5 billets -", finalC,
      "\nBillets unitaires -", finalD,
      "\nTotal billets -", finalBillets)
print(f"Prix total - {finalPrix:.2f}$")
