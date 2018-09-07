import pygame

class Arrive:
    x_cercle = 0
    y_cercle = 0
    screen = None
    size = 20
    def __init__(self, screen, grille, y_cercle, x_cercle, size = 20):
        self.x_cercle = x_cercle
        self.y_cercle = y_cercle
        self.screen = screen
        self.grille = grille
        self.size = size
        self.grille.setInTab(((self.y_cercle*10)+self.x_cercle),"2")
        pygame.draw.rect(self.screen, (255, 0, 0), [0+(self.x_cercle-1*40), 0+(self.y_cercle-1*40), self.x_cercle*40, self.y_cercle*40], 0)