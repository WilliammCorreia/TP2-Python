# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 12

resultat =  1

valeur = int(input("Saisir une valeur : "))
puissance = int(input("Saisir une puissance : "))

for i in range(puissance):
    resultat *= valeur
    
print("\nLe résultat est de :", resultat)