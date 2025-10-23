
def verifier_pair_impair(nombre):
    if type(nombre) != int:
        print("Ce n'est pas un nombre entier")
    elif nombre < 0:
        print("Le nombre doit être positif")
    elif nombre % 2 == 0:
        print("Le nombre", nombre, "est pair")
    else:
        print("Le nombre", nombre, "est impair")

verifier_pair_impair(10)
verifier_pair_impair(7)
verifier_pair_impair(-5)
verifier_pair_impair(3.5)
verifier_pair_impair(0)