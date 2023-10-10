import sys
import os
from tkinter import Tk, Checkbutton, Label, Button, Entry, END, StringVar, LEFT, IntVar


class GuiRunner:

    # Add close all app on closing window
    @staticmethod
    def onClosing():
        sys.exit(0)

    def set_data(self):
        print(self.picture_path.get())
        print(self.team_nb.get())
        print(self.is_doc_generate.get())
        self.solver_win.destroy()


    def __init__(self):
        self.team_nb = 1
        self.generate_doc = True
        self.solver_win = Tk()
        self.solver_win.title("Rubik's solver 3000")

        self.solver_win.geometry("500x300")
        self.solver_win.configure(bg="#ffb121")
        self.solver_win.resizable(False, False)
        self.solver_win.iconbitmap('./logo/rubiks.ico')

        # Add action on window close event
        self.solver_win.protocol("WM_DELETE_WINDOW", self.onClosing)

        Label(self.solver_win, text="Picture path:", font=("Arial", 15, "bold"), bg="#ffb121").pack(padx=(55, 300))
        self.picture_path = Entry(self.solver_win, font=("Arial", 25), borderwidth=3, relief="solid")
        self.picture_path.pack(pady=(0, 15))

        Label(self.solver_win, text="Number of teams on the project:", font=("Arial", 15, "bold"), bg="#ffb121").pack(padx=(55, 120))
        self.team_nb = Entry(self.solver_win, font=("Arial", 25), borderwidth=3, relief="solid")
        self.team_nb.insert(END, "1")
        self.team_nb.pack(pady=(0, 15))

        self.is_doc_generate = IntVar()
        self.doc_generation = Checkbutton(self.solver_win, text='Generate all the documentation?', variable=self.is_doc_generate, onvalue=1, font=("Arial", 15, "bold"), bg="#ffb121")
        self.doc_generation.pack()

        # Add login button
        Button(self.solver_win, text="Valid", font=("Arial", 25), borderwidth=1, relief="solid",
               command=self.set_data).pack(side=LEFT, pady=(5, 20), padx=(190, 20))

        self.solver_win.mainloop()
