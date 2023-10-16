from tkinter import Tk, Label


class GuiWarning:

    def __init__(self, warning_message):
        # Initialize the warning window
        self.warning_win = Tk()
        self.warning_win.title("Rubik's solver 3000: WARNING")

        # Set the window dimensions and background color
        self.warning_win.geometry("400x75")
        self.warning_win.configure(bg="#ffb121")

        # Disable window resizing and set the window icon
        self.warning_win.resizable(False, False)
        self.warning_win.iconbitmap('./logo/rubiks.ico')

        # Display the warning message as a label with specified font and background color
        Label(self.warning_win, text=warning_message, font=("Arial", 15, "bold"), bg="#ffb121").pack()

        # Start the warning window's main event loop
        self.warning_win.mainloop()
