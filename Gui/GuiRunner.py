import sys
from tkinter import Tk, Checkbutton, Label, Button, Entry, END, StringVar, LEFT, IntVar


class GuiRunner:

    # Add close all app on closing window
    @staticmethod
    def onClosing():
        """
        Static method to handle the window close event.

        Example:
            RubiksSolverWindow.onClosing()

        Note:
            This method is called when the user attempts to close the application window. It exits the application
            gracefully by calling sys.exit(0).
        """
        sys.exit(0)

    def get_data(self):
        """
        Get user input data.

        Returns:
            list: A list containing user input data [picture_path, team_nb, is_doc_generate].

        Example:
            data = self.get_data()

        Note:
            This method retrieves user input data from the GUI elements and returns it as a list.
        """
        return [self.picture_path, self.team_nb, self.is_doc_generate]

    def set_data(self):
        """
        Set data based on user input.

        Example:
            self.set_data()

        Note:
            This method reads user input data from GUI elements, such as input fields and checkboxes, and updates the
            corresponding attributes of the class.
        """
        self.picture_path = self.picture_path.get()
        self.team_nb = self.team_nb.get()
        self.is_doc_generate = self.is_doc_generate.get()
        self.solver_win.destroy()

    def run_window(self):
        """
        Start the main event loop for the GUI window.

        Example:
            self.run_window()

        Note:
            This method initiates the main event loop for the GUI window, allowing the user to interact with the
            application.
        """
        self.solver_win.mainloop()

    def __init__(self):
        """
        Initialize the Rubik's Solver window and default values.

        Example:
            solver_window = RubiksSolverWindow()

        Note:
            This constructor initializes the main GUI window, default values, and various elements, such as labels, input
            fields, checkboxes, and buttons. It also sets up the appearance and configuration of the window, and binds the
            'onClosing' method to the window's close event.
        """
        self.team_nb = 1
        self.generate_doc = True
        self.solver_win = Tk()
        self.solver_win.title("Rubik's solver 3000")

        # Configure window dimensions and appearance
        self.solver_win.geometry("500x300")
        self.solver_win.configure(bg="#ffb121")
        self.solver_win.resizable(False, False)
        self.solver_win.iconbitmap('./assets/rubiks.ico')

        # Add action on window close event
        self.solver_win.protocol("WM_DELETE_WINDOW", self.onClosing)

        # Create and configure GUI elements: labels, input fields, checkboxes, and buttons
        Label(self.solver_win, text="Picture path:", font=("Arial", 15, "bold"), bg="#ffb121").pack(padx=(55, 300))
        self.picture_path = Entry(self.solver_win, font=("Arial", 25), borderwidth=3, relief="solid")
        self.picture_path.pack(pady=(0, 15))

        Label(self.solver_win, text="Number of teams on the project:", font=("Arial", 15, "bold"), bg="#ffb121").pack(
            padx=(55, 120))
        self.team_nb = Entry(self.solver_win, font=("Arial", 25), borderwidth=3, relief="solid")
        self.team_nb.insert(END, "1")
        self.team_nb.pack(pady=(0, 15))

        self.is_doc_generate = IntVar()
        self.doc_generation = Checkbutton(self.solver_win, text='Generate all the documentation?',
                                          variable=self.is_doc_generate, onvalue=1, font=("Arial", 15, "bold"),
                                          bg="#ffb121")
        self.doc_generation.pack()

        # Add validation button
        Button(self.solver_win, text="Valid", font=("Arial", 25), borderwidth=1, relief="solid",
               command=self.set_data).pack(side=LEFT, pady=(5, 20), padx=(190, 20))
