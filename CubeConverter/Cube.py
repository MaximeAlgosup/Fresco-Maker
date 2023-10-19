class Cube:
    def __init__(self):
        self.UP = 0
        self.LEFT = 1
        self.FACE = 2
        self.RIGHT = 3
        self.BACK = 4
        self.DOWN = 5
        self.cube = [
            ['W', 'W', 'W',
             'W', 'W', 'W',
             'W', 'W', 'W'],
            ['R', 'R', 'R',
             'R', 'R', 'R',
             'R', 'R', 'R'],
            ['B', 'B', 'B',
             'B', 'B', 'B',
             'B', 'B', 'B'],
            ['O', 'O', 'O',
             'O', 'O', 'O',
             'O', 'O', 'O'],
            ['G', 'G', 'G',
             'G', 'G', 'G',
             'G', 'G', 'G'],
            ['Y', 'Y', 'Y',
             'Y', 'Y', 'Y',
             'Y', 'Y', 'Y'],
        ]

        self.moves_history = []
        print("passe")
        if not self.__base_check():
            exit(1)

    # moves

    # Move Face from center
    def move_center(self, matrix):
        centerColor = matrix[4]
        match centerColor:
            case 'R':
                self.cube = [
                    ['B', 'B', 'B',
                     'B', 'B', 'B',
                     'B', 'B', 'B'],
                    ['W', 'W', 'W',
                     'W', 'W', 'W',
                     'W', 'W', 'W'],
                    ['R', 'R', 'R',
                     'R', 'R', 'R',
                     'R', 'R', 'R'],
                    ['Y', 'Y', 'Y',
                     'Y', 'Y', 'Y',
                     'Y', 'Y', 'Y'],
                    ['O', 'O', 'O',
                     'O', 'O', 'O',
                     'O', 'O', 'O'],
                    ['G', 'G', 'G',
                     'G', 'G', 'G',
                     'G', 'G', 'G']
                ]
            case 'B':
                self.cube = [
                    ['W', 'W', 'W',
                     'W', 'W', 'W',
                     'W', 'W', 'W'],
                    ['R', 'R', 'R',
                     'R', 'R', 'R',
                     'R', 'R', 'R'],
                    ['B', 'B', 'B',
                     'B', 'B', 'B',
                     'B', 'B', 'B'],
                    ['O', 'O', 'O',
                     'O', 'O', 'O',
                     'O', 'O', 'O'],
                    ['G', 'G', 'G',
                     'G', 'G', 'G',
                     'G', 'G', 'G'],
                    ['Y', 'Y', 'Y',
                     'Y', 'Y', 'Y',
                     'Y', 'Y', 'Y'],
                ]
            case 'O':
                self.cube = [
                    ['W', 'W', 'W',
                     'W', 'W', 'W',
                     'W', 'W', 'W'],
                    ['B', 'B', 'B',
                     'B', 'B', 'B',
                     'B', 'B', 'B'],
                    ['O', 'O', 'O',
                     'O', 'O', 'O',
                     'O', 'O', 'O'],
                    ['G', 'G', 'G',
                     'G', 'G', 'G',
                     'G', 'G', 'G'],
                    ['R', 'R', 'R',
                     'R', 'R', 'R',
                     'R', 'R', 'R'],
                    ['Y', 'Y', 'Y',
                     'Y', 'Y', 'Y',
                     'Y', 'Y', 'Y']
                ]
            case 'G':
                self.cube = [
                    ['W', 'W', 'W',
                     'W', 'W', 'W',
                     'W', 'W', 'W'],
                    ['O', 'O', 'O',
                     'O', 'O', 'O',
                     'O', 'O', 'O'],
                    ['G', 'G', 'G',
                     'G', 'G', 'G',
                     'G', 'G', 'G'],
                    ['R', 'R', 'R',
                     'R', 'R', 'R',
                     'R', 'R', 'R'],
                    ['B', 'B', 'B',
                     'B', 'B', 'B',
                     'B', 'B', 'B'],
                    ['Y', 'Y', 'Y',
                     'Y', 'Y', 'Y',
                     'Y', 'Y', 'Y']
                ]
            case 'W':
                self.cube = [
                    ['G', 'G', 'G',
                     'G', 'G', 'G',
                     'G', 'G', 'G'],
                    ['R', 'R', 'R',
                     'R', 'R', 'R',
                     'R', 'R', 'R'],
                    ['W', 'W', 'W',
                     'W', 'W', 'W',
                     'W', 'W', 'W'],
                    ['O', 'O', 'O',
                     'O', 'O', 'O',
                     'O', 'O', 'O'],
                    ['Y', 'Y', 'Y',
                     'Y', 'Y', 'Y',
                     'Y', 'Y', 'Y'],
                    ['B', 'B', 'B',
                     'B', 'B', 'B',
                     'B', 'B', 'B']
                ]
            case 'Y':
                self.cube = [
                    ['G', 'G', 'G',
                     'G', 'G', 'G',
                     'G', 'G', 'G'],
                    ['O', 'O', 'O',
                     'O', 'O', 'O',
                     'O', 'O', 'O'],
                    ['Y', 'Y', 'Y',
                     'Y', 'Y', 'Y',
                     'Y', 'Y', 'Y'],
                    ['R', 'R', 'R',
                     'R', 'R', 'R',
                     'R', 'R', 'R'],
                    ['W', 'W', 'W',
                     'W', 'W', 'W',
                     'W', 'W', 'W'],
                    ['B', 'B', 'B',
                     'B', 'B', 'B',
                     'B', 'B', 'B']
                ]

    # Move U x times
    def move_u(self, x=1):
        print("move U")
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


    # Move D x times
    def move_d(self, x=1):
        print("move D")
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
            print("error invalid cube")
            exit(1)
        print("passe")

    # Move U' x times
    def move_u_p(self, x=1):
        print("move U'")
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

    # Move D' x times
    def move_d_p(self, x=1):
        print("move D'")
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

    # Move L x times
    def move_l(self, x=1):
        print("move L")
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

    # Move L' x times
    def move_l_p(self, x=1):
        print("move L'")
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

    # Move R x times
    def move_r(self, x=1):
        print("move R")
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

    # Move R' x times
    def move_r_p(self, x=1):
        print("move R'")
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

    # Move F x times
    def move_f(self, x=1):
        print("move F")
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

    # Move F' x times
    def move_f_p(self, x=1):
        print("move F'")
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

    # Move B x times
    def move_b(self, x=1):
        print("move B")
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

        # Move B x times

    def move_b_p(self, x=1):
        print("move B'")
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

    # getters
    def get_cube(self):
        string_res = ""
        for big_face in self.cube:
            for face in big_face:
                string_res += face
        return string_res

    def get_matrix_cube(self):
        return self.cube

    def get_moves(self):
        return self.moves_history

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
            {"moves": [["B", 1], ["R", 1], ["D'", 1]], "color": self.cube[self.DOWN][7]},
        ]

    def get_left_crown_edges(self):
        return [
            {"moves": [["L", 1]], "color": self.cube[self.UP][3]},
            {"moves": [["B", 1], ["L'", 1], ["F'", 1], ["D", 1], ["F", 1]], "color": self.cube[self.UP][1]},
            {"moves": [["U", 2], ["L'", 1], ["U", 2]], "color": self.cube[self.UP][5]},
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
            {"moves": [["B'", 1], ["L", 2]], "color": self.cube[self.BACK][1]},
            {"moves": [["L", 2]], "color": self.cube[self.BACK][3]},
            {"moves": [["B'", 2], ["L", 2]], "color": self.cube[self.BACK][5]},
            {"moves": [["B", 1], ["L", 2]], "color": self.cube[self.BACK][7]},

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
            {"moves": [["F", 1], ["U", 1], ["F'", 1]], "color": self.cube[self.RIGHT][1]},
            {"moves": [["R", 1], ["F'", 1], ["U", 1], ["F", 1]], "color": self.cube[self.RIGHT][3]},
            {"moves": [["B", 1], ["U", 1], ["R", 1], ["U'", 1]], "color": self.cube[self.RIGHT][5]},
            {"moves": [["F", 1], ["D'", 1], ["F'", 1]], "color": self.cube[self.RIGHT][7]},
            {"moves": [["B'", 1], ["R", 2]], "color": self.cube[self.BACK][1]},
            {"moves": [["R", 2]], "color": self.cube[self.BACK][3]},
            {"moves": [["B", 2], ["R", 2]], "color": self.cube[self.BACK][5]},
            {"moves": [["B", 1], ["R", 2]], "color": self.cube[self.BACK][7]},
        ]

    def get_top_left_corners(self):
        return [
            {"moves": [["L'", 1], ["B'", 1], ["L", 1]], "color": self.cube[self.LEFT][0]},
            {"moves": [["U", 1], ["B'", 1], ["U'", 1], ["B'", 2], ["U", 1], ["B", 2], ["U'", 1]],
             "color": self.cube[self.LEFT][2]},
            {"moves": [["B", 2], ["L'", 1], ["B", 1], ["L", 1]], "color": self.cube[self.LEFT][6]},
            {"moves": [["L'", 1], ["B", 1], ["L", 1]], "color": self.cube[self.RIGHT][2]},
            {"moves": [["B", 2], ["L'", 1], ["B'", 1], ["L", 1]], "color": self.cube[self.RIGHT][8]},
            {"moves": [["U", 1], ["B'", 1], ["U'", 1]], "color": self.cube[self.DOWN][6]},
            {"moves": [["B", 1], ["F'", 1], ["D'", 1], ["B", 2], ["D", 1], ["F", 1]], "color": self.cube[self.DOWN][8]},
            {"moves": [["B'", 1], ["L'", 1], ["B", 1], ["L", 1]], "color": self.cube[self.UP][0]},
            {"moves": [["B", 1], ["L'", 1], ["B'", 1], ["L", 1]], "color": self.cube[self.UP][2]},
            {"moves": [["L'", 1], ["B'", 1], ["L", 1], ["L", 1], ["B'", 1], ["L'", 1], ["B", 1], ["L", 1]],
             "color": self.cube[self.UP][6]},
        ]

    # private
    def __rotate_matrix(self, face_nb):
        return [self.cube[face_nb][6], self.cube[face_nb][3], self.cube[face_nb][0],
                self.cube[face_nb][7], self.cube[face_nb][4], self.cube[face_nb][1],
                self.cube[face_nb][8], self.cube[face_nb][5], self.cube[face_nb][2]]

    def __rotate_matrix_reverse(self, face_nb):
        return [self.cube[face_nb][2], self.cube[face_nb][5], self.cube[face_nb][8],
                self.cube[face_nb][1], self.cube[face_nb][4], self.cube[face_nb][7],
                self.cube[face_nb][0], self.cube[face_nb][3], self.cube[face_nb][6]]

    def __base_check(self):
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
