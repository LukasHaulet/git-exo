L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
nouvelle_liste =[]

for nbr in L:
    existe = False
    for element in nouvelle_liste:
        if element == nbr:
            existe = True 
    if existe == False:
        nouvelle_liste.append(nbr)

print(nouvelle_liste)