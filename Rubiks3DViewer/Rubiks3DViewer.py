# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os
import logging


class RubiksViewer:
    red = 'red'  # red
    orange = 'orange'  # orange
    green = 'green'  # green
    blue = 'blue'  # blue
    yellow = 'yellow'  # yellow
    white = 'white'  # white
    black = 'black'  # black

    def __init__(self, cube_size=3):
        self.plt = plt
        self.fig = plt.figure(figsize=(10, 10))
        self.ax = plt.axes(projection='3d')
        self.axes = [cube_size, cube_size, cube_size]
        self.pic_name = None
        self.rubiks_config = None
        self.folder_path = None
        # Set axis limits
        self.ax.set_xlim(0, 3)
        self.ax.set_ylim(0, 3)
        self.ax.set_zlim(0, 3)

        # turn off/on axis
        self.plt.axis('off')

    def set_new_pic(self, rubiks_config):
        self.rubiks_config = rubiks_config + str('N')
        self.plt = self.__generate_pic()

    def show_pic(self):
        self.plt.show()

    def close_plt(self):
        self.plt.close()

    def save_pic(self, folder_path, pic_name):
        # save picture with name and folder specified
        # check path
        if os.path.exists(folder_path):
            self.folder_path = folder_path
            self.pic_name = pic_name
            self.plt.savefig(self.folder_path + "/" + self.pic_name, dpi='figure', format='png')
        else:
            logging.error("Path doesn't exist")
            exit(1)

    def __generate_pic(self):
        # Create a 3x3x3 Rubik's Cube with different face colors
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    # Define the vertices of each small cube
                    vertices = [
                        [x, y, z],
                        [x + 1, y, z],
                        [x + 1, y + 1, z],
                        [x, y + 1, z],
                        [x, y, z + 1],
                        [x + 1, y, z + 1],
                        [x + 1, y + 1, z + 1],
                        [x, y + 1, z + 1]
                    ]

                    # Define the faces of the small cube
                    faces = [
                        [vertices[0], vertices[1], vertices[2], vertices[3]],
                        [vertices[4], vertices[5], vertices[6], vertices[7]],
                        [vertices[0], vertices[3], vertices[7], vertices[4]],
                        [vertices[1], vertices[2], vertices[6], vertices[5]],
                        [vertices[0], vertices[1], vertices[5], vertices[4]],
                        [vertices[2], vertices[3], vertices[7], vertices[6]]
                    ]

                    colors_axis = self.__face_color_mapper(x, y, z)
                    x_axis_color = self.__color_converter(self.rubiks_config[colors_axis[0]])
                    y_axis_color = self.__color_converter(self.rubiks_config[colors_axis[1]])
                    z_axis_color = self.__color_converter(self.rubiks_config[colors_axis[2]])

                    # Create a Poly3DCollection for the small cube with the appropriate color
                    cube = Poly3DCollection(faces, facecolors=[z_axis_color, z_axis_color, y_axis_color, y_axis_color,
                                                               x_axis_color, x_axis_color], edgecolors='black')
                    # Add the small cube to the plot
                    self.ax.add_collection3d(cube)
        # return the plot
        return plt

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
            case 'N':
                return self.black

    @staticmethod
    def __face_color_mapper(x, y, z):
        encoded_face_id = str(x) + str(y) + str(z)
        match encoded_face_id:
            case "000":
                return [24, 17, 45]
            case "001":
                return [21, 14, 54]
            case "002":
                return [18, 11, 6]
            case "010":
                return [54, 16, 48]
            case "011":
                return [54, 13, 54]
            case "012":
                return [54, 10, 3]
            case "020":
                return [44, 15, 51]
            case "021":
                return [41, 12, 54]
            case "022":
                return [38, 9, 0]
            case "100":
                return [25, 54, 46]
            case "101":
                return [22, 54, 54]
            case "102":
                return [19, 54, 7]
            case "110":
                return [54, 54, 49]
            case "111":
                return [54, 54, 54]
            case "112":
                return [54, 54, 4]
            case "120":
                return [43, 54, 52]
            case "121":
                return [40, 54, 54]
            case "122":
                return [37, 54, 1]
            case "200":
                return [26, 33, 47]
            case "201":
                return [23, 30, 54]
            case "202":
                return [20, 27, 8]
            case "210":
                return [54, 34, 50]
            case "211":
                return [54, 31, 54]
            case "212":
                return [54, 28, 5]
            case "220":
                return [42, 35, 53]
            case "221":
                return [39, 32, 54]
            case "222":
                return [36, 29, 2]
