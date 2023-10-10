from Rubiks3DViewer.Rubiks3DViewer import RubiksViewer as viewer
from PictureConverter.PictureConverter import PictureConverter as pic_converter
import os
from Gui.GuiRunner import GuiRunner
from Gui.GuiError import GuiError

start_win = GuiRunner()
start_win.run_widow()
user_data = start_win.get_data()

# Check the path
if not os.path.exists(str(user_data[0])):
    GuiError("ERROR: file not found at: "+str(user_data[0]))

# Check file is picture file
if not str(user_data[0]).lower().endswith(('.png', '.jpg', '.jpeg')):
    GuiError("ERROR: file must be a picture")

# Check team member nb
if int(user_data[1]) < 1:
    GuiError("ERROR: team number must be \n equal or upper than 1")
