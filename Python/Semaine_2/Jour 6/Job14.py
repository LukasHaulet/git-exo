def my_long_word(n, phrase):
    mots = phrase.split()
    resultat = ""

    for mot in mots:
        compteur = 0
        for lettre in mot:
            compteur = compteur + 1

        if compteur > n:
            resultat = resultat + mot + " "

    return resultat

texte = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, texte))