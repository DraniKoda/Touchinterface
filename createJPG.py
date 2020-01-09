import subprocess
import os
import io
from PyPDF2 import PdfFileReader
readdir = "./data"

OrdnerListe = os.listdir(readdir)


os.chdir(readdir)


# scanning the directory of all the data and creating the html code per data and page

pdftoppm_path = r"C:\Program Files (x86)\Poppler\bin\pdftoppm.exe"
count = 1
for pdf_file in OrdnerListe:
    if pdf_file.endswith(".pdf"):
        subprocess.Popen('"%s" -jpeg %s %s' %
                         (pdftoppm_path, pdf_file, count))
        count += 1
