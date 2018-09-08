import pygame

class Balle:
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
        self.grille.setInTab(((y_cercle*10)+x_cercle),"1") #positionner la balle dans la grille valeur 1
        pygame.draw.circle(self.screen, (0, 0, 255), (self.x_cercle * 40-20, self.y_cercle * 40-20), self.size)

    def moveUp(self):
        if self.grille.getTab((((self.y_cercle-1)*10)+self.x_cercle)) == "0" and (((self.y_cercle-1)*10)+self.x_cercle) > 11: #si la case suppérieur est un 0 et qu'elle n'est pas hors champs
            pygame.draw.circle(self.screen, (0, 255, 0), (self.x_cercle * 40 - 20, self.y_cercle * 40 - 20), self.size)
            self.y_cercle -= 1
            self.grille.setInTab((((self.y_cercle)*10)+self.x_cercle),"1")
            pygame.draw.circle(self.screen, (0, 0, 255), (self.x_cercle * 40 - 20, self.y_cercle * 40 - 20), self.size)

    def moveDown(self):
        try: # except erreur d'index == sors de la grille
            if self.grille.getTab((((self.y_cercle+1) * 10) + self.x_cercle)) == "0": #si la case en dessous est un 0
                pygame.draw.circle(self.screen, (0, 255, 0), (self.x_cercle * 40 - 20, self.y_cercle * 40 - 20), self.size)
                self.y_cercle += 1
                self.grille.setInTab(((self.y_cercle * 10) + self.x_cercle), "1")
                pygame.draw.circle(self.screen, (0, 0, 255), (self.x_cercle * 40 - 20, self.y_cercle * 40 - 20), self.size)
        except IndexError:
            pass
    def moveLeft(self):
        if self.grille.getTab(((self.y_cercle * 10) + self.x_cercle-1)) == "0" and ((self.y_cercle * 10) + self.x_cercle)%10 != 1:
            pygame.draw.circle(self.screen, (0, 255, 0), (self.x_cercle * 40 - 20, self.y_cercle * 40 - 20), self.size)
            self.x_cercle -= 1
            self.grille.setInTab(((self.y_cercle * 10) + self.x_cercle), "1")
            pygame.draw.circle(self.screen, (0, 0, 255), (self.x_cercle * 40 - 20, self.y_cercle * 40 - 20), self.size)

    def moveRight(self):
        try: # except erreur d'index == sors de la grille
            if self.grille.getTab(((self.y_cercle * 10) + self.x_cercle+1)) == "0" and ((self.y_cercle * 10) + self.x_cercle)%10 != 0:
                pygame.draw.circle(self.screen, (0, 255, 0), (self.x_cercle * 40 - 20, self.y_cercle * 40 - 20), self.size)
                self.x_cercle += 1
                self.grille.setInTab(((self.y_cercle * 10) + self.x_cercle), "1")
                pygame.draw.circle(self.screen, (0, 0, 255), (self.x_cercle * 40 - 20, self.y_cercle * 40 - 20), self.size)
        except IndexError:
            pass