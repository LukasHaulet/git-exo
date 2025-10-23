a = float(input("Entre la longueur a : "))
b = float(input("Entre la longueur b : "))
c = float(input("Entre la longueur c : "))

# On vérifie si on peut former un triangle
if a + b > c and a + c > b and b + c > a:
    print("C'est un triangle possible !")

    # On vérifie si c'est un triangle équilatéral
    if a == b and b == c:
        print("Le triangle est équilatéral.")

    # On vérifie si c'est un triangle isocèle
    elif a == b or a == c or b == c:
        print("Le triangle est isocèle.")

        # On regarde aussi si c’est rectangle
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Et il est aussi rectangle !")

    # On vérifie si c'est un triangle rectangle (seul)
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Le triangle est rectangle.")

    # Sinon, c’est un triangle quelconque
    else:
        print("Le triangle est quelconque.")

else:
    print("Ce n'est pas un triangle possible.")