from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader

def secure_pdf(PATH,password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(PATH)
    # READ PDF FILE
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    # ENCRYPT
    parser.encrypt(password)
    # OPEN ENCRYPTED FILE
    with open(f"encypted_{PATH}","wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{PATH} Created...")
if __name__ == "__main__":
    PATH = input("Your PDF file PATH...")
    password = input("Type the password you want for encrypting")
    secure_pdf(PATH,password)
