liste = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
long = len(liste)

somp = 0
for i in range (long) :
    if liste[i] %2 == 0:
        somp = somp + liste[i]
print("Somme des valeurs paires : ", somp)