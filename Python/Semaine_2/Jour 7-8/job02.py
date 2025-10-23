def draw_triangle(t):
    space = t
    for i in range(t):
        print(" " * space + "/" + " " * i * 2 + "\\")
        space = space - 1

    print(" " * space + "/" + "_" * t * 2 + "\\")

draw_triangle(5)