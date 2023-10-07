# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 4

annee = int(input("Inserer une année : "))

if(annee % 4 == 0):
    if(annee % 100 == 0):
        if(annee % 400 == 0):
            print(f"L'année {annee:d} est bissextile.")
        else:
            print(f"L'année {annee:d} n'est pas bissextile.")
    else:
        print(f"L'année {annee:d} n'est pas bissextile.")
else:
    print(f"L'année {annee:d} est bissextile.")