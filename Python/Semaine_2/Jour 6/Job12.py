L = [ 68, 32, 23, 11, 21, 10, 99]

for i in range (7):
    for o in range (7):
        if L[i] < L[o]:
            temp = L[i]
            L[i] = L[o]
            L[o] = temp

print(L)