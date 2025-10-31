import tkinter as tk
from tkinter import messagebox
import random

# ---------- CLASSE : ARRIÈRE-PLAN ANIMÉ ----------
class AnimatedBackground(tk.Canvas):
    def __init__(self, parent, width, height, speed=30):
        super().__init__(parent, width=width, height=height,
                         highlightthickness=0, bg="black")
        self.width = width
        self.height = height
        self.speed = speed
        self.symbols = []
        self.create_objects()
        self.animate()

    def create_objects(self):
        for _ in range(35):
            x = random.randint(0, self.width)
            y = random.randint(-self.height, 0)
            symbol = random.choice(["❌", "⭕"])
            color = "#ff4c4c" if symbol == "❌" else "#3ca0ff"
            size = random.randint(14, 28)
            obj = self.create_text(x, y, text=symbol,
                                   font=("Arial", size, "bold"), fill=color)
            self.symbols.append((obj, random.uniform(1, 3)))

    def animate(self):
        for (obj, speed) in self.symbols:
            x, y = self.coords(obj)
            y += speed
            if y > self.height:
                y = random.randint(-50, 0)
                x = random.randint(0, self.width)
            self.coords(obj, x, y)
        self.after(self.speed, self.animate)


# ---------- IA AVEC MARGE D’ERREUR ----------
def est_gagnant(plateau, signe):
    """Vérifie si un joueur a gagné"""
    if plateau[0] == plateau[1] == plateau[2] == signe: return True
    if plateau[3] == plateau[4] == plateau[5] == signe: return True
    if plateau[6] == plateau[7] == plateau[8] == signe: return True
    if plateau[0] == plateau[3] == plateau[6] == signe: return True
    if plateau[1] == plateau[4] == plateau[7] == signe: return True
    if plateau[2] == plateau[5] == plateau[8] == signe: return True
    if plateau[0] == plateau[4] == plateau[8] == signe: return True
    if plateau[2] == plateau[4] == plateau[6] == signe: return True
    return False


def plateau_plein(plateau):
    """Renvoie True si le plateau est rempli"""
    return all(case != " " for case in plateau)


def minimax(plateau, profondeur, tour_ia, signe_ia, signe_humain, prof_max):
    if est_gagnant(plateau, signe_ia): return 10 - profondeur
    if est_gagnant(plateau, signe_humain): return profondeur - 10
    if plateau_plein(plateau) or profondeur >= prof_max: return 0

    if tour_ia:
        meilleur_score = -999
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = signe_ia
                score = minimax(plateau, profondeur + 1, False,
                                signe_ia, signe_humain, prof_max)
                plateau[i] = " "
                meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        pire_score = 999
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = signe_humain
                score = minimax(plateau, profondeur + 1, True,
                                signe_ia, signe_humain, prof_max)
                plateau[i] = " "
                pire_score = min(pire_score, score)
        return pire_score


def ia(plateau, signe):
    """IA Tic Tac Toe avec niveaux + marge d'erreur réaliste"""
    global niveau_difficulte
    adversaire = "X" if signe == "O" else "O"

    # Niveau 1 : totalement aléatoire
    if niveau_difficulte == 1:
        cases_libres = [i for i, case in enumerate(plateau) if case == " "]
        return random.choice(cases_libres) if cases_libres else None

    # Niveau 2 et 3 : Minimax avec marge d'erreur
    prof_max = 3 if niveau_difficulte == 2 else 999

    # 🟡 Moyen → 15 % d’erreur
    if niveau_difficulte == 2 and random.random() < 0.15:
        libres = [i for i, case in enumerate(plateau) if case == " "]
        if libres:
            return random.choice(libres)

    # 🔴 Expert → 5 % d’erreur maximum
    if niveau_difficulte == 3 and random.random() < 0.05:
        libres = [i for i, case in enumerate(plateau) if case == " "]
        if libres:
            return random.choice(libres)

    # Sinon → coup parfait (Minimax)
    meilleur_coup = None
    meilleur_score = -999
    for i in range(9):
        if plateau[i] == " ":
            plateau[i] = signe
            score = minimax(plateau, 0, False, signe, adversaire, prof_max)
            plateau[i] = " "
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = i
    return meilleur_coup


# ---------- VARIABLES ----------
plateau = [" "] * 9
player = "X"
mode = None
niveau_difficulte = 1
game_over = False
buttons = []
info = None
jeu_frame = None


# ---------- LOGIQUE DU JEU ----------
def reset():
    global plateau, player, game_over
    plateau = [" "] * 9
    player = "X"
    game_over = False
    for b in buttons:
        b.config(text="", bg="#222", state=tk.NORMAL)
    info.config(text=f"Au tour de : {player}")


