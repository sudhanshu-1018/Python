# #extracting text from pdf file
# # importing required modules
# import PyPDF2
 
# # creating a pdf file object
# pdfFileObj = open('data\python_book_01.pdf', 'rb')
 
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfReader(pdfFileObj)
 
# # printing number of pages in pdf file
# print(len(pdfReader.pages))
 
# # creating a page object
# pageObj = pdfReader.pages[0]
 
# # extracting text from page
# print(pageObj.extract_text())
 
# # closing the pdf file object
# pdfFileObj.close()


#merge pdf

# from PyPDF2 import PdfWriter

# merger = PdfWriter()

# for pdf in ["ragini resume.pdf", "doc ty.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()



#merge pdf
from PyPDF2 import PdfWriter
import os
merger=PdfWriter()
files=[file for file in os.listdir() if file .endswith(".pdf")]
for pdf in files:
    merger.append(pdf)
merger.write("two2.pdf")
merger.close()


#merge pdf with specific pages
# from PyPDF2 import PdfWriter

# merger = PdfWriter()

# input1 = open("document1.pdf", "rb")
# input2 = open("document2.pdf", "rb")
# input3 = open("document3.pdf", "rb")

# # add the first 3 pages of input1 document to output
# merger.append(fileobj=input1, pages=(0, 3))

# # insert the first page of input2 into the output beginning after the second page
# merger.merge(position=2, fileobj=input2, pages=(0, 1))

# # append entire input3 document to the end of the output document
# merger.append(input3)

# # Write to an output PDF document
# output = open("document-output.pdf", "wb")
# merger.write(output)

# # Close File Descriptors
# merger.close()
# output.close()



# extra for understanding only
# merger.append(pdf, pages=(0, 3))    # first 3 pages
# merger.append(pdf, pages=(0, 6, 2)) # pages 1,3, 5