<!DOCTYPE html>
<html>
<!-- <link rel="stylesheet" href="stylesheet.css">
<title>Webinterface Touchpanel</title> -->
<body>
    <div class="parent">
       <!--  <label for="hy">
            <div class="controlBar">
                <a class="link" href="index.html"><img src="design/logo.png" alt="Dormakaba Logo"></a>
                <a class="link" href="anwesenheit.php">Anwesenheiten</a>
                <a class="link" href="https://jira.dormakaba.net/secure/Dashboard.jspa">Jira</a>
                <div class="uhrzeit" id="time"></div>
            </div>
        </label>-->
        <div class="wrapper heading">
            <div class="HeaderContainer">
                <div> Anwesend </div>
            </div>
            <div class="HeaderContainer">
                <div> Dienstreise </div>
            </div>
            <div class="HeaderContainer">
                <div> Krankenstand </div>
            </div>
            <div class="HeaderContainer">
                <div> Urlaub </div>
            </div>
        </div>

<?php
$myfile = fopen("menschen.txt", "r") or die("Unable to open file!");
$countup=1;
$menschen = 26;
$fileread = fread($myfile,filesize("menschen.txt"));
$splitting = preg_split("/\\n/",$fileread);

for ($x=0; $x<=$menschen;$x=$x+2){
    $linereadnames=$splitting[$x];
    $linereadnumber = $splitting[$x+1];

    echo '<div class="wrapper"><div id="',$countup,'-defaults" class="container">';
    if ($linereadnumber == 1){
        echo '<div id="' , $linereadnames , '" class= "userblue"><p>' , $linereadnames , '</p><img class ="avatar" src="design/Avatar/',$linereadnames,'.jpg"></div>';
    }
    $countup = $countup +1;
    echo '</div><div id="',$countup,'-defaults" class="container">';
    if ($linereadnumber == 2){
        echo '<div id="' , $linereadnames , '" class= "userred">' , $linereadnames , '<img class ="avatar" src="design/Avatar/',$linereadnames,'.jpg"></div>';
    }
    $countup = $countup +1;
    echo '</div><div id="',$countup,'-defaults" class="container">';
    if ($linereadnumber == 3){
        echo '<div id="' , $linereadnames , '" class= "userred">' , $linereadnames , '<img class ="avatar" src="design/Avatar/',$linereadnames,'.jpg"></div>';
    }
    $countup = $countup +1;
    echo '</div><div id="',$countup,'-defaults" class="container">';
    if ($linereadnumber == 4){
        echo '<div id="' , $linereadnames , '" class= "userred">' , $linereadnames , '<img class ="avatar" src="design/Avatar/',$linereadnames,'.jpg"></div>';
    }
    $countup = $countup +1;
    echo '</div></div>';

}
?>
<div class="wrapper heading">
            <div class="HeaderContainer">
            </div>
            <div class="HeaderContainer">
            </div>
            <div class="HeaderContainer">
            </div>
            <div class="HeaderContainer">
            </div>
        </div>
</div>



    <!-- <script defer src="dist/dragula.js"></script>
    <script defer src="anwesenheit.js"></script>
    <script defer src="jquery-3.1.1.min.js"></script>
    <script defer src="time.js"></script> -->

</body>
</html>