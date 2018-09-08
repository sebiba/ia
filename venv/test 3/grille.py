import balle

class Grille:
    size = 0
    step = 0
    default = "0"
    tab = []
    def __init__(self, size, step):
        self.size = size
        self.step = step

    def createTab(self, caractere):
        self.default = caractere
        tab = []
        m = 0
        while m < (self.size/self.step)**2: # boucle sur longueur * largeur
            tab.append(caractere)
            m = m + 1
        self.tab = tab
        return tab

    def draw(self,pygame, screen):
        # lignes vertical
        for point in range(self.step, self.size, self.step):  # range(start, stop, step)
            pygame.draw.line(screen, (0, 0, 0), (point, 0), (point, self.size), 1)
        # lignes horizontal
        for point in range(self.step, self.size, self.step):  # range(start, stop, step)
            pygame.draw.line(screen, (0, 0, 0), (0, point), (self.size, point), 1)

    def setInTab(self, key, value):
        self.tab[key-11] = value # key - 11 pour que la premiere ligne ai comme fausse coordonée y 1
    def erraseInTab(self, key):
        self.tab[key] = self.default

    def getTab(self, index):
        return self.tab[index-11]

    def print(self): #print du tableau en respectant les lignes
        for y in range (0, int(self.size/self.step), 1):
            for x in range (0, int(self.size/self.step), 1):
                print (self.tab[(y*10)+x]+", ", end='')
            print("\n")
        print("\n\n")