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

        # if not self.__base_check():
        #     exit(1)

    # moves

    # Move U x times
    def move_u(self, x=1):
        for _ in range(x):
            new_up_face = self.__rotate_matrix(self.UP)
            # Define the faces to update in a loop
            face_order = [self.LEFT, self.FACE, self.RIGHT, self.BACK]
            new_faces = []

            for face_nb in face_order:
                new_face = [
                    self.cube[face_order[(face_order.index(face_nb) + 1) % 4]][0],
                    self.cube[face_order[(face_order.index(face_nb) + 1) % 4]][1],
                    self.cube[face_order[(face_order.index(face_nb) + 1) % 4]][2],
                    self.cube[face_nb][3],
                    self.cube[face_nb][4],
                    self.cube[face_nb][5],
                    self.cube[face_nb][6],
                    self.cube[face_nb][7],
                    self.cube[face_nb][8]
                ]
                new_faces.append(new_face)

            # Update the faces in the cube
            self.cube[self.UP] = new_up_face
            for i in range(4):
                self.cube[face_order[i]] = new_faces[i]

            # Add the move to history
            self.moves_history.append("U")

    # Move D x times
    def move_d(self, x=1):
        for _ in range(x):
            new_down_face = self.__rotate_matrix(self.DOWN)
            # Define the faces to update in a loop
            face_order = [self.LEFT, self.FACE, self.RIGHT, self.BACK]
            new_faces = []

            for face_nb in face_order:
                new_face = [
                    self.cube[face_nb][0],
                    self.cube[face_nb][1],
                    self.cube[face_nb][2],
                    self.cube[face_nb][3],
                    self.cube[face_nb][4],
                    self.cube[face_nb][5],
                    self.cube[face_order[(face_order.index(face_nb) - 1) % 4]][6],
                    self.cube[face_order[(face_order.index(face_nb) - 1) % 4]][7],
                    self.cube[face_order[(face_order.index(face_nb) - 1) % 4]][8]
                ]
                new_faces.append(new_face)

            # Update the faces in the cube
            self.cube[self.DOWN] = new_down_face
            for i in range(4):
                self.cube[face_order[i]] = new_faces[i]

            # Add the move to history
            self.moves_history.append("D")

    # Move U' x times
    def move_u_p(self, x=1):
        for _ in range(x):
            new_up_face = self.__rotate_matrix_reverse(self.UP)
            # Define the faces to update in a loop
            face_order = [self.LEFT, self.FACE, self.RIGHT, self.BACK]
            new_faces = []

            for face_nb in face_order:
                new_face = [
                    self.cube[face_order[(face_order.index(face_nb) - 1) % 4]][0],
                    self.cube[face_order[(face_order.index(face_nb) - 1) % 4]][1],
                    self.cube[face_order[(face_order.index(face_nb) - 1) % 4]][2],
                    self.cube[face_nb][3],
                    self.cube[face_nb][4],
                    self.cube[face_nb][5],
                    self.cube[face_nb][6],
                    self.cube[face_nb][7],
                    self.cube[face_nb][8]
                ]
                new_faces.append(new_face)

            # Update the faces in the cube
            self.cube[self.UP] = new_up_face
            for i in range(4):
                self.cube[face_order[i]] = new_faces[i]

            # Add the move to history
            self.moves_history.append("u'")

    # Move D' x times
    def move_d_p(self, x=1):
        for _ in range(x):
            new_down_face = self.__rotate_matrix_reverse(self.DOWN)
            # Define the faces to update in a loop
            face_order = [self.LEFT, self.FACE, self.RIGHT, self.BACK]
            new_faces = []
            for face_nb in face_order:
                new_face = [
                    self.cube[face_nb][0],
                    self.cube[face_nb][1],
                    self.cube[face_nb][2],
                    self.cube[face_nb][3],
                    self.cube[face_nb][4],
                    self.cube[face_nb][5],
                    self.cube[face_order[(face_order.index(face_nb) + 1) % 4]][6],
                    self.cube[face_order[(face_order.index(face_nb) + 1) % 4]][7],
                    self.cube[face_order[(face_order.index(face_nb) + 1) % 4]][8]
                ]
                new_faces.append(new_face)
                # Update the faces in the cube
            self.cube[self.DOWN] = new_down_face
            for i in range(4):
                self.cube[face_order[i]] = new_faces[i]
                # Add the move to history
            self.moves_history.append("D'")

    # Move L x times
    def move_l(self, x=1):
        for i in range(x):
            # move left face
            new_left_face = self.__rotate_matrix(self.LEFT)
            # move up face
            face_nb = self.UP
            new_up_face = [self.cube[self.BACK][2], self.cube[face_nb][1], self.cube[face_nb][2],
                           self.cube[self.BACK][5], self.cube[face_nb][4], self.cube[face_nb][5],
                           self.cube[self.BACK][8], self.cube[face_nb][7], self.cube[face_nb][8]]
            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[self.UP][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.UP][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.UP][6], self.cube[face_nb][7], self.cube[face_nb][8]]
            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.DOWN][0],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.DOWN][3],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.DOWN][6]]
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

    # Move L' x times
    def move_l_p(self, x=1):
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
            new_back_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.UP][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.UP][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.UP][8]]
            # move down face
            face_nb = self.DOWN
            new_down_face = [self.cube[self.BACK][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.BACK][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.BACK][6], self.cube[face_nb][7], self.cube[face_nb][8]]

            self.cube[self.UP] = new_up_face
            self.cube[self.LEFT] = new_left_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.BACK] = new_back_face
            self.cube[self.DOWN] = new_down_face

            # Add the move to history
            self.moves_history.append("L'")

    # Move R x times
    def move_r(self, x=1):
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
            new_back_face = [self.cube[self.UP][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.UP][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.UP][6], self.cube[face_nb][7], self.cube[face_nb][8]]
            # move down face
            face_nb = self.DOWN
            new_down_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.BACK][0],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.BACK][3],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.BACK][6]]

            self.cube[self.UP] = new_up_face
            self.cube[self.RIGHT] = new_right_face
            self.cube[self.FACE] = new_main_face
            self.cube[self.BACK] = new_back_face
            self.cube[self.DOWN] = new_down_face

            # Add the move to history
            self.moves_history.append("R")

    # Move R' x times
    def move_r_p(self, x=1):
        for i in range(x):
            # move right face
            new_right_face = self.__rotate_matrix_reverse(self.RIGHT)
            # move up face
            face_nb = self.UP
            new_up_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.BACK][0],
                           self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.BACK][3],
                           self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.BACK][6]]
            # move main face
            face_nb = self.FACE
            new_main_face = [self.cube[face_nb][0], self.cube[face_nb][1], self.cube[self.UP][2],
                             self.cube[face_nb][3], self.cube[face_nb][4], self.cube[self.UP][5],
                             self.cube[face_nb][6], self.cube[face_nb][7], self.cube[self.UP][8]]
            # move back face
            face_nb = self.BACK
            new_back_face = [self.cube[self.DOWN][0], self.cube[face_nb][1], self.cube[face_nb][2],
                             self.cube[self.DOWN][3], self.cube[face_nb][4], self.cube[face_nb][5],
                             self.cube[self.DOWN][6], self.cube[face_nb][7], self.cube[face_nb][8]]
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

    # Move F x times
    def move_f(self, x=1):
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

    # Move F' x times
    def move_f_p(self, x=1):
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

    # Move B x times
    def move_b(self, x=1):
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

        # Move B x times
    def move_b_p(self, x=1):
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

    # getters
    def get_cube(self):
        string_res = ""
        for big_face in self.cube:
            for face in big_face:
                string_res += face
        return string_res

    def get_moves(self):
        return self.moves_history

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
