<!DOCTYPE html>
<html>
<link rel="stylesheet" href="stylesheet.css">
<title>Webinterface Touchpanel</title>
<body>
    <div class="parent">
        <label for="hy">
            <div class="flex-container">
                <div class="flex-container">
                    <div class="controlBar">
                        <a class="link" href="index.html"><img src="logo.png" alt="Dormakaba Logo"></a>
                        <a class="link" href="anwesenheit.php">Anwesenheiten</a>
                    </div>
                </div>
            </div>
        </label>
        <div class="wrapper">
            <div class="container">
                <div> Anwesend </div>
            </div>
            <div class="container">
                <div> Dienstreise </div>
            </div>
            <div class="container">
                <div> Krankenstand </div>
            </div>
            <div class="container">
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
        echo '<div id="' , $linereadnames , '">' , $linereadnames , '</div>';
    }
    $countup = $countup +1;
    echo '</div><div id="',$countup,'-defaults" class="container">';
    if ($linereadnumber == 2){
        echo '<div id="' , $linereadnames , '">' , $linereadnames , '</div>';
    }
    $countup = $countup +1;
    echo '</div><div id="',$countup,'-defaults" class="container">';
    if ($linereadnumber == 3){
        echo '<div id="' , $linereadnames , '">' , $linereadnames , '</div>';
    }
    $countup = $countup +1;
    echo '</div><div id="',$countup,'-defaults" class="container">';
    if ($linereadnumber == 4){
        echo '<div id="' , $linereadnames , '">' , $linereadnames , '</div>';
    }
    $countup = $countup +1;
    echo '</div></div>';

}
?>

</div>



    <script defer src="dist/dragula.js"></script>
    <script defer src="anwesenheit.js"></script>
    <script defer src="jquery-3.1.1.min.js"></script>

</body>
</html>