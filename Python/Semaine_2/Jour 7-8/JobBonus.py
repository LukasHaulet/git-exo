def my_sort(liste):
    
    nombre_coups = 0

    
    n = len(liste)

    for i in range(n):

        for j in range(n - i - 1):
           
            if liste[j] > liste[j + 1]:
               
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                
                nombre_coups += 1

    print(f"Nombre total de coups : {nombre_coups}")

    return liste

ma_liste = [64, 34, 25, 12, 22, 11, 90]
print("Liste avant tri : ", ma_liste)
liste_triee = my_sort(ma_liste)
print("liste apres tri : ", liste_triee)