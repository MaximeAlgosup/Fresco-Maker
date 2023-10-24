import sys
from tkinter import Tk, Label, StringVar


class GuiError:

    @staticmethod
    def onClosing():
        """
        Static method to handle the window close event.

        Example:
            ErrorWindow.onClosing()

        Note:
            This method is called when the user attempts to close the error message window. It exits the application
            gracefully by calling sys.exit(0).
        """
        sys.exit(0)

    def __init__(self, error_message):
        """
        Initialize the error message window.

        Args:
            error_message (str): The error message to display in the window.

        Example:
            error_msg = "An error occurred while solving the Rubik's Cube."
            error_window = ErrorWindow(error_msg)

        Note:
            This constructor sets up the error message window. It configures the window's dimensions, background color,
            title, and icon. It also binds the 'onClosing' method to the window's close event. The error message is displayed
            in the window as a label with a specified font and background color. The main event loop for the window is started
            within this constructor.
        """
        self.errors_win = Tk()
        self.errors_win.title("Fresco Maker: ERROR")

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
