import fitz  # PyMuPDF

def add_screenshot_to_first_page(input_pdf_path, screenshot_path, output_pdf_path):
    # Open the PDF document
    pdf_document = fitz.open(input_pdf_path)
    
    # Load the first page
    first_page = pdf_document.load_page(0)
    
    # Insert the screenshot image onto the first page
    # Adjust the rect to fit your needs
    screenshot_rect = fitz.Rect(0, 0, first_page.rect.width, first_page.rect.height)
    first_page.insert_image(screenshot_rect, filename=screenshot_path)

    # Save the modified PDF
    pdf_document.save(output_pdf_path)
    pdf_document.close()

# Paths to your files
input_pdf = r"C:\Users\sudha\Downloads\Optimized_PDF.pdf"
screenshot_path = r"C:\Users\sudha\Downloads\Screenshot 2024-08-26 103707.png"  # Path to your screenshot
output_pdf = r"C:\Users\sudha\Downloads\PDF_with_Screenshot.pdf"

add_screenshot_to_first_page(input_pdf, screenshot_path, output_pdf)
