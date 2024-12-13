import pikepdf

def clean_up_pdf(input_pdf_path, output_pdf_path):
    pdf = pikepdf.Pdf.open(input_pdf_path)
    pdf.save(output_pdf_path)
    pdf.close()

input_pdf = r"C:\Users\sudha\Downloads\Optimized_PDF.pdf"
output_pdf = r"C:\Users\sudha\Downloads\Final_Optimized_PDF.pdf"

clean_up_pdf(input_pdf, output_pdf)
