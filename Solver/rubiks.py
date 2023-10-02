import kociemba
import random

#solution = kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

#   W
# O G R B
#   Y

pattern = [
    'B', 'B', 'B',
    'B', 'U', 'U',
    'B', 'U', 'B'
]

def colorsReset():
    colors = {"U": 0, "R": 0, "F": 0, "D": 0, "L": 0, "B": 0}
    
    for i in range(0, len(pattern)):
        if i != 4:
            letter = pattern[i]
            colors[letter] += 1
    
    return colors

colors = colorsReset()

def pattern_to_string():
    
    patternString = ""
    
    for letter in pattern:
        patternString = patternString + letter
    
    
    return patternString

def split_all_letters(string):
  letters = []
  for letter in string:
    letters.append(letter)
  return letters


upside = "....U...."
rightside = "....R...."
face = "....F...."
downside = "....D...."
leftside = "....L...."
back = "....B...."
    
match pattern[4]:
    case "U":
        upside = pattern_to_string()
    case "R":
        rightside = pattern_to_string()
    case "F":
        face = pattern_to_string()
    case "D":
        downside = pattern_to_string()
    case "L":
        leftside = pattern_to_string()
    case "B":
        back = pattern_to_string()

custom_pattern = upside + rightside + face + downside + leftside + back

# Create a solved state
solved_cube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

solution = ""
solved = False
    
def split_string_by_length(string, length):
    return [string[i:i+length] for i in range(0, len(string), length)]


    

def get_random_color():
    searching = True

    while searching:
        index = random.randrange(6)
        
        if list(colors.values())[index] < 8:
            colors[list(colors)[index]] += 1
            
            searching = False
            
            return list(colors)[index]
        
    

result = split_string_by_length(custom_pattern, 9)




def createRdmCubestring():
    custom_pattern = ""
    for i in range(0,6) :
        string = list(result)[i]
        string_letter = split_all_letters(string)
        
        completeString = ""
        
        for j in range(0, 9):
            if string_letter[j] == ".":
                rdmLetter = get_random_color()
                letter = string_letter[j].replace(".", rdmLetter)
            else:
                letter = string_letter[j]
            
            completeString += letter
            
            
       
        custom_pattern += completeString
        
    return custom_pattern



upsideExploded = split_all_letters(upside)
rightsideExploded = split_all_letters(rightside)
faceExploded = split_all_letters(face)
downsideExploded = split_all_letters(downside)
leftsideExploded = split_all_letters(leftside)
backExploded = split_all_letters(back)

def checkValidCubestring(cubeString):
    try:
        solution = kociemba.solve(solved_cube, cubeString)
        return True, solution
    except ValueError as e:
        # Handle the error
        print("Error:", e)
        return False, ""
    
while solved == False:

    # "BBURUDBFUFFFRRFUUFLULUFUDLRRDBBDBDBLUDDFLLRR(BRLLLBRDDF"
    
    cubestring = createRdmCubestring()
    print("Cubestring: " + cubestring)
    solved, solution = checkValidCubestring(cubestring)
    colors = colorsReset()

# Print the solution
if solved:
    print("Rubik's Cube Solution:")
    print(solution)
    
print("test")