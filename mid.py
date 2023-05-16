# Example file showing a basic pygame "game loop"
from AppleClasses import *
from AppleFunction import file_to_list
from AppleFunction import Timer
from AppleFunction import Save
import datetime as dt
import pygame.freetype

# pygame setup
fenetre = pygame.init()

bx = 720 #bx = width of the board
by = 480 #by = height of the board

player_name = "AAAAA" #test var
score = 10 #test var
today = dt.date.today()  # today's date
formatted_date = today.strftime("%d-%m-%Y")  # turn today's date into str
# %d le jour
# %m le mois
# %Y l'année
# formatted_date = string

list_of_leader = file_to_list() #to get the data file's data in a list of lists form


Save(score, player_name)

board = pygame.display.set_mode((bx, by))
start_time = pygame.time.get_ticks()
running = True

Gapple = GoodApple(bx, by)
Bapple = BadApple(bx, by)
while running == True: #test window
    board.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Timer(start_time,bx,by,board)
    Gapple.AppleLocationRandomizer
    Gapple.DrawApple(board)
    Bapple.AppleLocationRandomizer
    Bapple.DrawApple(board)
    pygame.display.flip()