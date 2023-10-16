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
        
        ##### DON'T TOUCH
        self.check_folder_exist()
        self.output_file = output_file
        self.doc = SimpleDocTemplate("pdfDocumentations/"+output_file, pagesize=letter)
        self.story = []

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
        
    def add_image(self, image_path, width=400, height=400):
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
        
        
        if len(move) > 1:
            realMove = move[0:1]
            
            match move[1:2]:
                case "'":
                    moveindex = "_Apostrophe"
                case "2":
                    moveindex = "_two"
            
        imagename = realMove
        imageindex = moveindex
        
        icon = imagename+imageindex
        
        
        return self.iconsPath + icon + '.png'
            
    def add_aligned_images(self, movements):
        data = [[Image(self.selectIcons(move), 25, 37) for move in movements]]
        col_widths = [25 for _ in range(len(movements))]
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