import fitz  # PyMuPDF

def compress_pdf(input_pdf_path, output_pdf_path):
    # Open the PDF document
    pdf_document = fitz.open(input_pdf_path)
    
    # Create a new PDF to save the optimized result
    output_pdf_document = fitz.open()
    
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        # Save page with lower image quality
        output_pdf_document.insert_pdf(pdf_document, from_page=page_number, to_page=page_number)
    
    # Save the new optimized PDF
    output_pdf_document.save(output_pdf_path, deflate=True)  # 'deflate' compression for size reduction
    output_pdf_document.close()
    pdf_document.close()

# Paths to your PDF file using raw strings
input_pdf = r"C:\Users\sudha\Downloads\Optimized_PDF.pdf"
output_pdf = r"C:\Users\sudha\Downloads\Optimized254_PDF.pdf"

compress_pdf(input_pdf, output_pdf)
