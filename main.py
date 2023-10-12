from Rubiks3DViewer.Rubiks3DViewer import RubiksViewer as viewer
from PictureConverter.PictureConverter import PictureConverter as pic_converter

# converted_pic = pic_converter("./test_pic.png")
# converted_pic.tile(3, "./split_out")
# converted_pic.get_formatted_matrix()


## NEW Solver

from RubiksSolver.RubiksSolver import RubiksSolver as RSolver

cubestring = "FLBUULFFLFDURRDBUBUUDDFFBRDDBLRDRFLLRLRULFUDRRBDBBBUFL"

if __name__ == '__main__':
    
    solver = RSolver()
    
    state, result = solver.tryToSolve(cubestring)
    
    if state:
        print("Rubik's Cube Solution:")
        print(result)
    else:
        print("cannot be solve")
        print(result)


