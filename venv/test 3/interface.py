import time
import pygame
import balle
import grille
import arrive

class Interface:
    use = None
    def __init__(self, size, step, name):
        pygame.init()
        pygame.display.set_caption(name)
        screen = pygame.display.set_mode((size, size))
        screen.fill((235, 235, 235))
        gril = grille.Grille(size, step)
        gril.createTab("0") # cré une table rempli de 0
        self.finish = arrive.Arrive(screen, gril, 2, 2) # instancie une arrivé en position 2,2
        self.use = balle.Balle(screen, gril, 3, 2,int (step/2)) # instancie une balle en position 3,2 avec un rayon qui vaut la moitié de la taille d'une case
        gril.draw(pygame, screen)

    def run(self):
        running = True
        while running: # boucle vérifiant si une touche a été appuyé
            pygame.display.flip()  # actualise l'affichage
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.use.moveDown()
                time.sleep(0.2) # affin de ne pas repassé dans le if directement
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.use.moveUp()
                time.sleep(0.2) # affin de ne pas repassé dans le if directement
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.use.moveRight()
                time.sleep(0.2) # affin de ne pas repassé dans le if directement
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.use.moveLeft()
                time.sleep(0.2) # affin de ne pas repassé dans le if directement

            for event in pygame.event.get(): # si pygame quit alors on arrete tout
                if event.type == pygame.QUIT:
                    running = False