import os
import logging
from PIL import Image
from itertools import product


class PictureConverter:

    def __init__(self, picture_path):
        """
        Initialize the PictureConverter with a picture path and apply a specific color palette to the image.

        Args:
            picture_path (str): The file path to the input picture.

        The `PictureConverter` class is initialized with an image specified by `picture_path`. It performs the following steps:

        1. If the specified image exists, it proceeds with the initialization; otherwise, it logs an error message and exits.

        2. The image is loaded using `Image.open`, and its width and height are stored in class attributes.

        3. A specific palette for color mapping is defined, which contains six RGB colors representing the Rubik's cube colors.

        4. The image is converted to RGB mode to ensure it's in a suitable format for palette manipulation.

        5. A palette image is created with the specific Rubik's cube color palette.

        6. The input image is quantized using the specified palette, resulting in an image with a limited color set that matches
        the Rubik's cube colors.

        Args:
            picture_path (str): The file path to the input picture.

        Raises:
            IOError: If the specified image file does not exist.
        """

        if os.path.exists(picture_path):
            self.picture_path = picture_path
            self.picture = Image.open(self.picture_path)
            self.width, self.height = self.picture.size
            self.color_matrix = []

            rubiks_palette = [
                213, 37, 37,  # Red
                106, 190, 48,  # Green
                91, 110, 225,  # Blue
                251, 242, 54,  # Yellow
                255, 255, 255,  # White
                246, 121, 36  # Orange
            ]

            self.picture = self.picture.convert("RGB")

            palette_image = Image.new("P", (1, 1))
            palette_image.putpalette(rubiks_palette)

            self.picture = self.picture.quantize(colors=6, palette=palette_image)
        else:
            logging.error("Can't find the picture at the specified path")
            exit(1)

    def split(self, team_nb, output_dir):
        """
        Split the picture into sub-images for multiple teams.

        Args:
            team_nb (int): The number of teams for which to split the picture.
            output_dir (str): The output directory where the sub-images will be saved.

        Returns:
            None

        If there is only one team, the picture is saved as-is without splitting.

        For multiple teams, the picture is divided into sub-images according to the specified team number. The number of rows
        and columns for the sub-images is determined based on the team number.

        If the team number is 2, one row with 2 columns is created. For other team numbers, the rows and columns are
        calculated as follows:
        - If the team number is even, it results in 2 rows and team_nb // 2 columns.
        - If the team number is odd, it results in 1 row and team_nb columns.

        The column and row sizes are calculated based on the dimensions of the original picture and the number of rows and
        columns. The calculation ensures that the sub-images fit evenly within the original picture.

        Args:
            team_nb (int): The number of teams for which to split the picture.
            output_dir (str): The output directory where the sub-images will be saved.

        Returns:
            None

        Example:
            To split the picture for 3 teams and save the sub-images in the "output_images" directory:
            ```
            picture_converter.split(3, "output_images")
            ```

        This method automatically creates sub-images, saves them to the appropriate team directories, and increments the team
        number counter.

        Raises:
            IOError: If there is an issue saving the sub-images or if the output directory is not accessible.
        """

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
        """
        Tile the picture into smaller blocks and optionally save them.

        Args:
            block_size (int): The size of the smaller blocks.
            out_folder (str): The directory where the smaller blocks will be saved.
            save_pic (bool): If True, save the cropped pictures; if False, only extract color matrix information.

        Returns:
            None

        This method divides the picture into smaller blocks of the specified size. It generates a grid of coordinates for
        these blocks based on the original picture's dimensions.

        Args:
            block_size (int): The size of the smaller blocks.
            out_folder (str): The directory where the smaller blocks will be saved.
            save_pic (bool): If True, save the cropped pictures; if False, only extract color matrix information.

        Returns:
            None

        The method iterates through the grid of coordinates, creates a box for each block, and extracts the sub-image
        (crop_pic). If `save_pic` is set to True, it saves the cropped picture in the specified `out_folder`.

        The `color_matrix` attribute of the class is updated with information about the color composition of each block.
        The color matrix is a two-dimensional list that represents the colors within each block.

        Args:
            block_size (int): The size of the smaller blocks.
            out_folder (str): The directory where the smaller blocks will be saved.
            save_pic (bool): If True, save the cropped pictures; if False, only extract color matrix information.

        Returns:
            None

        Example:
            To tile the picture into 50x50 pixel blocks and save them in the "output_images" directory:
            ```
            picture_converter.tile(50, "output_images", save_pic=True)
            ```

        Note:
            When `save_pic` is set to False, only the color matrix information is collected, and no images are saved. This can
            be useful for processing and analyzing the colors within the blocks.

        Raises:
            IOError: If there is an issue saving the sub-images or if the output directory is not accessible.
        """

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
        """
        Check if the picture resolution is compatible with a Rubik's Cube.

        This method evaluates the dimensions (width and height) of the loaded picture and checks if they are
        compatible with a Rubik's Cube. The resolution is considered compatible if both the width and height are
        divisible by 3, ensuring the Rubik's Cube can be divided into even-sized rows and columns.

        Returns:
            bool: True if the resolution is compatible; False otherwise.
        """
        if self.width % 3 > 0 or self.height % 3 > 0:
            return False
        return True

    def get_matrix(self):
        """
        Get the color matrix of the Rubik's Cube faces.

        Returns:
            list: A list representing the color matrix of the Rubik's Cube, with nested lists for each face.
        """
        return self.color_matrix

    def get_pic_width(self):
        """
        Get the width of the loaded picture.

        Returns:
            int: The width of the picture in pixels.
        """
        return self.picture.width

    def get_formatted_matrix(self):
        """
        Get the color matrix of the Rubik's Cube faces in a formatted representation.

        This method takes the color matrix and converts it into a more human-readable format, where the colors of each face
        are represented as a string of characters, making it easier to interpret.

        Returns:
            list: A list of strings representing the formatted color matrix.
        """
        # Implementation of the method goes here
        res = []
        for colors in self.color_matrix:
            face = ""
            for line in colors:
                for char in line:
                    face += char
            res.append(face)
        return res

    def __to_color_matrix(self, crop_pic, block_size):
        """
        Convert a cropped picture into a color matrix.

        This method takes a cropped picture and converts it into a color matrix, where each element in the matrix represents
        the color of a pixel in the cropped picture.

        Args:
            crop_pic (PIL.Image): The cropped image to be converted.
            block_size (int): The size of the block for the color matrix.

        Returns:
            list: A list representing the color matrix of the cropped image.
        """
        # Convert a cropped picture into a color matrix
        matrix = []
        for i in range(0, block_size):
            line = []
            for j in range(0, block_size):
                line.append(self.__get_pixel_color_char(crop_pic, j, i))
            matrix.append(line)
        return matrix

    def __get_pixel_color_char(self, pic, x, y):
        """
        Get the color character for a specific pixel.

        This method extracts the color information for a specific pixel in the input image and maps it to a character
        representation based on predefined color values.

        Args:
            pic (PIL.Image): The input image.
            x (int): The x-coordinate of the pixel.
            y (int): The y-coordinate of the pixel.

        Returns:
            str: A character representing the color of the pixel.
        """
        # Get the color character for a specific pixel
        color_matrix = self.__get_pixel_color(pic, x, y)
        return self.__color_to_char(color_matrix)

    @staticmethod
    def __get_pixel_color(pic, x, y):
        """
        Get the color of a specific pixel in the picture.

        This method retrieves the color value of a specific pixel in the input image.

        Args:
            pic (PIL.Image): The input image.
            x (int): The x-coordinate of the pixel.
            y (int): The y-coordinate of the pixel.

        Returns:
            tuple: A tuple representing the RGB color values of the pixel.
        """
        return pic.getpixel((x, y))

    @staticmethod
    def __color_to_char(color_nb):
        """
        Convert a color to a character representation.

        This method takes a numeric color value and maps it to a character representation based on predefined color mappings.

        Args:
            color_nb (int): The numeric color value.

        Returns:
            str: A character representing the color.
        """
        # Convert a color to a character representation
        match color_nb:
            case 0:
                return 'R'
            case 1:
                return 'G'
            case 2:
                return 'B'
            case 5:
                return 'O'
            case 3:
                return 'Y'
            case 4:
                return 'W'
            case _:
                return 'N'
