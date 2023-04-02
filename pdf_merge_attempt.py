import PyPDF2

pdf1= open('pdfs/output1.pdf', 'rb')
pdf2= open('pdfs/output2.pdf', 'rb')

file1 = PyPDF2.PdfReader(pdf1)
file2 = PyPDF2.PdfReader(pdf2)
output = PyPDF2.PdfWriter()
page = file1.pages[0]
page.merge_page(file2.pages[0])
output.add_page(page)

with open("merged_attempt.pdf", "wb") as outputStream:
    output.write(outputStream)

# Close the PDF files
pdf1.close()
pdf2.close()
