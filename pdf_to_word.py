from pdf2docx import Converter

def pdf_to_word(pdf_path, docx_path):
    print("[INFO] Initializing converter...")
    cv = Converter(pdf_path)
    
    print("[INFO] Starting conversion...")
    cv.convert(docx_path, start=0, end=1)  # Start with one page
    
    print("[INFO] Conversion completed!")
    cv.close()

# Convert PDF to Word
pdf_path = r"C:\Users\sudha\Downloads\Ragini_Kumari_CV.pdf"
docx_path = r"C:\Users\sudha\Downloads\Ragini_Kumari_CV.docx"
pdf_to_word(pdf_path, docx_path)

