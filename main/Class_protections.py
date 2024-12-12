
"""
  Développement d'un jeu : Space invaders 
  M'HAMED Hanan
  Décembre 2024
  
"""

# importation des bibliothéques nécessaires
from tkinter import *
"""
  Class protection : constituant les principales fonctions
  pour gérer les protections de vaisseau
"""
class protection():
  # Initialisation
  def __init__(self, fenetre, x, y):
    self.fenetre = fenetre
    self.x = x # 
    self.y = y 
    self.color = "blue"
    self.x_speed = 1
    self.id = self.fenetre.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill = self.color)
    
  def get_position(self):
    # fonction qui recupere les coordonnées d'un protection (rectangle)
    # entrée : vide
    # sortie : les coordonnées d'un rectangle
    return self.fenetre.canvas.coords(self.id)
