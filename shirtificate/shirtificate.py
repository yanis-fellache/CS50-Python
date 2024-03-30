from fpdf import FPDF
from PIL import Image

class PDFWithFile(FPDF):
    def write_file(self, file, name):
        self.add_page()
        image = Image.open(file)

        img_width, img_height = image.size
        aspect_ratio = img_width / img_height
        max_width = 190
        new_width = min(max_width, img_width)
        new_height = new_width / aspect_ratio
        x = (210 - new_width) / 2
        y = (297 - new_height) / 2

        self.image(file, x, y, new_width)

        self.set_font("helvetica", "B", 45)
        self.set_text_color(0, 0, 0)
        width = img_width / 3
        height = img_height / 15
        self.cell(width, height, "CS50 Shirtificate", align="C", ln=True)

        self.set_font("helvetica", "B", 30)
        self.set_text_color(255, 255, 255)
        n_width = img_width/3
        self.cell(n_width,150, f"{name} took CS50", align= "C", ln=True)



def main():
    file = 'shirtificate.png'
    name = input("What's your name? ")
    pdf = PDFWithFile()
    pdf.write_file(file, name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
