import subprocess
from PyPDF2 import PdfFileReader
import os
import io
readdir = "/Users/raphi/git/Webinterface_Touchpanel/data"
savedir = "/Users/raphi/git/Webinterface_Touchpanel"
OrdnerListe = os.listdir(readdir)
NameSplit = list()
i = 0
j = 0
x = 0
htmldata = list()
pagenum = str()
linkname = list()
link = list()
dataId = 0
count = 1
pdftoppm_path = r"C:\Program Files (x86)\Poppler\bin\pdftoppm.exe"


# pdf_dir = r"C:\Users\raphi\git\pdftoimg"
os.chdir(readdir)


# for pdf_file in os.listdir(readdir):

# if pdf_file.endswith(".pdf"):

#     subprocess.Popen('"%s" -jpeg %s out' % (pdftoppm_path, pdf_file))


# scanning the directory of all the data and creating the html code per data and page
while i < len(OrdnerListe):
    NameSplit = OrdnerListe[i].split(".")

    if NameSplit[1] == "pdf":
        subprocess.Popen('"%s" -jpeg %s %s' %
                         (pdftoppm_path, OrdnerListe[i], NameSplit[0]))
        count += 1

    #     file = open(
    #         '/Users/raphi/git/Webinterface_Touchpanel/data/' + OrdnerListe[i], 'rb')
    #     pdf = PdfFileReader(file)
    #     NumberOfPages = pdf.getNumPages()
    #     file.close
    #     j = 0
    #     while j < NumberOfPages:
    #         j += 1
    #         dataId += 1
    #         pagenum = str(j)
    #         htmldata.append('\n<embed class = "embedded pdf" id="' + str(dataId) + '" src = "data/' +
    #                         OrdnerListe[i] + '#page=' + pagenum +
    #                         '&scrollbar=0&view=fit&toolbar=0&statusbar=0&navpanes=0" type = "application/pdf">')
while i < len(OrdnerListe):
    NameSplit = OrdnerListe[i].split(".")

    if NameSplit[1] == "png":
        dataId += 1
        htmldata.append('\n<img class="embedded" id="' + str(dataId) + '" src="data/' +
                        OrdnerListe[i] + '" alt="image">')
    if NameSplit[1] == "jpg":
        dataId += 1
        htmldata.append('\n<img class="embedded" id="' + str(dataId) + '" src="data/' +
                        OrdnerListe[i] + '" alt="image">')

    i += 1

file = open('/Users/raphi/git/Webinterface_Touchpanel/link.txt', 'r+')
link = file.readlines()
file.close

file = open('/Users/raphi/git/Webinterface_Touchpanel/menschen.txt', 'r+')
menschen = file.readlines()
file.close

######################################################################################
# building up the html file here
os.chdir(savedir)


htmlinput = '<!DOCTYPE html>\n'
htmlinput = htmlinput + '<html lang="de">\n'
htmlinput = htmlinput + '<link rel = "stylesheet" href = "stylesheet.css">\n'
htmlinput = htmlinput + '<title>Webinterface Touchpanel</title>\n'
htmlinput = htmlinput + '\n<body>\n'
htmlinput = htmlinput + \
    '<button type = "button" class = "leftButton" onclick = "prevStep()"><img src="arrowleft.png" alt="links" height="50" width="50"></button>\n'
htmlinput = htmlinput + \
    '<button type = "button" class = "rightButton" onclick = "nextStep()"><img src="arrowright.png" alt="rechts" height="50" width="50"></button>\n'


htmlinput = htmlinput + '<div class = "flex-container">\n'

x = 0
while x < len(link):
    htmlinput = htmlinput + '<div class="controlBar">\n<a class="link" href ="' + \
        link[x + 1] + '">' + link[x] + '</a>\n</div>\n'
    x += 2

htmlinput = htmlinput + '</div>\n'

x = 0
while x < len(htmldata):
    htmlinput = htmlinput + htmldata[x]
    x += 1


htmlinput = htmlinput + '\n<script defer src = "javascript.js"></script>\n'
htmlinput = htmlinput + '<script defer src = "jquery-3.1.1.min.js"></script>\n'
htmlinput = htmlinput + '\n</body>\n'
htmlinput = htmlinput + '</html>'


