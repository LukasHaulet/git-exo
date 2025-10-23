L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

for i in range (9):
    entier = int(L[i])
    decimal = L[i] - entier

    if decimal >= 0.5:
        L[i] = entier + 1
    else:
        L[i] = entier 
        
for i in range (9):
    for o in range (9):
        if L[i] < L[o]:
            temp = L[i]
            L[i] = L[o]
            L[o] = temp

print(L)