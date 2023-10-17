# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 13

calcul = 1
resultat = 0

print("Un programme qui calcule la somme de x^i allant de i=1 à n\n")
valeur = int(input("Saisir une valeur : "))
puissance = int(input("Saisir une puissance : "))

for i in range(puissance):
    calcul = 1
    for j in range(i+1):
        calcul *= valeur
    resultat += calcul
    
print("\nLe résultat est de :", resultat)