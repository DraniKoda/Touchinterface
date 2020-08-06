from PyPDF2 import PdfFileReader
import fitz
import os
import io
readdir = "./data"

OrdnerListe = os.listdir(readdir)
os.chdir(readdir)

for jpg_file in OrdnerListe:
    if jpg_file.endswith(".jpg") | jpg_file.endswith(".png"):
        os.remove(jpg_file)

count = 1
for pdf_file in OrdnerListe:
    if pdf_file.endswith(".pdf") | pdf_file.endswith(".PDF"):
        pagenumber = PdfFileReader(open(pdf_file, 'rb')).getNumPages()
        # print(pagenumber)

        for i in range(pagenumber):
            # print(i)
            doc = fitz.open(pdf_file)
            page = doc.loadPage(i)
            pix = page.getPixmap()
            if i < 10:
                x = str(0) + str(i)
            else:
                x = str(i)
            pix.writePNG(str(count) + "_" + x + ".png")
        count += 1
