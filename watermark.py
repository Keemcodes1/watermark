import PyPDF2

template = PyPDF2.PdfReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfWriter()

watermark_page = watermark.pages[0]




for page in (template.pages):
    page.merge_page(watermark_page)
    output.add_page(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)







# from pypdf import PdfWriter

# merger = PdfWriter()

# for pdf in ["super.pdf", "wtr.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()










# import PyPDF2

# # Open the Template and Watermark PDFs
# template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))

# # Create a PdfWriter Object
# output = PyPDF2.PdfWriter()

# # Get the Watermark Page
# watermark_page = watermark.pages[0]

# # Merge the Watermark with Each Template Page
# for page in template.pages:
#     page.merge_page(watermark_page)
#     output.add_page(page)

# # Write the Watermarked PDF to a New File
# with open('watermarked_output.pdf', 'wb') as file:
#     output.write(file)