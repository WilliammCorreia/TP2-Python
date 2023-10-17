# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 11

quotient = 0

valeur = int(input("Saisir la valeur à diviser : "))
diviseur = int(input("Saisir le diviseur : "))

while(valeur > diviseur):
    valeur -= diviseur
    quotient += 1
    

print(f"\nLe résultat de la division est : {quotient:d}, avec un reste de {valeur:d}")