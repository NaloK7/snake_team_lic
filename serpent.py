import pygame


class Snake:
    """
    objet liste qui va contenir un objet Head et des objet Body
    """

    def __init__(self, width, height):
        # largeur de la fenetre pygame
        self.width_max = width
        # hauteur de la fenetre pygame
        self.height_max = height

        self.snake_liste = []
        self.initial_length = 4
        self.number_of_del = 1

        for _ in range(self.initial_length):
            self.AddPart(True)

    def AddPart(self, init=False):
        """
        creer une objet Body
        lui affecte des coordonnees
        puis l'ajoute au snake
        """
        new_part = SnakePart()
        if init:
            self.SetInitCoord(new_part)
        else:
            self.SetPartCoord(new_part)
        self.snake_liste.append(new_part)

    def DelPart(self):
        "supprime les derniers éléments de la liste snake."
        for _ in range(self.number_of_del):
            self.snake_liste.remove(self.snake_liste[-1])

    def SetPartCoord(self, part):
        """
        defini les coords d'un element au coord que le dernier element
        """
        last_part = self.snake_liste[-1]
        part.x = last_part.x
        part.y = last_part.y

    def SetInitCoord(self, part):
        """
        para: SnakePart object
        attribut les coordonees d'initialisation
        """
        if len(self.snake_liste) == 0:
            part.x = (self.width_max / 2) - (part.width / 2)
            part.y = (self.height_max / 2) - (part.height / 2)
        else:
            last_part = self.snake_liste[-1]
            part.x = last_part.x
            part.y = last_part.y + last_part.height

    def draw_snake(self, fenetre):
        """
        Dessine le serpent + couleurs
        """

        a = 0

        for i in range(len(self.snake_liste)):

            rect = pygame.Rect(
                self.snake_liste[i].x,
                self.snake_liste[i].y,
                self.snake_liste[i].height,
                self.snake_liste[i].width,
            )
            if a == 0:
                pygame.draw.rect(fenetre, (255, 255, 255), rect)
            elif a < 5 and a != 0:
                pygame.draw.rect(fenetre, (255, 0, 0), rect)
            elif a >= 5 and a <= 10:
                pygame.draw.rect(fenetre, (255, 128, 0), rect)
            elif a >= 10 and a <= 15:
                pygame.draw.rect(fenetre, (255, 255, 0), rect)
            elif a >= 15 and a <= 20:
                pygame.draw.rect(fenetre, (128, 255, 0), rect)
            elif a >= 20 and a <= 25:
                pygame.draw.rect(fenetre, (0, 255, 0), rect)
            elif a >= 25 and a <= 30:
                pygame.draw.rect(fenetre, (0, 255, 255), rect)
            elif a >= 30 and a <= 35:
                pygame.draw.rect(fenetre, (0, 0, 255), rect)
            elif a >= 35 and a <= 40:
                pygame.draw.rect(fenetre, (128, 0, 255), rect)
            elif a >= 40 and a <= 45:
                pygame.draw.rect(fenetre, (255, 0, 128), rect)
                if a == 55:
                    a = 0
            a += 1


class SnakePart:
    """
    nouvelle partie du Snake
    """
    def __init__(self):
        # hauteur d'une partie
        self.height = 40
        # lageur d'une partie
        self.width = 40
        # coordonnées initial
        self.x = 0
        self.y = 0
    
    def getYCoord(self):
        return self.y
    
    def getXCoord(self):
        return self.x
    
    def setYCoord(self, y):
        self.y = y

    def setXCoord(self, x):
        self.x = x