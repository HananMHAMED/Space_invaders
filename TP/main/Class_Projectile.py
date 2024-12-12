"""
  Développement d'un jeu : Space invaders 
  M'HAMED Hanan
  Décembre 2024
  
"""

# importation des bibliothéques nécessaires
from tkinter import *
from Class_Vaisseau import Vaisseau

"""
Class projectile : constituant les principales fonctions du tires 
 
    
"""
class projectile():
    def __init__(self, fenetre, x, y, dir=-1):
        self.fenetre = fenetre
        offset_y = -20
        y += offset_y
        # création d'un projectile (line)
        couleur = "green" if dir == -1 else "red"
        self.id = self.fenetre.canvas.create_rectangle(x, y, x + 5, y + 10, fill = couleur)
        self.y_speed = 10 * dir
        
    def move_proj(self):
        # fonction qui gére le mouvement des projectiles
        # entrée : vide
        # sortie : vide
        self.fenetre.canvas.move(self.id, 0, self.y_speed)
    
    def get_position(self):
        # fonction qui recupere les coordonnées d'un projectile
        # entrée : vide
        # sortie : les coordonnées d'un projectile
        return self.fenetre.canvas.coords(self.id)
    
