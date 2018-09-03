import time
import pygame
import balle
import grille

class Interface:
    use = None
    def __init__(self, size, step, name):
        pygame.init()
        pygame.display.set_caption(name)
        screen = pygame.display.set_mode((size, size))
        screen.fill((235, 235, 235))
        gril = grille.Grille(size, step)
        gril.createTab("0")
        self.use = balle.Balle(screen, gril, 3, 2,int (step/2))
        gril.draw(pygame, screen)

    def run(self):
        running = True
        while running:
            pygame.display.flip()  # actualise l'affichage
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.use.moveDown()
                time.sleep(0.2)
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.use.moveUp()
                time.sleep(0.2)
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.use.moveRight()
                time.sleep(0.2)
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.use.moveLeft()
                time.sleep(0.2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False