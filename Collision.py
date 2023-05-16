import endGameWindow

class collision:
    """
    Reçoit plusieurs objets et un string:

    -Un snake

    -Un board

    -Un apple

    -un string qui contient le mouvement actuel

    Renvoi:

    -Dead = Fin de partie

    -Add = Ajoute une partie au snake

    -Del = Enlève une partie au snake

    -Continue = lance le prochain mouvement dans la même direction

    -False = Aucune collision
    """

    def __init__(self, board):
        # Récupère les 3 éléments et les initialises
        self.snake = board.snake
        self.board = board
        self.apple = board.apple

    def getCollision(self, move_choice):
        if self.collisionDead():
            print("collision dead")
            return "Dead"
        
        if self.collisionApple() == "Apple":
            print("collision apple")
            return "Apple"

        if not self.collisionContinue(move_choice):
            print("collision continue")
            return "Continue"
        
        else:
            print("colision false")
            return False

    def collisionDead(self):
        # Vérifie si l'une des 2 fonctions ont retourné True
        if self.collisionBoard() or self.selfCollision():
            return True
        return False

    def collisionApple(self):
        print("in aplle func")
        if (self.snake.snake_liste[0].getYCoord() == self.apple.y and self.snake.snake_liste[0].getXCoord() == self.apple.x):
            print("collide")
            if self.apple.type:
                self.snake.AddPart()
                print("good")
                return "Apple"
            elif not self.apple.type:
                self.snake.DelPart()
                print("bad")
                return "Apple"
        

    def collisionContinue(self, move_choice):
        match move_choice:
            case "Up":
                if (
                    self.snake.snake_liste[0].getYCoord()
                    > self.snake.snake_liste[1].getYCoord()
                ):
                    return False
            case "Down":
                if (
                    self.snake.snake_liste[0].getYCoord()
                    < self.snake.snake_liste[1].getYCoord()
                ):
                    return False
            case "Left":
                if (
                    self.snake.snake_liste[0].getXCoord()
                    > self.snake.snake_liste[1].getXCoord()
                ):
                    return False
            case "Right":
                if (
                    self.snake.snake_liste[0].getXCoord()
                    < self.snake.snake_liste[1].getXCoord()
                ):
                    return False
            case _:
                return True

    def collisionBoard(self):
        # Vérifie que le snake ne sort pas du plateau sinon fin de partie
        if (
            self.snake.snake_liste[0].getYCoord() == -40
            or self.snake.snake_liste[0].getYCoord() == self.board.height
        ):
            return True
        if (
            self.snake.snake_liste[0].getXCoord() == -40
            or self.snake.snake_liste[0].getXCoord() == self.board.width
        ):
            return True
        return False

    def selfCollision(self):
        # Vérifie que le snake ne se touche pas lui même
        for i in range(1, len(self.snake.snake_liste)):
            if (
                self.snake.snake_liste[0].getYCoord()
                == self.snake.snake_liste[i].getYCoord()
                and self.snake.snake_liste[0].getXCoord()
                == self.snake.snake_liste[i].getXCoord()
            ):
                return True
        return False
