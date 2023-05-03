from fpdf import FPDF

# get user's name
name = input("Enter your name: ")

# create PDF object
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

# set font and text color
pdf.set_font('Arial', 'B', 40)
pdf.set_text_color(255, 255, 255)

# add title
pdf.cell(0, 40, 'CS50 Shirtificate', 0, 1, 'C', 0)

# add shirt image
pdf.image('shirtificate.png', x=50, y=100, w=110, h=110)

# add name
pdf.set_xy(95, 130)
pdf.cell(0, 0, name, 0, 1, 'C')

# output PDF
pdf.output('shirtificate.pdf', 'F')
