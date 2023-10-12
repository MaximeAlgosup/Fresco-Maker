from Rubiks3DViewer.Rubiks3DViewer import RubiksViewer as viewer
from PictureConverter.PictureConverter import PictureConverter as pic_converter
import os
from Gui.GuiRunner import GuiRunner
from Gui.GuiError import GuiError

<<<<<<< HEAD
start_win = GuiRunner()
start_win.run_widow()
user_data = start_win.get_data()
=======
# converted_pic = pic_converter("./test_pic.png")
# converted_pic.tile(3, "./split_out")
# converted_pic.get_formatted_matrix()
>>>>>>> 51d308a (Relation Mappin-Solver)

# Check the path
if not os.path.exists(str(user_data[0])):
    GuiError("ERROR: file not found at: "+str(user_data[0]))

# Check file is picture file
if not str(user_data[0]).lower().endswith(('.png', '.jpg', '.jpeg')):
    GuiError("ERROR: file must be a picture")

# Check team member nb
if int(user_data[1]) < 1:
    GuiError("ERROR: team number must be \n equal or upper than 1")
<<<<<<< Updated upstream
=======
=======
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


>>>>>>> 6d49067 (Poo + Class Mapping)
>>>>>>> Stashed changes
