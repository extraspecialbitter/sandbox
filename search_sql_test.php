<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>
<head>
<title>search haikupoet.com</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link href="images/styles.css" rel="stylesheet" type="text/css" />
</head>

<BODY BGCOLOR="#000000" TEXT="#888888" LINK="#888888" ALINK="#888888" VLINK="#888888"> 
 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title></title>
</head>

<body>

<p>&nbsp;</p>

<h1 align="center"><strong>search results</strong></h1> 
  
<p>&nbsp;</p>

<p>&nbsp;</p>

<p>

<pre>
<?php
error_reporting(-1);
$string = $_POST['keywords'];
// Connect to Database
mysql_connect("localhost", "root", "menagerie") or die(mysql_error()); 
 mysql_select_db("haiku_archive") or die(mysql_error()); 
 $query = mysql_query("SELECT * FROM archive_test WHERE haiku_text LIKE '%$string%'");
 if (!$query) {
    $message  = 'Invalid query: ' . mysql_error() . "\n";
    $message .= 'Whole query: ' . $query;
    die($message);
 }

 while($row=mysql_fetch_row($query))
 {
    echo $row[0];
    echo "     $row[1]";
    echo "\n";
    echo "\n";
 }

?>
</pre>

</p>
</body>
</html>
