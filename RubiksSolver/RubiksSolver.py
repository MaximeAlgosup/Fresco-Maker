import kociemba
import random
from RubiksSolver.RubiksMapping.RubiksMapping import RubiksMapping


# mapping = Mapping(pattern)
# adjacent_cubes = mapping.get_adjacent_cubes(cube_to_find)
# print(f'Les cubes adjacents à {cube_to_find} sont : {adjacent_cubes}')
#   W
# O G R B
#   Y

class RubiksSolver:
    
    def __init__(self, pattern):
        self.pattern = pattern
        self.colors = self.colorsReset()
        self.upside = "....U...."
        self.rightside = "....R...."
        self.face = "....F...."
        self.downside = "....D...."
        self.leftside = "....L...."
        self.back = "....B...."
        self.custom_pattern = ""
        self.solved_cube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        
        self.solution = ""
        self.solved = False
        
        self.mapping = RubiksMapping()
        
        
        #self.addPatternToCubestring()
        self.backface = self.invertColors()
        
        self.createCubestring()
        
        #self.tryToSolve()
        
        self.custom_pattern = self.upside + self.rightside + self.face + self.downside + self.leftside + self.back
        # self.result = self.split_string_by_length(self.custom_pattern, 9)
        
        print(self.custom_pattern)
        
        
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
        letters = []
    
        for letter in string:
            letters.append(letter)
            
        return letters



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
            
            ## ERREUR : Boucle Infini car valeurs tableau = 8
            # sachant qu'un rubiks cube ne peux avec que 9 fois la même couleur et que les centres ne sont pas pris en compte
            # Le tableau ne devrait pas pouvoir dépasser 8 avant la fin de l'execution
            if list(colors.values())[index] < 8:
                colors[list(colors)[index]] += 1
                searching = False
                
                return list(colors)[index]
        


    def invertColors(self):    
        
        backface = []
            
        for i in range(0, len(self.pattern)):
            
            
            letter =self.pattern[i]+ str(i+1)
                
            # adjacent_cubes = self.mapping.get_adjacent_cubes(letter)
                 
            opposite = self.mapping.get_opposite_cubes(self.pattern[i])
                
            backface.extend([opposite])
            
        return backface
    
    def completeFaces(self, face, index):
        index = index-1
        print(face+str(index))
        match face:
            case "U":
                upside = self.split_all_letters(self.upside)
                if upside[index] == ".":
                    upside[index] = face
                    self.upside = ''.join(upside)
            case "D":
                downside = self.split_all_letters(self.downside)
                if downside[index] == ".":
                    downside[index] = face
                    self.downside = ''.join(downside)
            case "L":
                leftside = self.split_all_letters(self.leftside)
                if leftside[index] == ".":
                    leftside[index] = face
                    self.leftside = ''.join(leftside)
            case "R":
                rightside = self.split_all_letters(self.rightside)
                if rightside[index] == ".":
                    rightside[index] = face
                    self.rightside = ''.join(rightside)
            case "B":
                backside = self.split_all_letters(self.back)
                if backside[index] == ".":
                    backside[index] = face
                    self.back = ''.join(backside)
            case "F":
                faceside = self.split_all_letters(self.face)
                if faceside[index] == ".":
                    faceside[index] = face
                    self.face = ''.join(faceside)
    
    def setFacesPos(self, center, face):
        
        match center:
            case "U":
                self.upside = face
            case "D":
                self.downside = face
            case "L":
                self.leftside = face
            case "R":
                self.rightside = face
            case "B":
                self.back = face
            case "F":
                self.face = face
            
            
    def setAdjacentFaces(self, face, position):
        cubeName = face+str(position+1)
        if not self.mapping.get_used_cubes(cubeName):
            mapping = self.mapping.get_adjacent_cubes(cubeName)
            
            for facename in mapping:
                face = facename[0:1]
                index = facename[1:2]
                self.completeFaces(face, int(index))
            
            
        
    
    def createCubestring(self):
    
        
        faceCenter = self.pattern[4]
        backCenter = self.backface[4]
        completeFace = ""
        completeBack = ""
        
        
        for i in range(0, len(self.pattern)):
            completeFace = completeFace + self.pattern[i]
            self.setAdjacentFaces(self.pattern[i], i)
        
        self.setFacesPos(faceCenter, completeFace)
            
        for i in range(0, len(self.backface)):
            completeBack = completeBack + self.backface[i]
            self.setAdjacentFaces(self.backface[i], i)
        self.setFacesPos(backCenter, completeBack)
    
    
        print(self.custom_pattern)
    
        return self.custom_pattern

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