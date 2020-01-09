<?php

// echo phpinfo();


$q = $_REQUEST["q"];
// $q = "4-defaults-Markus Kornhofer";
// echo $q;
$splitting = preg_split("/\-/",$q);
$Nummer = $splitting[0];
$Names = $splitting[2];
// echo $Nummer, $Names;

$menschen = 26;



$myfile = fopen("menschen.txt", "r") or die("Unable to open file!");
$fileread = fread($myfile,filesize("menschen.txt"));
$splitting = preg_split("/\r\\n/",$fileread);
// var_dump($Names);
// var_dump($splitting[0]);
// if ($Names == $splitting[0]){
//     echo "yolo";
// }

fclose($myfile);
// echo count($splitting);

$myfile = fopen("menschen.txt", "w") or die("Unable to open file!");
fclose($myfile);
$myfile = fopen("menschen.txt", "w") or die("Unable to open file!");
for ($x = 0; $x <= $menschen; $x=$x+2) {

    // echo $x."swag\n";

    fwrite($myfile, $splitting[$x]."\r\n");
    
    // echo $splitting[$x];

    if ($Names == $splitting[$x]){
        // echo "servus";        
        if ($Nummer == 1){
            fwrite($myfile,$Nummer."\r\n");
            // echo $Nummer;
        }elseif ($Nummer == 2){
            fwrite($myfile,$Nummer."\r\n");
            // echo $Nummer;
        }elseif ($Nummer == 3){
            fwrite($myfile,$Nummer."\r\n");
            // echo $Nummer;
        }elseif ($Nummer == 4){
            fwrite($myfile,$Nummer."\r\n");
            // echo $Nummer;
        }
    }
    if($Names != $splitting[$x]) {
        if($x >= $menschen-1){
            fwrite($myfile, $splitting[$x+1]);
            // echo "yolo";

        }else{
            fwrite($myfile, $splitting[$x+1]."\r\n");
            // echo "swag";

        }
        // echo $splitting[$x+1];
    }
    if($Nummer <= 0){
        $Nummer = 0;
    }else{
        $Nummer = $Nummer - 4;
    }

}

fclose($myfile);




?>