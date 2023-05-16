import tkinter as tk
from tkinter import ttk
import board
import os


class MainWindow(tk.Tk):
    """
    fenetre principal pour lancer le jeu et afficher le leaderboard
    """

    def __init__(self):
        super().__init__()
        # liste de test pour le leaderboard
        self.geometry("500x500+50+50")
        self.title("team project")

        # le titre
        self.frame_title = tk.Frame(self)
        self.frame_title.pack()
        self.label_title = tk.Label(
            self.frame_title,
            text="Team Project",
            font=("Reem Kufi", 20, "underline"),
            fg="green",
        )
        self.label_title.pack(ipady=30)

        # le bouton de lancement du jeu
        self.frame_launch_button = tk.Frame(self)
        self.frame_launch_button.pack()
        self.button_launch_snake = tk.Button(
            self.frame_launch_button,
            text="SNAKE",
            command=self.LaunchSnakeWindow,
            bg="red",
            font=("Reem Kufi", 10, "bold"),
        )
        self.button_launch_snake.pack(pady=5, ipadx=10, ipady=10)

        # le leaderboard
        self.frame_leaderboard_title = tk.Frame(self)
        self.frame_leaderboard_title.pack()
        self.label_leaderboard = tk.Label(
            self.frame_leaderboard_title, text="", font=("Reem Kufi", 20)
        )
        self.label_leaderboard.pack()

        self.frame_table_leaderboard = tk.Frame(self)
        self.frame_table_leaderboard.pack(side="bottom")

        self.columns = ("number", "pseudo", "date", "score")

        self.table_leadearboard = ttk.Treeview(
            self.frame_table_leaderboard, columns=self.columns, show="headings"
        )
        self.table_leadearboard.column("number", anchor="center", width=30)
        self.table_leadearboard.column("pseudo", anchor="center", width=100)
        self.table_leadearboard.column("date", anchor="center", width=100)
        self.table_leadearboard.column("score", anchor="center", width=200)

        self.table_leadearboard.heading("number", text="N°")
        self.table_leadearboard.heading("pseudo", text="Pseudo")
        self.table_leadearboard.heading("date", text="Date")
        self.table_leadearboard.heading("score", text="Score")
        self.table_leadearboard.pack(pady=40)

        self.updateLeaderBoard()
        self.mainloop()

    def LaunchSnakeWindow(self):
        """
        lance la fenetre de jeu pygame du snake
        para: cette instance
        """
        tableau = board.Board(self)
        tableau

    def updateLeaderBoard(self):
        """
        verifie le fichier txt pour mettre a jour
        l'affichage du leaderboard
        """
        for item in self.table_leadearboard.get_children():
            self.table_leadearboard.delete(item)

        list_leader = self.file_to_list()
        print("update display learderboard")
        for elem in list_leader:
            self.table_leadearboard.insert("", tk.END, values=elem)

    def file_to_list(self):
        """
        return a list of [ [top1],..., [top10] ]
        """
        list_of_leader = []
        data_path = os.getcwd() + "\Data.txt"
        file = open(data_path, "r")
        line = file.readline()
        while line != "":
            line_in_list = line.replace("\n", "").split(";")
            list_of_leader.append(line_in_list)
            line = file.readline()
        file.close()
        return list_of_leader