# writing the html file

htmlfile = open("index.html", "w+")
htmlfile.write(htmlinput)
htmlfile.close()

# handling the anwesenheit.html
dataId = 1

htmlinput = '<!DOCTYPE html>\n'
htmlinput = htmlinput + '<html lang="de">\n'
htmlinput = htmlinput + '<link rel = "stylesheet" href = "stylesheet.css">\n'
htmlinput = htmlinput + '<title>Webinterface Touchpanel</title>\n'
htmlinput = htmlinput + '\n<body>\n'
htmlinput = htmlinput + '<div class = "parent">\n'
htmlinput = htmlinput + '<label for = "hy" >\n'
htmlinput = htmlinput + '<div class = "flex-container">\n'

x = 0
while x < len(link):
    htmlinput = htmlinput + '<div class="controlBar">\n<a class="link" href ="' + \
        link[x + 1] + '">' + link[x] + '</a>\n</div>\n'
    x += 2
htmlinput = htmlinput + '</div>\n'
x = 0
htmlinput = htmlinput + '</label>\n'


htmlinput = htmlinput + '<div class = "wrapper" >\n'
htmlinput = htmlinput + '<div class = "container" >\n'
htmlinput = htmlinput + '<div > Anwesend </div >\n'
htmlinput = htmlinput + '</div >\n'
htmlinput = htmlinput + '<div class = "container" >\n'
htmlinput = htmlinput + '<div > Dienstreise </div >\n'
htmlinput = htmlinput + '</div >\n'
htmlinput = htmlinput + '<div class = "container" >\n'
htmlinput = htmlinput + '<div > Krankenstand </div >\n'
htmlinput = htmlinput + '</div >\n'
htmlinput = htmlinput + '<div class = "container" >\n'
htmlinput = htmlinput + '<div > Urlaub </div >\n'
htmlinput = htmlinput + '</div >\n'
htmlinput = htmlinput + '</div >\n'

while x < len(menschen):
    htmlinput = htmlinput + '<div class = "wrapper" >\n'
    htmlinput = htmlinput + '<div id="' + str(dataId) + \
        '-defaults" class = "container" >\n'
    dataId += 1
    if int(menschen[x + 1]) == 1:
        htmlinput = htmlinput + '<div > ' + menschen[x] + ' </div >\n'
    htmlinput = htmlinput + '</div >\n'
    htmlinput = htmlinput + '<div id="' + str(dataId) + \
        '-defaults" class = "container" >\n'
    dataId += 1
    if int(menschen[x + 1]) == 2:
        htmlinput = htmlinput + '<div > ' + menschen[x] + ' </div >\n'
    htmlinput = htmlinput + '</div >\n'
    htmlinput = htmlinput + '<div id="' + str(dataId) + \
        '-defaults" class = "container" >\n'
    dataId += 1
    if int(menschen[x + 1]) == 3:
        htmlinput = htmlinput + '<div > ' + menschen[x] + ' </div >\n'
    htmlinput = htmlinput + '</div >\n'
    htmlinput = htmlinput + '<div id="' + str(dataId) + \
        '-defaults" class = "container" >\n'
    dataId += 1
    if int(menschen[x + 1]) == 4:
        htmlinput = htmlinput + '<div > ' + menschen[x] + ' </div >\n'
    htmlinput = htmlinput + '</div >\n'
    htmlinput = htmlinput + '</div >\n'
    x += 2


htmlinput = htmlinput + '</div>\n'
htmlinput = htmlinput + '\n<script defer src = "dist/dragula.js"></script>\n'
htmlinput = htmlinput + '\n<script defer src = "example.js"></script>\n'
htmlinput = htmlinput + '<script defer src = "jquery-3.1.1.min.js"></script>\n'
htmlinput = htmlinput + '\n</body>\n'
htmlinput = htmlinput + '</html>'


htmlfile = open("anwesenheit.html", "w+")
htmlfile.write(htmlinput)
htmlfile.close()
