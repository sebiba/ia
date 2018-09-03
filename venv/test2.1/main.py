import pygame
import time
import interface
step = 40 # largeur et longeur de chaque case
size = 400 # largeur et longeur de l'écran


def main():
    inter = interface.Interface(size, step, "IA")
    inter.run()

if __name__=="__main__":
    main()