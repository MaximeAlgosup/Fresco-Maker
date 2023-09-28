# Import libraries
import matplotlib.pyplot as plt
import numpy as np


class RubiksViewer:
    red = [1, 0, 0, 1]  # red
    orange = [1, 0.5, 0.5, 1]  # orange
    green = [0, 1, 0, 1]  # green
    blue = [0, 0, 1, 1]  # blue
    yellow = [1, 1, 0, 1]  # yellow
    white = [1, 1, 1, 1]  # white

    def __init__(self, cube_size=3):
        self.fig = plt.figure(figsize=(10, 10))
        self.ax = plt.axes(projection='3d')
        self.axes = [cube_size, cube_size, cube_size]
        self.pic_name = None
        self.rubiks_config = None
        self.folder_path = None

    def set_new_pic(self, folder_path, pic_name, rubiks_config):
        self.folder_path = folder_path
        self.rubiks_config = rubiks_config
        self.pic_name = pic_name
        self.__generate_pic()

    def show_pic(self):
        print("show pic")
        plt.show()

    def save_pic(self):
        # save picture with name and folder specified
        print("save pic")

    def __generate_pic(self):
        # split cube config string each 9 characters
        split_config = [self.rubiks_config[i:i + 9] for i in range(0, len(self.rubiks_config), 9)]
        i = 0
        for face in split_config:
            j = 0
            for color in face:
                print(str(i) + " " + str(j) + " " + color)
                print(str(i) + " " + str(j) + " " + str(self.__color_converter(color)))
                print()
                j += 1
            i += 1

    def __color_converter(self, color_char):
        match color_char:
            case 'O':
                return self.orange
            case 'B':
                return self.blue
            case 'R':
                return self.red
            case 'W':
                return self.white
            case 'Y':
                return self.yellow
            case 'G':
                return self.green
