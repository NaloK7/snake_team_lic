import random
import pygame
import pygame.freetype
import datetime as dt

# from mid import Gapple
# def appleGenerator(type):
#         if type == "good":


def AppleLocationRandomizer(
    bx, by, step
):  # board = bx and by (ex : bx = 1080, by=720)
    # x = random.randint(0,bx)
    # y = random.randint(0,by)
    x = random.randrange(
        15, bx, step
    )  # had tu pud the radius directly because it would have cause a circular error
    y = random.randrange(
        15, by, step
    )  # to have the random location of the apple, i need it's radius but to make an apple, i need the location
    localisation = [x, y]
    return localisation


def CheckRanking(
    score, leaderboard
):  # get the rank that will appear in the score (place in the list = rank -1)
    rank = 1
    for player_info in range(len(leaderboard) - 1):
        if score >= int(leaderboard[player_info][3]):
            return rank
        rank += 1


"new player's score, standardized data's file"


def addScore(
    rank, leaderboard, new_record
):  # add the new record to the right place to the leaderboard list i extracted from the data file
    for player_info in range(len(leaderboard) - 1):
        if leaderboard[player_info][0] == str(rank):
            leaderboard.pop(9)
            leaderboard.insert(player_info, new_record)

            return leaderboard


"rank, standardized data's file, list of the new record player's info"


def NewRecord(
    rank, name, date, score
):  # create a list of the new record with the needed player's info
    nv_name = nameVerif(name)
    n_list = [rank, nv_name, date, str(score)]
    return n_list


"rank, name, date, new player's score"


def NewRanking(
    leaderboard,
):  # shift down the lesser rank  and delete the 10th rank (the new 11th rank)
    n_rank = 1
    for player_info in range(len(leaderboard)):
        leaderboard[player_info].pop(0)
        leaderboard[player_info].insert(0, str(n_rank))
        n_rank += 1

    return leaderboard


def file_to_list():
    """
    return a list of [ [top1],..., [top10] ]
    """
    contenu = []
    file = open("Data.txt", "r")
    line = file.readline()
    while line != "":
        line_in_list = line.replace("\n", "").split(";")
        contenu.append(line_in_list)
        line = file.readline()
    file.close()
    return contenu


def SaveRanking(save_new_ranking):  # save the new leaderboard in the data file
    """parameters : need an organized version of the new leaderboard
    clean and save a standardized format of the save info"""
    x = ""
    for player_info in range(len(save_new_ranking)):
        x += ";".join(save_new_ranking[player_info])

        x += "\n"

    file = open("Data.txt", "w")
    file.write(str(x))
    file.close()


def nameVerif(name,):  # check if str == alphanum, take the 5 first characters of the name (what if the name is < 5 ?) et return an Uppercased version
    "parameters: the name of the player"
    checked_name = ""
    if len(name) >= 5:
        for i in range(5):
            if not name[i].isalnum():
                checked_name += " "
            else:
                checked_name += name[i]
    else:
        for i in range(len(name)):
            checked_name += name[i]

    return checked_name.upper()
    #   elif len(checked_name) <


"new holding record player's name"


def IncreaseScore(score):
    "parameters : score (int)"
    score += 10
    return score


def DecreaseScore(score):
    "parameters : score (int)"
    score -= 10
    return score


def AreYouIn(rank):  # check if the score can be added to the leaderboard
    if rank >= 10:
        return True
    else:
        return False


def DrawApple(board, color, localisation, radius):  # make it into a method
    pygame.draw.circle(board, color, localisation, radius)


def Timer(start_time, bx, by, board):
    font = pygame.freetype.SysFont("Times New Roman", 30)
    current_time = (
        pygame.time.get_ticks()
    )  # get the current time in milisecond
    delta_time_s = (
        current_time - start_time
    ) // 1000  # get the time in second
    text_surf, text_rect = font.render(str(delta_time_s), (0, 255, 0), size=30)
    margin = -10  # margin to the window
    # size = (bx, by)
    text_pos = (
        text_rect.width - margin,
        text_rect.height + margin,
    )  # localisation of the timer
    board.blit(text_surf, text_pos)


def Save(score, player_name):
    """parameters : score(int), player_name(str)"""
    today = dt.date.today()
    formatted_date = today.strftime("%d-%m-%Y")  # turn today's date into str
    # %d le jour
    # %m le mois
    # %Y l'année
    # formatted_date = string

    list_of_leader = file_to_list()

    rank = CheckRanking(score, list_of_leader)
    if rank is not None:
        new_record = NewRecord(
            rank, player_name, formatted_date, score
        )  # create a list of the new record with the needed player's info
        new_ranking = addScore(rank, list_of_leader, new_record)
        new_ranking_tidy = NewRanking(
            new_ranking
        )  # shift down the lesser rank
        SaveRanking(new_ranking_tidy)
    else:
        pass
