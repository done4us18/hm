<?php
echo "+===========================+\n";
echo "{@} Author : done4us\n";
echo "{@} Facebook : done4us18\n";
echo "{@} YouTube : done4us\n";
echo "+===========================+\n";
echo "{1} Welcome\n";
echo "{2} Subscribe\n";
echo "{3} Like\n";
echo "{0} Exit\n";
echo "+============================+\n";
echo "{+} Choose : ";
$choose = trim(fgets(STDIN));
/* welcome */
if($choose = 01 or $choose = 1){
  system("figlet Welcome");
}
/*subcribe*/
elseif($choose = 02 or $choose = 2){
  system("figlet Subscribe");
 }
/*like*/
elseif($choose = 03 or $choose = 3){
  system("figlet Like");
 }
/*exit*/
elseif($choose = 00 or $choose = 0){
  system("exit");
 }
?>
