# Modules necessaire
import time
import random
# Couleur qui affiche le plateau et TIC TAC TOE 
ROUGE = "\033[91m"
BLEU = "\033[94m"
VERT = "\033[92m"
JAUNE = "\033[93m"
RESET = "\033[0m"
GRAS = "\033[1m"

# Variables du jeu
case_vide = " "
plateau = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
joueur_actuel = "X"
niveau_difficulte = 1  # Variable pour le niveau de difficulté

def afficher_plateau():
    print("\n ———+———+———")
    print("| " + ROUGE + plateau[0] + RESET + " | " + ROUGE + plateau[1] + RESET + " | " + ROUGE + plateau[2] + RESET + " |")
    print(" ———+———+———")
    print("| " + ROUGE + plateau[3] + RESET + " | " + ROUGE + plateau[4] + RESET + " | " + ROUGE + plateau[5] + RESET + " |")
    print(" ———+———+———")
    print("| " + ROUGE + plateau[6] + RESET + " | " + ROUGE + plateau[7] + RESET + " | " + ROUGE + plateau[8] + RESET + " |")
    print(" ———+———+———\n")
   
   #fonction si un joueur a win 
def verifier_victoire():
   # verifier les ligne vertical
    if plateau[0] == plateau[1] == plateau[2] != " ":
        return True
    if plateau[3] == plateau[4] == plateau[5] != " ":
        return True 
    if plateau[6] == plateau[7] == plateau[8] != " ":
        return True 
    
  # verifier les ligne horizontal
    if plateau[0] == plateau[3] == plateau[6] != " ":
        return True
    if plateau[1] == plateau[4] == plateau[7] != " ":
        return True 
    if plateau[2] == plateau[5] == plateau[8] != " ":
        return True 
  # verifier les diagonales 
    if plateau[0] == plateau[4] == plateau[8] != " ":
        return True 
    if plateau[2] == plateau[4] == plateau[6] != " ":
        return True 
    
    return False 

def verifier_match_nul():
    for case in plateau:
        if case == " ":
            return False 
    return True 


########  DEBUT BOT IA AVEC MINIMAX #######

def est_gagnant(plateau, signe):
    """Verifie si un joueur a gagne"""
    # Lignes horizontales
    if plateau[0] == plateau[1] == plateau[2] == signe:
        return True
    if plateau[3] == plateau[4] == plateau[5] == signe:
        return True
    if plateau[6] == plateau[7] == plateau[8] == signe:
        return True
    
    # Lignes verticales
    if plateau[0] == plateau[3] == plateau[6] == signe:
        return True
    if plateau[1] == plateau[4] == plateau[7] == signe:
        return True
    if plateau[2] == plateau[5] == plateau[8] == signe:
        return True
    
    # Diagonales
    if plateau[0] == plateau[4] == plateau[8] == signe:
        return True
    if plateau[2] == plateau[4] == plateau[6] == signe:
        return True
    
    return False


def plateau_plein(plateau):
    """Verifie si toutes les cases sont prises"""
    for case in plateau:
        if case == " ":
            return False
    return True


def minimax(plateau, profondeur, tour_ia, signe_ia, signe_humain, prof_max):
    """
    Algorithme qui calcule le meilleur coup possible
    - Plus le score est eleve, mieux c'est pour l'IA
    - Plus le score est bas, mieux c'est pour l'humain
    """
    
    # L'IA a gagne = bon pour elle
    if est_gagnant(plateau, signe_ia):
        return 10 - profondeur
    
    # L'humain a gagne = mauvais pour l'IA
    if est_gagnant(plateau, signe_humain):
        return profondeur - 10
    
    # Match nul ou limite atteinte
    if plateau_plein(plateau) or profondeur >= prof_max:
        return 0
    
    # Tour de l'IA : elle cherche le meilleur score
    if tour_ia:
        meilleur_score = -999
        
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = signe_ia
                score = minimax(plateau, profondeur + 1, False, signe_ia, signe_humain, prof_max)
                plateau[i] = " "
                
                if score > meilleur_score:
                    meilleur_score = score
        
        return meilleur_score
    
    # Tour de l'humain : il cherche le pire score pour l'IA
    else:
        meilleur_score = 999
        
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = signe_humain
                score = minimax(plateau, profondeur + 1, True, signe_ia, signe_humain, prof_max)
                plateau[i] = " "
                
                if score < meilleur_score:
                    meilleur_score = score
        
        return meilleur_score


