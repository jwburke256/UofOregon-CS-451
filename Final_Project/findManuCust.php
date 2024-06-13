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

$manufact = mysqli_real_escape_string($conn, $manufact);
// this is a small attempt to avoid SQL injection
// better to use prepared statements

$query = "SELECT fname, lname, description FROM customer c ";
$query .= "JOIN orders o ON c.customer_num = o.customer_num ";
$query .= "JOIN items i ON o.order_num = i.order_num ";
$query .= "JOIN stock s ON i.stock_num = s.stock_num ";
$query .= "JOIN manufact m ON s.manu_code = m.manu_code ";
$query .= "WHERE m.manu_name = '".$manufact."';";

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
    print "$row[fname]  $row[lname] $row[description]";
  }
print "</pre>";

mysqli_free_result($result);

mysqli_close($conn);

?>

<p>
<hr>

<p>
<a href="findManuCust.txt" >Contents</a>
of the PHP program that created this page. 	 
 
</body>
</html>
	  
