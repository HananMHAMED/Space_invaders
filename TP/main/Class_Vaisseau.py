"""
  Développement d'un jeu : Space invaders 
  M'HAMED Hanan
  Décembre 2024
  
"""

# importation des bibliothéques nécessaires
from tkinter import *

"""
Class vaisseau : gére l'apparition du vaisseau et leur deplacement
"""
class Vaisseau():
    def __init__(self, jeu, fenetre):
        self.jeu = jeu
        self.fenetre = fenetre
        self.vie = 3  # Initialisation nombre de vie de vaisseau
        # Position du vaisseau
        self.posx = 240
        self.posy = 450
        self.lon = 32
        self.lar = 30
        self.offset0 = -20
        self.offset1 = -18
        # Création du vaisseau (image)
        self.image_vaisseau = PhotoImage(file = 'joueur.gif')
        self.vaisseau_id = self.fenetre.canvas.create_image(self.posx, self.posy, anchor = 'center',image = self.image_vaisseau)
        self.rect_id = self.fenetre.canvas.create_rectangle(self.posx + self.offset0, self.posy + self.offset0, self.posx +
                                                            self.lon + self.offset1, self.posy + self.lar + self.offset1)
        # Lancement du déplacement du vaisseau
        self.fenetre.Space_invaders.bind('<Key>', self.callback)

    def callback(self, event):
        self.deplacer_vaisseau(event)
        self.jeu.fire_projectile(event)

    def get_position(self):
        # fonction qui recupere les coordonnées de vaisseau
        # entrée : vide
        # sortie : les coordonnées de vaisseau
        return self.fenetre.canvas.coords(self.rect_id)
    
    def deplacer_vaisseau(self, event):
        
        # création de l'évenement event sur une touche de clavier
        touche = event.keysym
        print(touche)
        # deplacément du vaisseau vers la droite
        if touche == 'Right':
            self.posx += 10
            if self.posx > 550: 
                self.posx = 550
        # deplacement du vaisseau vers la gauche
        if touche  == 'Left':
            self.posx -= 10
            if self.posx < 10:
                self.posx = 10
        # deplacement
        prev_x, prev_y = self.posx, self.posy
        self.fenetre.canvas.coords(self.vaisseau_id, self.posx, self.posy)
        self.fenetre.canvas.coords(self.rect_id, self.posx + self.offset0, self.posy + self.offset0, self.posx + self.lon + self.offset1, self.posy + self.lar + self.offset1)

      
