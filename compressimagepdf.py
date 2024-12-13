import fitz  # PyMuPDF
from PIL import Image
import io

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
        
        # Create a new page in the output PDF with the same dimensions as the original
        new_page = output_pdf_document.new_page(width=page.rect.width, height=page.rect.height)
        
        # Extract and insert images
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            compressed_image_bytes = compress_image(image_bytes)
            # Insert the compressed image onto the new page
            new_page.insert_image(page.rect, stream=compressed_image_bytes)
        
        # If there's text or other elements, you need to handle them separately
        # For simplicity, we're just copying the images here

    # Save the compressed PDF
    output_pdf_document.save(output_pdf_path, deflate=True)
    output_pdf_document.close()
    pdf_document.close()

input_pdf = r"C:\Users\sudha\Downloads\Optimized_PDF.pdf"
output_pdf = r"C:\Users\sudha\Downloads\Compressed5465_PDF.pdf"

compress_pdf(input_pdf, output_pdf)
