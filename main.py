from Rubiks3DViewer.Rubiks3DViewer import RubiksViewer as viewer

test = viewer()
test.set_new_pic("OOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWWYYYYYYYYYGGGGGGGGG")
test.save_pic("./generatedPictures", "test.png")
