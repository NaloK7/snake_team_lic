import pygame
from serpent import Snake
import Move
import random
import AppleClasses
# import sys


class Board:
    """
    create a game board instance take a master window at init
    """

    # set window size
    def __init__(self, master):
        """
        para: tkinter window
        """
        self.height = 600
        self.width = 600
        self.score = 10
        self.blockSize = 40  # Set the size of the grid block
        # self.master est la fenetre principale
        self.master_window = master
        # permet de cacher la fenetre principal
        self.master_window.withdraw()

        # LE SERPENT
        self.apple = self.appleType()
        self.snake = Snake(self.width, self.height)

        self.move = Move.Move(self)
        self.timer = 6000
        self.SetWindow()

    def appleType(self):
        if random.randint(0, 1) == 1:
            self.apple = AppleClasses.GoodApple(self.width, self.height)
        else:
            self.apple = AppleClasses.BadApple(self.width, self.height)
        return self.apple

    # will draw the winadow
    def SetWindow(self):
        pygame.init()
        # draw window with set sizes
        self.window = pygame.display.set_mode((self.height, self.width))
        self.RunWindow()

    def drawGrid(self):
        compteur = 0
        for x in range(0, self.width, self.blockSize):
            for y in range(0, self.height, self.blockSize):
                rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                pygame.draw.rect(self.window, (40, 40, 40), rect, 1)
                compteur += 1
        return compteur

    def CrossQuit(self, event):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

    # check event to quit the window
    def Quit(self):
        self.run = False
        # fait reaparaitre la fenetre principal
        self.master_window.deiconify()
        pygame.quit()

    # let the code run while the window isn't close
    def RunWindow(self):
        # set the text font
        font = pygame.font.Font(None, 40)
        self.run = True
        self.i = 0
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("check event")
                    self.CrossQuit(event)
            if self.i == self.timer:
                self.apple = self.appleType()
                self.i = 0
            # color the window in black on each frame
            self.window.fill((0, 0, 0))
            self.drawGrid()
            # time for the window to refresh in millisecond
            pygame.time.delay(200)
            # set the text to show
            text = font.render(str(self.score), True, (255, 255, 255), None)
            # draw a rect around the text
            textRect = text.get_rect()
            # set the textRect to the given coords
            textRect.center = ((550), (50))
            # tell the window to show the text
            self.window.blit(text, textRect)
            self.snake.draw_snake(self.window)
            self.apple.DrawApple(self.window)
            self.move.run()

            # print(self.apple.x)

            # apple go here
            # apple
            self.i += 100
            pygame.display.update()
        # pygame.quit()
        return self.score


# must give snake,apple and score in param when using SetWindow()
