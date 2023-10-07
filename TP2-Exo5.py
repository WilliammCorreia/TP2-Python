# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 5

print("Choisir l'opérateur :")
print("1) + ")
print("2) - ")
print("3) * ")
print("4) / ")

operateur = int(input(""))

valeur = []

valeur.append(int(input('Insérer un premier nombre : ')))
valeur.append(int(input('Insérer un premier nombre : ')))

if( operateur == 1 ):
    valeur.append( valeur[0] + valeur[1] )
    print(f"Le résultat de {valeur[0]:d} + {valeur[1]:d} est de {valeur[2]:d}")
elif( operateur == 2 ):
    valeur.append( valeur[0] - valeur[1] )
    print(f"Le résultat de {valeur[0]:d} - {valeur[1]:d} est de {valeur[2]:d}")
elif( operateur == 3 ):
    valeur.append( valeur[0] * valeur[1] )
    print(f"Le résultat de {valeur[0]:d} * {valeur[1]:d} est de {valeur[2]:d}")
elif( operateur == 4 ):
    valeur.append( valeur[0] / valeur[1] )
    print(f"Le résultat de {valeur[0]:d} / {valeur[1]:d} est de {valeur[2]:d}")