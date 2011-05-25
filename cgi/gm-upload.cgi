#!/usr/bin/perl

# =============================
# GREYMATTER - Uploading Module
# Weblog/Journal Software
# version one point two
# Copyright (c)2000 Noah Grey
# http://noahgrey.com/greysoft/
# =============================

# ***  Your possession of this software indicates that you agree to the terms   ***
# *** specified under the "Copyright & Usage" heading in the "manual.txt" file. ***

eval {
	($0 =~ m,(.*)/[^/]+,) && unshift (@INC, "$1");
	($0 =~ m,(.*)\\[^\\]+,) && unshift (@INC, "$1");
};

use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);

require "gm-library.cgi";

print "Content-type: text/html\n\n";

$authorIP = $ENV{'REMOTE_ADDR'};

$| = 1;
use CGI qw(:standard);
$cgiquery = new CGI;

$otherkeys = "";

foreach $key (sort {$a <=> $b} $cgiquery->param()) {
	$otherparams = param($key);
	$otherkeys .= "$otherparams|";
}

chop ($otherkeys);
@otherkeyvalues = split (/\|/, $otherkeys);
$IN{'authorname'} = $otherkeyvalues[0];
$IN{'authorpassword'} = $otherkeyvalues[1];

if (($IN{'authorname'} eq "") || ($IN{'authorpassword'} eq "")) {
	&gm_dangermouse("The author name or password is blank.  This file is only to be used by logging into Greymatter.");
}

&gm_validate;

if ($gmuploadaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to upload a file without authorization");
	&gm_dangermouse("You don't have access to upload files.");
}

