import sys
from tkinter import Tk, Label, StringVar


class GuiWarning:

    def __init__(self, warning_message):
        self.warning_win = Tk()
        self.warning_win.title("Rubik's solver 3000: WARNING")

        self.warning_win.geometry("400x75")
        self.warning_win.configure(bg="#ffb121")
        self.warning_win.resizable(False, False)
        self.warning_win.iconbitmap('./logo/rubiks.ico')

        Label(self.warning_win, text=warning_message, font=("Arial", 15, "bold"), bg="#ffb121").pack()

        self.warning_win.mainloop()
