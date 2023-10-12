import sys
from tkinter import Tk, Label, StringVar


class GuiError:

    # Add close all app on closing window
    @staticmethod
    def onClosing():
        sys.exit(0)

    def __init__(self, error_message):
        self.errors_win = Tk()
        self.errors_win.title("Rubik's solver 3000: ERROR")

        self.errors_win.geometry("400x75")
        self.errors_win.configure(bg="#ffb121")
        self.errors_win.resizable(False, False)
        self.errors_win.iconbitmap('./logo/rubiks.ico')

        # Add action on window close event
        self.errors_win.protocol("WM_DELETE_WINDOW", self.onClosing)

        Label(self.errors_win, text=error_message, font=("Arial", 15, "bold"), bg="#ffb121").pack()

        self.errors_win.mainloop()
