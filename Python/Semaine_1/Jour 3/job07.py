chaine = "abcdefghijklmnopqrstuvwxyz" * 10
position = 0

for ligne in range (1, 100):
    fin = position + ligne 

    if fin > len(chaine):
        break 
    
    print(chaine[position:fin])
    position = fin  