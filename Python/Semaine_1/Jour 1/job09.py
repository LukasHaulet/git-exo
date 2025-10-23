nom = "apex"
prix = 350
stock = 800
jeux  = "nom : %s, prix : %s €, stock : %s exemplaires" % (nom, prix, stock)
print (jeux)
newStock = int(input("saisir un stock"))
stock = stock+newStock
print ("Le nouveau stock est de ", stock, "exemplaires")
prix = prix + (prix * ( 10 / 100))
print (" Le nouveau prix est de ", prix, "€")
jeuxVideo  = "nom : %s, prix :%s €, stock : %s exemplaires" % (nom, prix, stock)
print (jeuxVideo)