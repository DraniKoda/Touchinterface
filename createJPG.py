from PyPDF2 import PdfFileReader
import fitz
import os
import io
readdir = "./data"

OrdnerListe = os.listdir(readdir)
os.chdir(readdir)


count = 1
for pdf_file in OrdnerListe:
    if pdf_file.endswith(".pdf"):
        pagenumber = PdfFileReader(open(pdf_file, 'rb')).getNumPages()
        # print(pagenumber)

        for i in range(pagenumber):
            # print(i)
            doc = fitz.open(pdf_file)
            page = doc.loadPage(i)
            pix = page.getPixmap()
            pix.writePNG(str(count) + "_" + str(i) + ".png")
        count += 1
