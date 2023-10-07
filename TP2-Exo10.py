# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 10

resultat = 0

print("Saisir deux valeurs à multiplier :")
a = int(input())
b = int(input())

for i in range(a):
    resultat += b

print(f"\nLe résultat de la multiplication est : {resultat:d}")