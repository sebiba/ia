import pygame

def main():
    pygame.init()
    pygame.display.set_caption("mini program")
    image = pygame.image.load("Include/img/connerie.jpg")
    screen = pygame.display.set_mode((340,280))

    #image.set_colorkey((255,255,255))#doit etre avant le blit
    #image.set_alpha(128)
    screen.fill((255,255,255))
    screen.blit(image, (10, 10))#image après le fill pour passer au dessus

    pygame.display.flip()#actualise l'affichage
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__=="__main__":
    main()