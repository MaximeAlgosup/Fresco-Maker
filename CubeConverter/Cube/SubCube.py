#             |************|                          |                ----------------
#             |*W **W **W *|                          |                | 0  | 1  | 2  |
#             |************|                          |                ----------------
#             |*W **W **W *|                          |                | 3  | 4  | 5  |
#             |************|                          |                ----------------
#             |*W **W **W *|                          |                | 6  | 7  | 8  |
#             |************|                          |                ----------------
# ************|************|************|************ | -------------------------------------------------------------
# *O **O **O *|*G **G **G *|*R **R **R *|*B **B **B * | | 9  | 10 | 11 | 18 | 19 | 20 | 27 | 28 | 29 | 36 | 37 | 38 |
# ************|************|************|************ | -------------------------------------------------------------
# *O **O **O *|*G **G **G *|*R **R **R *|*B **B **B * | | 12 | 13 | 14 | 21 | 22 | 23 | 30 | 31 | 32 | 39 | 40 | 41 |
# ************|************|************|************ | -------------------------------------------------------------
# *O **O **O *|*G **G **G *|*R **R **R *|*B **B **B * | | 15 | 16 | 17 | 24 | 25 | 26 | 33 | 34 | 35 | 42 | 43 | 44 |
# ************|************|************|************ | -------------------------------------------------------------
#             |************|                          |                ----------------
#             |*Y **Y **Y *|                          |                | 45 | 46 | 47 |
#             |************|                          |                ----------------
#             |*Y **Y **Y *|                          |                | 48 | 49 | 50 |
#             |************|                          |                ----------------
#             |*Y **Y **Y *|                          |                | 51 | 52 | 53 |
#             |************|                          |                ----------------
#
#             |************|                          |                ----------------
#             |*U1**U2**U3*|                          |                | 0  | 1  | 2  |
#             |************|                          |                ----------------
#             |*U4**U5**U6*|                          |                | 3  | 4  | 5  |
#             |************|                          |                ----------------
#             |*U7**U8**U9*|                          |                | 6  | 7  | 8  |
#             |************|                          |                ----------------
# ************|************|************|************ | -------------------------------------------------------------
# *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3* | | 9  | 10 | 11 | 18 | 19 | 20 | 27 | 28 | 29 | 36 | 37 | 38 |
# ************|************|************|************ | -------------------------------------------------------------
# *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6* | | 12 | 13 | 14 | 21 | 22 | 23 | 30 | 31 | 32 | 39 | 40 | 41 |
# ************|************|************|************ | -------------------------------------------------------------
# *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9* | | 15 | 16 | 17 | 24 | 25 | 26 | 33 | 34 | 35 | 42 | 43 | 44 |
# ************|************|************|************ | -------------------------------------------------------------
#             |************|                          |                ----------------
#             |*D1**D2**D3*|                          |                | 45 | 46 | 47 |
#             |************|                          |                ----------------
#             |*D4**D5**D6*|                          |                | 48 | 49 | 50 |
#             |************|                          |                ----------------
#             |*D7**D8**D9*|                          |                | 51 | 52 | 53 |
#             |************|                          |                ----------------
class SubCube:

    def __init__(self, face_nb, faces):
        self.face_nb = face_nb
        if isinstance(faces, list):
            self.faces = faces
        else:
            self.faces = [faces]
        if len(self.faces) == self.face_nb:
            self.is_valid = True
        else:
            self.is_valid = False

    def get_size(self):
        return self.face_nb
    def get_pos(self):
        res = []
        for face in self.faces:
            res.append(face.pos)

        return res

    def get_code_pos(self):
        res = []
        for face in self.faces:
            res.append(face.code_pos)

        return res

    @staticmethod
    def swap(sub1, sub2):
        if sub1.get_size() != sub1.get_size():
            print("ERROR: Can't swap sub cube with different faces number")
            return [sub1, sub2]