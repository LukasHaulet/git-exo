def inverser_string(texte):
    texte_inverse = ""
    for lettre in texte:
        texte_inverse = lettre + texte_inverse
    return texte_inverse

print(inverser_string("nikana"))