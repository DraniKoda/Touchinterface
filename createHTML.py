import os
import io
readdir = "./data"
savedir = ".."

OrdnerListe = os.listdir(readdir)
os.chdir(readdir)


dataId = 0
count = 0
htmldata = list()

while count < len(OrdnerListe):

    if OrdnerListe[count].endswith(".png") | OrdnerListe[count].endswith(".jpg"):
        dataId += 1
        htmldata.append('\n<img class="embedded" id="' + str(dataId) + '" src="data/' +
                        OrdnerListe[count] + '" alt="image">')
    count += 1

######################################################################################
# building up the html file here
os.chdir(savedir)

htmlinput = '<!DOCTYPE html>\n'
htmlinput = htmlinput + '<html lang="de">\n'
htmlinput = htmlinput + '<link rel = "stylesheet" href = "stylesheet.css">\n'
htmlinput = htmlinput + '<title>Webinterface Touchpanel</title>\n'
htmlinput = htmlinput + '\n<body>\n'
htmlinput = htmlinput + \
    '<button type = "button" id = "leftButton" onclick = "prevStep()"><img src="design/arrowleft.png" alt="links"></button>\n'
htmlinput = htmlinput + \
    '<button type = "button" id = "rightButton" onclick = "nextStep()"><img src="design/arrowright.png" alt="rechts"></button>\n'
htmlinput = htmlinput + \
    '<button type = "button" id = "stopButton" onclick = "stop()"><img src="design/stop.jpg" alt="stop"></button>\n'
htmlinput = htmlinput + \
    '<button type = "button" id = "resumeButton" onclick = "resume()"><img src="design/resume.png" alt="resume"></button>\n'


htmlinput = htmlinput + '<div class = "controlBar" >\n'
htmlinput = htmlinput + \
    '<a class = "link" href = "index.html"><img src="design/logo.png" alt="Dormakaba Logo"></a >\n'
htmlinput = htmlinput + \
    '<a class = "link" href = "anwesenheit.php">Anwesenheiten</a >\n'
htmlinput = htmlinput + \
    '<a class = "link" href = "https://jira.dormakaba.net/secure/Dashboard.jspa" > Jira < /a >\n'
htmlinput = htmlinput + '<div class="uhrzeit" id="time"></div>'

htmlinput = htmlinput + '</div >\n'


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
htmlinput = htmlinput + '<script defer src = "time.js"></script>\n'
htmlinput = htmlinput + '\n</body>\n'
htmlinput = htmlinput + '</html>'

# writing the html file

htmlfile = open("index.html", "w+")
htmlfile.write(htmlinput)
htmlfile.close()
