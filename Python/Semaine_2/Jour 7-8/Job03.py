def tapis(n):
    #Bord superieure
    print("+" + "-" * (n + 1) + "+")

    for i in range (n + 1):
        ligne = "|"
        for j in range(n + 1):
            if j == n - i:
                ligne += " "
            else:
                ligne += "#"
        ligne += "|"
        print(ligne)

    print("+" + "-" * (n + 1) + "+")

# Expmple d'utilisation 
tapis(10)
