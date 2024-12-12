"""
  Développement d'un jeu : Space invaders 
  M'HAMED Hanan
  Décembre 2024
  
"""

# importation des bibliothéques nécessaires
from tkinter import *


Largeur = 550 # Largeur de canvas
Hauteur = 500 # Hauteur de canvas

#class Fenetre
class Fenetre():
    #initialisation
    def __init__(self, Space_invaders):
        self.Space_invaders = Space_invaders
        # Image de fond
        self.image = PhotoImage(file = 'tp4-image.gif')
        # création d'un widget canvas (zone graphique)
        self.canvas = Canvas(Space_invaders, width = Largeur, height = Hauteur)
        self.canvas.pack(padx = 10, pady = 10)
        self.canvas.create_image(0, 0, anchor = 'nw', image = self.image)
        # création du widget label "score"
        self.label = Label(Space_invaders, text = 'score: 0') 
        self.label.pack(padx = 10, pady = 10, side = 'top')
        # création du widget label "vies"
        self.label = Label(Space_invaders, text = 'vie: 3') 
        self.label.pack(padx = 10, pady = 10, side = 'top')
        # création du widget label 
        self.label1  = Label(Space_invaders, text = '') 
        # création du widget bouton (Demarrer)
        self.bouton = Button(Space_invaders, text = 'Demarrer')
        self.bouton.pack(padx = 10, pady = 10, side = 'left')
        # création du widget bouton (Bouton New game)
        self.bouton1 = Button(Space_invaders, text = 'New game') 
        self.bouton1.pack(padx = 10, pady = 10, side = 'left')
        # création du widget bouton (Bouton Quitter)
        self.bouton2 = Button(Space_invaders, text = 'Quit', command = Space_invaders.destroy)
        self.bouton2.pack(padx = 10, pady = 10, side = 'right')
        # Création d'un widget menu
        self.menubar = Menu(Space_invaders)
        self.menufichier = Menu(self.menubar, tearoff = 0)
        self.menufichier.add_command(label = "New Game")
        self.menufichier.add_command(label = "Quitter", command = Space_invaders.destroy)
        self.menufichier.add_command(label = "à propos")
        self.menubar.add_cascade(label = 'menu', menu = self.menufichier)
        # Affichage du menu
        Space_invaders.config(menu = self.menubar)