foreach $key (sort {$a <=> $b} $cgiquery->param()) {

	next if ($key =~ /^\s*$/);
	next if ($cgiquery->param($key) =~ /^\s*$/);
	next if ($key !~ /^uploadfile-(\d+)$/);

	if ($cgiquery->param($key) =~ /([^\/\\]+)$/) {
		$uploadfilename = $1;
		$uploadfilename =~ s/^\.+//;
		$uploadfilenamehandle = $cgiquery->param($key);
		if ($uploadfilename =~ m/\ /) { &gm_dangermouse("Your filename cannot contain spaces.  Please rename your file, go back, and try again."); }
	} else {
		&gm_dangermouse("Your filename cannot contain backslashes, or have a period at the beginning of its name.  Please rename your file, go back, and try again.");
	}

	if ($uploadfilename =~ /'/) { &gm_dangermouse("Your filename cannot contain apostrophes.  Please rename your file, go back, and try again."); }

	if ($uploadfilesallowed ne "") {
		$thisfileisokay = "no";
		@uploadfiletypecheck = split (/;/, $uploadfilesallowed);
		foreach $checkagainstthis (@uploadfiletypecheck) {
			if ($uploadfilename =~ /\.$checkagainstthis$/i) { $thisfileisokay = "yes"; }
		}
		if ($thisfileisokay eq "no") {
			&gm_dangermouse("Uploading files of that type is currently not permitted.  Please go back and try a different file.");
		}
	}

	if (-e "$EntriesPath/$uploadfilename") { &gm_dangermouse("A file with that name already exists in your entries/archives directory.  Please go back and try a file with a different name."); }

	undef $bytesread;
	undef $buffer;

	open(OUTFILE, ">$EntriesPath/$uploadfilename") || &gm_dangermouse("Can't write to $EntriesPath/$uploadfilename.  Make sure that $EntriesPath is your correct entries/archives directory, and that this directory is CHMODed to 777.");
	while ($bytes = read($uploadfilenamehandle, $buffer, 2096)) {
		$bytesread += $bytes;
		binmode OUTFILE;
		print OUTFILE $buffer;
	}

	push (@fileswritten, "$EntriesPath\/$uploadfilename");
	$totalbytes += $bytesread;
	$uploadconfirm{$uploadfilenamehandle} = $bytesread;
	close($uploadfilenamehandle);
	close(OUTFILE);

}

$filesuploaded = scalar(keys(%uploadconfirm));

if (($totalbytes eq $null) || ($totalbytes == 0)) { &gm_dangermouse("You didn't enter a filename, or you attempted to upload an empty file.  Please go back and try again."); }

$totalkbytes = $totalbytes / 1024;
$totalkbytes = sprintf("%.0f", $totalkbytes);

if (($uploadfilesizelimit ne "0") && ($totalkbytes > $uploadfilesizelimit)) {
	foreach $filetemp (@fileswritten) { unlink $filetemp; }
	$overthelimitby = $totalkbytes - $uploadfilesizelimit;
	&gm_dangermouse("The file you attempted to upload was too large ($overthelimitby\k over the $uploadfilesizelimit\k filesize limit).  Please go back and try a smaller file.");
}

&gm_writetocplog("$IN{'authorname'} uploaded a file ($uploadfilename, $totalkbytes\k)");

if (($uploadfilename =~ /\.jpg$/i) || ($uploadfilename =~ /\.gif$/i) || ($uploadfilename =~ /\.png$/i)) {

$usethisauthorname = $IN{'authorname'};
$usethisauthorpassword = $IN{'authorpassword'};
$filenameprefix = $uploadfilename;
$filenameprefix =~ s/\.(...)$//;

print<<UPLOADEDIMAGE;

<HTML>
<HEAD>
<TITLE>Measuring Image...</TITLE>

<SCRIPT TYPE="text/javascript" LANGUAGE="Javascript1.2">
<!--//
function writesize() {
	thisheight = document.thisimage.height;
	thiswidth = document.thisimage.width;
	document.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><HTML><HEAD><TITLE>Greymatter</TITLE><META NAME="Generator" CONTENT="Greymatter 1.2"></HEAD><BODY BGCOLOR="#8080B0" TEXT="#000000" LINK="#000000" VLINK="#000000" ALINK="#000000" MARGIN=10 TOPMARGIN=10 LEFTMARGIN=10 RIGHTMARGIN=10 BOTTOMMARGIN=10 MARGINHEIGHT=10 MARGINWIDTH=10 STYLE="scrollbar-face-color: #A0C0E0; scrollbar-shadow-color: #000000; scrollbar-highlight-color: #000000; scrollbar-3dlight-color: #000000; scrollbar-darkshadow-color: #000000; scrollbar-track-color: #000000; scrollbar-arrow-color: #000000"><BASE TARGET="_top"><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=100% HEIGHT=100%><TR><TD VALIGN=MIDDLE ALIGN=CENTER><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0><TR><TD><P ALIGN=LEFT><FONT FACE="VERDANA, ARIAL, HELVETICA" SIZE=2><FONT COLOR="#C0C0E0" SIZE=4><B>Greymatter</B></FONT></FONT></P><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=10 CELLSPACING=0 BGCOLOR="#FFFFFF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER><FONT FACE="VERDANA, ARIAL, HELVETICA" SIZE=2><B><FONT COLOR="#0000FF">Upload Complete</FONT></B><P>Your image (' + thiswidth + 'x' + thisheight + ', $totalkbytes\k) was successfully uploaded.<P><IMG BORDER=0 SRC="$EntriesWebPath/$uploadfilename" ALT="$filenameprefix ($totalkbytes\k image)" HEIGHT=' + thisheight + ' WIDTH=' + thiswidth + '><P><FONT SIZE=1>&lt;IMG BORDER=0 SRC="$EntriesWebPath/$uploadfilename" ALT="$filenameprefix ($totalkbytes\k image)" HEIGHT=' + thisheight + ' WIDTH=' + thiswidth + '&gt;<BR>{{popup $uploadfilename $filenameprefix ' + thiswidth + 'x' + thisheight + '}}$filenameprefix&lt;/A&gt;</FONT><P><FORM ACTION="gm.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$usethisauthorname"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$usethisauthorpassword"><INPUT TYPE=HIDDEN NAME="newentrymaintext" VALUE="&lt;IMG BORDER=0 SRC=&quot;$EntriesWebPath/$uploadfilename&quot; ALT=&quot;$filenameprefix ($totalkbytes\k image)&quot; HEIGHT=' + thisheight + ' WIDTH=' + thiswidth + '&gt;"><INPUT TYPE=HIDDEN NAME="newentrypopuptext" VALUE="{{popup $uploadfilename $filenameprefix ' + thiswidth + 'x' + thisheight + '}}$filenameprefix&lt;/A&gt;"><P><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Include This Image In A New Entry" STYLE="background: #D0FFD0; font-family: verdana, arial, helvetica; font-size: 13px; border-color: #000000; width: 300; height: 26"><P><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Include In Entry As A Popup Window" STYLE="background: #D0FFD0; font-family: verdana, arial, helvetica; font-size: 13px; border-color: #000000; width: 300; height: 26"><P><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF; font-family: verdana, arial, helvetica; font-size: 13px; border-color: #000000; width: 240; height: 26"></FORM><P><FONT SIZE=1>"If God created us in his own image, we have more than reciprocated."&#151;Voltaire</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P ALIGN=RIGHT><FONT FACE="VERDANA, ARIAL, HELVETICA" SIZE=1><A HREF="http://noahgrey.com/greysoft/" STYLE="text-decoration: none" TARGET="NEW">v$gmversion &#183; &copy;2000-2001 Noah Grey</A></FONT></P></TD></TR></TABLE></TD></TR></TABLE></TD></TR></TABLE></BODY></HTML>');
}
//-->
</SCRIPT>

</HEAD>

<BODY onLoad="writesize();">

<IMG NAME="thisimage" SRC="$EntriesWebPath/$uploadfilename">

</BODY>
</HTML>

UPLOADEDIMAGE

exit;

}

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#0000FF">Upload Complete</FONT></B><P>); }

$uploadfilenamelink = qq(&lt;A HREF=&quot;$EntriesWebPath/$uploadfilename&quot;&gt;$uploadfilename ($totalkbytes\k file)&lt;/A&gt;);

print<<UPLOADCOMPLETE;

$gmheadtag

$gmframetop
$statusnote
Your file ($totalkbytes\k) was successfully uploaded.
<P>
<FONT SIZE=1>$uploadfilenamelink</FONT>
<P>
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="newentrymaintext" VALUE="$uploadfilenamelink">
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Include This Link In A New Entry" STYLE="background: #D0FFD0">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"We can never tell what is in store for us."&#151;Harry S. Truman</FONT>
$gmframebottom

</BODY>
</HTML>

UPLOADCOMPLETE

exit;
