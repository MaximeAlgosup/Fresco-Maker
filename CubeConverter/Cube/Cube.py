from CubeConverter.Cube.SubCube import SubCube


class Cube(SubCube):

    def __init__(self):
        self.three_faces_subs = []
        self.two_faces_subs = []
        self.one_faces_subs = []
        self.is_solved = False

    def set_default(self):
        # Up corners
        self.three_faces_subs.append(super().__init__(3, [
            {"pos": 0, "code_pos": "U1", "color": 'W'},
            {"pos": 9, "code_pos": "L1", "color": 'O'},
            {"pos": 38, "code_pos": "B3", "color": 'B'}]))
        self.three_faces_subs.append(super().__init__(3, [
            {"pos": 2, "code_pos": "U3", "color": 'W'},
            {"pos": 29, "code_pos": "R3", "color": 'R'},
            {"pos": 36, "code_pos": "B1", "color": 'B'}]))
        self.three_faces_subs.append(super().__init__(3, [
            {"pos": 6, "code_pos": "U7", "color": 'W'},
            {"pos": 11, "code_pos": "L3", "color": 'O'},
            {"pos": 18, "code_pos": "F1", "color": 'G'}]))
        self.three_faces_subs.append(super().__init__(3, [
            {"pos": 8, "code_pos": "U9", "color": 'W'},
            {"pos": 27, "code_pos": "R1", "color": 'R'},
            {"pos": 20, "code_pos": "F3", "color": 'G'}]))

        # Down corners
        self.three_faces_subs.append(super().__init__(3, [
            {"pos": 45, "code_pos": "D1", "color": 'Y'},
            {"pos": 17, "code_pos": "L9", "color": 'O'},
            {"pos": 24, "code_pos": "F7", "color": 'G'}]))
        self.three_faces_subs.append(super().__init__(3, [
            {"pos": 47, "code_pos": "D3", "color": 'Y'},
            {"pos": 26, "code_pos": "F9", "color": 'G'},
            {"pos": 33, "code_pos": "R7", "color": 'R'}]))
        self.three_faces_subs.append(super().__init__(3, [
            {"pos": 51, "code_pos": "D7", "color": 'Y'},
            {"pos": 15, "code_pos": "L7", "color": 'O'},
            {"pos": 44, "code_pos": "B9", "color": 'B'}]))
        self.three_faces_subs.append(super().__init__(3, [
            {"pos": 53, "code_pos": "D9", "color": 'Y'},
            {"pos": 42, "code_pos": "B7", "color": 'B'},
            {"pos": 35, "code_pos": "R9", "color": 'R'}]))

        # Up bi-face
        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 1, "code_pos": "U2", "color": 'W'},
            {"pos": 37, "code_pos": "B2", "color": 'B'}]))

        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 3, "code_pos": "U4", "color": 'W'},
            {"pos": 10, "code_pos": "L2", "color": 'O'}]))

        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 5, "code_pos": "U6", "color": 'W'},
            {"pos": 28, "code_pos": "R2", "color": 'R'}]))

        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 7, "code_pos": "U8", "color": 'W'},
            {"pos": 19, "code_pos": "F2", "color": 'G'}]))

        # Middle bi-face
        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 14, "code_pos": "L6", "color": 'O'},
            {"pos": 21, "code_pos": "F4", "color": 'G'}]))

        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 23, "code_pos": "F6", "color": 'G'},
            {"pos": 30, "code_pos": "R4", "color": 'R'}]))

        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 32, "code_pos": "R6", "color": 'R'},
            {"pos": 39, "code_pos": "B4", "color": 'B'}]))

        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 41, "code_pos": "B6", "color": 'B'},
            {"pos": 12, "code_pos": "L4", "color": 'O'}]))

        # Down bi-face
        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 46, "code_pos": "D2", "color": 'Y'},
            {"pos": 25, "code_pos": "F8", "color": 'G'}]))

        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 48, "code_pos": "D4", "color": 'Y'},
            {"pos": 16, "code_pos": "L8", "color": 'R'}]))

        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 50, "code_pos": "D6", "color": 'Y'},
            {"pos": 35, "code_pos": "R8", "color": 'B'}]))

        self.two_faces_subs.append(super().__init__(2, [
            {"pos": 52, "code_pos": "D8", "color": 'Y'},
            {"pos": 43, "code_pos": "B8", "color": 'O'}]))

        # All one face
        self.one_faces_subs.append(super().__init__(1, [
            {"pos": 4, "code_pos": "U5", "color": 'W'}]))
        self.one_faces_subs.append(super().__init__(1, [
            {"pos": 13, "code_pos": "L5", "color": 'O'}]))
        self.one_faces_subs.append(super().__init__(1, [
            {"pos": 22, "code_pos": "F5", "color": 'G'}]))
        self.one_faces_subs.append(super().__init__(1, [
            {"pos": 31, "code_pos": "R5", "color": 'R'}]))
        self.one_faces_subs.append(super().__init__(1, [
            {"pos": 40, "code_pos": "B5", "color": 'B'}]))
        self.one_faces_subs.append(super().__init__(1, [
            {"pos": 49, "code_pos": "D5", "color": 'Y'}]))



#   W
# O G R B
#   Y
