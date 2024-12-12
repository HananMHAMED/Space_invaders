"""
  Développement d'un jeu : Space invaders 
  M'HAMED Hanan
  Décembre 2024
  
"""
# importation des bibliothéques nécessaires
import random

from Class_Vaisseau import Vaisseau
from Class_Alien import Alien
from Class_protections import protection
from Class_Projectile import projectile

"""
  Class jeu constituant les principales fonctions du jeu 
  et sa gestion 
  
"""
class Jeu():
    
    # Initialisation
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.score = 0  # Initialisation de score
        # Association d'une commande au bouton demarrer 
        self.fenetre.bouton.config(command = self.Demarrer)
        self.aliens = []   # Initialisation de liste des aliens 
        self.protections = []   # liste de protections de vaisseau
        self.projectiles = []   # File de projectiles de vaisseau
        self.projectiles_alien = [] # liste de projectiles des aliens
        self.x_speed = 2
        self.y_offset = 0

    def Demarrer(self):
        """
        Fonction Demarrer permet de lancer le jeu en appelant 
        la fonction start_game et de désactiver le bouton demarrer 
        en le mettant en état "disabled"
        """
        self.start_game()
        self.fenetre.bouton.config(state = "disabled")
        
    def start_game(self):
        # fonction qui met en place le lancement du jeu
        # en entrée : vide 
        # en sortie : vide
        
        self.vaisseau = Vaisseau(self, self.fenetre)
        self.score = 0
        self.create_aliens()
        self.move_aliens()
        self.create_protection()
        self.game_loop()
        
    def create_aliens(self):
        # Fonction qui gére l'apparition des aliens
        # en entrée : vide
        # en sortie : liste des aliens
        for row in range(4):  # row nombre des alien par colonne
            for col in range(8):  # col nombres des aliens par ligne
                alien = Alien(self.fenetre, col*50, row*50)
                self.aliens.append(alien)
        return self.aliens
    
        
    def move_aliens(self):
        # Fonction qui gére les mouvements des aliens
        # en entrée : vide 
        # en sortie : vide
        self.y_offset = 0
        for alien in self.aliens:
            if alien.aux_font():
                self.x_speed *= -1
                self.y_offset += 20
                break

        for alien in self.aliens:
            alien.move(self.x_speed, self.y_offset)
            
    def create_protection(self):
        # Fonction qui permet de remplir le liste de protections par des rectangles
        # en entrée : vide 
        # en sortie : vide
        for i in range(4):
            prot = protection(self.fenetre, 50 + i*100, 300)
            self.protections.append(prot)
            
        
    def fire_projectile(self, event):
        # création de l'évenement event sur une touche de clavier
        touche = event.keysym
        if not touche == "space": return
        x, y = self.fenetre.canvas.coords(self.vaisseau.vaisseau_id)
        proj = projectile(self.fenetre, x, y)
        self.projectiles.append(proj)

    def check_collision(self):
        """
        Check_collision gér les interactions entre les différents éléments du jeu
        (les collisions entre les projectiles lancés par le vaisseau et les aliens,
        les projectiles des aliens et le vaisseau, et entre les projectiles aliens et les protections),
        et mettre à jour l'état du jeu en fonctions des collisions détevtées.
        
        """
        for proj in self.projectiles.copy():
            for protection in self.protections:
                if self.est_collide(protection.get_position(), proj.get_position()):
                    self.fenetre.canvas.delete(proj.id)
                    self.projectiles.remove(proj)
                    break
            for alien in self.aliens.copy():
                if self.est_collide(alien.get_position(), proj.get_position()):
                    self.score += 10
                    self.fenetre.label.config(text = f"score: {self.score}")
                    self.fenetre.canvas.delete(proj.id)
                    self.fenetre.canvas.delete(alien.id)
                    self.fenetre.canvas.delete(alien.rect_id)
                    self.aliens.remove(alien)
                    self.projectiles.remove(proj)
                    break

        for proj_alien in self.projectiles_alien.copy():
            for protection in self.protections:
                if self.est_collide(protection.get_position(), proj_alien.get_position()):
                    self.fenetre.canvas.delete(proj_alien.id)
                    self.projectiles_alien.remove(proj_alien)
                    break
            if not self.vaisseau.get_position():
                self.fenetre.canvas.delete(proj_alien.id)
                self.projectiles_alien.remove(proj_alien)
                continue

            if self.est_collide(proj_alien.get_position(), self.vaisseau.get_position()):
                self.vaisseau.vie -= 1
                self.fenetre.label.config(text = f"vie: {self.vaisseau.vie}")
                print(f"vie: {self.vaisseau.vie}")
                self.fenetre.canvas.delete(proj_alien.id)
                self.projectiles_alien.remove(proj_alien)
                continue

        for alien in self.aliens.copy():
            for protection in self.protections.copy():
                if self.est_collide(protection.get_position(), alien.get_position()):
                    print("alien avec protection")
                    for prot in self.protections:
                        self.fenetre.canvas.delete(prot.id)
                    self.protections = []
                    break

    def est_collide(self, rect1, rect2):
        """
        Prend deux rectangles(rect1 et rect2 sont deux listes) et vérifie d'ils 
        se chevauchent. Renvoi True s'ils se chevauchent et False si non, si
        une exception est déclenchée elle renvoie False (pas de collision)
        """
        try:
            return not (rect1[2] <= rect2[0] or rect1[0] >= rect2[2] or rect1[3] <= rect2[1] or rect1[1] >= rect2[3])
        except:
            return False
     
    def tire_alien(self):
        """
        Cette fonction tire un projectile depuis un alien agressif avec une
        probabilité de 10% à 20%. Elle vérifie d'abord si la liste des aliens 
        n'est pas vide puis choisit aléatoirement un alien agressif parmi eux.
        Ensuite, elle récupère les coordonnées de cet alien et crée un projectile 
        à partir de ces coordonnées. Enfin, elle ajoute ce projectile à la liste
        des projectiles aliens.
        """
        if 0.1 < random.random() < 0.2:
            if not self.aliens: return
            alien_aggresive = random.choice(self.aliens)
            x, y = self.fenetre.canvas.coords(alien_aggresive.id)
            proj = projectile(self.fenetre, x, y, 1)
            self.projectiles_alien.append(proj)
        return

    def est_perdu(self):
        """
        vérifie si le jouer est perdu, return True si c'est le cas
        et False si non 
        """
        if self.vaisseau.vie <= 0: return True
        for alien in self.aliens:
            pos = self.fenetre.canvas.coords(alien.id)
            if pos[1] >= 430:
                return True
        return False

    def game_over(self):
        # arreter le jeu en cas de victoire ou perte
        # en entrée : vide 
        # en sortie : vide
        self.fenetre.canvas.delete("all")
        self.fenetre.bouton1.config(command = self.start_game)
        self.fenetre.bouton1.pack(padx = 10, pady = 10, side = 'left')
        self.fenetre.label1.config(text = "est Perdu!!")
        self.fenetre.label1.pack(padx = 10, pady = 10, side = 'top')

    def move_projectiles(self, proj_list):
        # permet de déplacer les projectiles et de gérer leur suppression lorsqu'ils quittent le fenetre
        # en entrée : liste de projectiles
        # en sortie : vide
        for proj in proj_list.copy():
            proj.move_proj()
            try:
                x, y, _, _, = proj.get_position()
                if not(0 < y < 480):
                    self.fenetre.canvas.delete(proj.id)
                    proj_list.remove(proj)
            except:
                self.fenetre.canvas.delete(proj.id)
                proj_list.remove(proj)
              
    def game_loop(self):
        # mettre à jour l'etat du jeu 
        # en entrée : vide
        # en sortie : vide
        self.move_aliens()
        self.move_projectiles(self.projectiles_alien)
        self.move_projectiles(self.projectiles)
        self.tire_alien()
        self.check_collision()
        if self.est_perdu():
            self.game_over()
        else:
            self.fenetre.Space_invaders.after(30, self.game_loop)
