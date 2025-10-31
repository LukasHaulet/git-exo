import tkinter as tk
from tkinter import messagebox
import random
import math

class LightningTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ Morpion Orage Électrique ⚡")
        self.root.geometry("800x900")
        self.root.configure(bg='#0a0f1e')
        
        # Variables du jeu
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_over = False
        
        # Canvas unique avec tout dessus
        self.canvas = tk.Canvas(root, width=800, height=900, bg='#0f1420', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Effets d'animation
        self.lightnings = []
        self.clouds = []
        self.rain_drops = []
        self.flash_intensity = 0
        self.wind_offset = 0
        self.time = 0
        
        # Initialiser les nuages avec plus de détails
        for i in range(25):
            self.clouds.append({
                'x': random.randint(-100, 900),
                'y': random.randint(30, 180),
                'width': random.randint(120, 220),
                'height': random.randint(45, 80),
                'speed': random.uniform(0.1, 0.35),
                'darkness': random.uniform(0.6, 1.0),
                'puffiness': random.uniform(0.8, 1.3),
                'depth': random.random()  # Pour l'effet de profondeur
            })
        
        # Trier les nuages par profondeur pour effet 3D
        self.clouds.sort(key=lambda c: c['depth'])
        
        # Initialiser les gouttes de pluie
        for i in range(350):
            self.rain_drops.append({
                'x': random.randint(-100, 900),
                'y': random.randint(0, 900),
                'speed': random.uniform(12, 18),
                'length': random.randint(25, 40),
                'opacity': random.uniform(0.4, 0.8),
                'thickness': random.uniform(1.5, 2.5)
            })
        
        # Créer l'interface de jeu
        self.create_game_interface()
        
        # Démarrer l'animation
        self.animate()
    
    def create_game_interface(self):
        # Ces éléments seront recréés à chaque frame mais gardés au-dessus
        pass
    
    def draw_game_ui(self):
        """Dessiner l'interface de jeu par-dessus les animations"""
        # Fond semi-transparent pour le plateau
        self.canvas.create_rectangle(
            150, 200, 650, 800,
            fill='#0d1829', outline='', stipple='gray50', tags='ui'
        )
        
        # Titre avec effet de glow
        self.canvas.create_text(
            400, 60, 
            text="⚡ ORAGE ÉLECTRIQUE ⚡",
            font=('Arial', 36, 'bold'),
            fill='#66ccff', tags='ui'
        )
        
        # Status
        status_text = "Joueur: " + self.current_player
        if self.game_over:
            winner = self.check_winner()
            if winner:
                status_text = f"🏆 {winner} a gagné!"
            else:
                status_text = "Match nul!"
        
        self.canvas.create_text(
            400, 120,
            text=status_text,
            font=('Arial', 20, 'bold'),
            fill='#aaddff', tags='ui'
        )
        
        # Plateau de jeu
        board_x = 200
        board_y = 270
        board_size = 400
        cell_size = board_size // 3
        
        # Cadre du plateau avec effet lumineux bleu électrique
        self.canvas.create_rectangle(
            board_x - 25, board_y - 25,
            board_x + board_size + 25, board_y + board_size + 25,
            fill='', outline='#0088cc', width=5, tags='ui'
        )
        
        # Créer les cellules du morpion
        for i in range(9):
            row = i // 3
            col = i % 3
            x = board_x + col * cell_size
            y = board_y + row * cell_size
            
            # Fond de la cellule - bleu électrique TRÈS transparent
            rect = self.canvas.create_rectangle(
                x + 8, y + 8,
                x + cell_size - 8, y + cell_size - 8,
                fill='#050f1a', outline='#006699', width=2, tags=('ui', f'cell_{i}')
            )
            
            # Texte de la cellule
            text = self.canvas.create_text(
                x + cell_size // 2, y + cell_size // 2,
                text=self.board[i],
                font=('Arial', 56, 'bold'),
                fill='#88ddff', tags=('ui', f'cell_{i}')
            )
            
            # Bind click event
            self.canvas.tag_bind(f'cell_{i}', '<Button-1>', lambda e, idx=i: self.cell_clicked(idx))
        
        # Bouton Reset
        self.canvas.create_rectangle(
            275, 730, 525, 790,
            fill='#2266cc', outline='#5599ff', width=3, tags=('ui', 'reset_btn')
        )
        self.canvas.create_text(
            400, 760,
            text="🔄 Nouvelle Partie",
            font=('Arial', 18, 'bold'),
            fill='white', tags=('ui', 'reset_btn')
        )
        self.canvas.tag_bind('reset_btn', '<Button-1>', lambda e: self.reset_game())
    
    def create_lightning(self):
        """Créer un éclair ultra réaliste avec branches complexes"""
        lightning = {
            'start_x': random.randint(150, 650),
            'start_y': random.randint(60, 140),
            'segments': [],
            'branches': [],
            'life': 28,
            'max_life': 28,
            'color_type': random.choices(['blue', 'yellow', 'cyan'], weights=[60, 25, 15])[0],
            'thickness': random.uniform(1.2, 2.0),
            'intensity': random.uniform(0.8, 1.2)
        }
        
        # Créer le tracé principal avec mouvement naturel
        x = lightning['start_x']
        y = lightning['start_y']
        lightning['segments'].append((x, y))
        
        max_segments = random.randint(45, 65)
        direction = random.choice([-1, 1]) * 0.4
        chaos = random.uniform(0.8, 1.2)
        
        for i in range(max_segments):
            # Mouvement ultra erratique
            x += random.randint(-60, 60) * chaos + direction * 8
            y += random.randint(10, 28)
            
            # Changement de direction aléatoire
            if random.random() < 0.15:
                direction *= -1
                chaos = random.uniform(0.7, 1.3)
            
            lightning['segments'].append((x, y))
            
            # Créer des branches majeures
            if random.random() < 0.4 and i > 3 and len(lightning['branches']) < 20:
                branch = self.create_branch(x, y, i, max_segments, depth=0)
                if branch:
                    lightning['branches'].append(branch)
            
            if y > 900:
                break
        
        return lightning
    
    def create_branch(self, start_x, start_y, parent_depth, max_depth, depth=0):
        """Créer une branche d'éclair avec sous-branches récursives"""
        if depth > 2 or parent_depth > max_depth * 0.85:
            return None
            
        branch = []
        x, y = start_x, start_y
        length = random.randint(5, 12) - depth * 2
        angle_bias = random.choice([-1.2, 1.2])
        
        for i in range(max(3, length)):
            x += random.randint(-45, 45) * angle_bias
            y += random.randint(8, 22)
            branch.append((x, y))
            
            # Créer des sous-branches
            if random.random() < 0.25 and i > 2 and depth < 2:
                sub_branch = self.create_branch(x, y, parent_depth, max_depth, depth + 1)
                if sub_branch:
                    # Ajouter la sous-branche comme branche séparée
                    return [branch, sub_branch]
        
        return branch
    
    def draw_lightning(self, lightning):
        """Dessiner un éclair avec effet glow multicouche ultra réaliste"""
        life_ratio = lightning['life'] / lightning['max_life']
        
        # Effet de pulsation électrique
        pulse = 1 + math.sin(lightning['life'] * 0.4) * 0.3
        alpha = min(1.0, life_ratio * pulse * lightning['intensity'])
        
        # Couleurs selon le type avec plus de variété
        if lightning['color_type'] == 'blue':
            colors = [
                (f'#{int(30*alpha):02x}{int(100*alpha):02x}{int(255*alpha):02x}', 10),  # Glow externe
                (f'#{int(80*alpha):02x}{int(160*alpha):02x}{int(255*alpha):02x}', 6),   # Glow moyen
                (f'#{int(150*alpha):02x}{int(200*alpha):02x}{int(255*alpha):02x}', 3.5),  # Proche
                (f'#{int(220*alpha):02x}{int(240*alpha):02x}{int(255*alpha):02x}', 1.8), # Très proche
                ('#f0f8ff', 0.8)  # Cœur blanc-bleuté pur
            ]
        elif lightning['color_type'] == 'yellow':
            colors = [
                (f'#{int(200*alpha):02x}{int(130*alpha):02x}{int(15*alpha):02x}', 10),
                (f'#{int(255*alpha):02x}{int(170*alpha):02x}{int(40*alpha):02x}', 6),
                (f'#{int(255*alpha):02x}{int(210*alpha):02x}{int(100*alpha):02x}', 3.5),
                (f'#{int(255*alpha):02x}{int(245*alpha):02x}{int(180*alpha):02x}', 1.8),
                ('#ffffd8', 0.8)
            ]
        else:  # cyan
            colors = [
                (f'#{int(20*alpha):02x}{int(180*alpha):02x}{int(200*alpha):02x}', 10),
                (f'#{int(60*alpha):02x}{int(220*alpha):02x}{int(240*alpha):02x}', 6),
                (f'#{int(120*alpha):02x}{int(240*alpha):02x}{int(255*alpha):02x}', 3.5),
                (f'#{int(200*alpha):02x}{int(250*alpha):02x}{int(255*alpha):02x}', 1.8),
                ('#e0ffff', 0.8)
            ]
        
        # Fonction récursive pour dessiner les branches
        def draw_branch_recursive(branch_data, is_main=False):
            if isinstance(branch_data, list) and len(branch_data) > 0:
                if isinstance(branch_data[0], tuple):
                    # C'est une branche simple
                    if len(branch_data) > 1:
                        width_mult = 1.0 if is_main else 0.6
                        for color, width in colors:
                            self.canvas.create_line(
                                branch_data, fill=color, 
                                width=width*lightning['thickness']*width_mult, 
                                smooth=True, capstyle=tk.ROUND, joinstyle=tk.ROUND,
                                tags='lightning'
                            )
                else:
                    # C'est une liste de branches
                    for sub_branch in branch_data:
                        draw_branch_recursive(sub_branch, False)
        
        # Dessiner toutes les branches d'abord
        for branch in lightning['branches']:
            draw_branch_recursive(branch, False)
        
        # Éclair principal avec toutes les couches
        if len(lightning['segments']) > 1:
            for color, width in colors:
                self.canvas.create_line(
                    lightning['segments'], fill=color, 
                    width=width*lightning['thickness'], 
                    smooth=True, capstyle=tk.ROUND, joinstyle=tk.ROUND,
                    tags='lightning'
                )
    
    def draw_cloud(self, cloud):
        """Dessiner un nuage ultra volumétrique et réaliste"""
        darkness = cloud['darkness']
        depth_factor = 0.5 + cloud['depth'] * 0.5
        base_color = int(20 + darkness * 30) 
        
        # Plus de puffs pour plus de détails
        num_puffs = 9
        
        for i in range(num_puffs):
            # Position des puffs en forme de nuage
            offset_x = (i - num_puffs/2) * cloud['width'] / (num_puffs + 1)
            
            # Créer une forme bombée
            height_factor = 1 - abs(i - num_puffs/2) / (num_puffs/2)
            offset_y = -height_factor * cloud['height'] / 2.5 + math.sin(i + self.time*0.015) * 10
            
            size_x = cloud['width'] / 2.8 * cloud['puffiness'] * (0.8 + height_factor * 0.4)
            size_y = cloud['height'] / 1.8 * cloud['puffiness'] * (0.7 + height_factor * 0.5)
            
            # Effet de profondeur - nuages loin sont plus clairs
            color_var = int(base_color * depth_factor + (i - num_puffs/2) * 2)
            color_var = max(15, min(80, color_var))
            
            # Variations de teinte pour le volume
            r = color_var
            g = color_var + 8
            b = color_var + 22
            
            color = f'#{r:02x}{g:02x}{b:02x}'
            
            # Dessiner le puff avec contour sombre pour plus de définition
            self.canvas.create_oval(
                cloud['x'] + offset_x - size_x,
                cloud['y'] + offset_y - size_y,
                cloud['x'] + offset_x + size_x,
                cloud['y'] + offset_y + size_y,
                fill=color, outline=f'#{max(0,r-10):02x}{max(0,g-10):02x}{max(0,b-10):02x}',
                width=1, tags='cloud'
            )
    
    def animate(self):
        """Boucle d'animation principale optimisée"""
        self.time += 1
        
        # Nettoyer le canvas
        self.canvas.delete('all')
        
        # Fond de ciel avec dégradé amélioré
        for i in range(25):
            intensity = 12 + i * 2.5
            
            if self.flash_intensity > 0:
                flash_add = int(self.flash_intensity * 180)
                r = min(255, int(intensity + flash_add * 0.8))
                g = min(255, int(intensity + flash_add * 0.9))
                b = min(255, int(intensity + 22 + flash_add))
                color = f'#{r:02x}{g:02x}{b:02x}'
            else:
                color = f'#{int(intensity):02x}{int(intensity):02x}{int(intensity+22):02x}'
            
            self.canvas.create_rectangle(
                0, i*36, 800, (i+1)*36,
                fill=color, outline='', tags='bg'
            )
        
        # Diminuer le flash
        if self.flash_intensity > 0:
            self.flash_intensity -= 0.05
            if self.flash_intensity < 0:
                self.flash_intensity = 0
        
        # Dessiner les nuages (ordre de profondeur)
        for cloud in self.clouds:
            cloud['x'] += cloud['speed'] * (0.5 + cloud['depth'] * 0.5)
            if cloud['x'] > 900:
                cloud['x'] = -cloud['width'] - 50
                cloud['y'] = random.randint(30, 180)
            
            self.draw_cloud(cloud)
        
        # Pluie diagonale ultra réaliste
        for drop in self.rain_drops:
            drop['x'] += drop['speed']
            drop['y'] += drop['speed'] * 0.45
            
            if drop['x'] > 1000 or drop['y'] > 950:
                drop['x'] = random.randint(-150, -50)
                drop['y'] = random.randint(0, 900)
            
            # Variation avec le vent turbulent
            wind = math.sin((drop['y'] + self.time * 2) * 0.015) * 6 + math.cos(drop['x'] * 0.01) * 3
            
            # Goutte avec variation d'opacité
            opacity = int(drop['opacity'] * 200)
            color = f'#{opacity:02x}{opacity+40:02x}{opacity+80:02x}'
            
            # Dessiner la goutte avec effet de vitesse
            self.canvas.create_line(
                drop['x'] + wind, drop['y'],
                drop['x'] + wind + drop['length'], drop['y'] + drop['length'] * 0.45,
                fill=color, width=drop['thickness'], capstyle=tk.ROUND, tags='rain'
            )
            
            # Mini-gouttes pour effet de splash
            if random.random() < 0.05:
                splash_color = f'#{int(opacity*0.6):02x}{int((opacity+40)*0.6):02x}{int((opacity+80)*0.6):02x}'
                self.canvas.create_oval(
                    drop['x'] + wind - 1, drop['y'] - 1,
                    drop['x'] + wind + 1, drop['y'] + 1,
                    fill=splash_color, outline='', tags='rain'
                )
        
        # Créer des éclairs plus fréquents
        if random.random() < 0.04:
            self.lightnings.append(self.create_lightning())
            self.flash_intensity = random.uniform(0.45, 0.75)
        
        # Dessiner les éclairs
        remaining_lightnings = []
        for lightning in self.lightnings:
            if lightning['life'] > 0:
                self.draw_lightning(lightning)
                lightning['life'] -= 1
                remaining_lightnings.append(lightning)
        
        self.lightnings = remaining_lightnings
        
        # Dessiner l'interface de jeu par-dessus
        self.draw_game_ui()
        
        # Continuer l'animation
        self.root.after(35, self.animate)
    
    def cell_clicked(self, index):
        """Gérer le clic sur une cellule"""
        if self.game_over or self.board[index] != '':
            return
        
        self.board[index] = self.current_player
        
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.root.after(100, lambda: messagebox.showinfo("Fin du jeu", f"Le joueur {winner} a gagné!"))
        elif '' not in self.board:
            self.game_over = True
            self.root.after(100, lambda: messagebox.showinfo("Fin du jeu", "Match nul!"))
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        """Vérifier s'il y a un gagnant"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] 
                and self.board[combo[0]] != ''):
                return self.board[combo[0]]
        return None
    
    def reset_game(self):
        """Réinitialiser le jeu"""
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_over = False

if __name__ == "__main__":
    root = tk.Tk()
    game = LightningTicTacToe(root)
    root.mainloop()