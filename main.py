from Rubiks3DViewer.Rubiks3DViewer import RubiksViewer as viewer
from PictureConverter.PictureConverter import PictureConverter as pic_converter

# converted_pic = pic_converter("./test_pic.png")
# converted_pic.tile(3, "./split_out")
# converted_pic.get_formatted_matrix()


## NEW Solver

from RubiksSolver.RubiksSolver import RubiksSolver as RSolver

pattern = [
    'B', 'B', 'B',
    'B', 'U', 'U',
    'B', 'U', 'B'
]
#BBBBUUBUB RRR.RR.RR .F..F...F FFFFDDFDF L.L.LLL.. ....B.BB.
if __name__ == '__main__':
    
    solver = RSolver(pattern)
    # cube_to_find = solver.getCenter() + "4"
    


    

   
    # print(solver)


