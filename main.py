from Rubiks3DViewer.Rubiks3DViewer import RubiksViewer as viewer
from PictureConverter.PictureConverter import PictureConverter as pic_converter
from RubiksSolver.RubiksSolver import RubiksSolver as RSolver
import os
from Gui.GuiRunner import GuiRunner
from Gui.GuiError import GuiError
from Gui.GuiWarning import GuiWarning


def solve_cube(team, result_folder):
    tmp_dir_path = "./" + str(result_folder) + "/team" + str(team) + "/tmp"
    pic_path = "./" + str(result_folder) + "/team" + str(team) + "/team" + str(team) + ".png"
    # create tmp folder
    os.mkdir(tmp_dir_path)

    # split pic in cubes
    pic_splitter = pic_converter(pic_path)
    pic_splitter.tile(3, tmp_dir_path)
    matrix_data = pic_splitter.get_matrix()
    for matrix in matrix_data:
        # format matrix to give it to the solver form [[a, b, c], [d, e, f], [g, h, i]] to [a, b, c, d, e, f, g, h, i]
        flattened_matrix = [element for row in matrix[1] for element in row]
        # give matrix to solver

        # get is answer
        result_cubes = ["OOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWWYYYYYYYYYGGGGGGGGG", "BBBBBBBBBOOOOOOOOORRRRRRRRRWWWWWWWWWYYYYYYYYYGGGGGGGGG"]
        result_length = len(result_cubes)
        for j in range(result_length):
            cube = result_cubes[j]
            r_viewer = viewer()
            r_viewer.set_new_pic(cube)
            r_viewer.save_pic(tmp_dir_path, str(str(matrix[0][0])+"_"+str(matrix[0][1])+"_part"+str(j)+".png"))
            r_viewer.close_plt()

    # delete tmp folder
    # os.rmdir(tmp_dir_path)


start_win = GuiRunner()
start_win.run_widow()
user_data = start_win.get_data()

picture_path = str(user_data[0])
team_nb = int(user_data[1])
is_create_doc = bool(user_data[2])

# picture_path = "./test_pic.png"
# team_nb = 8
# is_create_doc = True

# Check the path
if not os.path.exists(str(picture_path)):
    GuiError("ERROR: file not found at: " + str(picture_path))

# Check file is picture file
if not str(picture_path).lower().endswith(('.png', '.jpg', '.jpeg')):
    GuiError("ERROR: file must be a picture")

# Check team member nb
if team_nb < 1:
    GuiError("ERROR: team number must be \n equal or upper than 1")

# Check if "result" folder already exist if it exists add 0, 1, 2... to the name
res_folder_name = "result"
res_folder_number = 0
while os.path.exists("./" + res_folder_name + str(res_folder_number)):
    res_folder_number += 1

os.mkdir("./" + res_folder_name + str(res_folder_number))

# Start to launch the splitter and check the picture size
split = pic_converter(picture_path)
if not split.test_rubiks_resolution():
    GuiError("ERROR: the resolution of the selected\nimage is not achievable in rubik's cube")

GuiWarning("WARNING: if the colors do not\ncorrespond to the colors of the\nRubik's cube they can be modified")
for i in range(team_nb):
    os.mkdir("./" + res_folder_name + str(res_folder_number) + "/team" + str(i + 1))

split.split(team_nb, str("./" + res_folder_name + str(res_folder_number)))

if is_create_doc:

    for i in range(team_nb):
        solve_cube((i + 1), str(res_folder_name + str(res_folder_number)))

    # thread_tab = []
    # for i in range(team_nb):
    #     thread_calcul = threading.Thread(target=solve_cube, args=((i+1), str(res_folder_name + str(res_folder_number))))
    #     thread_tab.append(thread_calcul)
    #     thread_calcul.start()
    #
    # for thread in thread_tab:
    #     thread.join()
    
    
    

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