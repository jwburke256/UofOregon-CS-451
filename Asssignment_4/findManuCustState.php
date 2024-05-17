<?php

include('connectionData.txt');

$conn = mysqli_connect($server, $user, $pass, $dbname, $port)
or die('Error connecting to MySQL server.');

?>

<html>
<head>
  <title>CS 451 Assignment 4</title>
  </head>
  
  <body bgcolor="white">
  
  
  <hr>
  
  
<?php
  
$manufact = $_POST['manufact'];

$state = mysqli_real_escape_string($conn, $state);
// this is a small attempt to avoid SQL injection
// better to use prepared statements

$query = "SELECT order_num, CONCAT(fname, " ", lname) AS fullname, description ";
$query = $query."FROM stores7.orders o JOIN stores7.customer c USING(customer_num) ";
$query = $query."JOIN stores7.items i USING(order_num) JOIN stores7.stock s ON ";
$query = $query."i.stock_num=s.stock_num AND i.manu_code=s.manu_code JOIN ";
$query = $query."stores7.manufact m ON s.manu_code=m.manu_code WHERE manu_name = ";
$query = $query."'".$manufact."' ORDER BY order_num;";

?>

<p>
The query:
<p>
<?php
print $query;
?>

<hr>
<p>
Result of query:
<p>

<?php
$result = mysqli_query($conn, $query)
or die(mysqli_error($conn));

print "<pre>";
while($row = mysqli_fetch_array($result, MYSQLI_BOTH))
  {
    print "\n";
    print "$row[order_num]  $row[fullname]  $row[description]";
  }
print "</pre>";

mysqli_free_result($result);

mysqli_close($conn);

?>

<p>
<hr>

<p>
<a href="findManuCustState.txt" >Contents</a>
of the PHP program that created this page. 	 
 
</body>
</html>
	  