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
$string = $_POST['keywords'];
$matches = 0;
$file = fopen("archive.txt", "r") or die("Cannot open file!\n"); 
while ($line = fgets($file, 1024)) { 
    if (preg_match("/$string/", $line)) { 
        echo $line;
        echo "\n"; 
        $matches = 1;
    } 
}

if ($matches == 0) {
	echo "sorry, I haven&#8217;t written a haiku about ".$string." yet.";
} 

fclose($file); 
?>
</pre>

</p>
</body>
</html>