def click(i):
    global player, game_over
    if game_over or plateau[i] != " ":
        return

    plateau[i] = player
    color = "#ff4c4c" if player == "X" else "#3ca0ff"
    buttons[i].config(text=player, fg=color)

    if est_gagnant(plateau, player):
        messagebox.showinfo("Victoire", f"Le joueur {player} a gagné !")
        info.config(text=f"Victoire du joueur {player}")
        game_over = True
        return

    if plateau_plein(plateau):
        messagebox.showinfo("Match nul", "Personne ne gagne 😅")
        info.config(text="Match nul")
        game_over = True
        return

    player = "O" if player == "X" else "X"
    info.config(text=f"Au tour de : {player}")

    if mode == 2 and player == "O":
        app.after(500, tour_ia)


def tour_ia():
    global player, game_over
    if game_over:
        return
    choix = ia(plateau, "O")
    if choix is None:
        return
    plateau[choix] = "O"
    buttons[choix].config(text="O", fg="#3ca0ff")

    if est_gagnant(plateau, "O"):
        messagebox.showinfo("Défaite", "L'IA a gagné 🤖")
        info.config(text="Victoire de l'IA 🤖")
        game_over = True
        return

    if plateau_plein(plateau):
        messagebox.showinfo("Match nul", "Personne ne gagne 😅")
        info.config(text="Match nul")
        game_over = True
        return

    player = "X"
    info.config(text="À vous de jouer !")


# ---------- INTERFACE ----------
app = tk.Tk()
app.title("Tic Tac Toe")
app.geometry("540x540")
app.resizable(False, False)

bg = AnimatedBackground(app, 420, 540)
bg.pack(fill="both", expand=True)

menu_frame = tk.Frame(app, bg="", highlightthickness=0)
menu_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(menu_frame, text="❌ Tic Tac Toe ⭕",
         font=("Skia", 30, "bold"), fg="white", bg="black").pack(pady=40)
tk.Label(menu_frame, text="Choisissez un mode de jeu :",
         font=("Arial", 16, "bold"), fg="white", bg="black").pack(pady=10)


def retour_menu():
    global jeu_frame
    if jeu_frame and jeu_frame.winfo_exists():
        jeu_frame.destroy()
    menu_frame.place(relx=0.5, rely=0.5, anchor="center")


def choisir_mode(selected_mode):
    global mode
    mode = selected_mode
    menu_frame.place_forget()
    if mode == 2:
        afficher_difficulte()
    else:
        lancer_jeu()


tk.Button(menu_frame, text="🧍 Joueur vs Joueur", font=("Arial", 14, "bold"),
          width=20, bg="#ffffff", command=lambda: choisir_mode(1)).pack(pady=8)
tk.Button(menu_frame, text="🤖 Joueur vs IA", font=("Arial", 14, "bold"),
          width=20, bg="#ffffff", command=lambda: choisir_mode(2)).pack(pady=8)


def afficher_difficulte():
    diff_frame = tk.Frame(app, bg="", highlightthickness=0)
    diff_frame.place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(diff_frame, text="Niveau de difficulté de l'IA :",
             font=("Arial", 18, "bold"), fg="white", bg="black").pack(pady=20)

    def set_difficulte(niv):
        global niveau_difficulte
        niveau_difficulte = niv
        diff_frame.place_forget()
        lancer_jeu()

    tk.Button(diff_frame, text="🟢 Facile", font=("Arial", 14, "bold"),
              width=20, bg="white", command=lambda: set_difficulte(1)).pack(pady=6)
    tk.Button(diff_frame, text="🟡 Moyen", font=("Arial", 14, "bold"),
              width=20, bg="white", command=lambda: set_difficulte(2)).pack(pady=6)
    tk.Button(diff_frame, text="🔴 Expert", font=("Arial", 14, "bold"),
              width=20, bg="white", command=lambda: set_difficulte(3)).pack(pady=6)


def lancer_jeu():
    global buttons, info, plateau, player, game_over, jeu_frame
    plateau = [" "] * 9
    player = "X"
    game_over = False
    buttons.clear()

    jeu_frame = tk.Frame(app, bg="", highlightthickness=0)
    jeu_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(jeu_frame, text="❌ Tic Tac Toe ⭕",
             font=("Skia", 28, "bold"), fg="white", bg="black").pack(pady=20)

    info = tk.Label(jeu_frame, text="Au tour de : X",
                    font=("Arial", 16, "bold"), fg="white", bg="black")
    info.pack(pady=10)

    board = tk.Frame(jeu_frame, bg="black")
    board.pack()

    for i in range(9):
        b = tk.Button(board, text="", font=("Arial", 36, "bold"),
                      width=3, height=1, bg="#222", activebackground="#333",
                      command=lambda i=i: click(i))
        b.grid(row=i//3, column=i%3, padx=5, pady=5)
        buttons.append(b)

    controls = tk.Frame(jeu_frame, bg="black")
    controls.pack(pady=10)
    tk.Button(controls, text="🔄", font=("Arial", 22, "bold"),
              bg="#555", fg="white", activebackground="#777",
              width=3, height=1, command=reset).grid(row=0, column=0, padx=15)
    tk.Button(controls, text="⬅️", font=("Arial", 22, "bold"),
              bg="#777", fg="white", activebackground="#999",
              width=3, height=1, command=retour_menu).grid(row=0, column=1, padx=15)


app.mainloop()