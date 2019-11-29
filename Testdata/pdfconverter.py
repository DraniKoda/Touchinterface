from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter, TextConverter, XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from PyPDF2 import PdfFileReader

import io


def convert(case, fname):
    pagenums = list()
    file = open(fname, 'rb')
    pdf = PdfFileReader(file)
    number_of_pages = pdf.getNumPages()
    file.close
    i = 0
    while i < number_of_pages:
        pagenums.append(i)
        i += 1

    manager = PDFResourceManager()
    codec = 'utf-8'
    caching = True

    if case == 'text':
        output = io.StringIO()
        converter = TextConverter(
            manager, output, codec=codec, laparams=LAParams())
    if case == 'HTML':
        output = io.BytesIO()
        converter = HTMLConverter(
            manager, output, codec=codec, laparams=LAParams())

    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(fname, 'rb')

    for page in PDFPage.get_pages(infile, pagenums, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    print(pagenums)

    convertedPDF = output.getvalue()

    infile.close()
    converter.close()
    output.close()
    return convertedPDF


# //////////// main ///////////////////////
filePDF = '1.pdf'     # input
fileHTML = 'myHTML.html'   # output
fileTXT = 'myTXT.txt'     # output

case = "HTML"

if case == 'HTML':
    convertedPDF = convert('HTML', filePDF)
    fileConverted = open(fileHTML, "wb")
if case == 'text':
    convertedPDF = convert('text', filePDF)
    fileConverted = open(fileTXT, "w")

fileConverted.write(convertedPDF)
fileConverted.close()
# print(convertedPDF)
