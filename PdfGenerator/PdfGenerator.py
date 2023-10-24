import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

class PDFGenerator:
    def __init__(self, output_file, out_folder="pdfDocumentations"):
        # Config
        self.pdfsFolder = out_folder
        self.iconsPath = "PdfGenerator/icons/"
        self.iconsSize = {"h": 56, "w": 38}  # Height and Width of the image in px

        # DON'T TOUCH
        self.check_folder_exist()
        self.output_file = output_file
        self.doc = SimpleDocTemplate(self.pdfsFolder + "/" + output_file, pagesize=letter)
        self.story = []

    @staticmethod
    def reformat_image_name(filename):
        # Function to reformat an image name
        file_name_array = filename.split("_")
        return str(int(file_name_array[0])) + ":" + str(int(file_name_array[1]))

    def explanation_page(self):
        # Add the explanation page to the PDF

        self.add_title("Fresco Documentation")

        self.add_image("PDFGenerator/exemple.png", 600, 400)

        self.add_text(
            "You Fresco has been splitted in many parts like the example above, each part can be identified by its coordinates, the top-left corner is identified as 0:0")

        self.add_page_break()

    def add_title(self, text):
        # Add a title to the PDF

        style_title = getSampleStyleSheet()["Title"]
        style_title.alignment = 1
        self.story.append(Paragraph(text, style_title))
        self.story.append(Spacer(1, 12))

    def add_text(self, text):
        # Add a simple text to the PDF
        styles = getSampleStyleSheet()
        self.story.append(Paragraph(text, styles["Normal"]))
        self.story.append(Spacer(1, 12))

    def add_comment(self, comment):
        # Add a comment in red to the PDF
        styles = getSampleStyleSheet()
        comment_text = f"<font color=red>{comment}</font>"
        self.story.append(Paragraph(comment_text, styles["Normal"]))
        self.story.append(Spacer(1, 6))

    def add_image(self, image_path, width=200, height=200):
        # Add an image to the PDF
        img = Image(image_path, width, height)
        self.story.append(img)
        self.story.append(Spacer(1, 12))

    def generate_pdf(self):
        # Build the PDF
        self.doc.build(self.story)

    def check_folder_exist(self):
        # Check if the pdf output folder exists or if it needs to be created
        if not os.path.exists("./" + self.pdfsFolder):
            os.mkdir("./" + self.pdfsFolder)
            return True
        else:
            return False

    def add_page_break(self):
        # Add a page break to the PDF
        self.story.append(PageBreak())

    def select_icons(self, move):
        # Determine the icons to use for a movement

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
        # Remove unnecessary moves in a sequence

        if not moves:
            return []

        cleared_moves = [moves[0]]
        move_count = {"L": 0,"R": 0,"U": 0,"D": 0,"F": 0,"B": 0,"L'": 0,"R'": 0,"U'": 0,"D'": 0,"F'": 0,"B'": 0}
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
        # Add aligned images for movements to the PDF
        # Create a list to store the Image objects
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
