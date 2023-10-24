import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


class PDFGenerator:
    def __init__(self, output_file, out_folder="pdfDocumentations"):
        """
        Initialize the PDF documentation generator.

        Args:
            output_file (str): The name of the output PDF file.
            out_folder (str, optional): The folder where the PDFs will be saved. Default is 'pdfDocumentations'.

        Example:
            pdf_generator = PDFDocumentationGenerator("output.pdf", "pdfFolder")

        Note:
            This constructor sets up the PDF documentation generator with configuration parameters and initializes the
            output PDF file, pagesize, and story.
        """
        self.pdfsFolder = out_folder
        self.iconsPath = "assets/icons/"
        self.iconsSize = {"h": 56, "w": 38}  # Height and With of the image in px

        # DON'T TOUCH
        self.check_folder_exist()
        self.output_file = output_file
        self.doc = SimpleDocTemplate(self.pdfsFolder + "/" + output_file, pagesize=letter)
        self.story = []

    @staticmethod
    def reformat_image_name(filename):
        """
        Reformat an image name.

        Args:
            filename (str): The original image filename.

        Returns:
            str: The reformatted image name.

        Example:
            new_name = PDFDocumentationGenerator.reformat_image_name("1_2.png")

        Note:
            This static method reformats an image filename. It is used to convert an image filename from one format to
            another.
        """
        file_name_array = filename.split("_")
        return str(int(file_name_array[0])) + ":" + str(int(file_name_array[1]))

    def explanation_page(self):
        """
        Add an explanation page to the PDF documentation.

        Example:
            pdf_generator.explanation_page()

        Note:
            This method adds an explanation page to the PDF documentation. It includes a title, an image, and explanatory
            text.
        """
        self.add_title("Fresco Documentation")

        self.add_image("assets/exemple.png", 600, 400)

        self.add_text(
            "You Fresco has been splitted in many parts like the example above, each part can be identified by its coordinates, the top-left corner is identified as 0:0")

        self.add_page_break()

    def add_title(self, title):
        """
        Add a title to the PDF documentation.

        Args:
            title (str): The title to be added.

        Example:
            pdf_generator.add_title("Document Title")

        Note:
            This method adds a title to the PDF documentation.
        """
        style_title = getSampleStyleSheet()["Title"]
        style_title.alignment = 1
        self.story.append(Paragraph(title, style_title))
        self.story.append(Spacer(1, 12))

    def add_text(self, text):
        """
        Add text to the PDF documentation.

        Args:
            text (str): The text to be added.

        Example:
            pdf_generator.add_text("This is some text.")

        Note:
            This method adds text to the PDF documentation.
        """
        styles = getSampleStyleSheet()
        self.story.append(Paragraph(text, styles["Normal"]))
        self.story.append(Spacer(1, 12))

    def add_comment(self, comment):
        """
        Add a comment in red to the PDF.

        Args:
            comment (str): The comment text to be added.

        Example:
            pdf_generator.add_comment("This is a critical comment.")

        Note:
            This method adds a comment in red text to the PDF documentation. It uses HTML formatting to set the text color
            to red and appends it to the document's story with a small vertical spacer.
        """
        styles = getSampleStyleSheet()
        comment_text = f"<font color=red>{comment}</font>"
        self.story.append(Paragraph(comment_text, styles["Normal"]))
        self.story.append(Spacer(1, 6))

    def add_image(self, image_path, width=200, height=200):
        """
        Add an image to the PDF documentation.

        Args:
            image_path (str): The path to the image file.
            width (int): The width of the image in pixels. Default size 200 pixels.
            height (int): The height of the image in pixels. Default size 200 pixels.

        Example:
            pdf_generator.add_image("image.png", 400, 300)

        Note:
            This method adds an image to the PDF documentation with the specified width and height.
        """
        img = Image(image_path, width, height)
        self.story.append(img)
        self.story.append(Spacer(1, 12))

    def generate_pdf(self):
        """
        Generate the PDF documentation.

        This method builds the PDF document using the provided story and saves it to the specified output file.

        Example:
            pdf_generator = PDFDocumentationGenerator("output.pdf")
            pdf_generator.generate_pdf()

        Note:
            Call this method to generate the PDF documentation. It uses the story created with add_title, add_image,
            add_text, and other methods to build the content of the PDF document. The generated PDF will be saved to the
            output file specified during the initialization of the PDFDocumentationGenerator instance.
        """
        self.doc.build(self.story)

    def check_folder_exist(self):
        """
        Check if the PDF output folder exists or create it if necessary.

        Returns:
            bool: True if the folder was created; False if it already exists.

        Example:
            pdf_generator = PDFDocumentationGenerator("output.pdf")
            folder_created = pdf_generator.check_folder_exist()

        Note:
            This method checks if the specified PDF output folder exists. If it doesn't exist, it creates the folder
            and returns True. If the folder already exists, it returns False. The folder path is defined during the
            initialization of the PDFDocumentationGenerator instance.
        """
        if not os.path.exists(self.pdfsFolder):
            os.mkdir(self.pdfsFolder)
            return True
        else:
            return False

    def add_page_break(self):
        """
        Add a page break to the PDF documentation.

        Example:
            pdf_generator.add_page_break()

        Note:
            This method adds a page break to the PDF documentation, moving the content to the next page.
        """
        self.story.append(PageBreak())

    def select_icons(self, move):
        """
        Determine the icons to use for a movement.

        Args:
            move (str): The movement identifier, e.g., "R", "U'", "F2".

        Returns:
            tuple: A tuple containing the number of moves and the path to the corresponding icon image.

        Example:
            move_processor = MoveProcessor()
            num_moves, icon_path = move_processor.select_icons("R'")

        Note:
            This method takes a movement identifier as input and returns a tuple with two elements:
            1. The number of moves, which is typically 1 but can be 2 for double turns.
            2. The path to the icon image representing the movement.

            The input move can include single moves (e.g., "R"), double moves (e.g., "U2"), or inverse moves (e.g., "F'").

            The icon image path is constructed based on the input move.

        """
        icon = ""
        real_move = move
        move_index = ""
        nb_move = 1

        if len(move) > 1:
            real_move = move[0:1]

            match move[1:2]:
                case "'":
                    move_index = "_Apostrophe"
                case "2":
                    move_index = ""
                    nb_move = 2

        imagename = real_move
        imageindex = move_index

        icon = imagename + imageindex

        return nb_move, self.iconsPath + icon + '.png'

    @staticmethod
    def remove_useless_move(moves):
        """
        Remove unnecessary moves in a sequence.

        Args:
            moves (list): A list of movement identifiers.

        Returns:
            list: A list of cleaned movement identifiers with unnecessary moves removed.

        Example:
            move_processor = MoveProcessor()
            moves = ["R", "U2", "U'", "R2", "L2", "R"]
            cleaned_moves = move_processor.remove_useless_move(moves)

        Note:
            This method takes a list of movement identifiers and removes unnecessary moves from the sequence.
            Unnecessary moves are consolidated to simplify the sequence.

            For example, if the input sequence contains redundant moves (e.g., "R2" followed by "R2"), this method
            cleans the sequence by removing or modifying the redundant moves to make it more concise.

            The cleaned sequence is returned as a list.

        """
        if not moves:
            return []

        cleared_moves = [moves[0]]
        move_count = {"L": 0, "R": 0, "U": 0, "D": 0, "F": 0, "B": 0, "L'": 0, "R'": 0, "U'": 0, "D'": 0, "F'": 0,
                      "B'": 0}
        move_count[moves[0]] = 1
        last_move = cleared_moves[-1]
        need_to_pop = False

        for i in range(1, len(moves)):
            current_move = moves[i]

            if current_move == last_move:
                move_count[current_move] += 1
            else:
                move_count[current_move] += 1

                while move_count[last_move] >= 4:
                    move_count[last_move] -= 4

                if move_count[last_move] == 3:
                    cleared_moves.pop()
                    cleared_moves.append(last_move + "'")
                elif move_count[last_move] == 2:
                    cleared_moves.append(last_move)
                    cleared_moves.append(last_move)
                elif move_count[last_move]:
                    cleared_moves.append(last_move)

                if i == len(moves) - 1:
                    cleared_moves.append(current_move)
                elif i == 2:
                    cleared_moves.pop(1)

                if current_move == last_move + "'" or current_move + "'" == last_move or need_to_pop:
                    if need_to_pop:
                        if len(cleared_moves) >= 2:
                            cleared_moves.pop(-2)
                        else:
                            cleared_moves.pop(-1)
                    else:
                        cleared_moves.pop()
                    need_to_pop = not need_to_pop

                move_count[last_move] = 0
                last_move = current_move

        return cleared_moves

    def add_aligned_images(self, movements):
        """
        Add aligned images for movements to the PDF.

        Args:
            movements (list): A list of movement identifiers.

        Example:
            move_processor = MoveProcessor()
            moves = ["R", "U2", "U'", "R2", "L2", "R"]
            move_processor.add_aligned_images(moves)

        Note:
            This method takes a list of movement identifiers and adds aligned images for each movement to the PDF.

            It creates a list of Image objects for the movements, and for movements that correspond to double turns (e.g., "U2"),
            it adds two images side by side. The images are aligned in rows, with a maximum of 10 images per row.

            The resulting arrangement of images is added to the PDF story for inclusion in the PDF document.

        """
        images = []

        for move in movements:
            # Call selectIcon to determine the number of icons (1 or 2)
            num_icons, icon = self.select_icons(move)

            # Create Image objects based on the result of selectIcon
            image = Image(icon, self.iconsSize["w"], self.iconsSize["h"])
            images.append(image)

            if num_icons == 2:
                image = Image(icon, self.iconsSize["w"], self.iconsSize["h"])
                images.append(image)

        col_widths = [self.iconsSize["w"] for _ in range(len(images))]

        # Split images into rows of 10
        rows_of_images = [images[i:i + 10] for i in range(0, len(images), 10)]

        for row in rows_of_images:
            data = [row]
            table = Table(data, colWidths=col_widths)
            table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))
            self.story.append(table)