def ia(plateau, signe):
    """
    IA TIC TAC TOE avec 3 niveaux de difficulte
    """
    global niveau_difficulte
    
    # Trouver qui est l'adversaire
    adversaire = "X" if signe == "O" else "O"
    
    # Niveau 1 : Joue au hasard
    if niveau_difficulte == 1:
        cases_libres = []
        for i in range(9):
            if plateau[i] == " ":
                cases_libres.append(i)
        
        if len(cases_libres) > 0:
            return random.choice(cases_libres)
        else:
            return None
    
    # Niveau 2 et 3 : Utilise minimax
    if niveau_difficulte == 2:
        prof_max = 3  # Regarde 3 coups a l'avance
    else:
        prof_max = 999  # Regarde tous les coups possibles
    
    meilleur_coup = None
    meilleur_score = -999
    
    # Teste chaque case vide
    for i in range(9):
        if plateau[i] == " ":
            # Simule le coup
            plateau[i] = signe
            score = minimax(plateau, 0, False, signe, adversaire, prof_max)
            plateau[i] = " "
            
            # Garde le meilleur
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = i
    
    return meilleur_coup

######## FIN BOT IA AVEC MINIMAX #######


print(GRAS + JAUNE + "╔═══════════════════════════╗" + RESET)
print(GRAS + JAUNE + "║    ❌ TIC TAC TOE ⭕    ║" + RESET)
print(GRAS + JAUNE + "╚═══════════════════════════╝" + RESET)
print("Les cases sont numérotées de 0 a 8")

# Selection du mode de jeu 
print("\n🎮 MODE DE JEU:")
print("N°1 Player vs Player ")
print("N°2 Player vs IA")
mode = int(input("Choisissez votre mode de jeu : "))

# Si mode IA, choisir la difficulté
if mode == 2:
    print("\n  NIVEAU DE DIFFICULTÉ:")
    print("N°1 - 🟢 Débutant (Facile)")
    print("N°2 - 🟡 Intermédiaire (Moyen)")
    print("N°3 - 🔴 Expert (Imbattable)")
    niveau_difficulte = int(input("Choisissez le niveau : "))
    
    if niveau_difficulte == 1:
        print(VERT + "Vous affrontez une IA Débutant 🟢" + RESET)
    elif niveau_difficulte == 2:
        print(JAUNE + "Vous affrontez une IA Intermédiaire 🟡" + RESET)
    elif niveau_difficulte == 3:
        print(ROUGE + "Vous affrontez une IA Expert 🔴 - Bonne chance !" + RESET)

# Boucle principal du jeu
while True:
    afficher_plateau()

    # Au tour de l'ia " O "
    if mode == 2 and joueur_actuel == "O":
        print("🤖 L'IA réfléchit...")
        temps_reflexion = random.uniform(1.5, 3.0) # Entre 1 et 3 s d'attente 
        time.sleep(temps_reflexion) # Temps aleatoire de reflexion entre 1 et 3 s
        choix = ia(plateau, "O")

        if choix is None:
            print(" ERREUR L'ia ne peut pas jouer ")
            break 

        print(f"L'IA joue en case {choix}")
    else:
        # Tour de l'humain 
        print("Joueur", joueur_actuel, "c'est a vous !")
        choix = int(input("Choisissez une case : "))

        if choix < 0 or choix > 8:
            print("ERREUR : choisissez un numero entre 0 et 8")
            continue

        if plateau[choix] != " ":
             print("ERREUR : Cette case est deja occupée")
             continue
            
    plateau[choix] = joueur_actuel
    
     #verifier joueur win               
    if verifier_victoire():
        afficher_plateau()
        if joueur_actuel == "O" and mode == 2:
            print(ROUGE + GRAS + "🤖 L'IA gagne ! 🤖" + RESET)
        else:
            print(BLEU + GRAS + "👑 le joueur", joueur_actuel, "gagne la partie ! 👑 " + RESET)
        break  # permet de sortir de la boucle while 

    if verifier_match_nul():
        afficher_plateau()
        print(JAUNE + GRAS + "⚖️  MATCH NUL ! PERSONNE NE GAGNE ⚖️" + RESET)
        break


    #change de joueur
    if joueur_actuel ==  "X":
        joueur_actuel = "O"
    else:
        joueur_actuel = "X"

print("Fin du jeu !")