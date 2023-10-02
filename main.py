from Rubiks3DViewer.Rubiks3DViewer import RubiksViewer as viewer
from PictureConverter.PictureConverter import PictureConverter as pic_converter

test = pic_converter("./test_pic.png")
test.tile(3, "./split_out", True)
