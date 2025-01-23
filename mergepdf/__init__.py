import os
from reportlab.pdfgen.canvas import Canvas
def start():
    ppi = 300  # Set the desired PPI
    width_in_inches = 8.27  # Width of the page in inches (A4 size)
    height_in_inches = 11.69  # Height of the page in inches (A4 size)
    width = width_in_inches * ppi
    height = height_in_inches * ppi
    canvas = Canvas("hello.pdf" , pagesize=(width, height), boarder=0, )
    with os.scandir("Firmen") as files:
        perPage = 0
        for i, entry in enumerate(files):
            canvas.drawImage(entry, 0, 0 + perPage * 1170, preserveAspectRatio=True)
            perPage += 1
            if ((i+1) % 3 == 0):
                perPage = 0
                canvas.showPage()
    canvas.save()