from Rubiks3DViewer.Rubiks3DViewer import RubiksViewer as viewer
from PictureConverter.PictureConverter import PictureConverter as pic_converter
import os
from Gui.GuiRunner import GuiRunner
from Gui.GuiError import GuiError
from Gui.GuiWarning import GuiWarning

start_win = GuiRunner()
start_win.run_widow()
user_data = start_win.get_data()

picture_path = str(user_data[0])
team_nb = int(user_data[1])
is_create_doc = bool(user_data[2])

# Check the path
if not os.path.exists(str(picture_path)):
    GuiError("ERROR: file not found at: " + str(user_data[0]))

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
