import pygame
import random

apple_w = 30  # width of the apple
apple_h = 30  # height of the apple


class GoodApple:
    """"""

    def __init__(self, width, height):
        self.width_max = width
        self.height_max = height
        self.type = True
        self.color = (0, 255, 0)  # R,G,B
        self.radius = 20
        self.step = 40  # step = depending of the circle's radius
        self.x = 0
        self.y = 0
        self.localisation = self.AppleLocationRandomizer()

    def AppleLocationRandomizer(
        self,
    ):  # board = bx and by (ex : bx = 1080, by=720)
        # x = random.randint(0,bx)
        # y = random.randint(0,by)
        x = random.randrange(
            self.radius, self.width_max, self.step
        )  # had tu pud the radius directly because it would have cause a
        # circular error
        y = random.randrange(
            self.radius, self.height_max, self.step
        )  # to have the random location of the apple, i need it's radius but
        # to make an apple, i need the location
        self.x = x
        self.y = y

    def DrawApple(self, board):
        pygame.draw.circle(board, self.color, (self.x, self.y), self.radius)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def Score(self, score):
        "parameters : score (int)"
        print("score up")
        score += 10
        return score


class BadApple:
    "parameters : width and height of the board (int)"

    def __init__(self, width, height):
        self.width_max = width
        self.height_max = height
        self.type = False
        self.color = (255, 0, 0)  # R,G,B
        self.radius = 20
        self.step = 40
        self.x = 0
        self.y = 0
        self.localisation = self.AppleLocationRandomizer()

    def AppleLocationRandomizer(
        self,
    ):  # board = bx and by (ex : bx = 1080, by=720)
        # x = random.randint(0,bx)
        # y = random.randint(0,by)
        x = random.randrange(
            self.radius, self.width_max, self.step
        )  # had tu pud the radius directly because it would have cause a
        # circular error
        y = random.randrange(self.radius, self.height_max, self.step)
        self.x = x
        self.y = y

    def DrawApple(self, board):
        pygame.draw.circle(board, self.color, (self.x, self.y), self.radius)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def Score(self, score):
        "parameters : score (int)"
        print("score down")
        score -= 10
        return score
