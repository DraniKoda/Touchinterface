import subprocess
import os
import io
from PyPDF2 import PdfFileReader
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


os.chdir(readdir)

# scanning the directory of all the data and creating the html code per data and page

for pdf_file in os.listdir(readdir):
    if pdf_file.endswith(".pdf"):
        subprocess.Popen('"%s" -jpeg %s %s' %
                         (pdftoppm_path, pdf_file, count))
        count += 1


while i < len(OrdnerListe):

    if OrdnerListe[i].endswith(".png") | OrdnerListe[i].endswith(".jpg"):
        dataId += 1
        htmldata.append('\n<img class="embedded" id="' + str(dataId) + '" src="data/' +
                        OrdnerListe[i] + '" alt="image">')
    i += 1

# file = open('/Users/raphi/git/Webinterface_Touchpanel/link.txt', 'r+')
# link = file.readlines()
# file.close

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
    '<button type = "button" class = "leftButton" onclick = "prevStep()"><img src="arrowleft.png" alt="links"></button>\n'
htmlinput = htmlinput + \
    '<button type = "button" class = "rightButton" onclick = "nextStep()"><img src="arrowright.png" alt="rechts"></button>\n'
htmlinput = htmlinput + \
    '<button type = "button" class = "stopButton" onclick = "stop()"><img src="stop.jpg" alt="stop"></button>\n'


htmlinput = htmlinput + '<div class = "flex-container" >\n'
htmlinput = htmlinput + '<div class = "controlBar" >\n'
htmlinput = htmlinput + \
    '<a class = "link" href = "index.html"><img src="logo.png" alt="Dormakaba Logo"></a >\n'
htmlinput = htmlinput + \
    '<a class = "link" href = "anwesenheit.php">Anwesenheiten</a >\n </div >\n'
htmlinput = htmlinput + '</div>\n'


htmlinput = htmlinput + '<div class="flex-container">\n'
htmlinput = htmlinput + '<div class="sidebar1"></div>\n'
htmlinput = htmlinput + '<div class="main-content">\n'

x = 0
while x < len(htmldata):
    htmlinput = htmlinput + htmldata[x]
    x += 1


htmlinput = htmlinput + '</div>\n'
htmlinput = htmlinput + '<div class="sidebar2"></div>\n'
htmlinput = htmlinput + '</div>\n'
htmlinput = htmlinput + '\n<script defer src = "javascript.js"></script>\n'
htmlinput = htmlinput + '<script defer src = "jquery-3.1.1.min.js"></script>\n'
htmlinput = htmlinput + '\n</body>\n'
htmlinput = htmlinput + '</html>'


# writing the html file

htmlfile = open("index.html", "w+")
htmlfile.write(htmlinput)
htmlfile.close()
