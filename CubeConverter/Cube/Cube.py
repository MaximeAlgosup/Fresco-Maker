class Cube:

    def __init__(self):
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
             'Y', 'Y', 'Y'],
        ]

        self.moves_history = []

        if not self.__base_check():
            exit(1)

    # moves

    # Move U x times
    def move_u(self, x):
        for i in range(x):
            # move face up

            self.moves_history.append("U")

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
