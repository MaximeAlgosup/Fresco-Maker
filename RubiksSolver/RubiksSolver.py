#             |************|                                                       ----------------
#             |*U1**U2**U3*|                                                       | 0  | 1  | 2  |
#             |************|                                                       ----------------
#             |*U4**U5**U6*|                                                       | 3  | 4  | 5  |
#             |************|                                                       ----------------
#             |*U7**U8**U9*|                                                       | 6  | 7  | 8  |
#             |************|                                                       ----------------
# ************|************|************|************               -------------------------------------------------------------
# *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*               | 9  | 10 | 11 | 18 | 19 | 20 | 27 | 28 | 29 | 36 | 37 | 38 |
# ************|************|************|************               -------------------------------------------------------------
# *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*               | 12 | 13 | 14 | 21 | 22 | 23 | 30 | 31 | 32 | 39 | 40 | 41 |
# ************|************|************|************               -------------------------------------------------------------
# *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*               | 15 | 16 | 17 | 24 | 25 | 26 | 33 | 34 | 35 | 42 | 43 | 44 |
# ************|************|************|************               -------------------------------------------------------------
#             |************|                                                       ----------------
#             |*D1**D2**D3*|                                                       | 45 | 46 | 47 |
#             |************|                                                       ----------------
#             |*D4**D5**D6*|                                                       | 48 | 49 | 50 |
#             |************|                                                       ----------------
#             |*D7**D8**D9*|                                                       | 51 | 52 | 53 |
#             |************|                                                       ----------------


#   W
# O G R B
#   Y


##############################################################################################################

#import libraries
import kociemba
from RubiksSolver.RubiksMapping.RubiksMapping import RubiksMapping

class RubiksSolver:
    
    def __init__(self):
        # Initialize an empty solution string and the standard solved Rubik's Cube representation.
        self.solution = ""
        self.solved_cube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

    def tryToSolve(self, cubeString):
        try:
            # Attempt to solve the Rubik's Cube using Kociemba's algorithm.
            solution = kociemba.solve(self.solved_cube, cubeString)
            return True, solution  # Return success and the solution string.
        except ValueError as e:
            # Handle the error gracefully by returning False and an error message.
            return False, "Error: " + str(e)