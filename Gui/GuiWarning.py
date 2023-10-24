from tkinter import Tk, Label


class GuiWarning:

    def __init__(self, warning_message):
        """
        Initialize the warning window.

        Args:
            warning_message (str): The warning message to be displayed.

        Example:
            warning_window = RubiksWarningWindow("This is a warning message.")

        Note:
            This constructor initializes the warning window with the specified warning message and sets up its appearance.
            It also binds the 'onClosing' method to the window's close event.
        """
        self.warning_win = Tk()
        self.warning_win.title("Rubik's solver 3000: WARNING")

        # Set the window dimensions and background color
        self.warning_win.geometry("400x75")
        self.warning_win.configure(bg="#ffb121")

        # Disable window resizing and set the window icon
        self.warning_win.resizable(False, False)
        self.warning_win.iconbitmap('./assets/rubiks.ico')

        # Display the warning message as a label with specified font and background color
        Label(self.warning_win, text=warning_message, font=("Arial", 15, "bold"), bg="#ffb121").pack()

        # Start the warning window's main event loop
        self.warning_win.mainloop()
