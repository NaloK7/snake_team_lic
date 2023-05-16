import tkinter as tk
import AppleFunction
from tkinter import Toplevel


class EndGameWindow(Toplevel):
    def __init__(self, board):
        Toplevel.__init__(self, board.master_window)
        self.master_win = board.master_window
        self.master_win.withdraw()

        self.board = board
        self.title("fin de parti")
        self.geometry("300x200")
        self.end_window = tk.Frame(self)
        self.entreScore = 0

        self.leaderboard = tk.Frame(self.end_window)
        self.record = tk.Label(
            self.end_window, text="score: " + str(board.score)
        ).pack()

        self.info = tk.Frame(self.end_window)
        self.pseudo = tk.Label(self.info, text="Peudo: ").pack(side="left")

        self.input = tk.Entry(self.info)
        self.input.pack(side="right")
        self.info.pack()
        self.submitButton = tk.Button(
            self.leaderboard, text="enregistrer", command=self.saveScore
        )
        self.submitButton.pack()
        self.leaderboard.pack()

        self.again = tk.Frame(self.end_window)
        self.again.pack()
        self.play_again = tk.Button(
            self.again, text="rejouer", command=self.lauchAgain
        )
        self.play_again.pack()

        self.bouton_quit = tk.Button(
            self.end_window, text="fermer", command=self.quitter
        )
        self.bouton_quit.pack()

        self.end_window.pack()
        # from Game import window

    def saveScore(self):
        if self.entreScore == 0:
            AppleFunction.Save(self.board.score, self.input.get())
            self.board.master_window.updateLeaderBoard()
            self.entreScore = 1

    def lauchAgain(self):
        self.destroy()
        self.board.master_window.LaunchSnakeWindow()

    def quitter(self):
        print("quitter EgW")
        self.board.Quit()
        self.destroy()
