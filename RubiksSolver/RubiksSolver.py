import kociemba
import random
from  RubiksMapping.RubiksMapping import RubiksMapping as Mapping


mapping = Mapping(pattern)
adjacent_cubes = mapping.get_adjacent_cubes(cube_to_find)
print(f'Les cubes adjacents à {cube_to_find} sont : {adjacent_cubes}')
#   W
# O G R B
#   Y

class RubiksSolver:
    
    def __init__(self, pattern):
        self.pattern = pattern
        self.colors = self.colorsReset()
        self.letters = []
        self.upside = "....U...."
        self.rightside = "....R...."
        self.face = "....F...."
        self.downside = "....D...."
        self.leftside = "....L...."
        self.back = "....B...."
        
        self.solved_cube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        self.custom_pattern = self.upside + self.rightside + self.face + self.downside + self.leftside + self.back
        self.solution = ""
        self.solved = False
        
        self.result = self.split_string_by_length(self.custom_pattern, 9)
        self.addPatternToCubestring()
        
        self.tryToSolve()
        
        
        if self.solved:
            print("Rubik's Cube Solution:")
            print(self.solution)
            
            
        
    def colorsReset(self):
        self.colors = {"U": 0, "R": 0, "F": 0, "D": 0, "L": 0, "B": 0}
    
        for i in range(0, len(self.pattern)):
            if i != 4:
                letter = self.pattern[i]
                self.colors[letter] += 1
    
        return self.colors

    def pattern_to_string(self):
        
        patternString = ""
        
        for letter in self.pattern:
            patternString = patternString + letter
        
        
        return patternString

    def split_all_letters(self, string):
    
        for letter in string:
            self.letters.append(letter)
            
        return self.letters



    def addPatternToCubestring(self):
        match self.pattern[4]:
            case "U":
                self.upside = self.pattern_to_string()
            case "R":
                self.rightside = self.pattern_to_string()
            case "F":
                self.face = self.pattern_to_string()
            case "D":
                self.downside = self.pattern_to_string()
            case "L":
                self.leftside = self.pattern_to_string()
            case "B":
                self.back = self.pattern_to_string()
    
    def split_string_by_length(self, string, length):
        return [string[i:i+length] for i in range(0, len(string), length)]


    

    def get_random_color(self):
        searching = True
        colors =  self.colors


        print(list(colors.values()))
        while searching:
            index = random.randrange(6)
            
            if list(colors.values())[index] < 8:
                colors[list(colors)[index]] += 1
                searching = False
                
                return list(colors)[index]
        





    def createRdmCubestring(self):
        self.custom_pattern = ''
        for i in range(0,6) :
            string = list(self.result)[i]
            string_letter = self.split_all_letters(string)
            
            print(string_letter)
            
            completeString = ""
            
            for j in range(0, 9):
                if string_letter[j] == ".":
                    rdmLetter = self.get_random_color()
                    print(self.custom_pattern)
                    letter = string_letter[j].replace(".", rdmLetter)
                else:
                    letter = string_letter[j]
                
                completeString += letter
                
                
        
            self.custom_pattern += completeString
            
        return self.custom_pattern



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


    def checkValidCubestring(self, cubeString):
        try:
            solution = kociemba.solve(self.solved_cube, cubeString)
            return True, solution
        except ValueError as e:
            # Handle the error
            print("Error:", e)
            return False, ""
    
    
    def tryToSolve(self):
        while self.solved == False:

            # "BBURUDBFUFFFRRFUUFLULUFUDLRRDBBDBDBLUDDFLLRR(BRLLLBRDDF"
            
            
            cubestring = self.createRdmCubestring()
            print("Cubestring: " + cubestring)
            self.solved, self.solution = self.checkValidCubestring(cubestring)
            self.colors = self.colorsReset()

    # New Functions
    
    def getCenter(self):
        return self.pattern[4]