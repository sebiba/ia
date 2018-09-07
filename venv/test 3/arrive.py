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
        self.grille.setInTab(((y_cercle*10)+x_cercle),"1")
        pygame.draw.polygon(self.screen, (level.get_at(red)), [(0, 33), (0, 43), (70, 43), (76, 33)], 0)
        #pygame.draw.circle(self.screen, (0, 0, 255), (self.x_cercle * 40-20, self.y_cercle * 40-20), self.size)