import sys
from tkinter import Tk, Label, StringVar


class GuiError:

    # Add close all app on closing window
    @staticmethod
    def onClosing():
        # Define a function to exit the application when the window is closed
        sys.exit(0)

    def __init__(self, error_message):
        # Initialize the error message window
        self.errors_win = Tk()
        self.errors_win.title("Rubik's asolver 3000: ERROR")

        # Set the window dimensions and background color
        self.errors_win.geometry("400x75")
        self.errors_win.configure(bg="#ffb121")

        # Disable window resizing and set the window icon
        self.errors_win.resizable(False, False)
        self.errors_win.iconbitmap('./assets/rubiks.ico')

        # Add action on window close event
        self.errors_win.protocol("WM_DELETE_WINDOW", self.onClosing)

        # Display the error message as a label with specified font and background color
        Label(self.errors_win, text=error_message, font=("Arial", 15, "bold"), bg="#ffb121").pack()

        # Start the error window's main event loop
        self.errors_win.mainloop()
