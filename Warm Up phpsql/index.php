<?php
// Configuration
ini_set('display_errors', 0);
ini_set('display_startup_errors', 0);
error_reporting(0);

highlight_file(__FILE__);
include "secret.php" ;
// Database Connection
try {
    $charset='utf8';
    $bdd=new PDO ("mysql:host=$host;dbname=$dbname;charset=$charset",$user,$pass) ;
    }
catch (Exception $e)
    {
    die("Connection Error :".$e->getMessage()) ;
    }
// Some Jutsu :p
    if(strtolower($_GET['_'])==='admin'){
        die("No No Try Again Script kiddie");
    }
    else{
        $req=$bdd->prepare("SELECT * FROM users WHERE username=?");
        $req->execute(array($_GET['_']));
        if($response=$req->fetch()){
            echo $flag ;
        }
        else{
            echo "Try harder it's easy";
        }
    }

?>