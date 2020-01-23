<?php
//Config
ini_set('display_errors', 0);
ini_set('display_startup_errors', 0);
error_reporting(0);
//Some Jutsu :D
highlight_file(__FILE__);
include 'secret.php' ;
$_=['_'=>'SecurinetsBlaBla','__'=>'Grr'];
foreach($_ as $k=>$v){
	${'_'.$k}=$v ;
	}
$query=$_SERVER["QUERY_STRING"];
parse_str($query);
if ((substr_count($query,'_')>=4)||(substr_count($query,'.')>0)){
	die('You have used too much _');
}
if(@$__==='Madara'){
	if(unserialize(@$___)['o']['k']==='imBored'){
		echo $flag ;}
	else die("No No");
}
else die("it's too EZ go go");
?>
