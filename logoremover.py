import fitz  # PyMuPDF

# Paths to your PDF file using raw strings
input_pdf = r"C:\Users\sudha\Downloads\6523843d2cce78001806cd21_##_Is Matter Around Us Pure - Class Notes.pdf"
output_pdf = r"C:\Users\sudha\Downloads\Is_Matter_Around_Us_Pure_Class_Notes_NoLogo_Black.pdf"

# Open the PDF
pdf_document = fitz.open(input_pdf)

# Iterate through each page and locate the logo area (e.g., top-right corner)
for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)
    
    # Define the rectangle for the top-right corner to remove the logo
    # Doubling the size of the previous rectangle (assumed 50x50 previously)
    rect_to_remove = fitz.Rect(page.rect.width - 120, 0, page.rect.width, 100)  # Expanded dimensions
    
    # Add a redaction annotation and apply redaction with black color
    page.add_redact_annot(rect_to_remove, fill=(0, 0, 0))  # Redact with black fill (0, 0, 0) is RGB for black
    page.apply_redactions()

# Save the output PDF
pdf_document.save(output_pdf)
pdf_document.close()

print("Logo removed successfully! The new file is saved as 'Is_Matter_Around_Us_Pure_Class_Notes_NoLogo_Black.pdf'")
