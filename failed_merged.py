import PyPDF2

pdf1= open('pdfs/output1.pdf', 'rb')
pdf2= open('pdfs/output2.pdf', 'rb')

file1 = PyPDF2.PdfReader(pdf1)
file2 = PyPDF2.PdfReader(pdf2)
output = PyPDF2.PdfMerger()
output.append(file1)
output.append(file2)

with open("failed_merged.pdf", "wb") as outputStream:
    output.write(outputStream)


# Close the PDF files
pdf1.close()
pdf2.close()
