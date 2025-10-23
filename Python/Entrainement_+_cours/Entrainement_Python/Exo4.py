Nbr = int(input("Entrer un nombre: "))
rev = 0
  
while Nbr > 0 :
  rev = rev * 10 
  rev = rev + Nbr%10 
  Nbr = Nbr//10
print("Le nombre inversé est",rev)
