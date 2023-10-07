# CORREIA William Bachelor 2 Groupe 3 - TP2 Exercice 6

menu = 0

while( menu != 4):
    print("**** Menu ****")
    print("1 - Version A")
    print("2 - Version B")
    print("3 - Version C")
    print("4 - Quitter\n")
    menu = int(input())

    if( menu == 1 ):
        a = int(input("\nSaisir la valeur de a : "))
        b = int(input("Saisir la valeur de b : "))
        c = int(input("Saisir la valeur de c : "))

        if( a == 0 ):
            print("\nCette équation n'est pas une équation du second degrés.\n")
        else:
            resultat = (b*b) - (4*a*c)
            print(f"\nLe résultat de cette équation est : {resultat:d}\n")

    if( menu == 2 ):
        a = int(input("\nSaisir la valeur de a : "))
        b = int(input("Saisir la valeur de b : "))
        c = int(input("Saisir la valeur de c : "))

        while( a == 0 ):
            print("\nLa valeur de 'a' ne peut pas être '0'\n")
            a = int(input("Saisir la valeur de a : "))

        resultat = (b*b) - (4*a*c)
        print(f"\nLe résultat de cette équation est : {resultat:d}\n")
        
    if( menu == 3 ):
        a = int(input("\nSaisir la valeur de a : "))
        b = int(input("Saisir la valeur de b : "))
        c = int(input("Saisir la valeur de c : "))

        resultat = (b*b) - (4*a*c)
        print(f"\nLe résultat de cette équation est : {resultat:d}\n")