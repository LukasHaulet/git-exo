def chiffrer_cesar(message, decalage):  
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()
    resultat = ''

    for lettre in message:
        if lettre in alphabet:
            resultat += alphabet[(alphabet.index(lettre) + decalage) % 26]
        else:
            resultat += lettre

    return resultat

message = input("Donner un message : ")
key = int(input("Donner un nombre de décalage : "))
print("Messsage chiffré :", chiffrer_cesar(message, key))
