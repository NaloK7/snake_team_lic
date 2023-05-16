import pygame as pg
import endGameWindow

# Idée : Quand le snake sort du board faire reculer d'un mouvement le snake
# pour l'affichage


class Move:
    """
    Recoit:
    -Un objet snake
    -un objet collision
    -un objet EndGameWindow
    Renvoi :
    -Un mouvement si l'utilisateur essaie d'aller dans la direction opposé où
    si son input est validé
    -Affiche la fenêtre de fin et arrête le snake si il sors du tableau ou si
    il se touche lui même
    -Ajoute ou enlève des partis du snake selon la pomme qu'il a mangé
    """

    def __init__(self, board):
        self.movement = "STOP"
        self.board = board

        # self.egw = egw  # egw == EndGameWindow

    def run(self):
        self.getInput()
        if self.getCollision() == "Continue":
            # print("Move Continue")
            self.getMove()
        elif self.getCollision() == "Dead":
            # print("Move Dead")
            # self.egw.EndGameWindow()
            # freeze pygame window
            endGameWindow.EndGameWindow(self.board).mainloop()
            self.board.run = False
            self.movement = -1
        elif self.getCollision() == "Apple":
            print("Move Apple")
            # self.board.score = self.board.apple.Score(self.board.score)
            # self.board.apple = self.board.appleType()

        elif not self.getCollision():
            self.getMove()

    def getInput(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.movement = "Up"

                elif event.key == pg.K_DOWN:
                    self.movement = "Down"
                elif event.key == pg.K_LEFT:
                    self.movement = "Left"
                elif event.key == pg.K_RIGHT:
                    self.movement = "Right"

    def getMove(self):
        match self.movement:
            case "Up":
                self.moveUp()
            case "Down":
                self.moveDown()
            case "Left":
                self.moveLeft()
            case "Right":
                self.moveRight()

    def moveUp(self):
        for i in range(len(self.board.snake.snake_liste)):
            if i == 0:
                head_y = self.board.snake.snake_liste[i].getYCoord()
                head_x = self.board.snake.snake_liste[i].getXCoord()
                self.board.snake.snake_liste[i].setYCoord(
                    self.board.snake.snake_liste[i].getYCoord()
                    - self.board.snake.snake_liste[i].height
                )
            else:
                old_y = self.board.snake.snake_liste[
                    i
                ].getYCoord()  # save the coordinate for use to the next round
                old_x = self.board.snake.snake_liste[i].getXCoord()
                self.board.snake.snake_liste[i].setYCoord(
                    head_y
                )  # moves under the part of the snake
                self.board.snake.snake_liste[i].setXCoord(head_x)
                head_y = old_y
                head_x = old_x

    def moveDown(self):
        for i in range(len(self.board.snake.snake_liste)):
            if i == 0:
                head_y = self.board.snake.snake_liste[i].getYCoord()
                head_x = self.board.snake.snake_liste[i].getXCoord()
                self.board.snake.snake_liste[i].setYCoord(
                    self.board.snake.snake_liste[i].getYCoord()
                    + self.board.snake.snake_liste[i].height
                )

            else:
                old_y = self.board.snake.snake_liste[
                    i
                ].getYCoord()  # save the coordinate for use to the next round
                old_x = self.board.snake.snake_liste[i].getXCoord()
                self.board.snake.snake_liste[i].setYCoord(
                    head_y
                )  # moves under the part of the snake
                self.board.snake.snake_liste[i].setXCoord(head_x)
                head_y = old_y
                head_x = old_x

    def moveLeft(self):
        for i in range(len(self.board.snake.snake_liste)):
            if i == 0:
                head_y = self.board.snake.snake_liste[i].getYCoord()
                head_x = self.board.snake.snake_liste[i].getXCoord()
                self.board.snake.snake_liste[i].setXCoord(
                    self.board.snake.snake_liste[i].getXCoord()
                    - self.board.snake.snake_liste[i].height
                )

            else:
                old_y = self.board.snake.snake_liste[
                    i
                ].getYCoord()  # save the coordinate for use to the next round
                old_x = self.board.snake.snake_liste[i].getXCoord()
                self.board.snake.snake_liste[i].setYCoord(
                    head_y
                )  # moves under the part of the snake
                self.board.snake.snake_liste[i].setXCoord(head_x)
                head_y = old_y
                head_x = old_x

    def moveRight(self):
        for i in range(len(self.board.snake.snake_liste)):
            if i == 0:
                head_y = self.board.snake.snake_liste[i].getYCoord()
                head_x = self.board.snake.snake_liste[i].getXCoord()
                self.board.snake.snake_liste[i].setXCoord(
                    self.board.snake.snake_liste[i].getXCoord()
                    + self.board.snake.snake_liste[i].height
                )

            else:
                old_y = self.board.snake.snake_liste[
                    i
                ].getYCoord()  # save the coordinate for use to the next round
                old_x = self.board.snake.snake_liste[i].getXCoord()
                self.board.snake.snake_liste[i].setYCoord(
                    head_y
                )  # moves under the part of the snake
                self.board.snake.snake_liste[i].setXCoord(head_x)
                head_y = old_y
                head_x = old_x

    def getCollision(self):
        if self.collisionDead():
            # print("collision dead")
            return "Dead"

        if self.collisionApple() == "Apple":
            # print("collision apple")
            return "Apple"

        if self.collisionContinue():
            # print("collision continue")
            return "Continue"

        # else:
        #     print("colision false")
        #     return False

    def collisionDead(self):
        # Vérifie si l'une des 2 fonctions ont retourné True
        if self.collisionBoard() or self.selfCollision():
            return True
        return False

    def collisionApple(self):
        if (
            self.board.snake.snake_liste[0].getYCoord()
            == self.board.apple.getY() - 20
            and self.board.snake.snake_liste[0].getXCoord()
            == self.board.apple.getX() - 20
        ):
            self.board.score = self.board.apple.Score(self.board.score)
            if self.board.apple.type:
                self.board.apple = self.board.appleType()
                self.board.snake.AddPart()

                return "Apple"
            elif not self.board.apple.type:
                if len(self.board.snake.snake_liste) > 2:
                    self.board.apple = self.board.appleType()
                    self.board.snake.DelPart()
                    return "Apple"
                else:
                    return "Dead"

    def collisionContinue(self):
        match self.movement:
            case "Up":
                if (
                    self.board.snake.snake_liste[0].getYCoord()
                    > self.board.snake.snake_liste[1].getYCoord()
                ):
                    return False
            case "Down":
                if (
                    self.board.snake.snake_liste[0].getYCoord()
                    < self.board.snake.snake_liste[1].getYCoord()
                ):
                    return False
            case "Left":
                if (
                    self.board.snake.snake_liste[0].getXCoord()
                    > self.board.snake.snake_liste[1].getXCoord()
                ):
                    return False
            case "Right":
                if (
                    self.board.snake.snake_liste[0].getXCoord()
                    < self.board.snake.snake_liste[1].getXCoord()
                ):
                    return False
            case _:
                return True

    def collisionBoard(self):
        # Vérifie que le snake ne sort pas du plateau sinon fin de partie
        if (
            self.board.snake.snake_liste[0].getYCoord() == -40
            or self.board.snake.snake_liste[0].getYCoord() == self.board.height
        ):
            return True
        if (
            self.board.snake.snake_liste[0].getXCoord() == -40
            or self.board.snake.snake_liste[0].getXCoord() == self.board.width
        ):
            return True
        return False

    def selfCollision(self):
        # Vérifie que le snake ne se touche pas lui même
        for i in range(1, len(self.board.snake.snake_liste)):
            if (
                self.board.snake.snake_liste[0].getYCoord()
                == self.board.snake.snake_liste[i].getYCoord()
                and self.board.snake.snake_liste[0].getXCoord()
                == self.board.snake.snake_liste[i].getXCoord()
            ):
                return True
        return False
