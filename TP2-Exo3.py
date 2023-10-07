# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 3

valeur = []

valeur.append(int(input("Inserer une première valeur : ")))
valeur.append(int(input("Inserer une deuxième valeur : ")))
valeur.append(int(input("Inserer une troisième valeur : ")))

if(valeur[0] > valeur[1]):
    if(valeur[0] > valeur[2]):
        print("La valeur",valeur[0],"est la plus grande")
    else:
        print("La valeur",valeur[2],"est la plus grande")
else:
    if(valeur[1] > valeur [2]):
        print("La valeur",valeur[1],"est la plus grande")
    else:
        print("La valeur",valeur[2],"est la plus grande")
