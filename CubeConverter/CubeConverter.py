class Converter:

    def __init__(self):
        self.pic_face = None
        self.cube_string = None
        self.solver_string = None
        self.possibility = [
            ['W', 'G', 'R', 'B', 'Y', 'O'],
            [['W', 'B'], ['W', 'R'], ['W', 'G'], ['W', 'O'], ['Y', 'B'], ['Y', 'R'], ['Y', 'G'], ['Y', 'O'], ['R', 'B'],
             ['G', 'R'], ['O', 'G'], ['B', 'O']],
            [['B', 'O', 'W'], ['R', 'O', 'W'], ['B', 'R', 'W'], ['G', 'R', 'W'], ['B', 'R', 'Y'], ['B', 'O', 'Y'],
             ['G', 'O', 'Y'], ['G', 'R', 'Y'], ],
        ]

    def face_to_cube(self, pic_face):
        self.pic_face = pic_face
        self.__first_crown__()
        # Generate the crown of the first face
        # generate the middle crown
        # generate the last crown

    def __first_crown__(self):
        res = []
        for i in range(3):
            for j in range(3):
                if (i == 0 or i == 2) and (j == 0 or j == 2):
                    res.append(self.__piece_mapper__(self.pic_face[i][j], 3))
                elif i == 1 and j == 1:
                    res.append(self.__piece_mapper__(self.pic_face[i][j], 1))
                else:
                    res.append(self.__piece_mapper__(self.pic_face[i][j], 2))
        print(self.possibility)
        print()
        print(res)
        print()
        print()

    def __piece_mapper__(self, color, face_nb):
        if face_nb == 1:
            idx = self.possibility[0].index(color)
            res = self.possibility[0][idx]
            self.possibility[0].pop(idx)
        elif face_nb == 2:
            res = None
            for bi_face in self.possibility[1]:
                if color in bi_face:
                    res = bi_face
                    break
            if res == None:
                exit(1)
            idx = self.possibility[1].index(res)
            self.possibility[1].pop(idx)
        else:
            res = None
            for bi_face in self.possibility[2]:
                if color in bi_face:
                    res = bi_face
                    break
            if res == None:
                exit(1)
            idx = self.possibility[2].index(res)
            self.possibility[2].pop(idx)
        return res
