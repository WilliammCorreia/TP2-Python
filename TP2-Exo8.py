# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 8

valeur = []

n = int(input("Saisir le nombre de valeurs à saisir :\n"))

for i in range(n): 
    valeur.append(int(input(f"Saisir la valeur '{i+1}' : ")))

resultat = sum(valeur) /n 

print("La moyenne des valeurs est égale à : ", resultat)