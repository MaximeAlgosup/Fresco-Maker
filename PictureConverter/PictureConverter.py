import os
import logging
from PIL import Image
from itertools import product


class PictureConverter:
    # Define color constants
    red = (213, 37, 37)
    green = (106, 190, 48)
    blue = (91, 110, 225)
    yellow = (251, 242, 54)
    white = (255, 255, 255)
    orange = (246, 121, 36)
    black = (0, 0, 0)

    def __init__(self, picture_path):
        # Initialize the PictureConverter with a picture path
        if os.path.exists(picture_path):
            self.picture_path = picture_path
            self.picture = Image.open(self.picture_path)
            self.width, self.height = self.picture.size
            self.color_matrix = []

        # Convert picture color
        else:
            logging.error("Can't find the picture at the specified path")
            exit(1)

    def split(self, team_nb, output_dir):
        # Split the picture into sub-images for multiple teams
        if team_nb == 1:
            # Handle the case when there is only one team
            self.picture.save(os.path.join(output_dir, "team1/team1.png"))
            return
        # Determine the number of rows and columns for the sub-images
        if team_nb == 2:
            rows, cols = 1, 2
        else:
            # Calculate rows and columns based on team number
            if team_nb % 2 == 0:
                rows = 2
                cols = team_nb // 2
            else:
                rows = 1
                cols = team_nb
        # Define column and row sizes
        # Define cols size
        # set width in rubik's unit
        r_width = self.width // 3
        cols_size = r_width // cols
        rest_cols = r_width % cols

        cols_size_val = []
        for i in range(int(cols)):
            cols_size_val.append(cols_size * 3)
        cols_size_val[-1] = int(cols_size_val[-1]) + int(rest_cols) * 3

        # Define height size
        # set height in rubik's unit
        r_height = self.height // 3
        rows_size = r_height // rows
        rest_rows = r_height % rows

        rows_size_val = []
        for i in range(int(rows)):
            rows_size_val.append(rows_size * 3)

        rows_size_val[-1] = int(rows_size_val[-1]) + int(rest_rows) * 3

        coords = []

        start_row = 0
        for row in rows_size_val:
            start_col = 0
            end_row = start_row + row
            for col in cols_size_val:
                end_col = start_col + col
                coords.append([start_col, start_row, end_col, end_row])
                start_col = end_col
            start_row = end_row
        # Initialize a counter for team numbering
        nb = 1
        for cood in coords:
            # Crop the sub-image
            sub_image = self.picture.crop((cood[0], cood[1], cood[2], cood[3]))
            # Save the sub-image to the appropriate team directory
            sub_image.save(os.path.join(output_dir, f"team{nb}/team{nb}.png"))
            # Increment the team number counter
            nb += 1

    def tile(self, block_size, out_folder, save_pic=True):
        # Tile the picture into smaller blocks
        if not os.path.exists(out_folder):
            logging.error("Can't find the out folder")
            exit(1)
        name, ext = os.path.splitext(self.picture_path)

        grid = product(range(0, self.height - self.height % block_size, block_size),
                       range(0, self.width - self.width % block_size, block_size))
        # Get coordinates of smaller blocks
        for i, j in grid:
            box = (j, i, j + block_size, i + block_size)
            crop_pic = self.picture.crop(box)
            # Append color matrix information
            self.color_matrix.append([[i, j], self.__to_color_matrix(crop_pic, block_size)])
            if save_pic:
                # Save the cropped picture
                out = os.path.join(out_folder, f'{int(i / 3)}_{int(j / 3)}{ext}')
                crop_pic.save(out)

    def test_rubiks_resolution(self):
        # Check if the picture resolution is compatible with a Rubik's Cube
        if self.width % 3 > 0 or self.height % 3 > 0:
            return False
        return True

    def get_matrix(self):
        # Get the color matrix
        return self.color_matrix

    def get_formatted_matrix(self):
        # Get the color matrix in a formatted representation
        res = []
        for colors in self.color_matrix:
            face = ""
            for line in colors:
                for char in line:
                    face += char
            res.append(face)
        return res

    def __to_color_matrix(self, crop_pic, block_size):
        # Convert a cropped picture into a color matrix
        matrix = []
        for i in range(0, block_size):
            line = []
            for j in range(0, block_size):
                line.append(self.__get_pixel_color_char(crop_pic, j, i))
            matrix.append(line)
        return matrix

    def __get_pixel_color_char(self, pic, x, y):
        # Get the color character for a specific pixel
        color_matrix = self.__get_pixel_color(pic, x, y)
        return self.__color_to_char(color_matrix)

    @staticmethod
    def __get_pixel_color(pic, x, y):
        # Get the color of a specific pixel in the picture
        return pic.getpixel((x, y))

    def __color_to_char(self, color_matrix):
        # Convert a color to a character representation
        match color_matrix:
            case self.red:
                return 'R'
            case self.green:
                return 'G'
            case self.blue:
                return 'B'
            case self.orange:
                return 'O'
            case self.yellow:
                return 'Y'
            case self.white:
                return 'W'
            case _:
                return 'N'


# Convert the picture colors
def __closest_color(self, pixel):
    target_colors = {
        'red': self.red,
        'green': self.green,
        'blue': self.blue,
        'yellow': self.yellow,
        'white': self.white,
        'orange': self.orange
    }
    min_distance = float('inf')
    closest_color = None

    for color, target_color in target_colors.items():
        r1, g1, b1 = pixel
        r2, g2, b2 = target_color
        distance = (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

        if distance < min_distance:
            min_distance = distance
            closest_color = color

    return target_colors[closest_color]


def __convert_image_to_target_colors(self):
    img = self.picture.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            pixel = pixels[i, j]
            new_color = self._closest_color(pixel)
            pixels[i, j] = new_color
    img.save("./test.png")
    self.picture = img


