#!/usr/bin/perl

# Initializations

$issue="1202m2052";
$volume=substr($issue, 0, 2);
$number=substr($issue, 2, 2);
$filedir="../haiku/$issue";
$filename="$filedir/haiku.txt";
$number_of_poems=`wc -l $filename | cut -d' ' -f1`;
$number_of_poems/=6;
$number_of_pages=$number_of_poems / 10;
if ($number_of_poems % 10 gt 0)
{
    $number_of_pages= int($number_of_pages) + 1;
}
$name_number=4;
$poem_offset=6;
$page_offset=60;

# Open the input file and copy each line into an array

open(INFILE,$filename);

while (<INFILE>) {
     $line = $_;
     last if $. == $line_count;
     push (@text, $line);
}

# Do this for each page

$page_count=1;
$poem_count=1;
$text_index=0;
while ($page_count <= $number_of_pages)
{
    $thispage=$page_count;
    $thispagename="h" . $thispage;

    $pagefile="$filedir/thn_issue.h" . $thispage . ".html";
    open(OUTFILE, "> $pagefile");

    $nextpage=$thispage + 1;
    $nextpagename="h" . $nextpage;
    if ($nextpage > $number_of_pages)
    {
        $nextpagename=e1;
    }
    $lastpage=$thispage - 1;
    $lastpagename="h" . $lastpage;
    if ($lastpage < 1)
    {
        $lastpagename=c1;
    }

# Populate output file with the page template

    print OUTFILE "<html>\n";
    print OUTFILE "<head>\n";
    print OUTFILE "<title>The Heron&#8217;s Nest - v";
    print OUTFILE $volume;
    print OUTFILE ".";
    print OUTFILE $number;
    print OUTFILE " H";
    print OUTFILE $thispage;
    print OUTFILE ": Haiku</title>\n";
    print OUTFILE "<meta name=\"description\" content=\"The Heron\'s Nest: a haikai journal\">\n";
    print OUTFILE "<meta name=\"keywords\" content=\"The Heron\'s Nest,haiku,tanka,renku,renga,poetry,haibun,rengay,Christopher Herold,Alex Benedict,Paul MacNeil,Ferris Gilli,Paul David Mena,Peggy Willis Lyles,Robert Gilliland,Alice Frampton,Robert Bauer\">\n";
    print OUTFILE "<link rel=\"icon\" href=\"http://www.theheronsnest.com/images/heron.ico\" type=\"image/x-icon\">\n";
    print OUTFILE "<link rel=\"shortcut icon\" href=\"http://www.theheronsnest.com/images/heron.ico\" type=\"image/x-icon\">\n";
    print OUTFILE "</head>\n";
    print OUTFILE "<body background=\"http://www.theheronsnest.com/images/bkgnd00.gif\">\n";
    print OUTFILE "<table border=\"0\" width=\"900\">\n";
    print OUTFILE "<tr>\n";
    print OUTFILE "<td rowspan=\"2\" valign=\"top\" width=\"120\">\n";
    print OUTFILE "&nbsp;\n";
    print OUTFILE "<br>\n";
    print OUTFILE "<a href=\"./thn_issue.";
    print OUTFILE $nextpagename;
    print OUTFILE ".html\">Next Page</a><br>\n";
    print OUTFILE "<a href=\"./thn_issue.";
    print OUTFILE $lastpagename;
    print OUTFILE ".html\">Previous Page</a><br>\n";
    print OUTFILE "<p>&nbsp;</p>\n";
    print OUTFILE "<p>\n";
    print OUTFILE "<hr size=\"2\">\n";
    print OUTFILE "<br>\n";
    print OUTFILE "<font size=\"4\" color=\"#FF0000\"><b>READERS&#8217; CHOICE AWARDS</b></font><br>\n";
    print OUTFILE "<p></p><p>\n";
    print OUTFILE "<a href=\"http://www.theheronsnest.com/haiku/1201J1201/readers_choice_2009.html\"><b>Favorites from 2009</b></a> <br><br>\n";
    print OUTFILE "<a href=\"http://www.theheronsnest.com/haiku/1104N1128/2009_illustration_contest.html\"><b>Illustration Contest Results</b></a>\n";
    print OUTFILE "</p>\n";
    print OUTFILE "<br>\n";
    print OUTFILE "<hr size=\"2\">\n";
    print OUTFILE "</td>\n";
    print OUTFILE "<td rowspan=\"2\" valign=\"center\" width=\"125\">\n";
    print OUTFILE "<img src=\"http://www.theheronsnest.com/images/heron1in.lr.no.gif\" align=\"TOP\" border=\"0\">\n";
    print OUTFILE "</td>\n";
    print OUTFILE "<td width=\"480\">\n";
    print OUTFILE "<p align=\"center\"><font size=6 face=\"Bookman Old Style, Arial, Helvetica\" color=\"#6666CC\"><strong>The Heron&#8217;s Nest</strong></font></p>\n";
    print OUTFILE "<p>&nbsp;</p>\n";
    print OUTFILE "<p align=\"center\">\n";
    print OUTFILE "<font size=\"4\"><a href=\"http://www.theheronsnest.com\">Home</a>&nbsp;&#149;&nbsp;<a href=\"http://www.theheronsnest.com/haiku/\">Volume Contents</a>&nbsp;&#149;&nbsp;<a href=\"http://www.theheronsnest.com/journal/\">About</a>&nbsp;&#149;&nbsp;<a href=\"http://www.theheronsnest.com/connections/\">Connections</a></font>\n";
    print OUTFILE "</p>\n";
    print OUTFILE "</td></tr>\n";
    print OUTFILE "<tr align=\"center\" valign=\"top\">\n";
    print OUTFILE "<td colspan=\"1\" align=\"center\">\n";
    print OUTFILE "<br><hr><br>\n";
    print OUTFILE "<font size=\"4\" color=\"#6666CC\">Volume XII, Number 2: June, 2010.</font><br>\n";
    print OUTFILE "<font size=\"2\" color=\"#6666CC\"><i>Copyright &copy; 2010. All rights reserved by the respective authors.</i></font>\n";
    print OUTFILE "<p>\n";
    print OUTFILE "<a href=\"./thn_issue.e1.html\">Editors&#8217; Choices</a>&nbsp;&#149;&nbsp;<a href=\"./thn_issue.c1.html\">Commentary</a>&nbsp;&#149;&nbsp;<a href=\"./thn_issue.i1.html\">Index of Poets</a>&nbsp;&#149;&nbsp;<br>\n";
    print OUTFILE "<font color=\"#666666\">Haiku Pages:</font>\n";
    print OUTFILE "<a href=\"./thn_issue.h1.html\">&nbsp;1,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h2.html\">&nbsp;2,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h3.html\">&nbsp;3,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h4.html\">&nbsp;4,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h5.html\">&nbsp;5,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h6.html\">&nbsp;6,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h7.html\">&nbsp;7,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h8.html\">&nbsp;8,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h9.html\">&nbsp;9,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h10.html\">&nbsp;10,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h11.html\">&nbsp;11,</a>\n";
    print OUTFILE "<a href=\"./thn_issue.h12.html\">&nbsp;12</a>\n<br>";

    print OUTFILE "</p>\n";
    print OUTFILE "<br><hr>\n";
    print OUTFILE "</td></tr></table>\n";
    print OUTFILE "<table border=\"0\" width=\"900\">\n";
    print OUTFILE "<tr>\n";
    print OUTFILE "<td align=\"left\" valign=\"top\" width=\"200\">\n";
    print OUTFILE "<p><a href=\"#POEM1\">" . @text[$text_index + 3] . "</a>\n";
    print OUTFILE "<p><a href=\"#POEM2\">" . @text[$text_index + 9] . "</a>\n";
    print OUTFILE "<p><a href=\"#POEM3\">" . @text[$text_index + 15] . "</a>\n";
    print OUTFILE "<p><a href=\"#POEM4\">" . @text[$text_index + 21] . "</a>\n";
    print OUTFILE "<p><a href=\"#POEM5\">" . @text[$text_index + 27] . "</a>\n";
    print OUTFILE "<p><a href=\"#POEM6\">" . @text[$text_index + 33] . "</a>\n";
    print OUTFILE "<p><a href=\"#POEM7\">" . @text[$text_index + 39] . "</a>\n";
    print OUTFILE "<p><a href=\"#POEM8\">" . @text[$text_index + 45] . "</a>\n";
    print OUTFILE "<p><a href=\"#POEM9\">" . @text[$text_index + 51] . "</a>\n";
    print OUTFILE "<p><a href=\"#POEM10\">" . @text[$text_index + 57] . "</a>\n";
    print OUTFILE "</TD>\n";
    print OUTFILE "<TD ALIGN=LEFT VALIGN=TOP WIDTH=350>\n";
    print OUTFILE "<TABLE>\n";
    print OUTFILE "<A NAME=POEM1></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>";
    print OUTFILE @text[$text_index] . "<br>\n";
    print OUTFILE @text[$text_index + 1] . "<br>\n";
    print OUTFILE @text[$text_index + 2] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 3] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "<A NAME=POEM3></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>";
    print OUTFILE @text[$text_index + 12] . "<br>\n";
    print OUTFILE @text[$text_index + 13] . "<br>\n";
    print OUTFILE @text[$text_index + 14] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 15] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "<A NAME=POEM5></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>";
    print OUTFILE @text[$text_index + 24] . "<br>\n";
    print OUTFILE @text[$text_index + 25] . "<br>\n";
    print OUTFILE @text[$text_index + 26] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 27] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "<A NAME=POEM7></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>";
    print OUTFILE @text[$text_index + 36] . "<br>\n";
    print OUTFILE @text[$text_index + 37] . "<br>\n";
    print OUTFILE @text[$text_index + 38] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 39] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "<A NAME=POEM9></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>";
    print OUTFILE @text[$text_index + 48] . "<br>\n";
    print OUTFILE @text[$text_index + 49] . "<br>\n";
    print OUTFILE @text[$text_index + 50] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 51] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "</TABLE></TD>\n";
    print OUTFILE "<TD ALIGN=LEFT VALIGN=TOP WIDTH=350>\n";
    print OUTFILE "<TABLE><TR ALIGN=LEFT VALIGN=TOP>\n";
    print OUTFILE "<TD><FONT SIZE=-2>&nbsp;</FONT></TD></TR>\n";
    print OUTFILE "<TR ALIGN=RIGHT VALIGN=TOP><TD>&nbsp;</TD></TR>\n";
    print OUTFILE "<A NAME=POEM2></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>\n";
    print OUTFILE @text[$text_index + 6] . "<br>\n";
    print OUTFILE @text[$text_index + 7] . "<br>\n";
    print OUTFILE @text[$text_index + 8] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 9] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "<A NAME=POEM4></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>\n";
    print OUTFILE @text[$text_index + 18] . "<br>\n";
    print OUTFILE @text[$text_index + 19] . "<br>\n";
    print OUTFILE @text[$text_index + 20] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 21] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "<A NAME=POEM6></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>\n";
    print OUTFILE @text[$text_index + 30] . "<br>\n";
    print OUTFILE @text[$text_index + 31] . "<br>\n";
    print OUTFILE @text[$text_index + 32] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 33] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "<A NAME=POEM8></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>\n";
    print OUTFILE @text[$text_index + 42] . "<br>\n";
    print OUTFILE @text[$text_index + 43] . "<br>\n";
    print OUTFILE @text[$text_index + 44] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 45] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "<A NAME=POEM10></A>\n";
    print OUTFILE "<TR ALIGN=LEFT VALIGN=TOP><TD><P><FONT SIZE=+1>\n";
    print OUTFILE @text[$text_index + 54] . "<br>\n";
    print OUTFILE @text[$text_index + 55] . "<br>\n";
    print OUTFILE @text[$text_index + 56] . "</FONT></TD></TR> <TR ALIGN=RIGHT VALIGN=TOP><TD>\n";
    print OUTFILE @text[$text_index + 57] . "<P>&nbsp;</TD></TR>\n";
    print OUTFILE "</table></TD></TR>\n";
    print OUTFILE "<TR><TD WIDTH=\"200\">&nbsp;</TD>\n";
    print OUTFILE "<TD ALIGN=CENTER COLSPAN=\"2\" WIDTH=\"550\">\n";
    print OUTFILE "<BR>&nbsp\n";
    print OUTFILE "<p><a href=\"thn_issue." . $lastpagename . ".html\">Previous Page</a>&nbsp;&#149;&nbsp;";
    print OUTFILE "<a href=\"thn_issue." . $thispagename . ".html#TOP\">Top</a>&nbsp;&#149;&nbsp;";
    print OUTFILE "<a href=\"thn_issue." . $nextpagename . ".html\">Next Page</a></td></p>\n";
    print OUTFILE "</TR></TABLE></BODY></HTML>\n";

    close(OUTFILE);

    $page_count+=1;
    $text_index+=$page_offset;

}
