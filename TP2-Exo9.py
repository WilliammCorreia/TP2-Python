# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 9

valeur = []
minimum = 0

n = int(input("Saisir le nombre de valeurs à saisir :\n"))

valeur.append(int(input(f"\nSaisir la valeur '{1}' : ")))

minimum = valeur[0]

for i in range(n-1): 
    valeur.append(int(input(f"\nSaisir la valeur '{i+2}' : ")))

    if( valeur[i+1] < minimum ):
        minimum = valeur[i+1]


print("\nLa valeur la plus basse est égale à : ", minimum)