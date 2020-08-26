import fpdf


def print_pdf_map():
    # PDF constructor:
    # Portrait, millimeter units, A4 page size
    pdf = fpdf.FPDF("P", "mm", "A4")
    # create a new page
    pdf.add_page()
    # Set font: arial, bold, size 20
    pdf.set_font('Arial', 'B', 20)
    # Layout cell: 160 x 25mm, title, no border, centered
    pdf.cell(160, 25, 'Hancock County Boundary', border=0, align="C")
    # Write the image specifying the size
    pdf.image("sample_data\hancock.png", 25, 50, 110, 160)
    # Save the file: filename, F = to file System
    pdf.output('sample_data\map.pdf', 'F')


if __name__ == "__main__":
    print_pdf_map()
