def gardien_phare(nombre_marches, hauteur_marche):
    distance_aller = nombre_marches * hauteur_marche
    distance_aller_retour = distance_aller * 2

    distance_par_jour = distance_aller_retour * 5

    distance_par_semaine_cm = distance_par_jour * 7

    distance_par_semaine_m = distance_par_semaine_cm / 100

    print(f"Pour {nombre_marches} marche de {hauteur_marche} cm , le guardien parcourt {distance_par_semaine_m:.2f} m par semaine. ")

gardien_phare(100,20)