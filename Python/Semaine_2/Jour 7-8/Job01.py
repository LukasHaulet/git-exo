def draw_rectangle(height, width):
    for i in range (height):
        for j in range(width):
            if i == 0 or i == height -1 :
                if j == 0 or j == width -1 :
                    print("|", end=' ')
                else:
                    print("-", end=' ')
            else:
                if j == 0 or j == width -1 :
                    print("|", end=' ')
                else:
                    print(" ", end=' ')
        print()

draw_rectangle(3,10)