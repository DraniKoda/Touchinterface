<!DOCTYPE html>
<html lang="de">
<link rel = "stylesheet" href = "stylesheet.css">
<title>Webinterface Touchpanel</title>

<body>
<div class = "controlBar" >
<a class = "link" href = "index.php"><img src="design/logo.png" alt="Dormakaba Logo"></a >
<a class = "link" href = "anwesenheit_main.php">Anwesenheit</a >
<a class = "link" href = "https://jira.dormakaba.net/secure/Dashboard.jspa" > Jira </a >
<div class="uhrzeit" id="time"></div></div >
<div class="flex-container">
<div class="sidebar1"></div>
<div class="main-content">
<div class="embedded" id="1"><?php include "anwesenheit.php";?></div>

</div>
<div class="sidebar2"></div>
</div>

<!-- <script defer src = "javascript.js"></script> -->
<script defer src = "dist/dragula.js"></script>
<script defer src = "anwesenheit.js"></script>
<!-- <script defer src = "jquery-3.1.1.min.js"></script> -->
<script defer src = "time.js"></script>
<script>
setTimeout(() => {
    window.location.href = "index.php"
}, 3000);
</script>

</body>
</html>