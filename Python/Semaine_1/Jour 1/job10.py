montant_initial = 20000  
taux_rendement = 5 
gain_annuel = montant_initial * (taux_rendement / 100)
print("Gain annuel initial :", gain_annuel, "€")
montant_ajuste = montant_initial + 5000
taux_ajuste = taux_rendement + 2  
gain_apres_augmentation = montant_ajuste * (taux_ajuste / 100)
print("Gain après augmentation du capital :", gain_apres_augmentation, "€")
montant_final = montant_ajuste * 0.9  
taux_final = taux_ajuste - 1          
gain_final = montant_final * (taux_final / 100)
print("Montant final de l’investissement :", montant_final, "€")
print("Gain final après retrait :", gain_final, "€")