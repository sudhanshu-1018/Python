import fitz  # PyMuPDF
import pikepdf

# Paths to your PDF file using raw strings
input_pdf = r"C:\Users\sudha\Downloads\Is_Matter_Around_Us_Pure_Class_Notes_NoPage1.pdf"
output_pdf = r"C:\Users\sudha\Downloads\Is_Matter_Around_Us_Pure_Class_Notes_NoPage2.pdf"
optimized_pdf = r"C:\Users\sudha\Downloads\cleaned_output.pdf"

# Open the PDF document
pdf_document = fitz.open(input_pdf)

# Create a new PDF to save the result
output_pdf_document = fitz.open()

# Iterate through each page except the first one and add it to the new PDF
for page_number in range(1, len(pdf_document)-2):  # Skip the first page (index 0)
    page = pdf_document.load_page(page_number)
    output_pdf_document.insert_pdf(pdf_document, from_page=page_number, to_page=page_number)

# Save the new PDF without the first page
output_pdf_document.save(output_pdf)
output_pdf_document.close()
pdf_document.close()

# Optimize the new PDF using pikepdf
pdf = pikepdf.Pdf.open(output_pdf)
pdf.save(optimized_pdf, optimize_images=True)

print(f"First page removed successfully! The new file is saved as '{output_pdf}' and optimized as '{optimized_pdf}'.")
