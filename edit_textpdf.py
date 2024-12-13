import pdfplumber

# Open the PDF and extract text and coordinates
pdf_path = r"C:\Users\sudha\Downloads\Ragini_Kumari_CV.pdf"
with pdfplumber.open(pdf_path) as pdf:
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    print(text)
    
    # Extract text with its bounding boxes (coordinates)
    for word in first_page.extract_words():
        print(word)
