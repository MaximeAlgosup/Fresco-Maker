import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

class PDFGenerator:
    def __init__(self, output_file):
        ##### Config 
        self.pdfsFolder = "pdfDocumentations"
        self.iconsPath = "PdfGenerator/icons/"
        self.iconsSize = { "h":56, "w":38 } # Height and With of the image in px
        
        ##### DON'T TOUCH
        self.check_folder_exist()
        self.output_file = output_file
        self.doc = SimpleDocTemplate("pdfDocumentations/"+output_file, pagesize=letter)
        self.story = []
        
    def explainationPage(self):
        
        self.add_title("Fresco Documentation")
        
        self.add_image("PDFGenerator/exemple.png", 600, 400)
        
        self.add_text("You Fresco has been splitted in many parts like the exemple above, each part can be identified by is coords the top-left corner is identified as 0:0")
        
        self.add_pageBreak()

    def add_title(self, text):
        style_title = getSampleStyleSheet()["Title"]
        style_title.alignment = 1
        self.story.append(Paragraph(text, style_title))
        self.story.append(Spacer(1, 12))

    def add_text(self, text):
        #Add a simple text to your pdf
        styles = getSampleStyleSheet()
        self.story.append(Paragraph(text, styles["Normal"]))
        self.story.append(Spacer(1, 12))

    def add_comment(self, comment):
        #add a comment in red to your pdf
        styles = getSampleStyleSheet()
        comment_text = f"<font color=red>{comment}</font>"
        self.story.append(Paragraph(comment_text, styles["Normal"]))
        self.story.append(Spacer(1, 6))
        
    def add_image(self, image_path, width=200, height=200):
        # add an image to your pdf
        img = Image(image_path, width, height)
        self.story.append(img)
        self.story.append(Spacer(1, 12))

    def generate_pdf(self):
        # Build the PDF
        self.doc.build(self.story)

    def check_folder_exist(self):
        # Check if the pdf output folder exist or if it need to be create
        if not os.path.exists("./" + self.pdfsFolder):
            os.mkdir("./" + self.pdfsFolder)
            return True
        else: 
           return False
       
    def add_pageBreak(self):
        self.story.append(PageBreak())
       
    def selectIcons(self, move):
        icon = ""
        realMove = move
        moveindex = ""
        nb_move = 1
        
        
        if len(move) > 1:
            realMove = move[0:1]
            
            match move[1:2]:
                case "'":
                    moveindex = "_Apostrophe"
                case "2":
                    moveindex = ""
                    nb_move = 2
                    
            
        imagename = realMove
        imageindex = moveindex
        
        icon = imagename+imageindex
        
        
        return nb_move, self.iconsPath + icon + '.png'
            
    def add_aligned_images(self, movements):
        # Create a list to store the Image objects
        images = []

        for move in movements:
            # Call selectIcon to determine the number of icons (1 or 2)
            num_icons, icon = self.selectIcons(move)

            # Create Image objects based on the result of selectIcon
            image = Image(icon, self.iconsSize["w"], self.iconsSize["h"])
            images.append(image)
            
            if num_icons == 2:
                image = Image(icon, self.iconsSize["w"], self.iconsSize["h"])
                images.append(image)
                # Add a second image if num_icons is 2

        col_widths = [self.iconsSize["w"] for _ in range(len(images))]

        # Split images into rows of 10
        rows_of_images = [images[i:i+10] for i in range(0, len(images), 10)]

        for row in rows_of_images:
            data = [row]
            table = Table(data, colWidths=col_widths)
            table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))
            self.story.append(table)

# How to generate a PDF
# call the class by passing the name of the output file
# use these method to add component in your pdf
# when you did it all just use the generate_pdf method and run the script