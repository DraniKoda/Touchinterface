<!DOCTYPE html>
<head>
<html lang="de">
<link rel = "stylesheet" type = "text/css" href = "stylesheet.css">
<link rel = "stylesheet" type = "text/css" href = "icofont.min.css">
<title>Webinterface Touchpanel</title>
</head>

<body>
<button type = "button" id = "leftButton" onclick = "prevStep()" > <div class = "icon-holder" > <div class = "icon" > <i class = "icofont-rounded-left" > </i > </div > </div > </button >
<button type = "button" id = "rightButton" onclick = "nextStep()" > <div class = "icon-holder" > <div class = "icon" > <i class = "icofont-rounded-right" > </i > </div > </div > </button >
<button type = "button" id = "stopButton" onclick = "stop()" > <div class = "icon-holder" > <div class = "icon" > <i class = "icofont-ui-pause" > </i > </div > </div > </button >
<button type = "button" id = "resumeButton" onclick = "resume()" > <div class = "icon-holder" > <div class = "icon" > <i class = "icofont-ui-play" > </i > </div > </div > </button >
<div class = "controlBar" >
<a class = "link" href = "index.php"><img src="design/logo.png" alt="Dormakaba Logo"></a >
<a class = "link" href = "anwesenheit_main.php"> Anwesenheit </a >
<a class = "link" href = "https://jira.dormakaba.net/secure/Dashboard.jspa" > Jira </a >
<div class="uhrzeit" id="time"></div></div >
<div class="flex-container">
<div class="sidebar1"></div>
<div class="main-content">
<div class="embedded" id="1"><?php include "anwesenheit.php";?></div>

<img class="embedded" id="2" src="data/1.png" alt="image">
<img class="embedded" id="3" src="data/2.png" alt="image"></div>

<div class="sidebar2"></div>
</div>

<script defer src = "javascript.js"></script>
<script defer src = "dist/dragula.js"></script>
<script defer src = "anwesenheit.js"></script>
<script defer src = "jquery-3.1.1.min.js"></script>
<script defer src = "time.js"></script>

</body>
</html>