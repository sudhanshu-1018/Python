import fitz  # PyMuPDF
from PIL import Image
import io

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

def compress_image(image_bytes, quality=30):
    image = Image.open(io.BytesIO(image_bytes))
    output = io.BytesIO()
    image.save(output, format="JPEG", quality=quality, optimize=True)
    return output.getvalue()

def compress_pdf(input_pdf_path, output_pdf_path):
    pdf_document = fitz.open(input_pdf_path)
    output_pdf_document = fitz.open()
    
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        new_page = output_pdf_document.new_page(width=page.rect.width, height=page.rect.height)
        
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            compressed_image_bytes = compress_image(image_bytes)
            new_page.insert_image(page.rect, stream=compressed_image_bytes)
        
        # Copy text and other elements from the old page
        new_page.insert_text((72, 72), "Compressed Page", fontsize=12)  # Placeholder for text
        
    output_pdf_document.save(output_pdf_path, deflate=True)
    output_pdf_document.close()
    pdf_document.close()

# Define file paths
input_pdf = r"C:\Users\sudha\Downloads\Optimized_PDF.pdf"
screenshot_path = r"C:\Users\sudha\Downloads\Screenshot 2024-08-26 103707.png"
temp_pdf = r"C:\Users\sudha\Downloads\Temp_PDF_With_Screenshot.pdf"
final_output_pdf = r"C:\Users\sudha\Downloads\Compressed55245_PDF.pdf"

# Add screenshot to the first page
add_screenshot_to_first_page(input_pdf, screenshot_path, temp_pdf)

# Compress the PDF
compress_pdf(temp_pdf, final_output_pdf)
