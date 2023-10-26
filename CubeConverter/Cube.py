class Cube:
    def __init__(self):
        """
        Initialize a Rubik's Cube object with the default configuration.

        The cube is represented as a list of faces, with each face being a list of stickers.
        The face colors are represented by characters: 'R' (red), 'G' (green), 'B' (blue),
        'W' (white), 'Y' (yellow), and 'O' (orange).

        The cube's faces are arranged as follows:
        - UP (0): White face
        - LEFT (1): Red face
        - FACE (2): Blue face
        - RIGHT (3): Orange face
        - BACK (4): Green face
        - DOWN (5): Yellow face

        The cube's moves_history is initialized as an empty list.

        If the cube's initial configuration does not match the base configuration, the program exits.

        Example:
            my_cube = RubiksCube()
            # Initializes a Rubik's Cube object with the default configuration.

        Note:
            You can customize the initial configuration by modifying the face lists (e.g., self.white_face) if needed.
        """
        self.red_face = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
        self.green_face = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
        self.blue_face = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
        self.white_face = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        self.yellow_face = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']
        self.orange_face = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        self.UP = 0
        self.LEFT = 1
        self.FACE = 2
        self.RIGHT = 3
        self.BACK = 4
        self.DOWN = 5
        self.cube = [self.white_face, self.red_face, self.blue_face, self.orange_face, self.green_face,
                     self.yellow_face]
        self.moves_history = []
        if not self.__base_check():
            exit(1)

    ####################################################################################################################
    # MOVES
    ####################################################################################################################

    def move_center(self, matrix):
        """
        Move a face from the center based on a center color.

        This method repositions the faces of a Rubik's Cube based on the center color of a face. The new arrangement
        depends on the color of the center of the specified face.

        Args:
            matrix (list): A color matrix representing the face with the center color.

        Returns:
            None

        Example:
            If the 'matrix' represents a face with the center color 'R' (Red), the method repositions the cube faces
            accordingly.
        """

        center_color = matrix[4]
        match center_color:
            case 'R':
                self.cube = [self.blue_face, self.white_face, self.red_face, self.yellow_face, self.orange_face,
                             self.green_face]
            case 'B':
                self.cube = [self.white_face, self.red_face, self.blue_face, self.orange_face, self.green_face,
                             self.yellow_face]
            case 'O':
                self.cube = [self.white_face, self.blue_face, self.orange_face, self.green_face, self.red_face,
                             self.yellow_face]
            case 'G':
                self.cube = [self.white_face, self.orange_face, self.green_face, self.red_face, self.blue_face,
                             self.yellow_face]
            case 'W':
                self.cube = [self.green_face, self.red_face, self.white_face, self.orange_face, self.yellow_face,
                             self.blue_face]
            case 'Y':
                self.cube = [self.green_face, self.orange_face, self.yellow_face, self.red_face, self.white_face,
                             self.blue_face]

    def move_u(self, x=1):
        """
        Move the 'U' face of a Rubik's Cube 'x' times.

        This method rotates the 'U' (Up) face of the cube 'x' times. It also updates the positions of adjacent faces
        accordingly and records the moves in the history.

        Args:
            x (int, optional): The number of times to rotate the 'U' face. Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'U' face will be rotated twice in a row, and the corresponding moves will be added to the
            move history.
        """

        for i in range(x):
            new_up_face = self.__rotate_matrix(self.UP)

            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[self.RIGHT][0], self.cube[self.RIGHT][1], self.cube[self.RIGHT][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            # move left face
            face_nb = self.LEFT
            new_left_face = [self.cube[self.FACE][0], self.cube[self.FACE][1], self.cube[self.FACE][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            # move right face
            face_nb = self.RIGHT
            new_right_face = [self.cube[self.BACK][0], self.cube[self.BACK][1], self.cube[self.BACK][2],
                              self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                              self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[self.LEFT][0], self.cube[self.LEFT][1], self.cube[self.LEFT][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            self.cube[self.UP] = new_up_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.RIGHT] = new_right_face
            self.cube[self.BACK] = new_back_face
            # Add the move to history
            self.moves_history.append("U")
        if not self.__base_check():
            exit(1)

    def move_d(self, x=1):
        """
        Move the 'D' face of a Rubik's Cube 'x' times.

        This method rotates the 'D' (Down) face of the cube 'x' times. It also updates the positions of adjacent faces
        accordingly and records the moves in the history.

        Args:
            x (int, optional): The number of times to rotate the 'D' face. Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'D' face will be rotated twice in a row, and the corresponding moves will be added to the
            move history.
        """

        for i in range(x):
            new_down_face = self.__rotate_matrix(self.DOWN)

            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.LEFT][6], self.cube[self.LEFT][7], self.cube[self.LEFT][8]]

            # move left face
            face_nb = self.LEFT
            new_left_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.BACK][6], self.cube[self.BACK][7], self.cube[self.BACK][8]]

            # move right face
            face_nb = self.RIGHT
            new_right_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                              self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                              self.cube[self.FACE][6], self.cube[self.FACE][7], self.cube[self.FACE][8]]

            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.RIGHT][6], self.cube[self.RIGHT][7], self.cube[self.RIGHT][8]]

            self.cube[self.DOWN] = new_down_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.RIGHT] = new_right_face
            self.cube[self.BACK] = new_back_face

            # Add the move to history
            self.moves_history.append("D")
        if not self.__base_check():
            exit(1)

    def move_u_p(self, x=1):
        """
        Move the 'U' face of a Rubik's Cube in a counterclockwise ('U') 'x' times.

        This method rotates the 'U' (Up) face of the cube in a counterclockwise 'x' times. It also updates the positions
        of adjacent faces accordingly and records the moves in the history.

        Args:
            x (int, optional): The number of times to rotate the 'U' face in counterclockwise. Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'U' face will be rotated in a counterclockwise twice in a row, and the corresponding moves will
            be added to the move history.
        """

        for i in range(x):
            new_up_face = self.__rotate_matrix_reverse(self.UP)
            # Define the faces to update in a loop
            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[self.LEFT][0], self.cube[self.LEFT][1], self.cube[self.LEFT][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            # move left face
            face_nb = self.LEFT
            new_left_face = [self.cube[self.BACK][0], self.cube[self.BACK][1], self.cube[self.BACK][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            # move right face
            face_nb = self.RIGHT
            new_right_face = [self.cube[self.FACE][0], self.cube[self.FACE][1], self.cube[self.FACE][2],
                              self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                              self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[self.RIGHT][0], self.cube[self.RIGHT][1], self.cube[self.RIGHT][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            self.cube[self.UP] = new_up_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.RIGHT] = new_right_face
            self.cube[self.BACK] = new_back_face
            # Add the move to history
            self.moves_history.append("U'")
        if not self.__base_check():
            exit(1)

    def move_d_p(self, x=1):
        """
        Move the 'D' face of a Rubik's Cube in a counterclockwise ('D') 'x' times.

        This method rotates the 'D' (Down) face of the cube in a counterclockwise 'x' times. It also updates the positions
        of adjacent faces accordingly and records the moves in the history.

        Args:
            x (int, optional): The number of times to rotate the 'D' face in counterclockwise. Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'D' face will be rotated in a counterclockwise twice in a row, and the corresponding moves will
            be added to the move history.
        """

        for i in range(x):
            new_down_face = self.__rotate_matrix_reverse(self.DOWN)

            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.RIGHT][6], self.cube[self.RIGHT][7], self.cube[self.RIGHT][8]]

            # move left face
            face_nb = self.LEFT
            new_left_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.FACE][6], self.cube[self.FACE][7], self.cube[self.FACE][8]]

            # move right face
            face_nb = self.RIGHT
            new_right_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                              self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                              self.cube[self.BACK][6], self.cube[self.BACK][7], self.cube[self.BACK][8]]

            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.LEFT][6], self.cube[self.LEFT][7], self.cube[self.LEFT][8]]

            self.cube[self.DOWN] = new_down_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.RIGHT] = new_right_face
            self.cube[self.BACK] = new_back_face

            self.moves_history.append("D'")
        if not self.__base_check():
            exit(1)

    def move_l(self, x=1):
        """
        Move the 'L' face of a Rubik's Cube 'x' times.

        This method rotates the 'L' (Left) face of the cube 'x' times and updates the positions of adjacent faces accordingly.
        It also records the moves in the move history.

        Args:
            x (int, optional): The number of times to rotate the 'L' face. Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'L' face will be rotated twice, and the corresponding moves will be added to the move history.
        """

        for i in range(x):
            # move left face
            new_left_face = self.__rotate_matrix(self.LEFT)
            # move up face
            face_nb = self.UP
            new_up_face = [self.cube[self.BACK][8], self.cube[face_nb][1], self.cube[face_nb][2],
                           self.cube[self.BACK][5], self.cube[face_nb][4], self.cube[face_nb][5],
                           self.cube[self.BACK][2], self.cube[face_nb][7], self.cube[face_nb][8]]
            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[self.UP][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.UP][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.UP][6], self.cube[face_nb][7], self.cube[face_nb][8]]
            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.DOWN][6],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.DOWN][3],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.DOWN][0]]
            # move down face
            face_nb = self.DOWN
            new_down_face = [self.cube[self.FACE][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.FACE][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.FACE][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            self.cube[self.UP] = new_up_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.BACK] = new_back_face
            self.cube[self.DOWN] = new_down_face

            # Add the move to history
            self.moves_history.append("L")
        if not self.__base_check():
            exit(1)

    def move_l_p(self, x=1):
        """
        Move the 'L' face of a Rubik's Cube counterclockwise ('L' or 'L'') 'x' times.

        This method rotates the 'L' (Left) face of the cube counterclockwise ('L') 'x' times and updates the positions
        of adjacent faces accordingly. It also records the moves in the move history.

        Args:
            x (int, optional): The number of times to rotate the 'L' face counterclockwise ('L'). Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'L' face will be rotated counterclockwise ('L') twice, and the corresponding moves will
            be added to the move history.
        """

        for i in range(x):
            # move left face
            new_left_face = self.__rotate_matrix_reverse(self.LEFT)
            # move up face
            face_nb = self.UP
            new_up_face = [self.cube[self.FACE][0], self.cube[face_nb][1], self.cube[face_nb][2],
                           self.cube[self.FACE][3], self.cube[face_nb][4], self.cube[face_nb][5],
                           self.cube[self.FACE][6], self.cube[face_nb][7], self.cube[face_nb][8]]
            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[self.DOWN][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.DOWN][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.DOWN][6], self.cube[face_nb][7], self.cube[face_nb][8]]
            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.UP][6],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.UP][3],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.UP][0]]
            # move down face
            face_nb = self.DOWN
            new_down_face = [self.cube[self.BACK][8], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.BACK][5], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.BACK][2], self.cube[face_nb][7], self.cube[face_nb][8]]

            self.cube[self.UP] = new_up_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.BACK] = new_back_face
            self.cube[self.DOWN] = new_down_face

            # Add the move to history
            self.moves_history.append("L'")
        if not self.__base_check():
            exit(1)

    def move_r(self, x=1):
        """
        Move the 'R' face of a Rubik's Cube clockwise ('R' or 'R'') 'x' times.

        This method rotates the 'R' (Right) face of the cube clockwise ('R') 'x' times and updates the positions
        of adjacent faces accordingly. It also records the moves in the move history.

        Args:
            x (int, optional): The number of times to rotate the 'R' face clockwise ('R'). Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'R' face will be rotated clockwise ('R') twice, and the corresponding moves will be
            added to the move history.
        """

        for i in range(x):
            # move right face
            new_right_face = self.__rotate_matrix(self.RIGHT)
            # move up face
            face_nb = self.UP
            new_up_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.FACE][2],
                           self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.FACE][5],
                           self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.FACE][8]]
            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.DOWN][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.DOWN][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.DOWN][8]]
            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[self.UP][8], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.UP][5], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.UP][2], self.cube[face_nb][7], self.cube[face_nb][8]]
            # move down face
            face_nb = self.DOWN
            new_down_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.BACK][6],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.BACK][3],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.BACK][0]]

            self.cube[self.UP] = new_up_face
            self.cube[self.RIGHT] = new_right_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.BACK] = new_back_face
            self.cube[self.DOWN] = new_down_face

            # Add the move to history
            self.moves_history.append("R")
        if not self.__base_check():
            exit(1)

    def move_r_p(self, x=1):
        """
        Move the 'R' face of a Rubik's Cube counterclockwise ('R'') 'x' times.

        This method rotates the 'R' (Right) face of the cube counterclockwise ('R'') 'x' times and updates the positions
        of adjacent faces accordingly. It also records the moves in the move history.

        Args:
            x (int, optional): The number of times to rotate the 'R' face counterclockwise ('R''). Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'R' face will be rotated counterclockwise ('R'') twice, and the corresponding moves will be
            added to the move history.
        """

        for i in range(x):
            # move right face
            new_right_face = self.__rotate_matrix_reverse(self.RIGHT)
            # move up face
            face_nb = self.UP
            new_up_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.BACK][6],
                           self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.BACK][3],
                           self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.BACK][0]]
            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.UP][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.UP][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.UP][8]]
            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[self.DOWN][8], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.DOWN][5], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.DOWN][2], self.cube[face_nb][7], self.cube[face_nb][8]]
            # move down face
            face_nb = self.DOWN
            new_down_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.FACE][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.FACE][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.FACE][8]]
            self.cube[self.UP] = new_up_face
            self.cube[self.RIGHT] = new_right_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.BACK] = new_back_face
            self.cube[self.DOWN] = new_down_face
            # Add the move to history
            self.moves_history.append("R'")
        if not self.__base_check():
            exit(1)

    def move_f(self, x=1):
        """
        Move the 'F' face of a Rubik's Cube counterclockwise ('F') 'x' times.

        This method rotates the 'F' (Front) face of the cube counterclockwise ('F') 'x' times and updates the positions of
        adjacent faces accordingly. It also records the moves in the move history.

        Args:
            x (int, optional): The number of times to rotate the 'F' face counterclockwise ('F'). Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'F' face will be rotated counterclockwise ('F') twice, and the corresponding moves will be
            added to the move history.
        """

        for i in range(x):
            # move right face
            new_main_face = self.__rotate_matrix(self.FACE)
            face_nb = self.LEFT
            new_left_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.DOWN][0],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.DOWN][1],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.DOWN][2]]
            face_nb = self.UP
            new_up_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                           self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                           self.cube[self.LEFT][8], self.cube[self.LEFT][5], self.cube[self.LEFT][2]]
            face_nb = self.RIGHT
            new_right_face = [self.cube[self.UP][6], self.cube[face_nb][1], self.cube[face_nb][2],
                              self.cube[self.UP][7], self.cube[face_nb][4], self.cube[face_nb][5],
                              self.cube[self.UP][8], self.cube[face_nb][7], self.cube[face_nb][8]]
            face_nb = self.DOWN
            new_down_face = [self.cube[self.RIGHT][6], self.cube[self.RIGHT][3], self.cube[self.RIGHT][0],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            self.cube[self.FACE] = new_main_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.UP] = new_up_face
            self.cube[self.RIGHT] = new_right_face
            self.cube[self.DOWN] = new_down_face
            # Add the move to history
            self.moves_history.append("F")
        if not self.__base_check():
            exit(1)

    def move_f_p(self, x=1):
        """
        Move the 'F' face of a Rubik's Cube counterclockwise ('F') 'x' times.

        This method rotates the 'F' (Front) face of the cube counterclockwise ('F') 'x' times and updates the positions of adjacent
        faces accordingly. It also records the moves in the move history.

        Args:
            x (int, optional): The number of times to rotate the 'F' face counterclockwise ('F'). Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'F' face will be rotated counterclockwise ('F') twice, and the corresponding moves will be added to
            the move history.
        """

        for i in range(x):
            # move right face
            new_main_face = self.__rotate_matrix_reverse(self.FACE)
            face_nb = self.LEFT
            new_left_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.UP][8],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.UP][7],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.UP][6]]
            face_nb = self.UP
            new_up_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                           self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                           self.cube[self.RIGHT][0], self.cube[self.RIGHT][3], self.cube[self.RIGHT][6]]
            face_nb = self.RIGHT
            new_right_face = [self.cube[self.DOWN][2], self.cube[face_nb][1], self.cube[face_nb][2],
                              self.cube[self.DOWN][1], self.cube[face_nb][4], self.cube[face_nb][5],
                              self.cube[self.DOWN][0], self.cube[face_nb][7], self.cube[face_nb][8]]
            face_nb = self.DOWN
            new_down_face = [self.cube[self.LEFT][2], self.cube[self.LEFT][5], self.cube[self.LEFT][8],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            self.cube[self.FACE] = new_main_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.UP] = new_up_face
            self.cube[self.RIGHT] = new_right_face
            self.cube[self.DOWN] = new_down_face
            # Add the move to history
            self.moves_history.append("F'")
        if not self.__base_check():
            exit(1)

    def move_b(self, x=1):
        """
        Move the 'B' face of a Rubik's Cube clockwise ('B') 'x' times.

        This method rotates the 'B' (Back) face of the cube clockwise ('B') 'x' times and updates the positions of adjacent
        faces accordingly. It also records the moves in the move history.

        Args:
            x (int, optional): The number of times to rotate the 'B' face clockwise ('B'). Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'B' face will be rotated clockwise ('B') twice, and the corresponding moves will be added to
            the move history.
        """

        for i in range(x):
            # move right face
            new_back_face = self.__rotate_matrix(self.BACK)
            face_nb = self.UP
            new_up_face = [self.cube[self.RIGHT][2], self.cube[self.RIGHT][5], self.cube[self.RIGHT][8],
                           self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                           self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            face_nb = self.LEFT
            new_left_face = [self.cube[self.UP][2], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.UP][1], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.UP][0], self.cube[face_nb][7], self.cube[face_nb][8]]
            face_nb = self.DOWN
            new_down_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.LEFT][0], self.cube[self.LEFT][3], self.cube[self.LEFT][6]]
            face_nb = self.RIGHT
            new_right_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.DOWN][8],
                              self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.DOWN][7],
                              self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.DOWN][6]]

            self.cube[self.BACK] = new_back_face
            self.cube[self.UP] = new_up_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.DOWN] = new_down_face
            self.cube[self.RIGHT] = new_right_face
            # Add the move to history
            self.moves_history.append("B")
        if not self.__base_check():
            exit(1)

    def move_b_p(self, x=1):
        """
        Move the 'B' face of a Rubik's Cube counterclockwise ('B') 'x' times.

        This method rotates the 'B' (Back) face of the cube counterclockwise ('B') 'x' times and updates the positions of adjacent
        faces accordingly. It also records the moves in the move history.

        Args:
            x (int, optional): The number of times to rotate the 'B' face counterclockwise ('B'). Default is 1.

        Returns:
            None

        Example:
            If 'x' is 2, the 'B' face will be rotated counterclockwise ('B') twice, and the corresponding moves will be added
            to the move history.
        """

        for i in range(x):
            # move right face
            new_back_face = self.__rotate_matrix_reverse(self.BACK)
            face_nb = self.UP
            new_up_face = [self.cube[self.LEFT][6], self.cube[self.LEFT][3], self.cube[self.LEFT][0],
                           self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                           self.cube[face_nb][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            face_nb = self.LEFT
            new_left_face = [self.cube[self.DOWN][6], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.DOWN][7], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.DOWN][8], self.cube[face_nb][7], self.cube[face_nb][8]]
            face_nb = self.DOWN
            new_down_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.RIGHT][8], self.cube[self.RIGHT][5], self.cube[self.RIGHT][2]]
            face_nb = self.RIGHT
            new_right_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.UP][0],
                              self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.UP][1],
                              self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.UP][2]]

            self.cube[self.BACK] = new_back_face
            self.cube[self.UP] = new_up_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.DOWN] = new_down_face
            self.cube[self.RIGHT] = new_right_face
            # Add the move to history
            self.moves_history.append("B'")
        if not self.__base_check():
            exit(1)

    ####################################################################################################################
    # ACCESSORS
    ####################################################################################################################
    def get_cube(self):
        """
        Get the current state of the Rubik's Cube as a string.

        Returns a string representing the current state of the Rubik's Cube, where each character corresponds to a
        sticker on the cube.

        Returns:
            str: A string representing the Rubik's Cube's current state.

        Example:
            cube_string = cube.get_cube()
            # cube_string may look like "WWWWWWWWWGGGGGGGGGBBBBBBBBBBRRRRRRRRROOOOOOOOOYYYYYYYYY"
        """
        string_res = ""
        for big_face in self.cube:
            for face in big_face:
                string_res += face
        return string_res

    def get_matrix_cube(self):
        """
        Get the current state of the Rubik's Cube as a matrix.

        Returns a list of lists representing the current state of the Rubik's Cube, where each sub-list represents a face
        of the cube.

        Returns:
            list: A matrix representing the Rubik's Cube's current state.

        Example:
            cube_matrix = cube.get_matrix_cube()
            # cube_matrix may be a 2D list with colors representing the cube's current state.
        """
        return self.cube

    def get_moves(self):
        """
        Get the history of moves made on the Rubik's Cube.

        Returns a list of strings containing the history of moves made on the Rubik's Cube.

        Returns:
            list: A list of strings representing the moves history.

        Example:
            moves_history = cube.get_moves()
            # moves_history may include ["R", "U'", "F", "L'", "D", ...]
        """
        return self.moves_history

    ####################################################################################################################
    # FACE SOLVER ALGORITHM
    ####################################################################################################################

    def get_top_crown_edges(self):
        return [
            {"moves": [["U'", 1]], "color": self.cube[self.LEFT][1]},
            {"moves": [["U", 1]], "color": self.cube[self.RIGHT][1]},
            {"moves": [["U", 2]], "color": self.cube[self.BACK][1]},
            {"moves": [["U'", 1], ["R'", 1], ["U", 1], ["F'", 1]], "color": self.cube[self.UP][7]},
            {"moves": [["F", 2], ["U'", 1], ["R'", 1], ["U", 1], ["F'", 1]], "color": self.cube[self.DOWN][1]}
        ]

    def get_bottom_crown_edges(self):
        return [
            {"moves": [["D", 1]], "color": self.cube[self.LEFT][7]},
            {"moves": [["D'", 1]], "color": self.cube[self.RIGHT][7]},
            {"moves": [["D", 2]], "color": self.cube[self.BACK][7]},
            {"moves": [["B'", 2], ["D'", 1], ["F'", 1], ["R", 1], ["F", 1]], "color": self.cube[self.UP][1]},
            {"moves": [["B", 1], ["R", 1], ["D'", 1]], "color": self.cube[self.DOWN][7]}
        ]

    def get_left_crown_edges(self):
        return [
            {"moves": [["L", 1]], "color": self.cube[self.UP][3]},
            {"moves": [["B", 1], ["L'", 1], ["F'", 1], ["D", 1], ["F", 1]], "color": self.cube[self.UP][1]},
            {"moves": [["U", 2], ["L", 1], ["U", 2]], "color": self.cube[self.UP][5]},
            {"moves": [["L'", 1]], "color": self.cube[self.DOWN][3]},
            {"moves": [["D", 2], ["L'", 1], ["D", 2]], "color": self.cube[self.DOWN][5]},
            {"moves": [["D", 1], ["L'", 1], ["D'", 1]], "color": self.cube[self.DOWN][7]},
            {"moves": [["L'", 1], ["B'", 1], ["U'", 1], ["L", 1], ["U", 1]], "color": self.cube[self.LEFT][1]},
            {"moves": [["B'", 1], ["U'", 1], ["L", 1], ["U", 1]], "color": self.cube[self.LEFT][3]},
            {"moves": [["L'", 2], ["B'", 1], ["U'", 1], ["L", 1], ["U", 1]], "color": self.cube[self.LEFT][5]},
            {"moves": [["F'", 1], ["D", 1], ["F", 1]], "color": self.cube[self.LEFT][7]},
            {"moves": [["F", 1], ["U", 1], ["F'", 1]], "color": self.cube[self.RIGHT][1]},
            {"moves": [["B", 1], ["U'", 1], ["L", 1], ["U", 1]], "color": self.cube[self.RIGHT][5]},
            {"moves": [["R'", 1], ["B", 1], ["R", 1], ["U'", 1], ["L", 1], ["U", 1]],
             "color": self.cube[self.RIGHT][7]},
            {"moves": [["B", 1], ["L", 2]], "color": self.cube[self.BACK][1]},
            {"moves": [["L", 2]], "color": self.cube[self.BACK][5]},
            {"moves": [["B'", 2], ["L", 2]], "color": self.cube[self.BACK][3]},
            {"moves": [["B'", 1], ["L", 2]], "color": self.cube[self.BACK][7]}
        ]

    def get_right_crown_edges(self):
        return [
            {"moves": [["U", 1], ["R'", 1], ["U'", 1]], "color": self.cube[self.UP][1]},
            {"moves": [["U", 2], ["R'", 1], ["U", 2]], "color": self.cube[self.UP][3]},
            {"moves": [["R'", 1]], "color": self.cube[self.UP][5]},
            {"moves": [["D", 2], ["R", 1], ["D", 2]], "color": self.cube[self.DOWN][3]},
            {"moves": [["R", 1]], "color": self.cube[self.DOWN][5]},
            {"moves": [["D'", 1], ["R", 1], ["D", 1]], "color": self.cube[self.DOWN][5]},
            {"moves": [["F'", 1], ["U'", 1], ["F", 1]], "color": self.cube[self.LEFT][1]},
            {"moves": [["B'", 1], ["U", 1], ["R'", 1], ["U'", 1]], "color": self.cube[self.LEFT][3]},
            {"moves": [["F", 1], ["D", 1], ["F'", 1]], "color": self.cube[self.LEFT][7]},
            {"moves": [["F'", 1], ["U", 1], ["F", 1]], "color": self.cube[self.RIGHT][1]},
            {"moves": [["R", 1], ["F'", 1], ["U", 1], ["F", 1]], "color": self.cube[self.RIGHT][3]},
            {"moves": [["B", 1], ["U", 1], ["R", 1], ["U'", 1]], "color": self.cube[self.RIGHT][5]},
            {"moves": [["F", 1], ["D'", 1], ["F'", 1]], "color": self.cube[self.RIGHT][7]},
            {"moves": [["B'", 1], ["R", 2]], "color": self.cube[self.BACK][1]},
            {"moves": [["R", 2]], "color": self.cube[self.BACK][3]},
            {"moves": [["B", 2], ["R", 2]], "color": self.cube[self.BACK][5]},
            {"moves": [["B", 1], ["R", 2]], "color": self.cube[self.BACK][7]}
        ]

    def get_top_left_corners(self):
        return [
            {"moves": [["L'", 1], ["B'", 1], ["L", 1]], "color": self.cube[self.LEFT][0]},
            {"moves": [["B", 2], ["L'", 1], ["B", 1], ["L", 1]], "color": self.cube[self.LEFT][6]},
            {"moves": [["L'", 1], ["B", 1], ["L", 1]], "color": self.cube[self.RIGHT][2]},
            {"moves": [["B", 2], ["L'", 1], ["B'", 1], ["L", 1]], "color": self.cube[self.RIGHT][8]},
            {"moves": [["U", 1], ["B'", 1], ["U'", 1]], "color": self.cube[self.DOWN][6]},
            {"moves": [["B", 1], ["F'", 1], ["D'", 1], ["B", 2], ["D", 1], ["F", 1]], "color": self.cube[self.DOWN][8]},
            {"moves": [["B'", 1], ["L'", 1], ["B", 1], ["L", 1]], "color": self.cube[self.UP][0]},
            {"moves": [["B", 1], ["L'", 1], ["B'", 1], ["L", 1]], "color": self.cube[self.UP][2]},
            {"moves": [["U", 1], ["B", 1], ["U'", 1], ["B'", 1], ["U", 1], ["B", 1], ["U'", 1]],
             "color": self.cube[self.UP][6]},
            {"moves": [["B'", 1], ["U", 1], ["B", 1], ["U'", 1], ["B", 1], ["U", 1], ["B'", 1], ["U'", 1]],
             "color": self.cube[self.BACK][0]},
            {"moves": [["B'", 2], ["U", 1], ["B", 1], ["U'", 1], ["B", 1], ["U", 1], ["B'", 1], ["U'", 1]],
             "color": self.cube[self.BACK][2]},
            {"moves": [["U", 1], ["B", 1], ["U'", 1], ["B", 1], ["U", 1], ["B'", 1], ["U'", 1]],
             "color": self.cube[self.BACK][6]},
            {"moves": [["B", 1], ["U", 1], ["B", 1], ["U'", 1], ["B", 1], ["U", 1], ["B'", 1], ["U'", 1]],
             "color": self.cube[self.BACK][8]}
        ]

    def get_top_right_corners(self):
        return [
            {"moves": [["R", 1], ["B", 1], ["R'", 1]], "color": self.cube[self.RIGHT][2]},
            {"moves": [["B'", 1], ["R", 1], ["B", 2], ["R'", 1]], "color": self.cube[self.RIGHT][8]},
            {"moves": [["R", 1], ["B'", 1], ["R'", 1]], "color": self.cube[self.LEFT][0]},
            {"moves": [["B", 2], ["R", 1], ["B", 1], ["R'", 1]], "color": self.cube[self.LEFT][6]},
            {"moves": [["B", 2], ["U'", 1], ["B'", 1], ["U", 1]], "color": self.cube[self.DOWN][6]},
            {"moves": [["U'", 1], ["B", 1], ["U", 1]], "color": self.cube[self.DOWN][8]},
            {"moves": [["B'", 1], ["R", 1], ["B", 1], ["R'", 1]], "color": self.cube[self.UP][0]},
            {"moves": [["B'", 2], ["R", 1], ["B", 2], ["R'", 1]], "color": self.cube[self.UP][2]},
            {"moves": [["U'", 1], ["B'", 1], ["U", 1], ["B", 1], ["U'", 1], ["B'", 1], ["U", 1]],
             "color": self.cube[self.UP][8]},
            {"moves": [["B", 2], ["U'", 1], ["B'", 1], ["U", 1], ["B'", 1], ["U'", 1], ["B", 1], ["U", 1]],
             "color": self.cube[self.BACK][0]},
            {"moves": [["B", 1], ["U'", 1], ["B'", 1], ["U", 1], ["B'", 1], ["U'", 1], ["B", 1], ["U", 1]],
             "color": self.cube[self.BACK][2]},
            {"moves": [["B'", 1], ["U'", 1], ["B'", 1], ["U", 1], ["B'", 1], ["U'", 1], ["B", 1], ["U", 1]],
             "color": self.cube[self.BACK][6]},
            {"moves": [["U'", 1], ["B'", 1], ["U", 1], ["B'", 1], ["U'", 1], ["B", 1], ["U", 1]],
             "color": self.cube[self.BACK][8]}
        ]

    def get_bottom_left_corners(self):
        return [
            {"moves": [["B", 1], ["D'", 1], ["B'", 1], ["D", 1]], "color": self.cube[self.LEFT][0]},
            {"moves": [["B'", 1], ["D'", 1], ["B", 1], ["D", 1]], "color": self.cube[self.LEFT][6]},
            {"moves": [["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1], ["B", 1], ["D", 1]], "color": self.cube[self.LEFT][8]},
            {"moves": [["D'", 1], ["B", 2], ["D", 1]], "color": self.cube[self.RIGHT][2]},
            {"moves": [["B'", 1], ["D'", 1], ["B'", 1], ["D", 1]], "color": self.cube[self.RIGHT][8]},
            {"moves": [["D'", 1], ["B'", 1], ["D", 1], ["B", 1], ["D'", 1], ["B'", 1], ["D", 1]],
             "color": self.cube[self.DOWN][0]},
            {"moves": [["D'", 1], ["B'", 1], ["D", 1]], "color": self.cube[self.DOWN][6]},
            {"moves": [["B", 1], ["D'", 1], ["B", 2], ["D", 1]], "color": self.cube[self.DOWN][8]},
            {"moves": [["D'", 1], ["B", 1], ["D", 1]], "color": self.cube[self.UP][0]},
            {"moves": [["B", 2], ["D'", 1], ["B'", 1], ["D", 1]], "color": self.cube[self.UP][2]},
            {"moves": [["B", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1],
                       ["D'", 1], ["B", 1], ["D", 1]], "color": self.cube[self.BACK][0]},
            {"moves": [["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1],
                       ["B", 1], ["D", 1]], "color": self.cube[self.BACK][2]},
            {"moves": [["B", 2], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1],
                       ["D'", 1], ["B", 1], ["D", 1]], "color": self.cube[self.BACK][6]},
            {"moves": [["B'", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1],
                       ["D'", 1], ["B", 1], ["D", 1]], "color": self.cube[self.BACK][8]}

        ]

    def get_bottom_right_corners(self):
        return [
            {"moves": [["D", 1], ["B'", 2], ["D'", 1]], "color": self.cube[self.LEFT][0]},
            {"moves": [["B", 1], ["D", 1], ["B", 1], ["D'", 1]], "color": self.cube[self.LEFT][6]},
            {"moves": [["B'", 1], ["D", 1], ["B", 1], ["D'", 1]], "color": self.cube[self.RIGHT][2]},
            {"moves": [["B", 1], ["D", 1], ["B'", 1], ["D'", 1]], "color": self.cube[self.RIGHT][8]},
            {"moves": [["D", 1], ["B", 1], ["D'", 1], ["B'", 1], ["D", 1], ["B", 1], ["D'", 1]],
             "color": self.cube[self.DOWN][2]},
            {"moves": [["B", 2], ["D", 1], ["B'", 1], ["D'", 1]], "color": self.cube[self.DOWN][6]},
            {"moves": [["D", 1], ["B", 1], ["D'", 1]], "color": self.cube[self.DOWN][8]},
            {"moves": [["B", 2], ["D", 1], ["B", 1], ["D'", 1]], "color": self.cube[self.UP][0]},
            {"moves": [["D", 1], ["B'", 1], ["D'", 1]], "color": self.cube[self.UP][2]},
            {"moves": [["B", 1], ["D", 1], ["B", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1]],
             "color": self.cube[self.BACK][0]},
            {"moves": [["D", 1], ["B", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1]],
             "color": self.cube[self.BACK][2]},
            {"moves": [["B", 2], ["D", 1], ["B", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1]],
             "color": self.cube[self.BACK][6]},
            {"moves": [["B'", 1], ["D", 1], ["B", 1], ["D'", 1], ["B", 1], ["D", 1], ["B'", 1], ["D'", 1]],
             "color": self.cube[self.BACK][8]},
        ]

    ####################################################################################################################
    # PRIVATE METHODS
    ####################################################################################################################
    def __rotate_matrix(self, face_nb):
        """
        Rotate the stickers of a face in a clockwise direction.

        Args:
            face_nb (int): The face number to be rotated.

        Returns:
            list: A list representing the rotated face.

        Example:
            rotated_face = self.__rotate_matrix(0)
            # rotated_face is a list representing the clockwise rotation of the specified face.
        """
        return [self.cube[face_nb][6], self.cube[face_nb][3], self.cube[face_nb][0],
                self.cube[face_nb][7], self.cube[face_nb][4], self.cube[face_nb][1],
                self.cube[face_nb][8], self.cube[face_nb][5], self.cube[face_nb][2]]

    def __rotate_matrix_reverse(self, face_nb):
        """
        Rotate the stickers of a face in a counter-clockwise direction.

        Args:
            face_nb (int): The face number to be rotated.

        Returns:
            list: A list representing the counter-clockwise rotation of the specified face.

        Example:
            reversed_face = self.__rotate_matrix_reverse(3)
            # reversed_face is a list representing the counter-clockwise rotation of the specified face.
        """
        return [self.cube[face_nb][2], self.cube[face_nb][5], self.cube[face_nb][8],
                self.cube[face_nb][1], self.cube[face_nb][4], self.cube[face_nb][7],
                self.cube[face_nb][0], self.cube[face_nb][3], self.cube[face_nb][6]]

    def __base_check(self):
        """
        Check if the Rubik's Cube has the base configuration.

        Returns True if the cube's faces match the base configuration, where each color appears exactly nine times.

        Returns:
            bool: True if the cube matches the base configuration, False otherwise.

        Example:
            is_base = self.__base_check()
            # is_base will be True if the cube matches the base configuration.
        """
        red = 0
        green = 0
        white = 0
        blue = 0
        orange = 0
        yellow = 0
        for big_face in self.cube:
            for face in big_face:
                match face:
                    case 'R':
                        red += 1
                    case 'G':
                        green += 1
                    case 'W':
                        white += 1
                    case 'B':
                        blue += 1
                    case 'O':
                        orange += 1
                    case 'Y':
                        yellow += 1

        return red == 9 and green == 9 and white == 9 and blue == 9 and orange == 9 and yellow == 9
