## Greymatter common subroutine library

# ===============================
# GREYMATTER - Subroutine Library
# Weblog/Journal Software
# version one point two
# Copyright (c)2000 Noah Grey
# http://noahgrey.com/greysoft/
# ===============================

# ***  Your possession of this software indicates that you agree to the terms   ***
# *** specified under the "Copyright & Usage" heading in the "manual.txt" file. ***

# -----------------
# program variables
# -----------------

$gmversion = "1.21b";

$gmfonttag = qq(<FONT FACE="VERDANA, ARIAL, HELVETICA" SIZE=2>);

$gmheadtag = qq#<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<TITLE>Greymatter</TITLE>
<META NAME="Generator" CONTENT="Greymatter $gmversion">

<STYLE TYPE="text/css">
<!--
.copynotice { text-decoration: none }
.copynotice:hover { color: \#FFFFFF }
.button { font-family: verdana, arial, helvetica; font-size: 13px; background: \#FFFFD0; border-color: \#000000 }
.textinput { font-family: verdana, arial, helvetica; font-size: 13px; background-color: \#EEEEFF; border-color: \#000000 }
.selectlist { font-family: verdana, arial, helvetica; font-size: 13px; background-color: \#EEEEFF; border-color: \#000000 }
BODY { scrollbar-face-color: \#A0C0E0; scrollbar-shadow-color: \#000000; scrollbar-highlight-color: \#000000; scrollbar-3dlight-color: \#000000; scrollbar-darkshadow-color: \#000000; scrollbar-track-color: \#000000; scrollbar-arrow-color: \#000000 }
input { font-family: verdana, arial, helvetica; font-size: 13px }
textarea { font-size: 13px; font-family: verdana, arial, helvetica; background-color: \#EEEEFF; border-color: \#000000 }
-->
</STYLE>

<STYLE TYPE="text/css" MEDIA="all">
<!--
.button { width: 240; height: 26 }
-->
</STYLE>

<SCRIPT TYPE="text/javascript" LANGUAGE="JavaScript">
<!--//

// Copyright (c) 1996-1997 Athenia Associates.
// http://www.webreference.com/js/
// License is granted if and only if this entire
// copyright notice is included. By Tomer Shiran.

function setCookie(name, value, expires, path, domain, secure) {
var curCookie = name + "=" + escape(value) + ((expires) ? "; expires=" + expires.toGMTString() : "") + ((path) ? "; path=" + path : "") + ((domain) ? "; domain=" + domain : "") + ((secure) ? "; secure" : "");
document.cookie = curCookie;
}

function getCookie(name) {
var prefix = name + "=";
var nullstring = "";
var cookieStartIndex = document.cookie.indexOf(prefix);
if (cookieStartIndex == -1)
return nullstring;
var cookieEndIndex = document.cookie.indexOf(";", cookieStartIndex + prefix.length);
if (cookieEndIndex == -1)
cookieEndIndex = document.cookie.length;
return unescape(document.cookie.substring(cookieStartIndex + prefix.length, cookieEndIndex));
}

function deleteCookie(name, path, domain) {
if (getCookie(name)) {
document.cookie = name + "=" + ((path) ? "; path=" + path : "") + ((domain) ? "; domain=" + domain : "") + "; expires=Thu, 01-Jan-70 00:00:01 GMT"
};
}

function fixDate(date) {
var base = new Date(0);
var skew = base.getTime();
if (skew > 0)
date.setTime(date.getTime() - skew);
}
#;

$gmheadtagtwo = $gmheadtag;

$gmheadtag .= qq#
//-->
</SCRIPT>

</HEAD>

<BODY BGCOLOR="\#8080B0" TEXT="\#000000" LINK="\#000000" VLINK="\#000000" ALINK="\#000000" MARGIN=10 TOPMARGIN=10 LEFTMARGIN=10 RIGHTMARGIN=10 BOTTOMMARGIN=10 MARGINHEIGHT=10 MARGINWIDTH=10>
<BASE TARGET="_top">#;

$gmheadtagtwo .= qq#
function gmshortcutkeys() {
	if ((parseInt(navigator.appVersion) >= 4) && (navigator.appName == "Microsoft Internet Explorer")) {
		if (event.ctrlKey != true) return;
		gmselection = document.selection.createRange().text;
		if (window.event.keyCode == 1) {
			gminsertlink = prompt("What do you want to link to?", "http://")
			if (gminsertlink == null) return;
			document.selection.createRange().text = '<A HREF="' + gminsertlink + '">' + gmselection + '</A>';
			return;
		}
		if (window.event.keyCode == 2) {
			document.selection.createRange().text = '<B>' + gmselection + '</B>';
			return;
		}
		if (window.event.keyCode == 9) {
			document.selection.createRange().text = '<I>' + gmselection + '</I>';
			return;
		}
		if (window.event.keyCode == 21) {
			document.selection.createRange().text = '<U>' + gmselection + '</U>';
			return;
		}
	}
}

//-->
</SCRIPT>

</HEAD>

<BODY BGCOLOR="\#8080B0" TEXT="\#000000" LINK="\#000000" VLINK="\#000000" ALINK="\#000000" MARGIN=10 TOPMARGIN=10 LEFTMARGIN=10 RIGHTMARGIN=10 BOTTOMMARGIN=10 MARGINHEIGHT=10 MARGINWIDTH=10 onKeyPress="gmshortcutkeys();">
<BASE TARGET="_top">#;

$gmframetop = qq(<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=100% HEIGHT=100%><TR><TD VALIGN=MIDDLE ALIGN=CENTER><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0><TR><TD><P ALIGN=LEFT>$gmfonttag<FONT COLOR="#C0C0E0" SIZE=4><B>Greymatter</B></FONT></FONT></P><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=10 CELLSPACING=0 BGCOLOR="#FFFFFF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag);
$gmframetoptwo = qq(<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=100% HEIGHT=100%><TR><TD VALIGN=MIDDLE ALIGN=CENTER><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0><TR><TD><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=10 CELLSPACING=0 BGCOLOR="#FFFFFF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag);
$gmframebottom = qq(</FONT></TD></TR></TABLE></TD></TR></TABLE><P ALIGN=RIGHT><FONT FACE="VERDANA, ARIAL, HELVETICA" SIZE=1><A HREF="http://noahgrey.com/greysoft/" CLASS="copynotice" TARGET="NEW">v$gmversion &#183; &copy;2000-2001 Noah Grey</A></FONT></P></TD></TR></TABLE></TD></TR></TABLE></TD></TR></TABLE>);
$gmframebottomtwo = qq(</FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR></TABLE></TD></TR></TABLE></TD></TR></TABLE>);
$statusnote = "";

# ---------------
# date subroutine
# ---------------

sub date {

$adjustTime = time() + ($serveroffset * 3600);

($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime($adjustTime);

$mon++;

@months = ("null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
@weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");

$fullmonth = $months[$mon];
$fullweekday = $weekdays[$wday];

$JSYear = $year + 1900;
$shortyear = substr($JSYear, -2, 2);

$mintwo = sprintf ("%2d", $min);
$mintwo =~ tr/ /0/;
$sectwo = sprintf ("%2d", $sec);
$sectwo =~ tr/ /0/;

$militaryhour = $hour;

if ($hour < 12) {
	$AMPM = "AM";
	$AMPMDOT = "A.M.";
}

if ($hour > 12) {
	$hour = $hour - 12;
	$AMPM = "PM";
	$AMPMDOT = "P.M.";
	$militaryhour = $militaryhour + 12;
}  	

if ($hour == 12) {
	$AMPM = "PM";
	$AMPMDOT = "P.M.";
}  	
	
if ($hour == 0) {
	$hour = "12";
}

$hourtwo = sprintf ("%2d", $hour);
$hourtwo =~ tr/ /0/;
$mintwo = sprintf ("%2d", $min);
$mintwo =~ tr/ /0/;
$montwo = sprintf ("%2d", $mon);
$montwo =~ tr/ /0/;
$mdaytwo = sprintf ("%2d", $mday);
$mdaytwo =~ tr/ /0/;

if (($hour eq "12") && ($AMPM eq "AM")) { $militaryhour = "0"; }

$militaryhourtwo = sprintf ("%2d", $hour);
$militaryhourtwo =~ tr/ /0/;


$basedate = "$montwo\/$mdaytwo\/$shortyear $hourtwo\:$mintwo $AMPM";

}

# -------------------------
# delouse for textarea edit
# -------------------------

sub delouse {
$_ = shift;
$_ =~ s/\|\*\|/\n/g;
$_ =~ s/&([A-Za-z0-9\#]+);/\|AMP\|$1;/g;
$_ =~ s/</\&lt;/g;
$_ =~ s/>/\&gt;/g;
$_ =~ s/"/\&quot;/g;
return($_);
}

# ---------------------------
# relouse after textarea edit
# ---------------------------

sub relouse {
$_ = shift;
$_ =~ s/\n/\|\*\|/g;
$_ =~ s/\r//g;
$_ =~ s/\&lt;/</g;
$_ =~ s/\&gt;/>/g;
$_ =~ s/\&quot;/"/g;
$_ =~ s/\|AMP\|([A-Za-z0-9\#]+);/&$1;/g;
return($_);
}

# ---------------------
# configuration delouse
# ---------------------

sub configdelouse {
$_ = shift;
$_ =~ s/\|//g;
$_ =~ s/\n//g;
$_ =~ s/\r//g;
$_ =~ s/^\s+//;
$_ =~ s/\s+$//;
return($_);
}

# ----------------
# read the counter
# ----------------

sub gm_readcounter {

open (FUNNYFEETKRACK, "gm-counter.cgi") || &gm_dangermouse("Can't read the counter file.  Please make sure that gm-counter.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@entrycounters = <FUNNYFEETKRACK>;
close (FUNNYFEETKRACK);

$newentrynumber = $entrycounters[0];
$newarchivenumber = $entrycounters[1];
$newstayattopnumber = $entrycounters[2];
$newalltimepktotalnumber = $entrycounters[3];
$newalltimenktotalnumber = $entrycounters[4];
$newalltimecommentstotalnumber = $entrycounters[5];
$newalltimeopenentriesnumber = $entrycounters[6];
$newalltimeclosedentriesnumber = $entrycounters[7];

chomp ($newentrynumber);
chomp ($newarchivenumber);
chomp ($newstayattopnumber);
chomp ($newalltimepktotalnumber);
chomp ($newalltimenktotalnumber);
chomp ($newalltimecommentstotalnumber);
chomp ($newalltimeopenentriesnumber);
chomp ($newalltimeclosedentriesnumber);

if ($newentrynumber eq "") { $newentrynumber = 0; }
if ($newarchivenumber eq "") { $newarchivenumber = 0; }
if ($newstayattopnumber eq "") { $newstayattopnumber = 0; }
if ($newalltimepktotalnumber eq "") { $newalltimepktotalnumber = 0; }
if ($newalltimenktotalnumber eq "") { $newalltimenktotalnumber = 0; }
if ($newalltimeopenentriesnumber eq "") { $newalltimeopenentriesnumber = 0; }
if ($newalltimeclosedentriesnumber eq "") { $newalltimeclosedentriesnumber = 0; }

}

# -----------------
# write the counter
# -----------------

sub gm_writecounter {

if ($newentrynumber eq "") { $newentrynumber = 0; }
if ($newarchivenumber eq "") { $newarchivenumber = 0; }
if ($newstayattopnumber eq "") { $newstayattopnumber = 0; }
if ($newalltimepktotalnumber eq "") { $newalltimepktotalnumber = 0; }
if ($newalltimenktotalnumber eq "") { $newalltimenktotalnumber = 0; }
if ($newalltimeopenentriesnumber eq "") { $newalltimeopenentriesnumber = 0; }
if ($newalltimeclosedentriesnumber eq "") { $newalltimeclosedentriesnumber = 0; }

open (FUNNYFEETAUGH, ">gm-counter.cgi") || &gm_dangermouse("Can't write to the counter file.  Please make sure that gm-counter.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEETAUGH "$newentrynumber\n";
print FUNNYFEETAUGH "$newarchivenumber\n";
print FUNNYFEETAUGH "$newstayattopnumber\n";
print FUNNYFEETAUGH "$newalltimepktotalnumber\n";
print FUNNYFEETAUGH "$newalltimenktotalnumber\n";
print FUNNYFEETAUGH "$newalltimecommentstotalnumber\n";
print FUNNYFEETAUGH "$newalltimeopenentriesnumber\n";
print FUNNYFEETAUGH "$newalltimeclosedentriesnumber\n";
close (FUNNYFEETAUGH);

}

# ------------------
# read the templates
# ------------------

sub gm_readtemplates {

open (FUNNYFEETTAMMY, "gm-templates.cgi") || &gm_dangermouse("Can't read the templates file.  Please make sure that gm-templates.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmtemplates = <FUNNYFEETTAMMY>;
close (FUNNYFEETTAMMY);

$gmcounter = 0;

foreach (@gmtemplates) {
	chomp ($gmtemplates[$gmcounter]);
	$gmtemplates[$gmcounter] =~ s/\|\*\|/\n/g;
	$gmcounter++;
}

$gmindextemplate = $gmtemplates[0];
$gmentrypagetemplate = $gmtemplates[1];
$gmarchiveindextemplate = $gmtemplates[2];
$gmarchiveentrypagetemplate = $gmtemplates[3];
$gmentrytemplate = $gmtemplates[4];
$gmarchiveentrytemplate = $gmtemplates[5];
$gmstayattoptemplate = $gmtemplates[6];
$gmdatetemplate = $gmtemplates[7];
$gmcommentstemplate = $gmtemplates[8];
$gmcommentsformtemplate = $gmtemplates[9];
$gmparaseparationtemplate = $gmtemplates[10];
$gmkarmaformtemplate = $gmtemplates[11];
$gmmoreprefacetemplate = $gmtemplates[12];
$gmmorelinktemplate = $gmtemplates[13];
$gmkarmalinktemplate = $gmtemplates[14];
$gmcommentslinktemplate = $gmtemplates[15];
$gmcommentauthoremailtemplate = $gmtemplates[16];
$gmcommentauthorhomepagetemplate = $gmtemplates[17];
$gmcommentdividertemplate = $gmtemplates[18];

$gmmoreentrytemplate = $gmtemplates[19];
$gmmoreentrypagetemplate = $gmtemplates[20];
$gmmorearchiveentrypagetemplate = $gmtemplates[21];
$gmpreviouslinktemplate = $gmtemplates[22];
$gmnextlinktemplate = $gmtemplates[23];
$gmpreviousmorelinktemplate = $gmtemplates[24];
$gmnextmorelinktemplate = $gmtemplates[25];
$gmarchivemasterindextemplate = $gmtemplates[26];
$gmlogarchiveslinktemplate = $gmtemplates[27];
$gmentrypagelinktemplate = $gmtemplates[28];
$gmmoreentrypagelinktemplate = $gmtemplates[29];
$gmlogarchiveslinkseparatortemplate = $gmtemplates[30];
$gmentrypagelinkseparatortemplate = $gmtemplates[31];
$gmentrypagelinkmonthseparatortemplate = $gmtemplates[32];
$gmentrypagelinkdayseparatortemplate = $gmtemplates[33];
$gmentrypagelinkyearseparatortemplate = $gmtemplates[34];
$gmheadertemplate = $gmtemplates[35];
$gmfootertemplate = $gmtemplates[36];
$gmsidebartemplate = $gmtemplates[37];
$gmcustomlinktemplate = $gmtemplates[38];
$gmentryseparatortemplate = $gmtemplates[39];
$gmarchiveentryseparatortemplate = $gmtemplates[40];
$gmmorearchiveentrytemplate = $gmtemplates[41];
$gmdatearchivetemplate = $gmtemplates[42];

$gmlogarchiveslinkweeklytemplate = $gmtemplates[43];
$gmcustomonetemplate = $gmtemplates[44];
$gmcustomtwotemplate = $gmtemplates[45];
$gmcustomthreetemplate = $gmtemplates[46];
$gmcustomfourtemplate = $gmtemplates[47];
$gmcustomfivetemplate = $gmtemplates[48];
$gmcustomsixtemplate = $gmtemplates[49];
$gmcustomseventemplate = $gmtemplates[50];
$gmcustomeighttemplate = $gmtemplates[51];
$gmcustomninetemplate = $gmtemplates[52];
$gmcustomtentemplate = $gmtemplates[53];
$gmpopuppagetemplate = $gmtemplates[54];
$gmpopupcodetemplate = $gmtemplates[55];
$gmsearchformtemplate = $gmtemplates[56];
$gmsearchresultspagetemplate = $gmtemplates[57];
$gmsearchresultsentrytemplate = $gmtemplates[58];
$gmcalendartablebeginningtemplate = $gmtemplates[59];
$gmcalendartableendingtemplate = $gmtemplates[60];
$gmcalendarblankcelltemplate = $gmtemplates[61];
$gmcalendarfullcelltemplate = $gmtemplates[62];
$gmcalendarfullcelllinktemplate = $gmtemplates[63];
$gmcalendarweekblankdaytemplate = $gmtemplates[64];
$gmcalendarweekfulldaytemplate = $gmtemplates[65];
$gmcalendarweekfulldaylinktemplate = $gmtemplates[66];
$gmcommentpreviewdividertemplate = $gmtemplates[67];
$gmcommentpreviewformtemplate = $gmtemplates[68];
$gmsmartlinknocommentstemplate = $gmtemplates[69];
$gmsmartlinkonecommenttemplate = $gmtemplates[70];
$gmsmartlinkmanycommentstemplate = $gmtemplates[71];
$gmlinebreaktemplate = $gmtemplates[72];

}

# ---------------------
# delouse all templates
# ---------------------

sub gm_delousealltemplates {

$gmindextemplate = &delouse($gmindextemplate);
$gmentrypagetemplate = &delouse($gmentrypagetemplate);
$gmarchiveindextemplate = &delouse($gmarchiveindextemplate);
$gmarchiveentrypagetemplate = &delouse($gmarchiveentrypagetemplate);
$gmentrytemplate = &delouse($gmentrytemplate);
$gmarchiveentrytemplate = &delouse($gmarchiveentrytemplate);
$gmstayattoptemplate = &delouse($gmstayattoptemplate);
$gmdatetemplate = &delouse($gmdatetemplate);
$gmcommentstemplate = &delouse($gmcommentstemplate);
$gmcommentsformtemplate = &delouse($gmcommentsformtemplate);
$gmparaseparationtemplate = &delouse($gmparaseparationtemplate);
$gmkarmaformtemplate = &delouse($gmkarmaformtemplate);
$gmmoreprefacetemplate = &delouse($gmmoreprefacetemplate);
$gmmorelinktemplate = &delouse($gmmorelinktemplate);
$gmkarmalinktemplate = &delouse($gmkarmalinktemplate);
$gmcommentslinktemplate = &delouse($gmcommentslinktemplate);
$gmcommentauthoremailtemplate = &delouse($gmcommentauthoremailtemplate);
$gmcommentauthorhomepagetemplate = &delouse($gmcommentauthorhomepagetemplate);
$gmcommentdividertemplate = &delouse($gmcommentdividertemplate);
$gmmoreentrytemplate = &delouse($gmmoreentrytemplate);
$gmmoreentrypagetemplate = &delouse($gmmoreentrypagetemplate);
$gmmorearchiveentrypagetemplate = &delouse($gmmorearchiveentrypagetemplate);
$gmpreviouslinktemplate = &delouse($gmpreviouslinktemplate);
$gmnextlinktemplate = &delouse($gmnextlinktemplate);
$gmpreviousmorelinktemplate = &delouse($gmpreviousmorelinktemplate);
$gmnextmorelinktemplate = &delouse($gmnextmorelinktemplate);
$gmarchivemasterindextemplate = &delouse($gmarchivemasterindextemplate);
$gmlogarchiveslinktemplate = &delouse($gmlogarchiveslinktemplate);
$gmentrypagelinktemplate = &delouse($gmentrypagelinktemplate);
$gmmoreentrypagelinktemplate = &delouse($gmmoreentrypagelinktemplate);
$gmlogarchiveslinkseparatortemplate = &delouse($gmlogarchiveslinkseparatortemplate);
$gmentrypagelinkseparatortemplate = &delouse($gmentrypagelinkseparatortemplate);
$gmentrypagelinkmonthseparatortemplate = &delouse($gmentrypagelinkmonthseparatortemplate);
$gmentrypagelinkdayseparatortemplate = &delouse($gmentrypagelinkdayseparatortemplate);
$gmentrypagelinkyearseparatortemplate = &delouse($gmentrypagelinkyearseparatortemplate);
$gmheadertemplate = &delouse($gmheadertemplate);
$gmfootertemplate = &delouse($gmfootertemplate);
$gmsidebartemplate = &delouse($gmsidebartemplate);
$gmcustomlinktemplate = "";
$gmentryseparatortemplate = &delouse($gmentryseparatortemplate);
$gmarchiveentryseparatortemplate = &delouse($gmarchiveentryseparatortemplate);
$gmmorearchiveentrytemplate = &delouse($gmmorearchiveentrytemplate);
$gmdatearchivetemplate = &delouse($gmdatearchivetemplate);

$gmlogarchiveslinkweeklytemplate = &delouse($gmlogarchiveslinkweeklytemplate);
$gmcustomonetemplate = &delouse($gmcustomonetemplate);
$gmcustomtwotemplate = &delouse($gmcustomtwotemplate);
$gmcustomthreetemplate = &delouse($gmcustomthreetemplate);
$gmcustomfourtemplate = &delouse($gmcustomfourtemplate);
$gmcustomfivetemplate = &delouse($gmcustomfivetemplate);
$gmcustomsixtemplate = &delouse($gmcustomsixtemplate);
$gmcustomseventemplate = &delouse($gmcustomseventemplate);
$gmcustomeighttemplate = &delouse($gmcustomeighttemplate);
$gmcustomninetemplate = &delouse($gmcustomninetemplate);
$gmcustomtentemplate = &delouse($gmcustomtentemplate);
$gmpopuppagetemplate = &delouse($gmpopuppagetemplate);
$gmpopupcodetemplate = &delouse($gmpopupcodetemplate);
$gmsearchformtemplate = &delouse($gmsearchformtemplate);
$gmsearchresultspagetemplate = &delouse($gmsearchresultspagetemplate);
$gmsearchresultsentrytemplate = &delouse($gmsearchresultsentrytemplate);
$gmcalendartablebeginningtemplate = &delouse($gmcalendartablebeginningtemplate);
$gmcalendartableendingtemplate = &delouse($gmcalendartableendingtemplate);
$gmcalendarblankcelltemplate = &delouse($gmcalendarblankcelltemplate);
$gmcalendarfullcelltemplate = &delouse($gmcalendarfullcelltemplate);
$gmcalendarfullcelllinktemplate = &delouse($gmcalendarfullcelllinktemplate);
$gmcalendarweekblankdaytemplate = "";
$gmcalendarweekfulldaytemplate = &delouse($gmcalendarweekfulldaytemplate);
$gmcalendarweekfulldaylinktemplate = &delouse($gmcalendarweekfulldaylinktemplate);
$gmcommentpreviewdividertemplate = &delouse($gmcommentpreviewdividertemplate);
$gmcommentpreviewformtemplate = &delouse($gmcommentpreviewformtemplate);
$gmsmartlinknocommentstemplate = &delouse($gmsmartlinknocommentstemplate);
$gmsmartlinkonecommenttemplate = &delouse($gmsmartlinkonecommenttemplate);
$gmsmartlinkmanycommentstemplate = &delouse($gmsmartlinkmanycommentstemplate);
$gmlinebreaktemplate = &delouse($gmlinebreaktemplate);

}

# --------------------
# read the config file
# --------------------

sub gm_readconfig {

open (FUNNYFEETCOCO, "gm-config.cgi") || &gm_dangermouse("Can't read the configuration file.  Please make sure that gm-config.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmconfig = <FUNNYFEETCOCO>;
close (FUNNYFEETCOCO);

$gmcounter = 0;

foreach (@gmconfig) {
	chomp ($gmconfig[$gmcounter]);
	$gmcounter++;
}

$LogPath = $gmconfig[0];
$EntriesPath = $gmconfig[1];
$LogWebPath = $gmconfig[2];
$EntriesWebPath = $gmconfig[3];
$NotifyEmail = $gmconfig[4];
$indexfilename = $gmconfig[5];
$entrysuffix = $gmconfig[6];
$indexdays = $gmconfig[7];
$serveroffset = $gmconfig[8];
$timezone = $gmconfig[9];
$keeplog = $gmconfig[10];
$posttoarchives = $gmconfig[11];
$allowkarmadefault = $gmconfig[12];
$allowcommentsdefault = $gmconfig[13];
$commentsorder = $gmconfig[14];
$generateentrypages = $gmconfig[15];
$allowhtmlincomments = $gmconfig[16];
$logkarmaandcomments = $gmconfig[17];
$mailprog = $gmconfig[18];
$NotifyForStatus = $gmconfig[19];
$autolinkurls = $gmconfig[20];
$striplinesfromcomments = $gmconfig[21];
$allowmultiplekarmavotes = $gmconfig[22];
$versionsetup = $gmconfig[23];
$cgilocalpath = $gmconfig[24];
$cgiwebpath = $gmconfig[25];
$concurrentmainandarchives = $gmconfig[26];
$keeparchivemasterindex = $gmconfig[27];
$entrylistsortorder = $gmconfig[28];
$allowkarmaorcomments = $gmconfig[29];
$entrylistcountnumber = $gmconfig[30];

$cookiesallowed = $gmconfig[31];
$logarchivesuffix = $gmconfig[32];
$censorlist = $gmconfig[33];
$censorenabled = $gmconfig[34];
$keepmonthlyarchives = $gmconfig[35];
$defaultentrylistview = $gmconfig[36];
$linktocalendarentries = $gmconfig[37];
$automaticrebuilddefault = $gmconfig[38];
$commententrylistonlyifokay = $gmconfig[39];
$otherfilelist = $gmconfig[40];
$otherfilelistentryrebuild = $gmconfig[41];
$archiveformat = $gmconfig[42];
$inlineformatting = $gmconfig[43];
$uploadfilesallowed = $gmconfig[44];
$uploadfilesizelimit = $gmconfig[45];

}

# ---------------------
# write the config file
# ---------------------

sub gm_writeconfig {

if ($versionsetup eq "") { $versionsetup = $gmversion; }

open (FUNNYFEETCONNIE, ">gm-config.cgi") || &gm_dangermouse("Can't write to the configuration file.  Please make sure that gm-config.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEETCONNIE "$LogPath\n";
print FUNNYFEETCONNIE "$EntriesPath\n";
print FUNNYFEETCONNIE "$LogWebPath\n";
print FUNNYFEETCONNIE "$EntriesWebPath\n";
print FUNNYFEETCONNIE "$NotifyEmail\n";
print FUNNYFEETCONNIE "$indexfilename\n";
print FUNNYFEETCONNIE "$entrysuffix\n";
print FUNNYFEETCONNIE "$indexdays\n";
print FUNNYFEETCONNIE "$serveroffset\n";
print FUNNYFEETCONNIE "$timezone\n";
print FUNNYFEETCONNIE "$keeplog\n";
print FUNNYFEETCONNIE "$posttoarchives\n";
print FUNNYFEETCONNIE "$allowkarmadefault\n";
print FUNNYFEETCONNIE "$allowcommentsdefault\n";
print FUNNYFEETCONNIE "$commentsorder\n";
print FUNNYFEETCONNIE "$generateentrypages\n";
print FUNNYFEETCONNIE "$allowhtmlincomments\n";
print FUNNYFEETCONNIE "$logkarmaandcomments\n";
print FUNNYFEETCONNIE "$mailprog\n";
print FUNNYFEETCONNIE "$NotifyForStatus\n";
print FUNNYFEETCONNIE "$autolinkurls\n";
print FUNNYFEETCONNIE "$striplinesfromcomments\n";
print FUNNYFEETCONNIE "$allowmultiplekarmavotes\n";
print FUNNYFEETCONNIE "$versionsetup\n";
print FUNNYFEETCONNIE "$cgilocalpath\n";
print FUNNYFEETCONNIE "$cgiwebpath\n";
print FUNNYFEETCONNIE "$concurrentmainandarchives\n";
print FUNNYFEETCONNIE "$keeparchivemasterindex\n";
print FUNNYFEETCONNIE "$entrylistsortorder\n";
print FUNNYFEETCONNIE "$allowkarmaorcomments\n";
print FUNNYFEETCONNIE "$entrylistcountnumber\n";
print FUNNYFEETCONNIE "$cookiesallowed\n";
print FUNNYFEETCONNIE "$logarchivesuffix\n";
print FUNNYFEETCONNIE "$censorlist\n";
print FUNNYFEETCONNIE "$censorenabled\n";
print FUNNYFEETCONNIE "$keepmonthlyarchives\n";
print FUNNYFEETCONNIE "$defaultentrylistview\n";
print FUNNYFEETCONNIE "$linktocalendarentries\n";
print FUNNYFEETCONNIE "$automaticrebuilddefault\n";
print FUNNYFEETCONNIE "$commententrylistonlyifokay\n";
print FUNNYFEETCONNIE "$otherfilelist\n";
print FUNNYFEETCONNIE "$otherfilelistentryrebuild\n";
print FUNNYFEETCONNIE "$archiveformat\n";
print FUNNYFEETCONNIE "$inlineformatting\n";
print FUNNYFEETCONNIE "$uploadfilesallowed\n";
print FUNNYFEETCONNIE "$uploadfilesizelimit\n";
close (FUNNYFEETCONNIE);

}

# ---------------------------------
# gather ye all thy entry variables
# ---------------------------------

sub gm_getentryvariables {

my $thisentrygetmynumber = shift;

&gm_readconfig;
&gm_readtemplates;
&gm_readcounter;

$thisentrynumberpadded = sprintf ("%8d", $thisentrygetmynumber);
$thisentrynumberpadded =~ tr/ /0/;

open (FUNNYFEETENTRY, "$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777, or try running Diagnostics & Repair in the Configuration screen.");
@entrylines = <FUNNYFEETENTRY>;
close (FUNNYFEETENTRY);

$gmcounter = 0;

foreach (@entrylines) {
	chomp ($entrylines[$gmcounter]);
	$entrylines[$gmcounter] =~ s/\|\*\|/\n/g;
	$gmcounter++;
}

($thisentrynumber, $thisentryauthor, $thisentrysubject, $thisentryweekdaynumber, $thisentrymonth, $thisentryday, $thisentryyearyear, $thisentryhour, $thisentryminute, $thisentrysecond, $thisentryampm, $thisentrypositivekarma, $thisentrynegativekarma, $thisentrycommentsnumber, $thisentryallowkarma, $thisentryallowcomments, $thisentryopenstatus) = split (/\|/, $entrylines[0]);

chomp ($thisentryopenstatus);

$thisentryisanarchive = "no";
if ($thisentrynumber <= $newarchivenumber) { $thisentryisanarchive = "yes"; }

if ($generateentrypages eq "no") { $thisentryallowcomments = "no"; }

$thisentryyear = substr($thisentryyearyear, -2, 2);

@months = ("null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
@weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");

$thisentryweekday = $weekdays[$thisentryweekdaynumber];
$thisentrymonthword = $months[$thisentrymonth];
$thisentryweekdayshort = substr($thisentryweekday, 0, 3);
$thisentrymonthwordshort = substr($thisentrymonthword, 0, 3);
$thisentryweekdayupper = uc($thisentryweekday);
$thisentrymonthwordupper = uc($thisentrymonthword);
$thisentryweekdaylower = lc($thisentryweekday);
$thisentrymonthwordlower = lc($thisentrymonthword);
$thisentryweekdayuppershort = uc($thisentryweekdayshort);
$thisentrymonthworduppershort = uc($thisentrymonthwordshort);
$thisentryweekdaylowershort = lc($thisentryweekdayshort);
$thisentrymonthwordlowershort = lc($thisentrymonthwordshort);

$thisentrymonthmonth = sprintf ("%2d", $thisentrymonth);
$thisentrydayday = sprintf ("%2d", $thisentryday);
$thisentryhourhour = sprintf ("%2d", $thisentryhour);
$thisentryminuteminute = sprintf ("%2d", $thisentryminute);
$thisentrysecondsecond = sprintf ("%2d", $thisentrysecond);
$thisentrymonthmonth =~ tr/ /0/;
$thisentrydayday =~ tr/ /0/;
$thisentryhourhour =~ tr/ /0/;
$thisentryminuteminute =~ tr/ /0/;
$thisentrysecondsecond =~ tr/ /0/;

$thisentryampmdot = "A.M.";
$thisentrymilitaryhour = $thisentryhour;
if ($thisentryampm eq "PM") {
	$thisentryampmdot = "P.M.";
	if ($thisentryhour ne "12") { $thisentrymilitaryhour = $thisentryhour + 12; }
}

$thisentrymilitaryhour = sprintf ("%2d", $thisentrymilitaryhour);
$thisentrymilitaryhour =~ tr/ /0/;
$thisentryampmlower = lc($thisentryampm);
$thisentryampmdotlower = lc($thisentryampmdot);

if (($thisentryhour eq "12") && ($thisentryampm eq "AM")) {
	$thisentrymilitaryhour = "00";
}

$leapyearcheck = $thisentryyearyear % 4;

$thisentrymaxdaysinthismonth = 31;
if (($thisentrymonthword eq "September") || ($thisentrymonthword eq "April") || ($thisentrymonthword eq "June") || ($thisentrymonthword eq "November")) { $thisentrymaxdaysinthismonth = 30; }
if ($thisentrymonthword eq "February") {
	$thisentrymaxdaysinthismonth = 28;
	if ($leapyearcheck eq "0") { $thisentrymaxdaysinthismonth = 29; }
}
$thisentrymaxdaysinpreviousmonth = 31;
if (($thisentrymonthword eq "October") || ($thisentrymonthword eq "May") || ($thisentrymonthword eq "July") || ($thisentrymonthword eq "December")) { $thisentrymaxdaysinpreviousmonth = 30; }
if ($thisentrymonthword eq "March") {
	$thisentrymaxdaysinpreviousmonth = 28;
	if ($leapyearcheck eq "0") { $thisentrymaxdaysinpreviousmonth = 29; }
}

$thisentryweekbeginningmonth = $thisentrymonth;
$thisentryweekbeginningyearyear = $thisentryyearyear;
$thisentryweekendingmonth = $thisentrymonth;
$thisentryweekendingyearyear = $thisentryyearyear;

$thisentryweekbeginningday = $thisentryday - $thisentryweekdaynumber;
$thisentryweekendingday = $thisentryweekbeginningday + 6;

if ($thisentryweekbeginningday < 1) {
	$thisentryweekbeginningday = $thisentryweekbeginningday + $thisentrymaxdaysinpreviousmonth;
	if ($thisentryweekbeginningday > $thisentryday) { $thisentryweekbeginningmonth--; }
	if ($thisentryweekbeginningmonth < 1) {
		$thisentryweekbeginningmonth = 12;
		$thisentryweekbeginningyearyear--;
	}
}

if ($thisentryweekendingday > $thisentrymaxdaysinthismonth) {
	$thisentryweekendingday = $thisentryweekendingday - $thisentrymaxdaysinthismonth;
	if ($thisentryweekendingday < $thisentryday) { $thisentryweekendingmonth++; }
	if ($thisentryweekendingmonth > 12) {
		$thisentryweekendingmonth = 1;
		$thisentryweekendingyearyear++;
	}
}

$thisentryweekbeginningyear = substr($thisentryweekbeginningyearyear, -2, 2);
$thisentryweekendingyear = substr($thisentryweekendingyearyear, -2, 2);

$thisentryweekbeginningdayday = sprintf ("%2d", $thisentryweekbeginningday);
$thisentryweekbeginningdayday =~ tr/ /0/;
$thisentryweekendingdayday = sprintf ("%2d", $thisentryweekendingday);
$thisentryweekendingdayday =~ tr/ /0/;
$thisentryweekbeginningmonthmonth = sprintf ("%2d", $thisentryweekbeginningmonth);
$thisentryweekbeginningmonthmonth =~ tr/ /0/;
$thisentryweekendingmonthmonth = sprintf ("%2d", $thisentryweekendingmonth);
$thisentryweekendingmonthmonth =~ tr/ /0/;

$thisentryweekbeginningweekday = "Sunday";
$thisentryweekbeginningmonthword = $months[$thisentryweekbeginningmonth];
$thisentryweekbeginningweekdayshort = substr($thisentryweekbeginningweekday, 0, 3);
$thisentryweekbeginningmonthwordshort = substr($thisentryweekbeginningmonthword, 0, 3);
$thisentryweekbeginningweekdayupper = uc($thisentryweekbeginningweekday);
$thisentryweekbeginningmonthwordupper = uc($thisentryweekbeginningmonthword);
$thisentryweekbeginningweekdaylower = lc($thisentryweekbeginningweekday);
$thisentryweekbeginningmonthwordlower = lc($thisentryweekbeginningmonthword);
$thisentryweekbeginningweekdayuppershort = uc($thisentryweekbeginningweekdayshort);
$thisentryweekbeginningmonthworduppershort = uc($thisentryweekbeginningmonthwordshort);
$thisentryweekbeginningweekdaylowershort = lc($thisentryweekbeginningweekdayshort);
$thisentryweekbeginningmonthwordlowershort = lc($thisentryweekbeginningmonthwordshort);

$thisentryweekendingweekday = "Saturday";
$thisentryweekendingmonthword = $months[$thisentryweekendingmonth];
$thisentryweekendingweekdayshort = substr($thisentryweekendingweekday, 0, 3);
$thisentryweekendingmonthwordshort = substr($thisentryweekendingmonthword, 0, 3);
$thisentryweekendingweekdayupper = uc($thisentryweekendingweekday);
$thisentryweekendingmonthwordupper = uc($thisentryweekendingmonthword);
$thisentryweekendingweekdaylower = lc($thisentryweekendingweekday);
$thisentryweekendingmonthwordlower = lc($thisentryweekendingmonthword);
$thisentryweekendingweekdayuppershort = uc($thisentryweekendingweekdayshort);
$thisentryweekendingmonthworduppershort = uc($thisentryweekendingmonthwordshort);
$thisentryweekendingweekdaylowershort = lc($thisentryweekendingweekdayshort);
$thisentryweekendingmonthwordlowershort = lc($thisentryweekendingmonthwordshort);

open (FUNNYFEETVISHNU, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gettheauthordata = <FUNNYFEETVISHNU>;
close (FUNNYFEETVISHNU);

$thisentryauthoremail = "";
$thisentryauthorhomepage = "";
$thisentryauthorentrycount = "";

foreach $gettheauthordataline (@gettheauthordata) {
	chomp ($gettheauthordataline);
	@gettheauthorinfo = split (/\|/, $gettheauthordataline);
	if ($gettheauthorinfo[0] eq $thisentryauthor) {
		$thisentryauthoremail = $gettheauthorinfo[2];
		$thisentryauthorhomepage = $gettheauthorinfo[3];
		$thisentryauthorentrycount = $gettheauthorinfo[5];
	}
}

$thisentryauthorsmartlink = $thisentryauthor;
if ($thisentryauthoremail ne "") { $thisentryauthorsmartlink = "<A HREF=\"mailto:$thisentryauthoremail\">$thisentryauthor</A>"; }
if ($thisentryauthorhomepage ne "") { $thisentryauthorsmartlink = "<A HREF=\"$thisentryauthorhomepage\">$thisentryauthor</A>"; }

$thisentryfilename = "$EntriesWebPath\/$thisentrynumberpadded\.$entrysuffix";

$thisentrycommentspostlink = "$thisentryfilename\#comments";

$thisentrycommentstatussmart = $gmsmartlinkmanycommentstemplate;

if ($thisentrycommentsnumber eq "0") { $thisentrycommentstatussmart = $gmsmartlinknocommentstemplate; }
if ($thisentrycommentsnumber eq "1") { $thisentrycommentstatussmart = $gmsmartlinkonecommenttemplate; }

$thisentrycommentstatussmartupper = uc($thisentrycommentstatussmart);
$thisentrycommentstatussmartlower = lc($thisentrycommentstatussmart);

$thisentrypagelink = $thisentryfilename;

$indexfilenamesmartcheck = "/$indexfilename";
$indexfilenameprefix = substr($indexfilename, 0, 6);

if ($indexfilenameprefix eq "index.") { $indexfilenamesmartcheck = "/"; }

$thisentrypageindexlink = "$LogWebPath$indexfilenamesmartcheck";
$thisentrypagearchiveindexlink = "$EntriesWebPath$indexfilenamesmartcheck";

if ($keepmonthlyarchives eq "no") {
	$thisentrypagearchivelogindexlink = $thisentrypageindexlink;
} else {
	if ($archiveformat eq "week") {
		$thisentrypagearchivelogindexlink = "$EntriesWebPath/archive-$thisentryweekbeginningmonthmonth$thisentryweekbeginningdayday$thisentryweekbeginningyearyear-$thisentryweekendingmonthmonth$thisentryweekendingdayday$thisentryweekendingyearyear\.$logarchivesuffix";
	} else {
		$thisentrypagearchivelogindexlink = "$EntriesWebPath/archive-$thisentrymonthmonth$thisentryyearyear\.$logarchivesuffix";
	}
}

$thisentrypagesmartindexlink = $thisentrypageindexlink;

if (($thisentrynumber <= $newarchivenumber) && ($keepmonthlyarchives ne "no")) {
	$thisentrypagesmartindexlink = $thisentrypagearchivelogindexlink;
}

$thisentrycommentslink = "";
$thisentrycommentsform = "";
if ($thisentryallowcomments eq "yes") {
	if (($allowkarmaorcomments eq "comments") || ($allowkarmaorcomments eq "both")) {
		$thisentrycommentslink = $gmcommentslinktemplate;
		$thisentrycommentsform = $gmcommentsformtemplate;
	}
}

$thisentrykarmalink = "";
$thisentrykarmaform = "";
if ($thisentryallowkarma eq "yes") {
	if (($allowkarmaorcomments eq "karma") || ($allowkarmaorcomments eq "both")) {
		$thisentrykarmalink = $gmkarmalinktemplate;
		$thisentrykarmaform = $gmkarmaformtemplate;
	}
}

if (($thisentryisanarchive eq "yes") && ($posttoarchives eq "no")) {
	$thisentrykarmalink = "";
	$thisentrykarmaform = "";
	$thisentrycommentslink = "";
	$thisentrycommentsform = "";
}

$thisentrysearchform = $gmsearchformtemplate;

if ($generateentrypages eq "no") {
	$thisentrycommentslink = "";
	$thisentrycommentsform = "";
	$thisentrysearchform = "";
}

$thisentrypositivekarmalink = "$cgiwebpath/gm-karma.cgi?vote=positive&entry=$thisentrynumberpadded";
$thisentrynegativekarmalink = "$cgiwebpath/gm-karma.cgi?vote=negative&entry=$thisentrynumberpadded";

$thisentrytotalkarma = $thisentrypositivekarma - $thisentrynegativekarma;

@thisentrykarmavoters = split (/\|/, $entrylines[1]);

$thisentrymainbody = $entrylines[2];
$thisentrymorebody = $entrylines[3];

if (($thisentrymainbody =~ /\|\*\|\|\*\|/) || ($thisentrymorebody =~ /\|\*\|\|\*\|/)) {
	$thisentrymainbody =~ s/\|\*\|\|\*\|/<PARABREAK>/g;
	$thisentrymorebody =~ s/\|\*\|\|\*\|/<PARABREAK>/g;
}
if (($thisentrymainbody =~ /\n\n/) || ($thisentrymorebody =~ /\n\n/)) {
	$thisentrymainbody =~ s/\n\n/<PARABREAK>/g;
	$thisentrymorebody =~ s/\n\n/<PARABREAK>/g;
}
if (($thisentrymainbody =~ /\|\*\|/) || ($thisentrymorebody =~ /\|\*\|/)) {
	$thisentrymainbody =~ s/\|\*\|/$gmlinebreaktemplate/g;
	$thisentrymorebody =~ s/\|\*\|/$gmlinebreaktemplate/g;
}
if (($thisentrymainbody =~ /\n/) || ($thisentrymorebody =~ /\n/)) {
	$thisentrymainbody =~ s/\n/$gmlinebreaktemplate/g;
	$thisentrymorebody =~ s/\n/$gmlinebreaktemplate/g;
}
if (($thisentrymainbody =~ /<PARABREAK>/) || ($thisentrymorebody =~ /<PARABREAK>/)) {
	$thisentrymainbody =~ s/<PARABREAK>/$gmparaseparationtemplate/g;
	$thisentrymorebody =~ s/<PARABREAK>/$gmparaseparationtemplate/g;
}

if (($censorenabled eq "both") || ($censorenabled eq "entries")) {
	unless ($censorlist eq "") {
		@censoredterms = split(/\|\*\|/, $censorlist);
		foreach $thisterm (@censoredterms) {
			unless ($thisterm eq "") {
				if ((substr($thisterm, 0, 1) eq "[") && (substr($thisterm, -1, 1) eq "]")) {
					$thisrealterm = $thisterm;
					$thisrealterm =~ s/\[//g;
					$thisrealterm =~ s/\]//g;
					$thisrealtermlength = length($thisrealterm);
					$thisrealtermreplace = "*" x $thisrealtermlength;
					$thisrealtermreplacedash = "-" x $thisrealtermlength;
					if ($thisentrysubject =~ m/$thisrealterm/i) {
						$thisentrysubject =~ s/\b$thisrealterm\b/$thisrealtermreplacedash/isg;
					}
					if ($thisentrymainbody =~ m/$thisrealterm/i) {
						$thisentrymainbody =~ s/\b$thisrealterm\b/$thisrealtermreplace/isg;
					}
					if ($thisentrymorebody =~ m/$thisrealterm/i) {
						$thisentrymorebody =~ s/\b$thisrealterm\b/$thisrealtermreplace/isg;
					}
				} else {
					$thisrealtermlength = length($thisterm);
					$thisrealtermreplace = "*" x $thisrealtermlength;
					$thisrealtermreplacedash = "-" x $thisrealtermlength;
					if ($thisentrysubject =~ m/$thisterm/i) {
						$thisentrysubject =~ s/\b$thisterm\b/$thisrealtermreplacedash/isg;
					}
					if ($thisentrymainbody =~ m/$thisterm/i) {
						$thisentrymainbody =~ s/\b$thisterm\b/$thisrealtermreplace/isg;
					}
					if ($thisentrymorebody =~ m/$thisterm/i) {
						$thisentrymorebody =~ s/\b$thisterm\b/$thisrealtermreplace/isg;
					}
				}
			}
		}
	}
}

$thisentrymorepreface = "";
$thisentrymorelink = "";
if (($thisentrymorebody ne "") && ($generateentrypages ne "no")) {
	$thisentrymorepreface = $gmmoreprefacetemplate;
	$thisentrymorelink = $gmmorelinktemplate;
}

$thisentrycommentdivider = "";
if ($thisentrycommentsnumber ne "0") { $thisentrycommentdivider = $gmcommentdividertemplate; }

$thisentrycomments = "";

if (($inlineformatting eq "entries") || ($inlineformatting eq "both")) {
	if (($thisentrysubject =~ /\*\*(.*?)\*\*/) || ($thisentrysubject =~ /\\\\(.*?)\\\\/) || ($thisentrysubject =~ /__(.*?)__/)) {
		$thisentrysubject =~ s/\*\*(.*?)\*\*/<B>$1<\/B>/isg;
		$thisentrysubject =~ s/\\\\(.*?)\\\\/<I>$1<\/I>/isg;
		$thisentrysubject =~ s/__(.*?)__/<U>$1<\/U>/isg;
	}
	if (($thisentrymainbody =~ /\*\*(.*?)\*\*/) || ($thisentrymainbody =~ /\\\\(.*?)\\\\/) || ($thisentrymainbody =~ /__(.*?)__/)) {
		$thisentrymainbody =~ s/\*\*(.*?)\*\*/<B>$1<\/B>/isg;
		$thisentrymainbody =~ s/\\\\(.*?)\\\\/<I>$1<\/I>/isg;
		$thisentrymainbody =~ s/__(.*?)__/<U>$1<\/U>/isg;
	}
	if (($thisentrymorebody =~ /\*\*(.*?)\*\*/) || ($thisentrymorebody =~ /\\\\(.*?)\\\\/) || ($thisentrymorebody =~ /__(.*?)__/)) {
		$thisentrymorebody =~ s/\*\*(.*?)\*\*/<B>$1<\/B>/isg;
		$thisentrymorebody =~ s/\\\\(.*?)\\\\/<I>$1<\/I>/isg;
		$thisentrymorebody =~ s/__(.*?)__/<U>$1<\/U>/isg;
	}
}

if (($thisentrycommentsnumber ne "0") && ($generateentrypages ne "no")) {
	$thisisaspellcheck = "no";
	&gm_collatecomments;
	$thisentrycomments =~ s/\&quot;/"/g;
}

}

# -----------------
# comment collating
# -----------------

sub gm_collatecomments {

$commentcounter = 4;
if ($commentsorder eq "ascending") { $commentcounter = $thisentrycommentsnumber + 3; }

$commentcountermax = $thisentrycommentsnumber + 3;
$commentcountercurrent = $thisentrycommentsnumber;

do {

$thiscommentordernumber = $commentcounter - 3;

($thiscommentauthor, $thiscommentauthorip, $thiscommentauthoremailabsolute, $thiscommentauthorhomepageabsolute, $thiscommentweekdaynumber, $thiscommentmonth, $thiscommentday, $thiscommentyearyear, $thiscommenthour, $thiscommentminute, $thiscommentsecond, $thiscommentampm, $thiscommenttext) = split (/\|/, $entrylines[$commentcounter]);

$thiscommentyear = substr($thiscommentyearyear, -2, 2);

@months = ("null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
@weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");

$thiscommentweekday = $weekdays[$thiscommentweekdaynumber];
$thiscommentmonthword = $months[$thiscommentmonth];
$thiscommentweekdayshort = substr($thiscommentweekday, 0, 3);
$thiscommentmonthwordshort = substr($thiscommentmonthword, 0, 3);
$thiscommentweekdayupper = uc($thiscommentweekday);
$thiscommentmonthwordupper = uc($thiscommentmonthword);
$thiscommentweekdaylower = lc($thiscommentweekday);
$thiscommentmonthwordlower = lc($thiscommentmonthword);
$thiscommentweekdayuppershort = uc($thiscommentweekdayshort);
$thiscommentmonthworduppershort = uc($thiscommentmonthwordshort);
$thiscommentweekdaylowershort = lc($thiscommentweekdayshort);
$thiscommentmonthwordlowershort = lc($thiscommentmonthwordshort);

$thiscommentmonthmonth = sprintf ("%2d", $thiscommentmonth);
$thiscommentdayday = sprintf ("%2d", $thiscommentday);
$thiscommenthourhour = sprintf ("%2d", $thiscommenthour);
$thiscommentminuteminute = sprintf ("%2d", $thiscommentminute);
$thiscommentsecondsecond = sprintf ("%2d", $thiscommentsecond);
$thiscommentmonthmonth =~ tr/ /0/;
$thiscommentdayday =~ tr/ /0/;
$thiscommenthourhour =~ tr/ /0/;
$thiscommentminuteminute =~ tr/ /0/;
$thiscommentsecondsecond =~ tr/ /0/;

$thiscommentampmdot = "A.M.";
$thiscommentmilitaryhour = $thiscommenthour;
if ($thiscommentampm eq "PM") {
	$thiscommentampmdot = "P.M.";
	if ($thiscommenthour ne "12") { $thiscommentmilitaryhour = $thiscommenthour + 12; }
}
$thiscommentmilitaryhour = sprintf ("%2d", $thiscommentmilitaryhour);
$thiscommentmilitaryhour =~ tr/ /0/;
$thiscommentampmlower = lc($thiscommentampm);
$thiscommentampmdotlower = lc($thiscommentampmdot);

$thiscommentauthor =~ s/"/\&quot;/g;
$thiscommentauthoremailabsolute =~ s/"/\&quot;/g;
$thiscommentauthorhomepageabsolute =~ s/"/\&quot;/g;

$thiscommentauthoremail = "";
$thiscommentauthorhomepage = "";

$thiscommentauthorsmartlink = $thiscommentauthor;
if ($thiscommentauthoremailabsolute ne "") {
	$thiscommentauthoremail = $gmcommentauthoremailtemplate;
	$thiscommentauthorsmartlink = "<A HREF=\"mailto:$thiscommentauthoremailabsolute\">$thiscommentauthor</A>";
}
if ($thiscommentauthorhomepageabsolute ne "") {
	$thiscommentauthorhomepage = $gmcommentauthorhomepagetemplate;
	$thiscommentauthorsmartlink = "<A HREF=\"$thiscommentauthorhomepageabsolute\">$thiscommentauthor</A>";
}

if (($allowhtmlincomments eq "linkboldital") || ($allowhtmlincomments eq "linkonly")) {
	if ($thiscommenttext =~ m/\*/i) { $thiscommenttext =~ s/\*/\|AMP\|/g; }
	if (($thiscommenttext =~ m/<A HREF/i) && ($thiscommenttext =~ m/<\/A>/i)) {
		$thiscommenttext =~ s/<A HREF/\*A HREF\*/isg;
		$thiscommenttext =~ s/<\/A>/\*A\*/isg;
	}
	if ($allowhtmlincomments eq "linkboldital") {
		if (($thiscommenttext =~ m/<B>/i) && ($thiscommenttext =~ m/<\/B>/i)) {
			$thiscommenttext =~ s/<B>/\*B\*/isg;
			$thiscommenttext =~ s/<\/B>/\*BB\*/isg;
		}
		if (($thiscommenttext =~ m/<I>/i) && ($thiscommenttext =~ m/<\/I>/i)) {
			$thiscommenttext =~ s/<I>/\*I\*/isg;
			$thiscommenttext =~ s/<\/I>/\*II\*/isg;
		}
	}
}

unless ($allowhtmlincomments eq "yes") { $thiscommenttext =~ s/<([^>]|\n)*>//g; }

if ($autolinkurls eq "yes") {
# these two lines of code written in part by Neal Coffey (cray@indecisions.org)
	$thiscommenttext =~ s#(^|\s)(\w+://)([A-Za-z0-9?=_\-/.%+&'~\#@!\^]+)#$1<A HREF="$2$3">$2$3</A>#isg;
	$thiscommenttext =~ s#(^|\s)(www.[A-Za-z0-9?=_\-/.%+&'~\#@!\^]+)#$1<A HREF="http://$2">$2</A>#isg;
# thanks, Neal!
	$thiscommenttext =~ s/(\w+\@\w+\.\w+)/<A HREF="mailto:$1">$1<\/A>/isg;
}

if (($allowhtmlincomments eq "linkboldital") || ($allowhtmlincomments eq "linkonly")) {
	if (($thiscommenttext =~ m/\*A HREF\*/i) && ($thiscommenttext =~ m/\*A\*/i)) {
		$thiscommenttext =~ s/\*A HREF\*/<A HREF/isg;
		$thiscommenttext =~ s/\*A\*/<\/A>/isg;
	}
	if ($allowhtmlincomments eq "linkboldital") {
		if (($thiscommenttext =~ m/\*B\*/i) && ($thiscommenttext =~ m/\*BB\*/i)) {
			$thiscommenttext =~ s/\*B\*/<B>/isg;
			$thiscommenttext =~ s/\*BB\*/<\/B>/isg;
		}
		if (($thiscommenttext =~ m/\*I\*/i) && ($thiscommenttext =~ m/\*II\*/i)) {
			$thiscommenttext =~ s/\*I\*/<I>/isg;
			$thiscommenttext =~ s/\*II\*/<\/I>/isg;
		}
	}
	if ($thiscommenttext =~ m/\|AMP\|/i) { $thiscommenttext =~ s/\|AMP\|/\*/g; }
}

if (($inlineformatting eq "comments") || ($inlineformatting eq "both")) {
	if (($thiscommenttext =~ /\*\*(.*?)\*\*/) || ($thiscommenttext =~ /\\\\(.*?)\\\\/) || ($thiscommenttext =~ /__(.*?)__/)) {
		$thiscommenttext =~ s/\*\*(.*?)\*\*/<B>$1<\/B>/isg;
		$thiscommenttext =~ s/\\\\(.*?)\\\\/<I>$1<\/I>/isg;
		$thiscommenttext =~ s/__(.*?)__/<U>$1<\/U>/isg;
	}
}

if ($striplinesfromcomments eq "yes") {
	if (($thiscommenttext =~ /\|\*\|/) || ($thiscommenttext =~ /\n/)) {
		$thiscommenttext =~ s/\|\*\|/ /g;
		$thiscommenttext =~ s/\n/ /g;
	}
} else {
	if (($thiscommenttext =~ /\|\*\|/) || ($thiscommenttext =~ /\n/)) {
		$thiscommenttext =~ s/\|\*\|\|\*\|/<PARABREAK>/g;
		$thiscommenttext =~ s/\n\n/<PARABREAK>/g;
		$thiscommenttext =~ s/\|\*\|/$gmlinebreaktemplate/g;
		$thiscommenttext =~ s/\n/$gmlinebreaktemplate/g;
		$thiscommenttext =~ s/<PARABREAK>/$gmparaseparationtemplate/g;
	}
}

if (($censorenabled eq "both") || ($censorenabled eq "comments")) {
	unless ($censorlist eq "") {
		@censoredterms = split(/\|\*\|/, $censorlist);
		foreach $thisterm (@censoredterms) {
			unless ($thisterm eq "") {
				if ((substr($thisterm, 0, 1) eq "[") && (substr($thisterm, -1, 1) eq "]")) {
					$thisrealterm = $thisterm;
					$thisrealterm =~ s/\[//g;
					$thisrealterm =~ s/\]//g;
					$thisrealtermlength = length($thisrealterm);
					$thisrealtermreplace = "*" x $thisrealtermlength;
					$thisrealtermreplacedash = "-" x $thisrealtermlength;
					if ($thiscommenttext =~ m/$thisrealterm/i) {
						$thiscommenttext =~ s/\b$thisrealterm\b/$thisrealtermreplace/isg;
					}
					if ($thiscommentauthor =~ m/$thisrealterm/i) {
						$thiscommentauthor =~ s/\b$thisrealterm\b/$thisrealtermreplacedash/isg;
					}
				} else {
					$thisrealtermlength = length($thisterm);
					$thisrealtermreplace = "*" x $thisrealtermlength;
					$thisrealtermreplacedash = "-" x $thisrealtermlength;
					if ($thiscommenttext =~ m/$thisterm/i) {
						$thiscommenttext =~ s/\b$thisterm\b/$thisrealtermreplace/isg;
					}
					if ($thiscommentauthor =~ m/$thisterm/i) {
						$thiscommentauthor =~ s/\b$thisterm\b/$thisrealtermreplacedash/isg;
					}
				}
			}
		}
	}
}

$thiscommentfullbody = $gmcommentstemplate;

if ($thiscommentfullbody =~ m/{{comment/i) {
	$thiscommentfullbody =~ s/{{commentbody}}/$thiscommenttext/gi;
	$thiscommentfullbody =~ s/{{commentauthoremail}}/$thiscommentauthoremail/gi;
	$thiscommentfullbody =~ s/{{commentauthorhomepage}}/$thiscommentauthorhomepage/gi;
	$thiscommentfullbody =~ s/{{commentauthor}}/$thiscommentauthor/gi;
	$thiscommentfullbody =~ s/{{commentauthoremailabsolute}}/$thiscommentauthoremailabsolute/gi;
	$thiscommentfullbody =~ s/{{commentauthorhomepageabsolute}}/$thiscommentauthorhomepageabsolute/gi;
	$thiscommentfullbody =~ s/{{commentauthorsmartlink}}/$thiscommentauthorsmartlink/gi;
	$thiscommentfullbody =~ s/{{commentauthorip}}/$thiscommentauthorip/gi;
	$thiscommentfullbody =~ s/{{commentordernumber}}/$thiscommentordernumber/gi;
}

$thiscommentfullbody =~ s/{{day}}/$thiscommentday/gi;
$thiscommentfullbody =~ s/{{month}}/$thiscommentmonth/gi;
$thiscommentfullbody =~ s/{{year}}/$thiscommentyear/gi;
$thiscommentfullbody =~ s/{{hour}}/$thiscommenthour/gi;
$thiscommentfullbody =~ s/{{minute}}/$thiscommentminute/gi;
$thiscommentfullbody =~ s/{{second}}/$thiscommentsecond/gi;
$thiscommentfullbody =~ s/{{dayday}}/$thiscommentdayday/gi;
$thiscommentfullbody =~ s/{{monthmonth}}/$thiscommentmonthmonth/gi;
$thiscommentfullbody =~ s/{{yearyear}}/$thiscommentyearyear/gi;
$thiscommentfullbody =~ s/{{hourhour}}/$thiscommenthourhour/gi;
$thiscommentfullbody =~ s/{{minuteminute}}/$thiscommentminuteminute/gi;
$thiscommentfullbody =~ s/{{secondsecond}}/$thiscommentsecondsecond/gi;
$thiscommentfullbody =~ s/{{weekday}}/$thiscommentweekday/gi;
$thiscommentfullbody =~ s/{{monthword}}/$thiscommentmonthword/gi;
$thiscommentfullbody =~ s/{{weekdayupper}}/$thiscommentweekdayupper/gi;
$thiscommentfullbody =~ s/{{monthwordupper}}/$thiscommentmonthwordupper/gi;
$thiscommentfullbody =~ s/{{weekdaylower}}/$thiscommentweekdaylower/gi;
$thiscommentfullbody =~ s/{{monthwordlower}}/$thiscommentmonthwordlower/gi;
$thiscommentfullbody =~ s/{{weekdayuppershort}}/$thiscommentweekdayuppershort/gi;
$thiscommentfullbody =~ s/{{monthworduppershort}}/$thiscommentmonthworduppershort/gi;
$thiscommentfullbody =~ s/{{weekdaylowershort}}/$thiscommentweekdaylowershort/gi;
$thiscommentfullbody =~ s/{{monthwordlowershort}}/$thiscommentmonthwordlowershort/gi;
$thiscommentfullbody =~ s/{{militaryhour}}/$thiscommentmilitaryhour/gi;
$thiscommentfullbody =~ s/{{ampm}}/$thiscommentampm/gi;
$thiscommentfullbody =~ s/{{ampmdot}}/$thiscommentampmdot/gi;
$thiscommentfullbody =~ s/{{ampmlower}}/$thiscommentampmlower/gi;
$thiscommentfullbody =~ s/{{ampmdotlower}}/$thiscommentampmdotlower/gi;

$thisentrycomments .= $thiscommentfullbody;

if ($commentsorder eq "ascending") { $commentcounter--; } else { $commentcounter++; }

$commentcountercurrent--;

} until $commentcountercurrent eq "0";

}

# ----------------
# format the entry
# ----------------

sub gm_formatentry {

my $entrygetreturn = shift;

$entryreturn = $entrygetreturn;

# $entryreturn =~ s/\|\*\|/\n/g;

if (($entryreturn =~ m/{{header}}/i) || ($entryreturn =~ m/{{footer}}/i) || ($entryreturn =~ m/{{sidebar}}/i)) {
	$entryreturn =~ s/{{header}}/$gmheadertemplate/gi;
	$entryreturn =~ s/{{footer}}/$gmfootertemplate/gi;
	$entryreturn =~ s/{{sidebar}}/$gmsidebartemplate/gi;
}

if ($entryreturn =~ m/{{custom/i) {
	$entryreturn =~ s/{{customone}}/$gmcustomonetemplate/gi;
	$entryreturn =~ s/{{customtwo}}/$gmcustomtwotemplate/gi;
	$entryreturn =~ s/{{customthree}}/$gmcustomthreetemplate/gi;
	$entryreturn =~ s/{{customfour}}/$gmcustomfourtemplate/gi;
	$entryreturn =~ s/{{customfive}}/$gmcustomfivetemplate/gi;
	$entryreturn =~ s/{{customsix}}/$gmcustomsixtemplate/gi;
	$entryreturn =~ s/{{customseven}}/$gmcustomseventemplate/gi;
	$entryreturn =~ s/{{customeight}}/$gmcustomeighttemplate/gi;
	$entryreturn =~ s/{{customnine}}/$gmcustomninetemplate/gi;
	$entryreturn =~ s/{{customten}}/$gmcustomtentemplate/gi;
}

if ($entryreturn =~ m/{{logarchivelist}}/i) {
	if ($keepmonthlyarchives eq "no") {
		$entryreturn =~ s/{{logarchivelist}}//gi;
	} else {
		&gm_generatearchiveloglist;
		$entryreturn =~ s/{{logarchivelist}}/$logarchivelistfinal/gi;
	}
}

if ($generateentrypages eq "yes") {
	if (($entryreturn =~ m/{{logshortentrylist/i) || ($entryreturn =~ m/{{logmoreentrylist/i) || ($entryreturn =~ m/{{logentrylist/i)) {
		&gm_generateentryloglist;
		$entryreturn =~ s/{{logshortentrylist}}/$logshortentrylistfinal/gi;
		$entryreturn =~ s/{{logmoreentrylist}}/$logmoreentrylistfinal/gi;
		$entryreturn =~ s/{{logentrylist}}/$logentrylistfinal/gi;
		$entryreturn =~ s/{{logshortentrylist month}}/$logshortentrylistmonthfinal/gi;
		$entryreturn =~ s/{{logshortentrylist day}}/$logshortentrylistdayfinal/gi;
		$entryreturn =~ s/{{logshortentrylist year}}/$logshortentrylistyearfinal/gi;
		$entryreturn =~ s/{{logmoreentrylist month}}/$logmoreentrylistmonthfinal/gi;
		$entryreturn =~ s/{{logmoreentrylist day}}/$logmoreentrylistdayfinal/gi;
		$entryreturn =~ s/{{logmoreentrylist year}}/$logmoreentrylistyearfinal/gi;
		$entryreturn =~ s/{{logentrylist month}}/$logentrylistmonthfinal/gi;
		$entryreturn =~ s/{{logentrylist day}}/$logentrylistdayfinal/gi;
		$entryreturn =~ s/{{logentrylist year}}/$logentrylistyearfinal/gi;
		$entryreturn =~ s/{{logshortentrylist number}}/$logshortentrylistnumberfinal/gi;
		$entryreturn =~ s/{{logmoreentrylist number}}/$logmoreentrylistnumberfinal/gi;
		$entryreturn =~ s/{{logentrylist number}}/$logentrylistnumberfinal/gi;
		$entryreturn =~ s/{{logshortentrylist firsthalf}}/$logshortentrylistfirsthalffinal/gi;
		$entryreturn =~ s/{{logshortentrylist secondhalf}}/$logshortentrylistsecondhalffinal/gi;
		$entryreturn =~ s/{{logmoreentrylist firsthalf}}/$logmoreentrylistfirsthalffinal/gi;
		$entryreturn =~ s/{{logmoreentrylist secondhalf}}/$logmoreentrylistsecondhalffinal/gi;
		$entryreturn =~ s/{{logentrylist firsthalf}}/$logentrylistfirsthalffinal/gi;
		$entryreturn =~ s/{{logentrylist secondhalf}}/$logentrylistsecondhalffinal/gi;
	}
	if (($entryreturn =~ m/{{logshortentrylist comments/i) || ($entryreturn =~ m/{{logmoreentrylist comments/i) || ($entryreturn =~ m/{{logentrylist comments/i)) {
		&gm_generateentryloglistcomments;
		$entryreturn =~ s/{{logshortentrylist comments}}/$logshortentrylistfinal/gi;
		$entryreturn =~ s/{{logmoreentrylist comments}}/$logmoreentrylistfinal/gi;
		$entryreturn =~ s/{{logentrylist comments}}/$logentrylistfinal/gi;
		$entryreturn =~ s/{{logshortentrylist commentsminimum}}/$logshortminimumentrylistfinal/gi;
		$entryreturn =~ s/{{logmoreentrylist commentsminimum}}/$logmoreminimumentrylistfinal/gi;
		$entryreturn =~ s/{{logentrylist commentsminimum}}/$logminimumentrylistfinal/gi;
		$entryreturn =~ s/{{logshortentrylist commentsnumber}}/$logshortnumberentrylistfinal/gi;
		$entryreturn =~ s/{{logmoreentrylist commentsnumber}}/$logmorenumberentrylistfinal/gi;
		$entryreturn =~ s/{{logentrylist commentsnumber}}/$lognumberentrylistfinal/gi;
	}
	if (($entryreturn =~ m/{{logshortentrylist /i) || ($entryreturn =~ m/{{logmoreentrylist /i) || ($entryreturn =~ m/{{logentrylist /i)) {
		open (FUNNYFEETBRAHMA, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
		@gettheauthordata = <FUNNYFEETBRAHMA>;
		close (FUNNYFEETBRAHMA);
		foreach $gettheauthordataline (@gettheauthordata) {
			chomp ($gettheauthordataline);
			@gettheauthorinfo = split (/\|/, $gettheauthordataline);
			$thisentryloglistauthor = $gettheauthorinfo[0];
			&gm_generateentryloglistauthor;
			$entryreturn =~ s/{{logshortentrylist $thisentryloglistauthor}}/$logshortentrylistfinal/gi;
			$entryreturn =~ s/{{logmoreentrylist $thisentryloglistauthor}}/$logmoreentrylistfinal/gi;
			$entryreturn =~ s/{{logentrylist $thisentryloglistauthor}}/$logentrylistfinal/gi;
		}
	}
}

if (($entryreturn =~ m/{{calendar}}/i) || ($entryreturn =~ m/{{calendarweek}}/i)) {
	$usethisentryweekdaynumber = $thisentryweekdaynumber;
	$usethisentryday = $thisentryday;
	$usethisentrymonth = $thisentrymonth;
	$usethisentrymonthmonth = $thisentrymonthmonth;
	$usethisentrymonthword = $thisentrymonthword;
	$usethisentryyear = $thisentryyear;
	$usethisentryyearyear = $thisentryyearyear;
	&gm_generatecalendar;
	$entryreturn =~ s/{{calendar}}/$calendarfull/gi;
	$entryreturn =~ s/{{calendarweek}}/$calendarweekfull/gi;
}

if ($entryreturn =~ m/{{calendar (..)\/(..)}}/i) {

	until ($entryreturn !~ m/{{calendar (..)\/(..)}}/ig) {

		$usethisentrymonthmonth = $1;
		$usethisentryyear = $2;

		open (FUNNYFEETKALI, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entry list file.  Please make sure that gm-entrylist.cgi is in the same directory as all your other Greymatter files and is CHMODed to 666; also, try running Diagnostics & Repair in the Configuration screen.");
		@loglistloglines = <FUNNYFEETKALI>;
		close (FUNNYFEETKALI);

		$gotthecalendarmonth = "no";

		foreach $thisloglistline (@loglistloglines) {
			($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
			&gm_getloglistvariables;
			if (($loglistmonthmonth eq $usethisentrymonthmonth) && ($loglistyear eq $usethisentryyear) && ($gotthecalendarmonth eq "no")) {
				$usethisentryweekdaynumber = $loglistentryweekdaynumber;
				$usethisentryday = $loglistday;
				$usethisentrymonth = $loglistmonth;
				$usethisentrymonthword = $loglistmonthword;
				$usethisentryyearyear = $loglistyearyear;
				&gm_generatecalendar;
				$entryreturn =~ s/{{calendar $usethisentrymonthmonth\/$usethisentryyear}}/$calendarfull/gi;
				$gotthecalendarmonth = "yes";
			}
		}
		
		if ($entryreturn =~ m/{{calendar $usethisentrymonthmonth\/$usethisentryyear}}/i) {
			$entryreturn =~ s/{{calendar $usethisentrymonthmonth\/$usethisentryyear}}//gi;
		}

	}

}

if (($entryreturn =~ m/{{commentdivider}}/i) || ($entryreturn =~ m/{{entrycommentsform}}/i) || ($entryreturn =~ m/{{entrykarmaform}}/i) || ($entryreturn =~ m/{{searchform}}/i)) {
	$entryreturn =~ s/{{commentdivider}}/$thisentrycommentdivider/gi;
	$entryreturn =~ s/{{entrycommentsform}}/$thisentrycommentsform/gi;
	$entryreturn =~ s/{{entrykarmaform}}/$thisentrykarmaform/gi;
	$entryreturn =~ s/{{searchform}}/$thisentrysearchform/gi;
}

if ($entryreturn =~ m/{{entry/i) {
	$entryreturn =~ s/{{entrymainbody}}/$thisentrymainbody/gi;
	$entryreturn =~ s/{{entrymorebody}}/$thisentrymorebody/gi;
	$entryreturn =~ s/{{entrycomments}}/$thisentrycomments/gi;
	if ($entryreturn =~ m/{{entrymainbodyfirstwords (\d+)}}/i) {
		until ($entryreturn !~ m/{{entrymainbodyfirstwords (\d+)}}/isg) {
			$firstwordscount = $1;
			$grabmainbodywords = $thisentrymainbody;
			if ($grabmainbodywords =~ m/{{link/i) {
				$grabmainbodywords =~ s/({{linkmo) (http|https|ftp)(:\/\/\S+?) (.+?)(\|)(.+?)(}})/$4/isg;
				$grabmainbodywords =~ s/({{link) (http|https|ftp)(:\/\/\S+?)(}})/$2$3/isg;
				$grabmainbodywords =~ s/({{link) (http|https|ftp)(:\/\/\S+?) (.+?)(}})/$4/isg;
			}
			if ($grabmainbodywords =~ m/{{email/i) {
				$grabmainbodywords =~ s/({{emailmo) (\S+\@\S+?) (.+?)(\|)(.+?)(}})/$3/isg;
				$grabmainbodywords =~ s/({{email) (\S+\@\S+?)(}})/$2/isg;
				$grabmainbodywords =~ s/({{email) (\S+\@\S+?) (.+?)(}})/$3/isg;
			}
			$grabmainbodywords =~ s/<([^>]|\n)*>/ /g;
			$grabmainbodywords =~ s/{{(.*?)}}/ /g;
			$grabmainbodywords =~ s/\n/ /g;
			$grabmainbodywords =~ s/\r/ /g;
			$grabmainbodywords =~ s/\|\*\|/ /g;
			$grabmainbodywords =~ s/^\s+//;
			$grabmainbodywords =~ s/\s+$//;
			$grabmainbodywords =~ s/\s{2,}/ /g;
			@grabmainbodywordslist = split (/ /, $grabmainbodywords);
			$countwordsfromhere = 0;
			(@finalmainbodywordslist, @finalmainbodywordslist = ());
			if ($firstwordscount < 1) { $firstwordscount = 1; }
			do {
				$finalmainbodywordslist[$countwordsfromhere] = $grabmainbodywordslist[$countwordsfromhere];
				$countwordsfromhere++;
			} until $countwordsfromhere eq $firstwordscount;
			$finalmainbodyfirstwords = join (" ", @finalmainbodywordslist);
			$finalmainbodyfirstwords =~ s/^\s+//;
			$finalmainbodyfirstwords =~ s/\s+$//;
			$finalmainbodyfirstwords =~ s/\s{2,}//g;
			if (substr($finalmainbodyfirstwords, -1) =~ /\W/) { chop($finalmainbodyfirstwords); }
			if (substr($finalmainbodyfirstwords, -1) eq / /) { chop($finalmainbodyfirstwords); }
			$entryreturn =~ s/{{entrymainbodyfirstwords ($firstwordscount)}}/$finalmainbodyfirstwords/isg;
		}
	}
	if ($entryreturn =~ m/{{entrymorebodyfirstwords (\d+)}}/i) {
		until ($entryreturn !~ m/{{entrymorebodyfirstwords (\d+)}}/isg) {
			$firstwordscount = $1;
			if ($thisentrymorebody eq "") {
				$entryreturn =~ s/{{entrymorebodyfirstwords ($firstwordscount)}}//isg;
			} else {
				$grabmorebodywords = $thisentrymorebody;
				if ($grabmorebodywords =~ m/{{link/i) {
					$grabmorebodywords =~ s/({{linkmo) (http|https|ftp)(:\/\/\S+?) (.+?)(\|)(.+?)(}})/$4/isg;
					$grabmorebodywords =~ s/({{link) (http|https|ftp)(:\/\/\S+?)(}})/$2$3/isg;
					$grabmorebodywords =~ s/({{link) (http|https|ftp)(:\/\/\S+?) (.+?)(}})/$4/isg;
				}
				if ($grabmorebodywords =~ m/{{email/i) {
					$grabmorebodywords =~ s/({{emailmo) (\S+\@\S+?) (.+?)(\|)(.+?)(}})/$3/isg;
					$grabmorebodywords =~ s/({{email) (\S+\@\S+?)(}})/$2/isg;
					$grabmorebodywords =~ s/({{email) (\S+\@\S+?) (.+?)(}})/$3/isg;
				}
				$grabmorebodywords =~ s/<([^>]|\n)*>/ /g;
				$grabmorebodywords =~ s/{{(.*?)}}/ /g;
				$grabmorebodywords =~ s/\n/ /g;
				$grabmorebodywords =~ s/\r/ /g;
				$grabmorebodywords =~ s/\|\*\|/ /g;
				$grabmorebodywords =~ s/^\s+//;
				$grabmorebodywords =~ s/\s+$//;
				$grabmorebodywords =~ s/\s{2,}/ /g;
				@grabmorebodywordslist = split (/ /, $grabmorebodywords);
				$countwordsfromhere = 0;
				(@finalmorebodywordslist, @finalmorebodywordslist = ());
				if ($firstwordscount < 1) { $firstwordscount = 1; }
				do {
					$finalmorebodywordslist[$countwordsfromhere] = $grabmorebodywordslist[$countwordsfromhere];
					$countwordsfromhere++;
				} until $countwordsfromhere eq $firstwordscount;
				$finalmorebodyfirstwords = join (" ", @finalmorebodywordslist);
				$finalmorebodyfirstwords =~ s/^\s+//;
				$finalmorebodyfirstwords =~ s/\s+$//;
				$finalmorebodyfirstwords =~ s/\s{2,}//g;
				if (substr($finalmorebodyfirstwords, -1) =~ /\W/) { chop($finalmorebodyfirstwords); }
				if (substr($finalmorebodyfirstwords, -1) eq / /) { chop($finalmorebodyfirstwords); }
				$entryreturn =~ s/{{entrymorebodyfirstwords ($firstwordscount)}}/$finalmorebodyfirstwords/isg;
			}
		}
	}
}

if (($entryreturn =~ m/link}}/i) || ($entryreturn =~ m/{{morepreface}}/i)) {
	$entryreturn =~ s/{{morepreface}}/$thisentrymorepreface/gi;
	$entryreturn =~ s/{{morelink}}/$thisentrymorelink/gi;
	$entryreturn =~ s/{{karmalink}}/$thisentrykarmalink/gi;
	$entryreturn =~ s/{{commentslink}}/$thisentrycommentslink/gi;
	$entryreturn =~ s/{{pagelink}}/$thisentrypagelink/gi;
	$entryreturn =~ s/{{pageindexlink}}/$thisentrypageindexlink/gi;
	$entryreturn =~ s/{{pagearchiveindexlink}}/$thisentrypagearchiveindexlink/gi;
	$entryreturn =~ s/{{pagearchivelogindexlink}}/$thisentrypagearchivelogindexlink/gi;
	$entryreturn =~ s/{{pagesmartindexlink}}/$thisentrypagesmartindexlink/gi;
	$entryreturn =~ s/{{commentspostlink}}/$thisentrycommentspostlink/gi;
	$entryreturn =~ s/{{authorsmartlink}}/$thisentryauthorsmartlink/gi;
}

if (($entryreturn =~ m/karma}}/i) || ($entryreturn =~ m/karmalink}}/i)) {
	$entryreturn =~ s/{{positivekarmalink}}/$thisentrypositivekarmalink/gi;
	$entryreturn =~ s/{{negativekarmalink}}/$thisentrynegativekarmalink/gi;
	$entryreturn =~ s/{{positivekarma}}/$thisentrypositivekarma/gi;
	$entryreturn =~ s/{{negativekarma}}/$thisentrynegativekarma/gi;
	$entryreturn =~ s/{{totalkarma}}/$thisentrytotalkarma/gi;
}

if ($entryreturn =~ m/{{entry/i) {
	$entryreturn =~ s/{{entrysubject}}/$thisentrysubject/gi;
	$entryreturn =~ s/{{entrynumber}}/$thisentrynumber/gi;
	$entryreturn =~ s/{{entrynumberpadded}}/$thisentrynumberpadded/gi;
}

if ($entryreturn =~ m/{{author/i) {
	$entryreturn =~ s/{{author}}/$thisentryauthor/gi;
	$entryreturn =~ s/{{authoremail}}/$thisentryauthoremail/gi;
	$entryreturn =~ s/{{authorhomepage}}/$thisentryauthorhomepage/gi;
	$entryreturn =~ s/{{authorentrycount}}/$thisentryauthorentrycount/gi;
}

if (($entryreturn =~ m/{{authoremail /i) || ($entryreturn =~ m/{{authorhomepage /i) || ($entryreturn =~ m/{{authorentrycount /i) || ($entryreturn =~ m/{{authoremaillink /i) || ($entryreturn =~ m/{{authorhomepagelink /i) || ($entryreturn =~ m/{{authorsmartlink /i)) {
	&gm_generateexternalauthorvariables;
}

if ($entryreturn =~ m/{{comments/i) {
	$entryreturn =~ s/{{commentstatussmart}}/$thisentrycommentstatussmart/gi;
	$entryreturn =~ s/{{commentstatussmartupper}}/$thisentrycommentstatussmartupper/gi;
	$entryreturn =~ s/{{commentstatussmartlower}}/$thisentrycommentstatussmartlower/gi;
	$entryreturn =~ s/{{commentsnumber}}/$thisentrycommentsnumber/gi;
}

if (($entryreturn =~ m/{{day/i) || ($entryreturn =~ m/{{month/i) || ($entryreturn =~ m/{{year/i) || ($entryreturn =~ m/{{hour/i) || ($entryreturn =~ m/{{minute/i) || ($entryreturn =~ m/{{second/i) || ($entryreturn =~ m/{{weekday/i) || ($entryreturn =~ m/{{militaryhour}}/i) || ($entryreturn =~ m/{{ampm/i) || ($entryreturn =~ m/{{timezone}}/i)) {
	$entryreturn =~ s/{{day}}/$thisentryday/gi;
	$entryreturn =~ s/{{month}}/$thisentrymonth/gi;
	$entryreturn =~ s/{{year}}/$thisentryyear/gi;
	$entryreturn =~ s/{{hour}}/$thisentryhour/gi;
	$entryreturn =~ s/{{minute}}/$thisentryminute/gi;
	$entryreturn =~ s/{{second}}/$thisentrysecond/gi;
	$entryreturn =~ s/{{dayday}}/$thisentrydayday/gi;
	$entryreturn =~ s/{{monthmonth}}/$thisentrymonthmonth/gi;
	$entryreturn =~ s/{{yearyear}}/$thisentryyearyear/gi;
	$entryreturn =~ s/{{hourhour}}/$thisentryhourhour/gi;
	$entryreturn =~ s/{{minuteminute}}/$thisentryminuteminute/gi;
	$entryreturn =~ s/{{secondsecond}}/$thisentrysecondsecond/gi;
	$entryreturn =~ s/{{weekday}}/$thisentryweekday/gi;
	$entryreturn =~ s/{{monthword}}/$thisentrymonthword/gi;
	$entryreturn =~ s/{{weekdayupper}}/$thisentryweekdayupper/gi;
	$entryreturn =~ s/{{monthwordupper}}/$thisentrymonthwordupper/gi;
	$entryreturn =~ s/{{weekdaylower}}/$thisentryweekdaylower/gi;
	$entryreturn =~ s/{{monthwordlower}}/$thisentrymonthwordlower/gi;
	$entryreturn =~ s/{{weekdayuppershort}}/$thisentryweekdayuppershort/gi;
	$entryreturn =~ s/{{monthworduppershort}}/$thisentrymonthworduppershort/gi;
	$entryreturn =~ s/{{weekdaylowershort}}/$thisentryweekdaylowershort/gi;
	$entryreturn =~ s/{{monthwordlowershort}}/$thisentrymonthwordlowershort/gi;
	$entryreturn =~ s/{{militaryhour}}/$thisentrymilitaryhour/gi;
	$entryreturn =~ s/{{ampm}}/$thisentryampm/gi;
	$entryreturn =~ s/{{ampmdot}}/$thisentryampmdot/gi;
	$entryreturn =~ s/{{ampmlower}}/$thisentryampmlower/gi;
	$entryreturn =~ s/{{ampmdotlower}}/$thisentryampmdotlower/gi;
	$entryreturn =~ s/{{timezone}}/$timezone/gi;
}

if (($entryreturn =~ m/{{weekbeginning/i) || ($entryreturn =~ m/{{weekending/i)) {
	$entryreturn =~ s/{{weekbeginningday}}/$thisentryweekbeginningday/gi;
	$entryreturn =~ s/{{weekbeginningdayday}}/$thisentryweekbeginningdayday/gi;
	$entryreturn =~ s/{{weekbeginningmonth}}/$thisentryweekbeginningmonth/gi;
	$entryreturn =~ s/{{weekbeginningmonthmonth}}/$thisentryweekbeginningmonthmonth/gi;
	$entryreturn =~ s/{{weekbeginningyear}}/$thisentryweekbeginningyear/gi;
	$entryreturn =~ s/{{weekbeginningyearyear}}/$thisentryweekbeginningyearyear/gi;
	$entryreturn =~ s/{{weekbeginningweekday}}/$thisentryweekbeginningweekday/gi;
	$entryreturn =~ s/{{weekbeginningmonthword}}/$thisentryweekbeginningmonthword/gi;
	$entryreturn =~ s/{{weekbeginningweekdayupper}}/$thisentryweekbeginningweekdayupper/gi;
	$entryreturn =~ s/{{weekbeginningmonthwordupper}}/$thisentryweekbeginningmonthwordupper/gi;
	$entryreturn =~ s/{{weekbeginningweekdaylower}}/$thisentryweekbeginningweekdaylower/gi;
	$entryreturn =~ s/{{weekbeginningmonthwordlower}}/$thisentryweekbeginningmonthwordlower/gi;
	$entryreturn =~ s/{{weekbeginningweekdayuppershort}}/$thisentryweekbeginningweekdayuppershort/gi;
	$entryreturn =~ s/{{weekbeginningmonthworduppershort}}/$thisentryweekbeginningmonthworduppershort/gi;
	$entryreturn =~ s/{{weekbeginningweekdaylowershort}}/$thisentryweekbeginningweekdaylowershort/gi;
	$entryreturn =~ s/{{weekbeginningmonthwordlowershort}}/$thisentryweekbeginningmonthwordlowershort/gi;
	$entryreturn =~ s/{{weekendingday}}/$thisentryweekendingday/gi;
	$entryreturn =~ s/{{weekendingdayday}}/$thisentryweekendingdayday/gi;
	$entryreturn =~ s/{{weekendingmonth}}/$thisentryweekendingmonth/gi;
	$entryreturn =~ s/{{weekendingmonthmonth}}/$thisentryweekendingmonthmonth/gi;
	$entryreturn =~ s/{{weekendingyear}}/$thisentryweekendingyear/gi;
	$entryreturn =~ s/{{weekendingyearyear}}/$thisentryweekendingyearyear/gi;
	$entryreturn =~ s/{{weekendingweekday}}/$thisentryweekendingweekday/gi;
	$entryreturn =~ s/{{weekendingmonthword}}/$thisentryweekendingmonthword/gi;
	$entryreturn =~ s/{{weekendingweekdayupper}}/$thisentryweekendingweekdayupper/gi;
	$entryreturn =~ s/{{weekendingmonthwordupper}}/$thisentryweekendingmonthwordupper/gi;
	$entryreturn =~ s/{{weekendingweekdaylower}}/$thisentryweekendingweekdaylower/gi;
	$entryreturn =~ s/{{weekendingmonthwordlower}}/$thisentryweekendingmonthwordlower/gi;
	$entryreturn =~ s/{{weekendingweekdayuppershort}}/$thisentryweekendingweekdayuppershort/gi;
	$entryreturn =~ s/{{weekendingmonthworduppershort}}/$thisentryweekendingmonthworduppershort/gi;
	$entryreturn =~ s/{{weekendingweekdaylowershort}}/$thisentryweekendingweekdaylowershort/gi;
	$entryreturn =~ s/{{weekendingmonthwordlowershort}}/$thisentryweekendingmonthwordlowershort/gi;
}

if ($entryreturn =~ m/{{link/i) {
	$entryreturn =~ s/({{linkmo) (http|https|ftp)(:\/\/\S+?) (.+?)(\|)(.+?)(}})/<A HREF="$2$3" onMouseOver="window.status='$6';return true" onMouseOut="window.status='';return true">$4<\/A>/isg;
	$entryreturn =~ s/({{link) (http|https|ftp)(:\/\/\S+?)(}})/<A HREF="$2$3">$2$3<\/A>/isg;
	$entryreturn =~ s/({{link) (http|https|ftp)(:\/\/\S+?) (.+?)(}})/<A HREF="$2$3">$4<\/A>/isg;
}

if ($entryreturn =~ m/{{email/i) {
	$entryreturn =~ s/({{emailmo) (\S+\@\S+?) (.+?)(\|)(.+?)(}})/<A HREF="mailto:$2" onMouseOver="window.status='$5';return true" onMouseOut="window.status='';return true">$3<\/A>/isg;
	$entryreturn =~ s/({{email) (\S+\@\S+?)(}})/<A HREF="mailto:$2">$2<\/A>/isg;
	$entryreturn =~ s/({{email) (\S+\@\S+?) (.+?)(}})/<A HREF="mailto:$2">$3<\/A>/isg;
}

if ($entryreturn =~ m/{{popup (\S+) (.+?) (\d+)x(\d+)}}/i) {
	until ($entryreturn !~ m/{{popup (\S+) (.+?) (\d+)x(\d+)}}/isg) {

		$popupfile = $1;
		$popuptitle = $2;
		$popupwidth = $3;
		$popupheight = $4;
		$popuphtmlfile = $1;
		$popuphtmlfile =~ s/\.(\S+)$//;
		$popuphtmlfile .= ".$entrysuffix";
		$popuppage = $gmpopuppagetemplate;
		$popupcode = $gmpopupcodetemplate;
		$popuppage =~ s/{{popupfile}}/$popupfile/gi;
		$popuppage =~ s/{{popuphtmlfile}}/$popuphtmlfile/gi;
		$popuppage =~ s/{{popuptitle}}/$popuptitle/gi;
		$popuppage =~ s/{{popupwidth}}/$popupwidth/gi;
		$popuppage =~ s/{{popupheight}}/$popupheight/gi;
		$popupcode =~ s/{{popupfile}}/$popupfile/gi;
		$popupcode =~ s/{{popuphtmlfile}}/$popuphtmlfile/gi;
		$popupcode =~ s/{{popuptitle}}/$popuptitle/gi;
		$popupcode =~ s/{{popupwidth}}/$popupwidth/gi;
		$popupcode =~ s/{{popupheight}}/$popupheight/gi;
		$popuppage =~ s/{{cgiwebpath}}/$cgiwebpath/gi;
		$popuppage =~ s/{{entrieswebpath}}/$EntriesWebPath/gi;
		$popuppage =~ s/{{logwebpath}}/$LogWebPath/gi;

		open (FUNNYFEETWAGS, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entry list file.  Please make sure that gm-entrylist.cgi is in the same directory as all your other Greymatter files and is CHMODed to 666; also, try running Diagnostics & Repair in the Configuration screen.");
		@loglistloglines = <FUNNYFEETWAGS>;
		close (FUNNYFEETWAGS);

		$foundpopupmatch = "no";

		foreach $thisloglistline (@loglistloglines) {
			chomp ($thisloglistline);
			($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
			if (($thisentrynumber eq $loglistnumber) && ($foundpopupmatch eq "no")) {
				&gm_getloglistvariables;
				$foundpopupmatch = "yes";
			}
		}

		$listsubsub = $popuppage;
		&entrylistsubsub;

		open (POPUPVIDEO, ">$EntriesPath/$popuphtmlfile") || &gm_dangermouse("Can't write to $EntriesPath/$popuphtmlfile.  Please make sure your entries/archives directory is correctly set and is CHMODed to 777; also, try running Diagnostics & Repair in the Configuration screen.");
		print POPUPVIDEO $listsubsub;
		close (POPUPVIDEO);

		$listsubsub = $popupcode;
		&entrylistsubsub;

		$entryreturn =~ s/{{popup $popupfile $popuptitle ($popupwidth)x($popupheight)}}/$listsubsub/isg;

	}
}

if (($entryreturn =~ m/{{previous/i) || ($entryreturn =~ m/{{next/i)) {

	open (FUNNYFEETSCRATCH, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entry list file.  Please make sure that gm-entrylist.cgi is in the same directory as all your other Greymatter files and is CHMODed to 666; also, try running Diagnostics & Repair in the Configuration screen.");
	@checkingloglistloglines = <FUNNYFEETSCRATCH>;
	close (FUNNYFEETSCRATCH);

	$entryreturn =~ s/{{previousmore/{{moreprevious/isg;
	$entryreturn =~ s/{{nextmore/{{morenext/isg;

	if ($thisentrynumber ne "1") {
		$thispreviousentrynumber = $thisentrynumber - 1;
		$foundregular = "no";
		$foundmore = "no";
		$foundboth = "no";
		do {
			
			foreach $thisloglistline (@checkingloglistloglines) {
				chomp ($thisloglistline);
				($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
				if (($thispreviousentrynumber eq $loglistnumber) && ($loglistnumber < $thisentrynumber) && ($foundregular eq "no") && ($loglistopenstatus ne "C")) {
					$entryreturn =~ s/{{previouslink}}/$gmpreviouslinktemplate/isg;
					&gm_getloglistvariables;
					$listsubsub = $entryreturn;
					$listsubsub =~ s/{{previous/{{/isg;
					&entrylistsubsub;
					$entryreturn = $listsubsub;
					$foundregular = "yes";
				}
				if (($thispreviousentrynumber eq $loglistnumber) && ($loglistmorestatus eq "Y") && ($loglistnumber < $thisentrynumber) && ($foundmore eq "no") && ($loglistopenstatus ne "C")) {
					$entryreturn =~ s/{{morepreviouslink}}/$gmpreviousmorelinktemplate/isg;
					$entryreturn =~ s/{{previousmore/{{moreprevious/isg;
					&gm_getloglistvariables;
					$listsubsub = $entryreturn;
					$listsubsub =~ s/{{moreprevious/{{/isg;
					&entrylistsubsub;
					$entryreturn = $listsubsub;
					$foundmore = "yes";
				}
			}

			if (($foundregular eq "yes") && ($foundmore eq "yes")) { $foundboth = "yes"; }
			if ($thispreviousentrynumber eq "1") { $foundboth = "yes"; }
			$thispreviousentrynumber--;

		} until $foundboth eq "yes";
	}

	if ($thisentrynumber ne $newentrynumber) {
		@checkingloglistloglines = reverse @checkingloglistloglines;
		$thisnextentrynumber = $thisentrynumber + 1;
		$foundregular = "no";
		$foundmore = "no";
		$foundboth = "no";
		do {
			
			foreach $thisloglistline (@checkingloglistloglines) {
				chomp ($thisloglistline);
				($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
				if (($thisnextentrynumber eq $loglistnumber) && ($loglistnumber > $thisentrynumber) && ($foundregular eq "no") && ($loglistopenstatus ne "C")) {
					$entryreturn =~ s/{{nextlink}}/$gmnextlinktemplate/isg;
					&gm_getloglistvariables;
					$listsubsub = $entryreturn;
					$listsubsub =~ s/{{next/{{/isg;
					&entrylistsubsub;
					$entryreturn = $listsubsub;
					$foundregular = "yes";
				}
				if (($thisnextentrynumber eq $loglistnumber) && ($loglistmorestatus eq "Y") && ($loglistnumber > $thisentrynumber) && ($foundmore eq "no") && ($loglistopenstatus ne "C")) {
					$entryreturn =~ s/{{morenextlink}}/$gmnextmorelinktemplate/isg;
					$entryreturn =~ s/{{nextmore/{{morenext/isg;
					&gm_getloglistvariables;
					$listsubsub = $entryreturn;
					$listsubsub =~ s/{{morenext/{{/isg;
					&entrylistsubsub;
					$entryreturn = $listsubsub;
					$foundmore = "yes";
				}
			}

			if (($foundregular eq "yes") && ($foundmore eq "yes")) { $foundboth = "yes"; }
			if ($thisnextentrynumber eq $newentrynumber) { $foundboth = "yes"; }
			$thisnextentrynumber++;

		} until $foundboth eq "yes";
	}

	$entryreturn =~ s/{{previouspagelink}}/$thisentrypagesmartindexlink/isg;
	$entryreturn =~ s/{{nextpagelink}}/$thisentrypagesmartindexlink/isg;
	$entryreturn =~ s/{{previousmorepagelink}}/$thisentrypagesmartindexlink/isg;
	$entryreturn =~ s/{{nextmorepagelink}}/$thisentrypagesmartindexlink/isg;
	$entryreturn =~ s/{{morepreviouspagelink}}/$thisentrypagesmartindexlink/isg;
	$entryreturn =~ s/{{morenextpagelink}}/$thisentrypagesmartindexlink/isg;
	$entryreturn =~ s/{{previouslink}}//isg;
	$entryreturn =~ s/{{nextlink}}//isg;

	if (($entryreturn =~ m/{{previous/i) || ($entryreturn =~ m/{{next/i)) {
		foreach $thisloglistline (@checkingloglistloglines) {
			chomp ($thisloglistline);
			($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
			if ($loglistnumber eq $thisentrynumber) {
				&gm_getloglistvariables;
				$listsubsub = $entryreturn;
				$listsubsub =~ s/{{previous/{{/isg;
				$listsubsub =~ s/{{next/{{/isg;
				&entrylistsubsub;
				$entryreturn = $listsubsub;
			}
		}
	}

	$entryreturn =~ s/{{morepagelink}}/$thisentrypagesmartindexlink/isg;

}


if ($entryreturn =~ m/window.status='(.*?)';/i) {
	$entryreturn =~ s/\(/GMLEFTPARENTHESES/g;
	$entryreturn =~ s/\)/GMRIGHTPARENTHESES/g;
	$entryreturn =~ s/\?/GMQUESTIONMARK/g;
	$entryreturn =~ s/\+/GMPLUS/g;
	until ($entryreturn !~ m/window.status='(.*?)';/ig) {
		$windowstatusorigstring = $1;
		$windowstatusmiddlenew = $1;
		$windowstatusmiddlenew =~ s#'#\\'#isg;
		$windowstatusmiddlenew =~ s#"#\\'#isg;
		$entryreturn =~ s/window.status='$windowstatusorigstring';/WSPLACEHOLDER='$windowstatusmiddlenew';/isg;
	}
	$entryreturn =~ s/WSPLACEHOLDER=/window.status=/isg;
	$entryreturn =~ s/GMLEFTPARENTHESES/\(/g;
	$entryreturn =~ s/GMRIGHTPARENTHESES/\)/g;
	$entryreturn =~ s/GMQUESTIONMARK/\?/g;
	$entryreturn =~ s/GMPLUS/\+/g;
}

if ($entryreturn =~ m/{{randomnumber (\d+)-(\d+)}}/i) {
	until ($entryreturn !~ m/{{randomnumber (\d+)-(\d+)}}/isg) {
		$minrand = $1;
		$maxrand = $2;
		$maxtemprand = $maxrand - $minrand;
		$maxtemprand++;
		$randresult = int(rand $maxtemprand) + $minrand;
		$entryreturn =~ s/{{randomnumber ($minrand)-($maxrand)}}/$randresult/i;
	}
}

if (($entryreturn =~ m/{{cgiwebpath}}/i) || ($entryreturn =~ m/{{entrieswebpath}}/i) || ($entryreturn =~ m/{{logwebpath}}/i)) {
	$entryreturn =~ s/{{cgiwebpath}}/$cgiwebpath/gi;
	$entryreturn =~ s/{{entrieswebpath}}/$EntriesWebPath/gi;
	$entryreturn =~ s/{{logwebpath}}/$LogWebPath/gi;
}

if (($entryreturn =~ m/{{gmversion}}/i) || ($entryreturn =~ m/{{gmicon}}/i)) {
	$entryreturn =~ s/{{gmversion}}/$gmversion/gi;
	$entryreturn =~ s/{{gmicon}}/<A HREF="http:\/\/noahgrey.com\/greysoft\/" TARGET="_top"><IMG BORDER=0 SRC="$LogWebPath\/gm-icon.gif" ALT="Powered By Greymatter"><\/A>/gi;
}

}

# ----------------------------
# generate the main index file
# ----------------------------

sub gm_generatemainindex {

&gm_readconfig;
&gm_readcounter;
&gm_readtemplates;

$indexlogbody = "";
$indexentrycounter = $newentrynumber;
$indexcurrentdatemarker = "erewhon";
$indexcurrentdatescounted = 0;

if ($newstayattopnumber ne "0") {
	&gm_getentryvariables($newstayattopnumber);
	if ($thisentryopenstatus eq "open") {
		&gm_formatentry($gmstayattoptemplate);
		$indexlogbody .= $entryreturn;
	}
}

do {

&gm_getentryvariables($indexentrycounter);

$datemark = "$thisentrymonth $thisentryday $thisentryyearyear";

if (($datemark ne $indexcurrentdatemarker) && ($thisentryopenstatus eq "open") && ($indexentrycounter ne $newstayattopnumber)) {
	$indexcurrentdatescounted++;
	if ($gmdatetemplate ne "") {
		$currentdatehead = $gmdatetemplate;
		$currentdatehead =~ s/{{day}}/$thisentryday/gi;
		$currentdatehead =~ s/{{dayday}}/$thisentrydayday/gi;
		$currentdatehead =~ s/{{year}}/$thisentryyear/gi;
		$currentdatehead =~ s/{{yearyear}}/$thisentryyearyear/gi;
		$currentdatehead =~ s/{{month}}/$thisentrymonth/gi;
		$currentdatehead =~ s/{{monthmonth}}/$thisentrymonthmonth/gi;
		$currentdatehead =~ s/{{weekday}}/$thisentryweekday/gi;
		$currentdatehead =~ s/{{monthword}}/$thisentrymonthword/gi;
		$currentdatehead =~ s/{{weekdayupper}}/$thisentryweekdayupper/gi;
		$currentdatehead =~ s/{{monthwordupper}}/$thisentrymonthwordupper/gi;
		$currentdatehead =~ s/{{weekdaylower}}/$thisentryweekdaylower/gi;
		$currentdatehead =~ s/{{monthwordlower}}/$thisentrymonthwordlower/gi;
		$currentdatehead =~ s/{{weekdayuppershort}}/$thisentryweekdayuppershort/gi;
		$currentdatehead =~ s/{{monthworduppershort}}/$thisentrymonthworduppershort/gi;
		$currentdatehead =~ s/{{weekdaylowershort}}/$thisentryweekdaylowershort/gi;
		$currentdatehead =~ s/{{monthwordlowershort}}/$thisentrymonthwordlowershort/gi;
		unless ($indexcurrentdatescounted > $indexdays) { $indexlogbody .= $currentdatehead; }
	}
	$indexcurrentdatemarker = "$thisentrymonth $thisentryday $thisentryyearyear";
} else {
	if (($indexentrycounter ne $newstayattopnumber) && ($thisentryopenstatus eq "open") && ($indexcurrentdatescounted <= $indexdays) && ($gmentryseparatortemplate ne "")) {
		$indexlogbody .= $gmentryseparatortemplate;
	}
}

if (($indexentrycounter ne $newstayattopnumber) && ($thisentryopenstatus eq "open") && ($indexcurrentdatescounted <= $indexdays)) {
	if ($thisentrymorebody ne "") {
		&gm_formatentry($gmmoreentrytemplate);
	} else {
		&gm_formatentry($gmentrytemplate);
	}
	$indexlogbody .= $entryreturn;
}

$indexentrycounter--;

if ($indexentrycounter eq "0") {
	if ($indexcurrentdatescounted > $indexdays) { $indexentrycounter++; }
	$indexcurrentdatescounted = $indexdays + 1;
}

if (($newstayattopnumber eq "1") && ($newentrynumber eq "1")) { $indexcurrentdatescounted = $indexdays + 1; }

if ($indexcurrentdatescounted > $indexdays) {
	if ($indexentrycounter < 0) { $indexentrycounter = 0; }
	unless ($indexentrycounter eq "0") { $indexentrycounter = $thisentrynumber; }
}

} until $indexcurrentdatescounted > $indexdays;

$newindexfile = $gmindextemplate;
$newindexfile =~ s/{{logbody}}/$indexlogbody/gi;

&gm_getentryvariables($newentrynumber);
&gm_formatentry($newindexfile);

open (THISFILECLAWS, ">$LogPath/$indexfilename") || &gm_dangermouse("Can't write to $LogPath/$indexfilename.  Please make sure your paths are configured correctly and that $indexfilename is CHMODed to 666; also try running Diagnostics & Repair from the Configuration screen.");
print THISFILECLAWS $entryreturn;
close (THISFILECLAWS);

$newarchivenumber = $indexentrycounter;

&gm_writecounter;

}

# ---------------------
# generate archive file
# ---------------------

sub gm_generatearchive {

my $getstartnumber = shift;

$startnumber = $getstartnumber;

&gm_readconfig;
&gm_readcounter;
&gm_readtemplates;

$indexarchivebody = "";
$indexentrycounter = $startnumber;
$indexcurrentdatemarker = "erewhon";
$indexcurrentdatescounted = 0;
&gm_getentryvariables($startnumber);
$indexcurrentmonthcounter = $thisentrymonth;
$indexcurrentweekcounter = "$thisentryweekbeginningdayday$thisentryweekendingdayday";

do {

&gm_getentryvariables($indexentrycounter);

$thisentryweek = "$thisentryweekbeginningdayday$thisentryweekendingdayday";

if (($generateentrypages eq "yes") && ($indexentrycounter eq $newarchivenumber)) {
	if ($thisentryopenstatus eq "open") {
		&gm_formatentry($gmarchiveentrypagetemplate);
		open (THISFILE, ">$EntriesPath/$thisentrynumberpadded.$entrysuffix") || &gm_dangermouse("Can't write to $EntriesPath/$thisentrynumberpadded.$entrysuffix.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
		print THISFILE $entryreturn;
		close (THISFILE);
	} else {
		unlink ("$EntriesPath/$thisentrynumberpadded.$entrysuffix");
	}
}

$datemark = "$thisentrymonth $thisentryday $thisentryyearyear";

if (($datemark ne $indexcurrentdatemarker) && ($thisentryopenstatus eq "open") && ($indexentrycounter ne $newstayattopnumber)) {
	$indexcurrentdatescounted++;
	if ($gmdatearchivetemplate ne "") {
		$currentdatehead = $gmdatearchivetemplate;
		$currentdatehead =~ s/{{day}}/$thisentryday/gi;
		$currentdatehead =~ s/{{dayday}}/$thisentrydayday/gi;
		$currentdatehead =~ s/{{year}}/$thisentryyear/gi;
		$currentdatehead =~ s/{{yearyear}}/$thisentryyearyear/gi;
		$currentdatehead =~ s/{{month}}/$thisentrymonth/gi;
		$currentdatehead =~ s/{{monthmonth}}/$thisentrymonthmonth/gi;
		$currentdatehead =~ s/{{weekday}}/$thisentryweekday/gi;
		$currentdatehead =~ s/{{monthword}}/$thisentrymonthword/gi;
		$currentdatehead =~ s/{{weekdayupper}}/$thisentryweekdayupper/gi;
		$currentdatehead =~ s/{{monthwordupper}}/$thisentrymonthwordupper/gi;
		$currentdatehead =~ s/{{weekdaylower}}/$thisentryweekdaylower/gi;
		$currentdatehead =~ s/{{monthwordlower}}/$thisentrymonthwordlower/gi;
		$currentdatehead =~ s/{{weekdayuppershort}}/$thisentryweekdayuppershort/gi;
		$currentdatehead =~ s/{{monthworduppershort}}/$thisentrymonthworduppershort/gi;
		$currentdatehead =~ s/{{weekdaylowershort}}/$thisentryweekdaylowershort/gi;
		$currentdatehead =~ s/{{monthwordlowershort}}/$thisentrymonthwordlowershort/gi;
		if ($archiveformat eq "week") {
			unless ($thisentryweek ne $indexcurrentweekcounter) { $indexarchivebody .= $currentdatehead; }
		} else {
			unless ($thisentrymonth ne $indexcurrentmonthcounter) { $indexarchivebody .= $currentdatehead; }
		}
	}
	$indexcurrentdatemarker = "$thisentrymonth $thisentryday $thisentryyearyear";
} else {
	if ($archiveformat eq "week") {
		if (($thisentryopenstatus eq "open") && ($thisentryweek eq $indexcurrentweekcounter) && ($gmarchiveentryseparatortemplate ne "")) {
			$indexarchivebody .= $gmarchiveentryseparatortemplate;
		}
	} else {
		if (($thisentryopenstatus eq "open") && ($thisentrymonth eq $indexcurrentmonthcounter) && ($gmarchiveentryseparatortemplate ne "")) {
			$indexarchivebody .= $gmarchiveentryseparatortemplate;
		}
	}
}

if ($archiveformat eq "week") {
	if (($thisentryopenstatus eq "open") && ($thisentryweek eq $indexcurrentweekcounter)) {
		if ($thisentrymorebody ne "") {
			&gm_formatentry($gmmorearchiveentrytemplate);
		} else {
			&gm_formatentry($gmarchiveentrytemplate);
		}
		$indexarchivebody .= $entryreturn;
	}
} else {
	if (($thisentryopenstatus eq "open") && ($thisentrymonth eq $indexcurrentmonthcounter)) {
		if ($thisentrymorebody ne "") {
			&gm_formatentry($gmmorearchiveentrytemplate);
		} else {
			&gm_formatentry($gmarchiveentrytemplate);
		}
		$indexarchivebody .= $entryreturn;
	}
}

$indexentrycounter--;

if ($archiveformat eq "week") {
	if ($thisentryweek ne $indexcurrentweekcounter) {
		$indexcurrentmonthcounter = "finis";
	} else {
		$indexcurrentmonthcounter = $thisentrymonth;
	}
}

if ($indexentrycounter eq "0") { $indexcurrentmonthcounter = "finis"; }

} until $thisentrymonth ne $indexcurrentmonthcounter;

$stoppednumber = $thisentrynumber;

&gm_getentryvariables($startnumber);

$newarchivefile = $gmarchiveindextemplate;
$newarchivefile =~ s/{{year}}/$thisentryyear/gi;
$newarchivefile =~ s/{{yearyear}}/$thisentryyearyear/gi;
$newarchivefile =~ s/{{month}}/$thisentrymonth/gi;
$newarchivefile =~ s/{{monthmonth}}/$thisentrymonthmonth/gi;
$newarchivefile =~ s/{{monthword}}/$thisentrymonthword/gi;
$newarchivefile =~ s/{{monthwordupper}}/$thisentrymonthwordupper/gi;
$newarchivefile =~ s/{{monthwordlower}}/$thisentrymonthwordlower/gi;
$newarchivefile =~ s/{{monthworduppershort}}/$thisentrymonthworduppershort/gi;
$newarchivefile =~ s/{{monthwordlowershort}}/$thisentrymonthwordlowershort/gi;
$newarchivefile =~ s/{{archivebody}}/$indexarchivebody/gi;
$newarchivefile =~ s/{{logbody}}/$indexarchivebody/gi;

&gm_formatentry($newarchivefile);

if ($archiveformat eq "week") {
	$usethisarchivefilename = "$EntriesPath/archive-$thisentryweekbeginningmonthmonth$thisentryweekbeginningdayday$thisentryweekbeginningyearyear-$thisentryweekendingmonthmonth$thisentryweekendingdayday$thisentryweekendingyearyear\.$logarchivesuffix";
} else {
	$usethisarchivefilename = "$EntriesPath/archive-$thisentrymonthmonth$thisentryyearyear\.$logarchivesuffix";
}

open (THISFILEPAWS, ">$usethisarchivefilename") || &gm_dangermouse("Can't write to $usethisarchivefilename.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
print THISFILEPAWS $entryreturn;
close (THISFILEPAWS);

chmod (0666, "$usethisarchivefilename");

}

# -----------------------
# rebuild connected files
# -----------------------

sub gm_rebuildconnectedfiles {

@connectedfilelist = split (/\|\*\|/, $otherfilelist);

@variabledatabase = ("{{header}}", "{{footer}}", "{{sidebar}}", "{{log", "{{calendar", "{{comment", "{{entry", "link}}", "karma}}", "{{author", "{{day", "{{month", "{{year", "{{hour", "{{minute", "{{second", "{{weekday", "{{militaryhour}}", "{{ampm", "{{timezone}}", "{{link", "{{email", "{{previous", "{{next", "webpath}}", "{{gm");

&gm_getentryvariables($newentrynumber);

$connectedfilesdone = "no";
$connectstartfromhere = $IN{'connectednumber'};
if ($connectstartfromhere eq "") { $connectstartfromhere = 0; }
$connectendhere = $connectstartfromhere + 19;
if (($connectendhere > $#connectedfilelist) || ($connectendhere eq $#connectedfilelist)) {
	$connectendhere = $#connectedfilelist;
	$connectedfilesdone = "yes";
}
$IN{'connectednumber'} = $connectendhere + 1;

$connectcounter = 0;

foreach $usethisfilename (@connectedfilelist) {
unless (($connectcounter < $connectstartfromhere) || ($connectcounter > $connectendhere)) {

	$usethisfilenamestripped = $usethisfilename;
	$usethisfilenamestripped =~ s/\//BACKSLASH/g;
	$usethisfilenamestripped =~ s/\W//g;
	$usethisfilenamestripped =~ s/BACKSLASH/-/g;

	$thereisapattern = "no";

	open (OTHERORIGFILE, "$usethisfilename") || &gm_dangermouse("Can't open $usethisfilename.  Please make sure that this file exists and is CHMODed to 666, or else remove it from your list of connected files in configuration.");
	@otherorigfilelines = <OTHERORIGFILE>;
	close (OTHERORIGFILE);

	unless (!(open(CHECKTHISFILE,"$EntriesPath/$usethisfilenamestripped.cgi"))) {
		open (OTHERPATTERNFILE, "$EntriesPath/$usethisfilenamestripped.cgi") || &gm_dangermouse("Can't open $EntriesPath/$usethisfilenamestripped.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
		@otherpatternfilelines = <OTHERPATTERNFILE>;
		close (OTHERPATTERNFILE);
		$thereisapattern = "yes";
	}
	close(CHECKTHISFILE);

	$gmcounter = 0;

	foreach (@otherorigfilelines) {
		chomp ($otherorigfilelines[$gmcounter]);
		$gmcounter++;
	}

	$otherorigfilebody = join ("|*|", @otherorigfilelines);

	foreach $thisvariablecheck (@variabledatabase) {
		if ($otherorigfilebody =~ m/$thisvariablecheck/i) { $thereisapattern = "no"; }
	}

	unless ($thereisapattern eq "no") {
		$gmcounter = 0;
		foreach (@otherpatternfilelines) {
			chomp ($otherpatternfilelines[$gmcounter]);
			$gmcounter++;
		}
		$otherpatternfilebody = join ("|*|", @otherpatternfilelines);
		$otherfilebody = $otherpatternfilebody;
	} else {
		$otherfilebody = $otherorigfilebody;
	}

	$newfilebodypattern = $otherfilebody;

	&gm_formatentry($otherfilebody);

	$entryreturn =~ s/\|\*\|/\n/g;
	$newfilebodypattern =~ s/\|\*\|/\n/g;

	chmod (0666, "$usethisfilename");

	open (OTHERFILEONE, ">$usethisfilename") || &gm_dangermouse("Can't write to $usethisfilename.  Please make sure that this file exists and is CHMODed to 666, or else remove it from your list of connected files in configuration.");
	print OTHERFILEONE $entryreturn;
	close (OTHERFILEONE);

	open (OTHERFILETWO, ">$EntriesPath/$usethisfilenamestripped.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$usethisfilenamestripped.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
	print OTHERFILETWO $newfilebodypattern;
	close (OTHERFILETWO);

	chmod (0666, "$EntriesPath/$usethisfilenamestripped.cgi");

}
$connectcounter++;
}

}

# -------------------------
# generate log archive list
# -------------------------

sub gm_generatearchiveloglist {

&gm_readcounter;

open (FUNNYFEETMIDNIGHT, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entry list file.  Please make sure that gm-entrylist.cgi is in the same directory as all your other Greymatter files and is CHMODed to 666; also, try running Diagnostics & Repair in the Configuration screen.");
@loglistloglines = <FUNNYFEETMIDNIGHT>;
close (FUNNYFEETMIDNIGHT);

$listcountmonthyear = "begin";
$listcountweek = "begin";

$logarchivelistfinal = "";

foreach $loglistline (@loglistloglines) {

	chomp ($loglistline);
	($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $loglistline);
	&gm_getloglistvariables;

	unless ($loglistopenstatus eq "C") {

		$thisloglistmonthyear = "$loglistmonthmonth $loglistyearyear";
		$thisloglistweek = "$loglistweekbeginningdayday$loglistweekendingdayday";

		if ($archiveformat eq "week") {
			if ($thisloglistweek ne $listcountweek) {
				$listsubsub = $gmlogarchiveslinkweeklytemplate;
				&entrylistsubsub;
				$listsubsub .= "|*|";
				$logarchivelistfinal .= $listsubsub;
				$listcountweek = $thisloglistweek;
			}
		} else {
			if ($thisloglistmonthyear ne $listcountmonthyear) {
				$listsubsub = $gmlogarchiveslinktemplate;
				&entrylistsubsub;
				$listsubsub .= "|*|";
				$logarchivelistfinal .= $listsubsub;
				$listcountmonthyear = $thisloglistmonthyear;
			}
		}

	}

}

@loglistfinalcollection = split (/\|\*\|/, $logarchivelistfinal);

if ($entrylistsortorder eq "descending") { @loglistfinalcollection = reverse @loglistfinalcollection; }

$logarchivelistfinal = join ("$gmlogarchiveslinkseparatortemplate", @loglistfinalcollection);

}

# -----------------------
# generate log entry list
# -----------------------

sub gm_generateentryloglist {

$logshortentrylistfinal = "";
$logmoreentrylistfinal = "";
$logentrylistfinal = "";
$logshortentrylistmonthfinal = "";
$logshortentrylistdayfinal = "";
$logshortentrylistyearfinal = "";
$logmoreentrylistmonthfinal = "";
$logmoreentrylistdayfinal = "";
$logmoreentrylistyearfinal = "";
$logentrylistmonthfinal = "";
$logentrylistdayfinal = "";
$logentrylistyearfinal = "";
$logshortentrylistnumberfinal = "";
$logmoreentrylistnumberfinal = "";
$logentrylistnumberfinal = "";
$logshortentrylistfirsthalffinal = "";
$logshortentrylistsecondhalffinal = "";
$logmoreentrylistfirsthalffinal = "";
$logmoreentrylistsecondhalffinal = "";
$logentrylistfirsthalffinal = "";
$logentrylistsecondhalffinal = "";

open (FUNNYFEETSPOT, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entry list file.  Please make sure that gm-entrylist.cgi is in the same directory as all your other Greymatter files and is CHMODed to 666; also, try running Diagnostics & Repair in the Configuration screen.");
@loglistloglines = <FUNNYFEETSPOT>;
close (FUNNYFEETSPOT);

if ($entrylistsortorder eq "descending") { @loglistloglines = reverse @loglistloglines; }

($toploglistnumber, $toploglistauthor, $toploglistsubject, $toploglistdate, $toploglisttimeampm, $toploglistopenstatus, $toploglistmorestatus) = split (/\|/, $loglistloglines[0]);
($toploglistmonthmonth, $toploglistdayday, $toploglistyear) = split (/\//, $toploglistdate);

$shortentrycounter = 0;
$moreentrycounter = 0;
$allentrycounter = 0;

$shorttotalentrycounter = 0;
$moretotalentrycounter = 0;
$alltotalentrycounter = 0;

foreach $loglistcounterline (@loglistloglines) {
	chomp ($loglistcounterline);
	($loglistcounternumber, $loglistcounterauthor, $loglistcountersubject, $loglistcounterdate, $loglistcountertimeampm, $loglistcounteropenstatus, $loglistcountermorestatus) = split (/\|/, $loglistcounterline);
	unless ($loglistcounteropenstatus eq "C") {
		$alltotalentrycounter++;
		if ($loglistcountermorestatus eq "Y") { $moretotalentrycounter++; } else { $shorttotalentrycounter++; }
	}
}

$shorttotalentryhalfcounter = sprintf("%.0f", ($shorttotalentrycounter / 2));
$moretotalentryhalfcounter = sprintf("%.0f", ($moretotalentrycounter / 2));
$alltotalentryhalfcounter = sprintf("%.0f", ($alltotalentrycounter / 2));

$listdaymarker = "tommy";
$listmonthmarker = "tommy";
$listyearmarker = "tommy";

foreach $loglistline (@loglistloglines) {

	chomp ($loglistline);
	($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $loglistline);

	unless ($loglistopenstatus eq "C") {

		&gm_getloglistvariables;

		$usethismorelinktemplate = $gmmoreentrypagelinktemplate;
		$usethislinktemplate = $gmentrypagelinktemplate;

		if (($gmentrypagelinkdayseparatortemplate ne "") && ($listdaymarker ne $loglistday)) {
			$usethismorelinktemplate = "$gmentrypagelinkdayseparatortemplate|*|$usethismorelinktemplate";
			$usethislinktemplate = "$gmentrypagelinkdayseparatortemplate|*|$usethislinktemplate";
		}

		if (($gmentrypagelinkmonthseparatortemplate ne "") && ($listmonthmarker ne $loglistmonth)) {
			$usethismorelinktemplate = "$gmentrypagelinkmonthseparatortemplate|*|$usethismorelinktemplate";
			$usethislinktemplate = "$gmentrypagelinkmonthseparatortemplate|*|$usethislinktemplate";
		}

		if (($gmentrypagelinkyearseparatortemplate ne "") && ($listyearmarker ne $loglistyear)) {
			$usethismorelinktemplate = "$gmentrypagelinkyearseparatortemplate|*|$usethismorelinktemplate";
			$usethislinktemplate = "$gmentrypagelinkyearseparatortemplate|*|$usethislinktemplate";
		}

		if ($loglistmorestatus eq "Y") {
			$moreentrycounter++;
			$listsubsub = $usethismorelinktemplate;
			&entrylistsubsub;
			$listsubsub .= "|*|";
			$logmoreentrylistfinal .= $listsubsub;
			if ($loglistmonthmonth eq $toploglistmonthmonth) { $logmoreentrylistmonthfinal .= $listsubsub; }
			if ($loglistdayday eq $toploglistdayday) { $logmoreentrylistdayfinal .= $listsubsub; }
			if ($loglistyear eq $toploglistyear) { $logmoreentrylistyearfinal .= $listsubsub; }
			unless ($moreentrycounter > $entrylistcountnumber) { $logmoreentrylistnumberfinal .= $listsubsub; }
			if ($moreentrycounter <= $moretotalentryhalfcounter) {
				$logmoreentrylistfirsthalffinal .= $listsubsub;
			} else {
				$logmoreentrylistsecondhalffinal .= $listsubsub;
			}
		} else {
			$shortentrycounter++;
			$listsubsub = $usethislinktemplate;
			&entrylistsubsub;
			$listsubsub .= "|*|";
			$logshortentrylistfinal .= $listsubsub;
			if ($loglistmonthmonth eq $toploglistmonthmonth) { $logshortentrylistmonthfinal .= $listsubsub; }
			if ($loglistdayday eq $toploglistdayday) { $logshortentrylistdayfinal .= $listsubsub; }
			if ($loglistyear eq $toploglistyear) { $logshortentrylistyearfinal .= $listsubsub; }
			unless ($shortentrycounter > $entrylistcountnumber) { $logshortentrylistnumberfinal .= $listsubsub; }
			if ($shortentrycounter <= $shorttotalentryhalfcounter) {
				$logshortentrylistfirsthalffinal .= $listsubsub;
			} else {
				$logshortentrylistsecondhalffinal .= $listsubsub;
			}
		}

		$allentrycounter++;
		$logentrylistfinal .= $listsubsub;
		if ($loglistmonthmonth eq $toploglistmonthmonth) { $logentrylistmonthfinal .= $listsubsub; }
		if ($loglistdayday eq $toploglistdayday) { $logentrylistdayfinal .= $listsubsub; }
		if ($loglistyear eq $toploglistyear) { $logentrylistyearfinal .= $listsubsub; }
		unless ($allentrycounter > $entrylistcountnumber) { $logentrylistnumberfinal .= $listsubsub; }
		if ($allentrycounter <= $alltotalentryhalfcounter) {
			$logentrylistfirsthalffinal .= $listsubsub;
		} else {
			$logentrylistsecondhalffinal .= $listsubsub;
		}

		$listdaymarker = $loglistday;
		$listmonthmarker = $loglistmonth;
		$listyearmarker = $loglistyear;

	}

}

@logshortentrylistfinalcollection = split (/\|\*\|/, $logshortentrylistfinal);
@logmoreentrylistfinalcollection = split (/\|\*\|/, $logmoreentrylistfinal);
@logentrylistfinalcollection = split (/\|\*\|/, $logentrylistfinal);
@logshortentrylistmonthfinalcollection = split (/\|\*\|/, $logshortentrylistmonthfinal);
@logshortentrylistdayfinalcollection = split (/\|\*\|/, $logshortentrylistdayfinal);
@logshortentrylistyearfinalcollection = split (/\|\*\|/, $logshortentrylistyearfinal);
@logmoreentrylistmonthfinalcollection = split (/\|\*\|/, $logmoreentrylistmonthfinal);
@logmoreentrylistdayfinalcollection = split (/\|\*\|/, $logmoreentrylistdayfinal);
@logmoreentrylistyearfinalcollection = split (/\|\*\|/, $logmoreentrylistyearfinal);
@logentrylistmonthfinalcollection = split (/\|\*\|/, $logentrylistmonthfinal);
@logentrylistdayfinalcollection = split (/\|\*\|/, $logentrylistdayfinal);
@logentrylistyearfinalcollection = split (/\|\*\|/, $logentrylistyearfinal);
@logshortentrylistnumberfinalcollection = split (/\|\*\|/, $logshortentrylistnumberfinal);
@logmoreentrylistnumberfinalcollection = split (/\|\*\|/, $logmoreentrylistnumberfinal);
@logentrylistnumberfinalcollection = split (/\|\*\|/, $logentrylistnumberfinal);
@logshortentrylistfirsthalffinalcollection = split (/\|\*\|/, $logshortentrylistfirsthalffinal);
@logshortentrylistsecondhalffinalcollection = split (/\|\*\|/, $logshortentrylistsecondhalffinal);
@logmoreentrylistfirsthalffinalcollection = split (/\|\*\|/, $logmoreentrylistfirsthalffinal);
@logmoreentrylistsecondhalffinalcollection = split (/\|\*\|/, $logmoreentrylistsecondhalffinal);
@logentrylistfirsthalffinalcollection = split (/\|\*\|/, $logentrylistfirsthalffinal);
@logentrylistsecondhalffinalcollection = split (/\|\*\|/, $logentrylistsecondhalffinal);

$logshortentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logshortentrylistfinalcollection);
$logmoreentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logmoreentrylistfinalcollection);
$logentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logentrylistfinalcollection);
$logshortentrylistmonthfinal = join ("$gmentrypagelinkseparatortemplate", @logshortentrylistmonthfinalcollection);
$logshortentrylistdayfinal = join ("$gmentrypagelinkseparatortemplate", @logshortentrylistdayfinalcollection);
$logshortentrylistyearfinal = join ("$gmentrypagelinkseparatortemplate", @logshortentrylistyearfinalcollection);
$logmoreentrylistmonthfinal = join ("$gmentrypagelinkseparatortemplate", @logmoreentrylistmonthfinalcollection);
$logmoreentrylistdayfinal = join ("$gmentrypagelinkseparatortemplate", @logmoreentrylistdayfinalcollection);
$logmoreentrylistyearfinal = join ("$gmentrypagelinkseparatortemplate", @logmoreentrylistyearfinalcollection);
$logentrylistmonthfinal = join ("$gmentrypagelinkseparatortemplate", @logentrylistmonthfinalcollection);
$logentrylistdayfinal = join ("$gmentrypagelinkseparatortemplate", @logentrylistdayfinalcollection);
$logentrylistyearfinal = join ("$gmentrypagelinkseparatortemplate", @logentrylistyearfinalcollection);
$logshortentrylistnumberfinal = join ("$gmentrypagelinkseparatortemplate", @logshortentrylistnumberfinalcollection);
$logmoreentrylistnumberfinal = join ("$gmentrypagelinkseparatortemplate", @logmoreentrylistnumberfinalcollection);
$logentrylistnumberfinal = join ("$gmentrypagelinkseparatortemplate", @logentrylistnumberfinalcollection);
$logshortentrylistfirsthalffinal = join ("$gmentrypagelinkseparatortemplate", @logshortentrylistfirsthalffinalcollection);
$logshortentrylistsecondhalffinal = join ("$gmentrypagelinkseparatortemplate", @logshortentrylistsecondhalffinalcollection);
$logmoreentrylistfirsthalffinal = join ("$gmentrypagelinkseparatortemplate", @logmoreentrylistfirsthalffinalcollection);
$logmoreentrylistsecondhalffinal = join ("$gmentrypagelinkseparatortemplate", @logmoreentrylistsecondhalffinalcollection);
$logentrylistfirsthalffinal = join ("$gmentrypagelinkseparatortemplate", @logentrylistfirsthalffinalcollection);
$logentrylistsecondhalffinal = join ("$gmentrypagelinkseparatortemplate", @logentrylistsecondhalffinalcollection);

}

# ----------------------------------------------
# generate log entry list for individual authors
# ----------------------------------------------

sub gm_generateentryloglistauthor {

$logshortentrylistfinal = "";
$logmoreentrylistfinal = "";
$logentrylistfinal = "";

open (FUNNYFEETINDY, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entry list file.  Please make sure that gm-entrylist.cgi is in the same directory as all your other Greymatter files and is CHMODed to 666; also, try running Diagnostics & Repair in the Configuration screen.");
@loglistloglines = <FUNNYFEETINDY>;
close (FUNNYFEETINDY);

if ($entrylistsortorder eq "descending") { @loglistloglines = reverse @loglistloglines; }

($toploglistnumber, $toploglistauthor, $toploglistsubject, $toploglistdate, $toploglisttimeampm, $toploglistopenstatus, $toploglistmorestatus) = split (/\|/, $loglistloglines[0]);
($toploglistmonthmonth, $toploglistdayday, $toploglistyear) = split (/\//, $toploglistdate);

$shortentrycounter = 0;
$moreentrycounter = 0;
$allentrycounter = 0;

$listdaymarker = "tommy";
$listmonthmarker = "tommy";
$listyearmarker = "tommy";

foreach $loglistline (@loglistloglines) {

	chomp ($loglistline);
	($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $loglistline);

	unless (($loglistopenstatus eq "C") || ($thisentryloglistauthor ne $loglistauthor)) {

		&gm_getloglistvariables;

		$usethismorelinktemplate = $gmmoreentrypagelinktemplate;
		$usethislinktemplate = $gmentrypagelinktemplate;

		if (($gmentrypagelinkdayseparatortemplate ne "") && ($listdaymarker ne $loglistday)) {
			$usethismorelinktemplate = "$gmentrypagelinkdayseparatortemplate|*|$usethismorelinktemplate";
			$usethislinktemplate = "$gmentrypagelinkdayseparatortemplate|*|$usethislinktemplate";
		}

		if (($gmentrypagelinkmonthseparatortemplate ne "") && ($listmonthmarker ne $loglistmonth)) {
			$usethismorelinktemplate = "$gmentrypagelinkmonthseparatortemplate|*|$usethismorelinktemplate";
			$usethislinktemplate = "$gmentrypagelinkmonthseparatortemplate|*|$usethislinktemplate";
		}

		if (($gmentrypagelinkyearseparatortemplate ne "") && ($listyearmarker ne $loglistyear)) {
			$usethismorelinktemplate = "$gmentrypagelinkyearseparatortemplate|*|$usethismorelinktemplate";
			$usethislinktemplate = "$gmentrypagelinkyearseparatortemplate|*|$usethislinktemplate";
		}

		if ($loglistmorestatus eq "Y") {
			$moreentrycounter++;
			$listsubsub = $usethismorelinktemplate;
			&entrylistsubsub;
			$listsubsub .= "|*|";
			$logmoreentrylistfinal .= $listsubsub;
		} else {
			$shortentrycounter++;
			$listsubsub = $usethislinktemplate;
			&entrylistsubsub;
			$listsubsub .= "|*|";
			$logshortentrylistfinal .= $listsubsub;
		}

		$allentrycounter++;
		$logentrylistfinal .= $listsubsub;

		$listdaymarker = $loglistday;
		$listmonthmarker = $loglistmonth;
		$listyearmarker = $loglistyear;

	}

}

@logshortentrylistfinalcollection = split (/\|\*\|/, $logshortentrylistfinal);
@logmoreentrylistfinalcollection = split (/\|\*\|/, $logmoreentrylistfinal);
@logentrylistfinalcollection = split (/\|\*\|/, $logentrylistfinal);

$logshortentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logshortentrylistfinalcollection);
$logmoreentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logmoreentrylistfinalcollection);
$logentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logentrylistfinalcollection);

}

# -------------------------------------------
# generate log entry list for comment sorting
# -------------------------------------------

sub gm_generateentryloglistcomments {

$logshortentrylistfinal = "";
$logmoreentrylistfinal = "";
$logentrylistfinal = "";
$logshortminimumentrylistfinal = "";
$logmoreminimumentrylistfinal = "";
$logminimumentrylistfinal = "";
$logshortnumberentrylistfinal = "";
$logmorenumberentrylistfinal = "";
$lognumberentrylistfinal = "";

$countfromhere = 1;

do {

	$countfromherenumberpadded = sprintf ("%8d", $countfromhere);
	$countfromherenumberpadded =~ tr/ /0/;
	open (FUNNYFEETCOMMIE, "$EntriesPath/$countfromherenumberpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$countfromherenumberpadded.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777, or try running Diagnostics & Repair in the Configuration screen.");
	@countfromhereentrylines = <FUNNYFEETCOMMIE>;
	close (FUNNYFEETCOMMIE);

	chomp ($countfromhereentrylines[0]);

	($countfromhereentrynumber, $countfromhereentryauthor, $countfromhereentrysubject, $countfromhereentryweekdaynumber, $countfromhereentrymonth, $countfromhereentryday, $countfromhereentryyearyear, $countfromhereentryhour, $countfromhereentryminute, $countfromhereentrysecond, $countfromhereentryampm, $countfromhereentrypositivekarma, $countfromhereentrynegativekarma, $countfromhereentrycommentsnumber, $countfromhereentryallowkarma, $countfromhereentryallowcomments, $countfromhereentryopenstatus) = split (/\|/, $countfromhereentrylines[0]);

	$countfromcanpost = "Y";

	if ($countfromhereentryallowcomments eq "no") { $countfromcanpost = "N"; }
	if (($posttoarchives eq "no") && ($countfromhereentrynumber <= $newarchivenumber)) { $countfromcanpost = "N"; }

	unless ($countfromhereentryopenstatus eq "closed") {
		$countslot = $countfromhere - 1;
		$countfromherelist[$countslot] = "$countfromhereentrycommentsnumber|$countfromhereentrynumber|$countfromcanpost";
	}

	$countfromhere++;

} until $countfromhere > $newentrynumber;

sub numerically { $a <=> $b }
@countfromherelist = sort numerically @countfromherelist;

unless ($entrylistsortorder eq "descending") { @countfromherelist = reverse @countfromherelist; }

open (FUNNYFEETBLECH, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entry list file.  Please make sure that gm-entrylist.cgi is in the same directory as all your other Greymatter files and is CHMODed to 666; also, try running Diagnostics & Repair in the Configuration screen.");
@loglistloglines = <FUNNYFEETBLECH>;
close (FUNNYFEETBLECH);

$shortentrycounter = 0;
$moreentrycounter = 0;
$allentrycounter = 0;

$listdaymarker = "tommy";
$listmonthmarker = "tommy";
$listyearmarker = "tommy";

foreach $countfromhereline (@countfromherelist) {

	($countfromherecommentsnumber, $countfromhereentrynumber, $countfromherecanpost) = split (/\|/, $countfromhereline);

	foreach $loglistline (@loglistloglines) {

		chomp ($loglistline);
		($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $loglistline);

		if ($loglistnumber eq $countfromhereentrynumber) {
			unless (($countfromherecanpost eq "N") && ($commententrylistonlyifokay eq "yes")) {

				&gm_getloglistvariables;

				$usethismorelinktemplate = $gmmoreentrypagelinktemplate;
				$usethislinktemplate = $gmentrypagelinktemplate;

				if (($gmentrypagelinkdayseparatortemplate ne "") && ($listdaymarker ne $loglistday)) {
					$usethismorelinktemplate = "$gmentrypagelinkdayseparatortemplate|*|$usethismorelinktemplate";
					$usethislinktemplate = "$gmentrypagelinkdayseparatortemplate|*|$usethislinktemplate";
				}

				if (($gmentrypagelinkmonthseparatortemplate ne "") && ($listmonthmarker ne $loglistmonth)) {
					$usethismorelinktemplate = "$gmentrypagelinkmonthseparatortemplate|*|$usethismorelinktemplate";
					$usethislinktemplate = "$gmentrypagelinkmonthseparatortemplate|*|$usethislinktemplate";
				}

				if (($gmentrypagelinkyearseparatortemplate ne "") && ($listyearmarker ne $loglistyear)) {
					$usethismorelinktemplate = "$gmentrypagelinkyearseparatortemplate|*|$usethismorelinktemplate";
					$usethislinktemplate = "$gmentrypagelinkyearseparatortemplate|*|$usethislinktemplate";
				}

				if ($loglistmorestatus eq "Y") {
					$moreentrycounter++;
					$listsubsub = $usethismorelinktemplate;
					&entrylistsubsub;
					$listsubsub .= "|*|";
					$logmoreentrylistfinal .= $listsubsub;
					unless ($countfromherecommentsnumber < 1) { $logmoreminimumentrylistfinal .= $listsubsub; }
					unless ($moreentrycounter > $entrylistcountnumber) { $logmorenumberentrylistfinal .= $listsubsub; }
				} else {
					$shortentrycounter++;
					$listsubsub = $usethislinktemplate;
					&entrylistsubsub;
					$listsubsub .= "|*|";
					$logshortentrylistfinal .= $listsubsub;
					unless ($countfromherecommentsnumber < 1) { $logshortminimumentrylistfinal .= $listsubsub; }
					unless ($shortentrycounter > $entrylistcountnumber) { $logshortnumberentrylistfinal .= $listsubsub; }
				}

				$allentrycounter++;
				$logentrylistfinal .= $listsubsub;
				unless ($countfromherecommentsnumber < 1) { $logminimumentrylistfinal .= $listsubsub; }
				unless ($allentrycounter > $entrylistcountnumber) { $lognumberentrylistfinal .= $listsubsub; }

				$listdaymarker = $loglistday;
				$listmonthmarker = $loglistmonth;
				$listyearmarker = $loglistyear;

			}
		}

	}

}

@logshortentrylistfinalcollection = split (/\|\*\|/, $logshortentrylistfinal);
@logmoreentrylistfinalcollection = split (/\|\*\|/, $logmoreentrylistfinal);
@logentrylistfinalcollection = split (/\|\*\|/, $logentrylistfinal);
@logshortminimumentrylistfinalcollection = split (/\|\*\|/, $logshortminimumentrylistfinal);
@logmoreminimumentrylistfinalcollection = split (/\|\*\|/, $logmoreminimumentrylistfinal);
@logminimumentrylistfinalcollection = split (/\|\*\|/, $logminimumentrylistfinal);
@logshortnumberentrylistfinalcollection = split (/\|\*\|/, $logshortnumberentrylistfinal);
@logmorenumberentrylistfinalcollection = split (/\|\*\|/, $logmorenumberentrylistfinal);
@lognumberentrylistfinalcollection = split (/\|\*\|/, $lognumberentrylistfinal);

$logshortentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logshortentrylistfinalcollection);
$logmoreentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logmoreentrylistfinalcollection);
$logentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logentrylistfinalcollection);
$logshortminimumentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logshortminimumentrylistfinalcollection);
$logmoreminimumentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logmoreminimumentrylistfinalcollection);
$logminimumentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logminimumentrylistfinalcollection);
$logshortnumberentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logshortnumberentrylistfinalcollection);
$logmorenumberentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @logmorenumberentrylistfinalcollection);
$lognumberentrylistfinal = join ("$gmentrypagelinkseparatortemplate", @lognumberentrylistfinalcollection);

}

# ----------------------
# get log list variables
# ----------------------

sub gm_getloglistvariables {

$loglistnumberpadded = sprintf ("%8d", $loglistnumber);
$loglistnumberpadded =~ tr/ /0/;

($loglistmonthmonth, $loglistdayday, $loglistyear) = split (/\//, $loglistdate);

if ((substr($loglistmonthmonth, 0, 1)) eq "0") {
	$loglistmonth = substr($loglistmonthmonth, -1, 1);
} else {
	$loglistmonth = $loglistmonthmonth;
}

if ((substr($loglistdayday, 0, 1)) eq "0") {
	$loglistday = substr($loglistdayday, -1, 1);
} else {
	$loglistday = $loglistdayday;
}

if ($loglistyear > 80) {
	$loglistyearyear = "19$loglistyear";
} else {
	$loglistyearyear = "20$loglistyear";
}

($loglisttime, $loglistampm) = split (/ /, $loglisttimeampm);
($loglisthourhour, $loglistminuteminute) = split (/:/, $loglisttime);

if ((substr($loglisthourhour, 0, 1)) eq "0") {
	$loglisthour = substr($loglisthourhour, -1, 1);
} else {
	$loglisthour = $loglisthourhour;
}

if ((substr($loglistminuteminute, 0, 1)) eq "0") {
	$loglistminute = substr($loglistminuteminute, -1, 1);
} else {
	$loglistminute = $loglistminuteminute;
}

$loglistmilitaryhour = $loglisthour;

if ($loglistampm eq "AM") {
	$loglistampmdot = "A.M.";
	$loglistampmlower = "am";
	$loglistampmdotlower = "a.m.";
} else {
	$loglistampmdot = "P.M.";
	$loglistampmlower = "pm";
	$loglistampmdotlower = "p.m.";
	$loglistmilitaryhour = $loglistmiltaryhour + 12;
}

$loglistmilitaryhour = sprintf ("%2d", $loglistmilitaryhour);
$loglistmilitaryhour =~ tr/ /0/;

@months = ("null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");

$loglistmonthword = $months[$loglistmonth];
$loglistmonthwordshort = substr($loglistmonthword, 0, 3);
$loglistmonthwordupper = uc($loglistmonthword);
$loglistmonthwordlower = lc($loglistmonthword);
$loglistmonthworduppershort = uc($loglistmonthwordshort);
$loglistmonthwordlowershort = lc($loglistmonthwordshort);

open (FUNNYFEETLOGME, "$EntriesPath/$loglistnumberpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$loglistnumberpadded.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777, or try running Diagnostics & Repair in the Configuration screen.");
@loglistentrylines = <FUNNYFEETLOGME>;
close (FUNNYFEETLOGME);

$gmcounter = 0;

foreach (@loglistentrylines) {
	chomp ($loglistentrylines[$gmcounter]);
	$gmcounter++;
}

($loglistentrynumber, $loglistentryauthor, $loglistentrysubject, $loglistentryweekdaynumber, $loglistentrymonth, $loglistentryday, $loglistentryyearyear, $loglistentryhour, $loglistentryminute, $loglistentrysecond, $loglistentryampm, $loglistentrypositivekarma, $loglistentrynegativekarma, $loglistentrycommentsnumber, $loglistentryallowkarma, $loglistentryallowcomments, $loglistentryopenstatus) = split (/\|/, $loglistentrylines[0]);
	
$loglistentrytotalkarma = $loglistentrypositivekarma - $loglistentrynegativekarma;

$loglistentrypositivekarmalink = "$cgiwebpath/gm-karma.cgi?vote=positive&entry=$loglistnumberpadded";
$loglistentrynegativekarmalink = "$cgiwebpath/gm-karma.cgi?vote=negative&entry=$loglistnumberpadded";

open (FUNNYFEETAUTHTWO, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gettheauthordata = <FUNNYFEETAUTHTWO>;
close (FUNNYFEETAUTHTWO);

$loglistentryauthoremail = "";
$loglistentryauthorhomepage = "";
$loglistentryauthorentrycount = "";

foreach $gettheauthordataline (@gettheauthordata) {
	chomp ($gettheauthordataline);
	@gettheauthorinfo = split (/\|/, $gettheauthordataline);
	if ($gettheauthorinfo[0] eq $loglistentryauthor) {
		$loglistentryauthoremail = $gettheauthorinfo[2];
		$loglistentryauthorhomepage = $gettheauthorinfo[3];
		$loglistentryauthorentrycount = $gettheauthorinfo[5];
	}
}

$loglistentryauthorsmartlink = $loglistentryauthor;
if ($loglistentryauthoremail ne "") { $loglistentryauthorsmartlink = "<A HREF=\"mailto:$loglistentryauthoremail\">$loglistentryauthor</A>"; }
if ($loglistentryauthorhomepage ne "") { $loglistentryauthorsmartlink = "<A HREF=\"$loglistentryauthorhomepage\">$loglistentryauthor</A>"; }

$loglistentryfilename = "$EntriesWebPath\/$loglistnumberpadded\.$entrysuffix";

$loglistentrycommentspostlink = "$loglistentryfilename\#comments";

$loglistentrycommentstatussmart = $gmsmartlinkmanycommentstemplate;

if ($loglistentrycommentsnumber eq "0") { $loglistentrycommentstatussmart = $gmsmartlinknocommentstemplate; }
if ($loglistentrycommentsnumber eq "1") { $loglistentrycommentstatussmart = $gmsmartlinkonecommenttemplate; }

$loglistentrycommentstatussmartupper = uc($loglistentrycommentstatussmart);
$loglistentrycommentstatussmartlower = lc($loglistentrycommentstatussmart);

$leapyearcheck = $loglistyearyear % 4;

$loglistmaxdaysinthismonth = 31;
if (($loglistmonthword eq "September") || ($loglistmonthword eq "April") || ($loglistmonthword eq "June") || ($loglistmonthword eq "November")) { $loglistmaxdaysinthismonth = 30; }
if ($loglistmonthword eq "February") {
	$loglistmaxdaysinthismonth = 28;
	if ($leapyearcheck eq "0") { $loglistmaxdaysinthismonth = 29; }
}
$loglistmaxdaysinpreviousmonth = 31;
if (($loglistmonthword eq "October") || ($loglistmonthword eq "May") || ($loglistmonthword eq "July") || ($loglistmonthword eq "December")) { $loglistmaxdaysinpreviousmonth = 30; }
if ($loglistmonthword eq "March") {
	$loglistmaxdaysinpreviousmonth = 28;
	if ($leapyearcheck eq "0") { $loglistmaxdaysinpreviousmonth = 29; }
}

$loglistweekbeginningmonth = $loglistmonth;
$loglistweekbeginningyearyear = $loglistyearyear;
$loglistweekendingmonth = $loglistmonth;
$loglistweekendingyearyear = $loglistyearyear;

$loglistweekbeginningday = $loglistday - $loglistentryweekdaynumber;
$loglistweekendingday = $loglistweekbeginningday + 6;

if ($loglistweekbeginningday < 1) {
	$loglistweekbeginningday = $loglistweekbeginningday + $loglistmaxdaysinpreviousmonth;
	if ($loglistweekbeginningday > $loglistday) { $loglistweekbeginningmonth--; }
	if ($loglistweekbeginningmonth < 1) {
		$loglistweekbeginningmonth = 12;
		$loglistweekbeginningyearyear--;
	}
}

if ($loglistweekendingday > $loglistmaxdaysinthismonth) {
	$loglistweekendingday = $loglistweekendingday - $loglistmaxdaysinthismonth;
	if ($loglistweekendingday < $loglistday) { $loglistweekendingmonth++; }
	if ($loglistweekendingmonth > 12) {
		$loglistweekendingmonth = 1;
		$loglistweekendingyearyear++;
	}
}

$loglistweekbeginningyear = substr($loglistweekbeginningyearyear, -2, 2);
$loglistweekendingyear = substr($loglistweekendingyearyear, -2, 2);

$loglistweekbeginningdayday = sprintf ("%2d", $loglistweekbeginningday);
$loglistweekbeginningdayday =~ tr/ /0/;
$loglistweekendingdayday = sprintf ("%2d", $loglistweekendingday);
$loglistweekendingdayday =~ tr/ /0/;
$loglistweekbeginningmonthmonth = sprintf ("%2d", $loglistweekbeginningmonth);
$loglistweekbeginningmonthmonth =~ tr/ /0/;
$loglistweekendingmonthmonth = sprintf ("%2d", $loglistweekendingmonth);
$loglistweekendingmonthmonth =~ tr/ /0/;

$loglistweekbeginningweekday = "Sunday";
$loglistweekbeginningmonthword = $months[$loglistweekbeginningmonth];
$loglistweekbeginningweekdayshort = substr($loglistweekbeginningweekday, 0, 3);
$loglistweekbeginningmonthwordshort = substr($loglistweekbeginningmonthword, 0, 3);
$loglistweekbeginningweekdayupper = uc($loglistweekbeginningweekday);
$loglistweekbeginningmonthwordupper = uc($loglistweekbeginningmonthword);
$loglistweekbeginningweekdaylower = lc($loglistweekbeginningweekday);
$loglistweekbeginningmonthwordlower = lc($loglistweekbeginningmonthword);
$loglistweekbeginningweekdayuppershort = uc($loglistweekbeginningweekdayshort);
$loglistweekbeginningmonthworduppershort = uc($loglistweekbeginningmonthwordshort);
$loglistweekbeginningweekdaylowershort = lc($loglistweekbeginningweekdayshort);
$loglistweekbeginningmonthwordlowershort = lc($loglistweekbeginningmonthwordshort);

$loglistweekendingweekday = "Saturday";
$loglistweekendingmonthword = $months[$loglistweekendingmonth];
$loglistweekendingweekdayshort = substr($loglistweekendingweekday, 0, 3);
$loglistweekendingmonthwordshort = substr($loglistweekendingmonthword, 0, 3);
$loglistweekendingweekdayupper = uc($loglistweekendingweekday);
$loglistweekendingmonthwordupper = uc($loglistweekendingmonthword);
$loglistweekendingweekdaylower = lc($loglistweekendingweekday);
$loglistweekendingmonthwordlower = lc($loglistweekendingmonthword);
$loglistweekendingweekdayuppershort = uc($loglistweekendingweekdayshort);
$loglistweekendingmonthworduppershort = uc($loglistweekendingmonthwordshort);
$loglistweekendingweekdaylowershort = lc($loglistweekendingweekdayshort);
$loglistweekendingmonthwordlowershort = lc($loglistweekendingmonthwordshort);

$loglistpagelink = "$EntriesWebPath\/$loglistnumberpadded\.$entrysuffix";

if ($keepmonthlyarchives eq "no") {
	$loglistpagearchivelogindexlink = "{{pageindexlink}}";
} else {
	if ($archiveformat eq "week") {
		$loglistpagearchivelogindexlink = "$EntriesWebPath/archive-$loglistweekbeginningmonthmonth$loglistweekbeginningdayday$loglistweekbeginningyearyear-$loglistweekendingmonthmonth$loglistweekendingdayday$loglistweekendingyearyear\.$logarchivesuffix";
	} else {
		$loglistpagearchivelogindexlink = "$EntriesWebPath/archive-$loglistmonthmonth$loglistyearyear\.$logarchivesuffix";
	}
}

$loglistmainbody = $loglistentrylines[2];
$loglistmorebody = $loglistentrylines[3];

if (($loglistmainbody =~ /\|\*\|/) || ($loglistmorebody =~ /\|\*\|/)) {
	$loglistmainbody =~ s/\|\*\|/<BR>/g;
	$loglistmorebody =~ s/\|\*\|/<BR>/g;
}
if (($loglistmainbody =~ /\n/) || ($loglistmorebody =~ /\n/)) {
	$loglistmainbody =~ s/\n/<BR>/g;
	$loglistmorebody =~ s/\n/<BR>/g;
}
if (($loglistmainbody =~ /<BR><BR>/) || ($loglistmorebody =~ /<BR><BR>/)) {
	$loglistmainbody =~ s/<BR><BR>/$gmparaseparationtemplate/g;
	$loglistmorebody =~ s/<BR><BR>/$gmparaseparationtemplate/g;
}

if (($censorenabled eq "both") || ($censorenabled eq "entries")) {
	unless ($censorlist eq "") {
		@censoredterms = split(/\|\*\|/, $censorlist);
		foreach $thisterm (@censoredterms) {
			unless ($thisterm eq "") {
				if ((substr($thisterm, 0, 1) eq "[") && (substr($thisterm, -1, 1) eq "]")) {
					$thisrealterm = $thisterm;
					$thisrealterm =~ s/\[//g;
					$thisrealterm =~ s/\]//g;
					$thisrealtermlength = length($thisrealterm);
					$thisrealtermreplace = "*" x $thisrealtermlength;
					$thisrealtermreplacedash = "-" x $thisrealtermlength;
					if ($loglistsubject =~ m/$thisrealterm/i) {
						$loglistsubject =~ s/\b$thisrealterm\b/$thisrealtermreplacedash/isg;
					}
					if ($loglistmainbody =~ m/$thisrealterm/i) {
						$loglistmainbody =~ s/\b$thisrealterm\b/$thisrealtermreplace/isg;
					}
					if ($loglistmorebody =~ m/$thisrealterm/i) {
						$loglistmorebody =~ s/\b$thisrealterm\b/$thisrealtermreplace/isg;
					}
				} else {
					$thisrealtermlength = length($thisterm);
					$thisrealtermreplace = "*" x $thisrealtermlength;
					$thisrealtermreplacedash = "-" x $thisrealtermlength;
					if ($loglistsubject =~ m/$thisterm/i) {
						$loglistsubject =~ s/\b$thisterm\b/$thisrealtermreplacedash/isg;
					}
					if ($loglistmainbody =~ m/$thisterm/i) {
						$loglistmainbody =~ s/\b$thisterm\b/$thisrealtermreplace/isg;
					}
					if ($loglistmorebody =~ m/$thisterm/i) {
						$loglistmorebody =~ s/\b$thisterm\b/$thisrealtermreplace/isg;
					}
				}
			}
		}
	}
}

if (($inlineformatting eq "entries") || ($inlineformatting eq "both")) {
	if (($loglistsubject =~ /\*\*(.*?)\*\*/) || ($loglistsubject =~ /\\\\(.*?)\\\\/) || ($loglistsubject =~ /__(.*?)__/)) {
		$loglistsubject =~ s/\*\*(.*?)\*\*/<B>$1<\/B>/isg;
		$loglistsubject =~ s/\\\\(.*?)\\\\/<I>$1<\/I>/isg;
		$loglistsubject =~ s/__(.*?)__/<U>$1<\/U>/isg;
	}
	if (($loglistmainbody =~ /\*\*(.*?)\*\*/) || ($loglistmainbody =~ /\\\\(.*?)\\\\/) || ($loglistmainbody =~ /__(.*?)__/)) {
		$loglistmainbody =~ s/\*\*(.*?)\*\*/<B>$1<\/B>/isg;
		$loglistmainbody =~ s/\\\\(.*?)\\\\/<I>$1<\/I>/isg;
		$loglistmainbody =~ s/__(.*?)__/<U>$1<\/U>/isg;
	}
	if (($loglistmorebody =~ /\*\*(.*?)\*\*/) || ($loglistmorebody =~ /\\\\(.*?)\\\\/) || ($loglistmorebody =~ /__(.*?)__/)) {
		$loglistmorebody =~ s/\*\*(.*?)\*\*/<B>$1<\/B>/isg;
		$loglistmorebody =~ s/\\\\(.*?)\\\\/<I>$1<\/I>/isg;
		$loglistmorebody =~ s/__(.*?)__/<U>$1<\/U>/isg;
	}
}

}

# --------------------------
# entry list sub-sub routine
# --------------------------

sub entrylistsubsub {

$listsubsub =~ s/{{year}}/$loglistyear/gi;
$listsubsub =~ s/{{yearyear}}/$loglistyearyear/gi;
$listsubsub =~ s/{{month}}/$loglistmonth/gi;
$listsubsub =~ s/{{monthmonth}}/$loglistmonthmonth/gi;
$listsubsub =~ s/{{monthword}}/$loglistmonthword/gi;
$listsubsub =~ s/{{monthwordshort}}/$loglistmonthword/gi;
$listsubsub =~ s/{{monthwordupper}}/$loglistmonthwordupper/gi;
$listsubsub =~ s/{{monthwordlower}}/$loglistmonthwordlower/gi;
$listsubsub =~ s/{{monthworduppershort}}/$loglistmonthworduppershort/gi;
$listsubsub =~ s/{{monthwordlowershort}}/$loglistmonthwordlowershort/gi;
$listsubsub =~ s/{{day}}/$loglistday/gi;
$listsubsub =~ s/{{dayday}}/$loglistdayday/gi;
$listsubsub =~ s/{{hour}}/$loglisthour/gi;
$listsubsub =~ s/{{hourhour}}/$loglisthourhour/gi;
$listsubsub =~ s/{{militaryhour}}/$loglistmilitaryhour/gi;
$listsubsub =~ s/{{minute}}/$loglistminute/gi;
$listsubsub =~ s/{{minuteminute}}/$loglistminuteminute/gi;
$listsubsub =~ s/{{ampm}}/$loglistampm/gi;
$listsubsub =~ s/{{ampmlower}}/$loglistampm/gi;
$listsubsub =~ s/{{ampmdot}}/$loglistampmdot/gi;
$listsubsub =~ s/{{ampmdotlower}}/$loglistampmdotlower/gi;
$listsubsub =~ s/{{author}}/$loglistauthor/gi;
$listsubsub =~ s/{{entrysubject}}/$loglistsubject/gi;
$listsubsub =~ s/{{entrynumber}}/$loglistnumber/gi;
$listsubsub =~ s/{{entrynumberpadded}}/$loglistnumberpadded/gi;
$listsubsub =~ s/{{pagelink}}/$loglistpagelink/gi;
$listsubsub =~ s/{{pagearchivelogindexlink}}/$loglistpagearchivelogindexlink/gi;

if ($listsubsub =~ m/{{author/i) {
	$listsubsub =~ s/{{author}}/$loglistentryauthor/gi;
	$listsubsub =~ s/{{authoremail}}/$loglistentryauthoremail/gi;
	$listsubsub =~ s/{{authorhomepage}}/$loglistentryauthorhomepage/gi;
	$listsubsub =~ s/{{authorentrycount}}/$loglistentryauthorentrycount/gi;
}

if (($listsubsub =~ m/{{weekbeginning/i) || ($listsubsub =~ m/{{weekending/i)) {
	$listsubsub =~ s/{{weekbeginningday}}/$loglistweekbeginningday/gi;
	$listsubsub =~ s/{{weekbeginningdayday}}/$loglistweekbeginningdayday/gi;
	$listsubsub =~ s/{{weekbeginningmonth}}/$loglistweekbeginningmonth/gi;
	$listsubsub =~ s/{{weekbeginningmonthmonth}}/$loglistweekbeginningmonthmonth/gi;
	$listsubsub =~ s/{{weekbeginningyear}}/$loglistweekbeginningyear/gi;
	$listsubsub =~ s/{{weekbeginningyearyear}}/$loglistweekbeginningyearyear/gi;
	$listsubsub =~ s/{{weekbeginningweekday}}/$loglistweekbeginningweekday/gi;
	$listsubsub =~ s/{{weekbeginningmonthword}}/$loglistweekbeginningmonthword/gi;
	$listsubsub =~ s/{{weekbeginningweekdayupper}}/$loglistweekbeginningweekdayupper/gi;
	$listsubsub =~ s/{{weekbeginningmonthwordupper}}/$loglistweekbeginningmonthwordupper/gi;
	$listsubsub =~ s/{{weekbeginningweekdaylower}}/$loglistweekbeginningweekdaylower/gi;
	$listsubsub =~ s/{{weekbeginningmonthwordlower}}/$loglistweekbeginningmonthwordlower/gi;
	$listsubsub =~ s/{{weekbeginningweekdayuppershort}}/$loglistweekbeginningweekdayuppershort/gi;
	$listsubsub =~ s/{{weekbeginningmonthworduppershort}}/$loglistweekbeginningmonthworduppershort/gi;
	$listsubsub =~ s/{{weekbeginningweekdaylowershort}}/$loglistweekbeginningweekdaylowershort/gi;
	$listsubsub =~ s/{{weekbeginningmonthwordlowershort}}/$loglistweekbeginningmonthwordlowershort/gi;
	$listsubsub =~ s/{{weekendingday}}/$loglistweekendingday/gi;
	$listsubsub =~ s/{{weekendingdayday}}/$loglistweekendingdayday/gi;
	$listsubsub =~ s/{{weekendingmonth}}/$loglistweekendingmonth/gi;
	$listsubsub =~ s/{{weekendingmonthmonth}}/$loglistweekendingmonthmonth/gi;
	$listsubsub =~ s/{{weekendingyear}}/$loglistweekendingyear/gi;
	$listsubsub =~ s/{{weekendingyearyear}}/$loglistweekendingyearyear/gi;
	$listsubsub =~ s/{{weekendingweekday}}/$loglistweekendingweekday/gi;
	$listsubsub =~ s/{{weekendingmonthword}}/$loglistweekendingmonthword/gi;
	$listsubsub =~ s/{{weekendingweekdayupper}}/$loglistweekendingweekdayupper/gi;
	$listsubsub =~ s/{{weekendingmonthwordupper}}/$loglistweekendingmonthwordupper/gi;
	$listsubsub =~ s/{{weekendingweekdaylower}}/$loglistweekendingweekdaylower/gi;
	$listsubsub =~ s/{{weekendingmonthwordlower}}/$loglistweekendingmonthwordlower/gi;
	$listsubsub =~ s/{{weekendingweekdayuppershort}}/$loglistweekendingweekdayuppershort/gi;
	$listsubsub =~ s/{{weekendingmonthworduppershort}}/$loglistweekendingmonthworduppershort/gi;
	$listsubsub =~ s/{{weekendingweekdaylowershort}}/$loglistweekendingweekdaylowershort/gi;
	$listsubsub =~ s/{{weekendingmonthwordlowershort}}/$loglistweekendingmonthwordlowershort/gi;
}

if (($listsubsub =~ m/karma}}/i) || ($listsubsub =~ m/karmalink}}/i)) {
	$listsubsub =~ s/{{positivekarmalink}}/$loglistentrypositivekarmalink/gi;
	$listsubsub =~ s/{{negativekarmalink}}/$loglistentrynegativekarmalink/gi;
	$listsubsub =~ s/{{positivekarma}}/$loglistentrypositivekarma/gi;
	$listsubsub =~ s/{{negativekarma}}/$loglistentrynegativekarma/gi;
	$listsubsub =~ s/{{totalkarma}}/$loglistentrytotalkarma/gi;
}

if ($listsubsub =~ m/{{comments/i) {
	$listsubsub =~ s/{{commentsnumber}}/$loglistentrycommentsnumber/gi;
	$listsubsub =~ s/{{commentstatussmart}}/$loglistentrycommentstatussmart/gi;
	$listsubsub =~ s/{{commentstatussmartupper}}/$loglistentrycommentstatussmartupper/gi;
	$listsubsub =~ s/{{commentstatussmartlower}}/$loglistentrycommentstatussmartlower/gi;
}

if ($listsubsub =~ m/{{entry/i) {
	$listsubsub =~ s/{{entrymainbody}}/$loglistmainbody/gi;
	$listsubsub =~ s/{{entrymorebody}}/$loglistmorebody/gi;
	$listsubsub =~ s/{{entrycomments}}/$loglistcomments/gi;
	if ($listsubsub =~ m/{{entrymainbodyfirstwords (\d+)}}/i) {
		until ($listsubsub !~ m/{{entrymainbodyfirstwords (\d+)}}/isg) {
			$firstwordscount = $1;
			$grabmainbodywords = $loglistmainbody;
			if ($grabmainbodywords =~ m/{{link/i) {
				$grabmainbodywords =~ s/({{linkmo) (http|https|ftp)(:\/\/\S+?) (.+?)(\|)(.+?)(}})/$4/isg;
				$grabmainbodywords =~ s/({{link) (http|https|ftp)(:\/\/\S+?)(}})/$2$3/isg;
				$grabmainbodywords =~ s/({{link) (http|https|ftp)(:\/\/\S+?) (.+?)(}})/$4/isg;
			}
			if ($grabmainbodywords =~ m/{{email/i) {
				$grabmainbodywords =~ s/({{emailmo) (\S+\@\S+?) (.+?)(\|)(.+?)(}})/$3/isg;
				$grabmainbodywords =~ s/({{email) (\S+\@\S+?)(}})/$2/isg;
				$grabmainbodywords =~ s/({{email) (\S+\@\S+?) (.+?)(}})/$3/isg;
			}
			$grabmainbodywords =~ s/<([^>]|\n)*>/ /g;
			$grabmainbodywords =~ s/{{(.*?)}}/ /g;
			$grabmainbodywords =~ s/\n/ /g;
			$grabmainbodywords =~ s/\r/ /g;
			$grabmainbodywords =~ s/\|\*\|/ /g;
			$grabmainbodywords =~ s/^\s+//;
			$grabmainbodywords =~ s/\s+$//;
			$grabmainbodywords =~ s/\s{2,}/ /g;
			@grabmainbodywordslist = split (/ /, $grabmainbodywords);
			$countwordsfromhere = 0;
			(@finalmainbodywordslist, @finalmainbodywordslist = ());
			if ($firstwordscount < 1) { $firstwordscount = 1; }
			do {
				$finalmainbodywordslist[$countwordsfromhere] = $grabmainbodywordslist[$countwordsfromhere];
				$countwordsfromhere++;
			} until $countwordsfromhere eq $firstwordscount;
			$finalmainbodyfirstwords = join (" ", @finalmainbodywordslist);
			$finalmainbodyfirstwords =~ s/^\s+//;
			$finalmainbodyfirstwords =~ s/\s+$//;
			$finalmainbodyfirstwords =~ s/\s{2,}//g;
			if (substr($finalmainbodyfirstwords, -1) =~ /\W/) { chop($finalmainbodyfirstwords); }
			if (substr($finalmainbodyfirstwords, -1) eq / /) { chop($finalmainbodyfirstwords); }
			$listsubsub =~ s/{{entrymainbodyfirstwords ($firstwordscount)}}/$finalmainbodyfirstwords/isg;
		}
	}
	if ($listsubsub =~ m/{{entrymorebodyfirstwords (\d+)}}/i) {
		until ($listsubsub !~ m/{{entrymorebodyfirstwords (\d+)}}/isg) {
			$firstwordscount = $1;
			if ($loglistmorebody eq "") {
				$listsubsub =~ s/{{entrymorebodyfirstwords ($firstwordscount)}}//isg;
			} else {
				$grabmorebodywords = $loglistmorebody;
				if ($grabmorebodywords =~ m/{{link/i) {
					$grabmorebodywords =~ s/({{linkmo) (http|https|ftp)(:\/\/\S+?) (.+?)(\|)(.+?)(}})/$4/isg;
					$grabmorebodywords =~ s/({{link) (http|https|ftp)(:\/\/\S+?)(}})/$2$3/isg;
					$grabmorebodywords =~ s/({{link) (http|https|ftp)(:\/\/\S+?) (.+?)(}})/$4/isg;
				}
				if ($grabmorebodywords =~ m/{{email/i) {
					$grabmorebodywords =~ s/({{emailmo) (\S+\@\S+?) (.+?)(\|)(.+?)(}})/$3/isg;
					$grabmorebodywords =~ s/({{email) (\S+\@\S+?)(}})/$2/isg;
					$grabmorebodywords =~ s/({{email) (\S+\@\S+?) (.+?)(}})/$3/isg;
				}
				$grabmorebodywords =~ s/<([^>]|\n)*>/ /g;
				$grabmorebodywords =~ s/{{(.*?)}}/ /g;
				$grabmorebodywords =~ s/\n/ /g;
				$grabmorebodywords =~ s/\r/ /g;
				$grabmorebodywords =~ s/\|\*\|/ /g;
				$grabmorebodywords =~ s/^\s+//;
				$grabmorebodywords =~ s/\s+$//;
				$grabmorebodywords =~ s/\s{2,}/ /g;
				@grabmorebodywordslist = split (/ /, $grabmorebodywords);
				$countwordsfromhere = 0;
				(@finalmorebodywordslist, @finalmorebodywordslist = ());
				if ($firstwordscount < 1) { $firstwordscount = 1; }
				do {
					$finalmorebodywordslist[$countwordsfromhere] = $grabmorebodywordslist[$countwordsfromhere];
					$countwordsfromhere++;
				} until $countwordsfromhere eq $firstwordscount;
				$finalmorebodyfirstwords = join (" ", @finalmorebodywordslist);
				$finalmorebodyfirstwords =~ s/^\s+//;
				$finalmorebodyfirstwords =~ s/\s+$//;
				$finalmorebodyfirstwords =~ s/\s{2,}//g;
				if (substr($finalmorebodyfirstwords, -1) =~ /\W/) { chop($finalmorebodyfirstwords); }
				if (substr($finalmorebodyfirstwords, -1) eq / /) { chop($finalmorebodyfirstwords); }
				$listsubsub =~ s/{{entrymorebodyfirstwords ($firstwordscount)}}/$finalmorebodyfirstwords/isg;
			}
		}
	}
}

}

# ----------------------------------
# generate external author variables
# ----------------------------------

sub gm_generateexternalauthorvariables {

open (FUNNYFEETAUTHORS, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gettheexternalauthordata = <FUNNYFEETAUTHORS>;
close (FUNNYFEETAUTHORS);

foreach $gettheexternalauthordataline (@gettheexternalauthordata) {
	chomp ($gettheexternalauthordataline);
	@gettheexternalauthorinfo = split (/\|/, $gettheexternalauthordataline);
	$thisexternalauthor = $gettheexternalauthorinfo[0];
	$thisexternalauthoremail = $gettheexternalauthorinfo[2];
	$thisexternalauthorhomepage = $gettheexternalauthorinfo[3];
	$thisexternalauthorentrycount = $gettheexternalauthorinfo[5];

	$thisexternalauthorsmartlink = $thisexternalauthor;
	if ($thisexternalauthoremail ne "") { $thisexternalauthorsmartlink = "<A HREF=\"mailto:$thisentryauthoremail\">$thisentryauthor</A>"; }
	if ($thisexternalauthorhomepage ne "") { $thisexternalauthorsmartlink = "<A HREF=\"$thisentryauthorhomepage\">$thisentryauthor</A>"; }

	$entryreturn =~ s/{{authoremail $thisexternalauthor}}/$thisexternalauthoremail/isg;
	$entryreturn =~ s/{{authorhomepage $thisexternalauthor}}/$thisexternalauthorhomepage/isg;
	$entryreturn =~ s/{{authorsmartlink $thisexternalauthor}}/$thisexternalauthorsmartlink/isg;
	$entryreturn =~ s/{{authorentrycount $thisexternalauthor}}/$thisexternalauthorentrycount/isg;
}

}

# -----------------
# generate calendar
# -----------------

sub gm_generatecalendar {

$usethisentrydayday = sprintf ("%2d", $usethisentryday);
$usethisentrydayday =~ tr/ /0/;
$usethisentrymonthmonth = sprintf ("%2d", $usethisentrymonth);
$usethisentrymonthmonth =~ tr/ /0/;
$usethisentryyear = substr($usethisentryyearyear, -2, 2);
$usethisentrymonthwordupper = uc($usethisentrymonthword);
$usethisentrymonthwordlower = lc($usethisentrymonthword);
$usethisentrymonthwordshort = substr($usethisentrymonthword, 0, 3);
$usethisentrymonthworduppershort = uc($usethisentrymonthwordshort);
$usethisentrymonthwordlowershort = lc($usethisentrymonthwordshort);

$leapyearcheck = $usethisentryyearyear % 4;

$maxdaysinthismonth = 31;
if (($usethisentrymonthword eq "September") || ($usethisentrymonthword eq "April") || ($usethisentrymonthword eq "June") || ($usethisentrymonthword eq "November")) { $maxdaysinthismonth = 30; }
if ($usethisentrymonthword eq "February") {
	$maxdaysinthismonth = 28;
	if ($leapyearcheck eq "0") { $maxdaysinthismonth = 29; }
}

$maxdaysinpreviousmonth = 31;
if (($usethisentrymonthword eq "October") || ($usethisentrymonthword eq "May") || ($usethisentrymonthword eq "July") || ($usethisentrymonthword eq "December")) { $maxdaysinpreviousmonth = 30; }
if ($usethisentrymonthword eq "March") {
	$maxdaysinpreviousmonth = 28;
	if ($leapyearcheck eq "0") { $maxdaysinpreviousmonth = 29; }
}

$calendarweekday[$usethisentryweekdaynumber] = $usethisentryday;
$weekcountfrom = $usethisentryweekdaynumber;
$weekcountfromday = $usethisentryday;
$weekcountspecial = "none";

unless ($weekcountfrom eq "0") {
	do {
		$weekcountfrom--;
		$weekcountfromday--;
		if ($weekcountfromday eq 0) {
			$weekcountfromday = $maxdaysinpreviousmonth;
			$weekcountspecial = "gotolastmonth";
		}
		unless ($weekcountfrom < 0) { $calendarweekday[$weekcountfrom] = $weekcountfromday; }
	} until $weekcountfrom eq "0";
}

$weekcountfrom = $usethisentryweekdaynumber;
$weekcountfromday = $usethisentryday;

unless ($weekcountfrom eq "6") {
	do {
		$weekcountfrom++;
		$weekcountfromday++;
		if ($weekcountfromday > $maxdaysinthismonth) {
			$weekcountfromday = 1;
			$weekcountspecial = "gotonextmonth";
		}
		unless ($weekcountfrom > 6) { $calendarweekday[$weekcountfrom] = $weekcountfromday; }
	} until $weekcountfrom eq "6";
}

$countfromhere = $usethisentryday;
$calendardataday[$usethisentryday] = $usethisentryweekdaynumber;

unless ($countfromhere eq "1") {
	do {
		$thistempday = $calendardataday[$countfromhere];
		$thistempday--;
		$countfromhere--;
		if ($thistempday < 0) { $thistempday = 6; }
		$calendardataday[$countfromhere] = $thistempday;
	} until $countfromhere eq "1";
}

$weekcountfromday = $usethisentryday;
$countfromhere = $usethisentryday;

unless ($countfromhere eq $maxdaysinthismonth) {
	do {
		$thistempday = $calendardataday[$countfromhere];
		$thistempday++;
		$countfromhere++;
		if ($thistempday > 6) { $thistempday = 0; }
		$calendardataday[$countfromhere] = $thistempday;
	} until $countfromhere eq $maxdaysinthismonth;
}

$calendarfull = $gmcalendartablebeginningtemplate;

$calendarfull .= "$gmcalendarblankcelltemplate" x $calendardataday[1];

open (FUNNYFEETLIST, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entry list file.  Please make sure that gm-entrylist.cgi is in the same directory as all your other Greymatter files and is CHMODed to 666; also, try running Diagnostics & Repair in the Configuration screen.");
@loglistloglines = <FUNNYFEETLIST>;
close (FUNNYFEETLIST);

$loglistdates = "";

foreach $thisloglistline (@loglistloglines) {
	($thisloglistnumber, $thisloglistauthor, $thisloglistsubject, $thisloglistdate, $thisloglisttimeampm, $thisloglistopenstatus, $thisloglistmorestatus) = split (/\|/, $thisloglistline);
	unless ($thisloglistopenstatus eq "C") { $loglistdates .= "$thisloglistdate "; }
}

$weekcountfrom = 0;
$calendarweekfull = "";

do {
	$currentcountday = $calendarweekday[$weekcountfrom];
	$currentcountmonth = $usethisentrymonth;
	$currentcountyearyear = $usethisentryyearyear;
	if (($currentcountday > 20) && ($weekcountspecial eq "gotolastmonth")) {
		$currentcountmonth--;
		if ($currentcountmonth < 1) {
			$currentcountmonth = 12;
			$currentcountyearyear--;
		}
	}
	if (($currentcountday < 10) && ($weekcountspecial eq "gotonextmonth")) {
		$currentcountmonth++;
		if ($currentcountmonth > 12) {
			$currentcountmonth = 1;
			$currentcountyearyear++;
		}
	}
	$currentcountdayday = sprintf ("%2d", $currentcountday);
	$currentcountdayday =~ tr/ /0/;
	$currentcountmonthmonth = sprintf ("%2d", $currentcountmonth);
	$currentcountmonthmonth =~ tr/ /0/;
	$currentcountyear = substr($currentcountyearyear, -2, 2);
	$thisweeklistdate = "$currentcountmonthmonth\/$currentcountdayday\/$currentcountyear";
	if ($loglistdates =~ /$thisweeklistdate/) {
		if ($generateentrypages eq "no") {
			foreach $thisloglistline (@loglistloglines) {
				chomp ($thisloglistline);
				($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
				if ($loglistdate eq $thisweeklistdate) {
					&gm_getloglistvariables;
					$listsubsub = $gmcalendarweekfulldaytemplate;
					&entrylistsubsub;
					$calendarweekfull .= $listsubsub;
				}
			}
		} else {
			$thiscalendarweeklink = "";
			foreach $thisloglistline (@loglistloglines) {
				chomp ($thisloglistline);
				($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
				if (($loglistdate eq $thisweeklistdate) && ($thiscalendarweeklink eq "")) {
					unless (($thisloglistmorestatus eq "N") && ($linktocalendarentries eq "more")) {
						$thiscalendarweeklink = "yes";
					}
				}
			}
			if ($thiscalendarweeklink eq "") {
				$listsubsub = $gmcalendarweekfulldaytemplate;
				$listsubsub =~ s/{{day}}/$currentcountday/g;
				$listsubsub =~ s/{{day}}/$currentcountday/g;
				$listsubsub =~ s/{{month}}/$currentcountmonth/g;
				$listsubsub =~ s/{{monthmonth}}/$currentcountmonthmonth/g;
				$listsubsub =~ s/{{year}}/$currentcountyear/g;
				$listsubsub =~ s/{{yearyear}}/$currentcountyearyear/g;
				$calendarweekfull .= $listsubsub;
			} else {
				foreach $thisloglistline (@loglistloglines) {
					chomp ($thisloglistline);
					($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
					if (($loglistdate eq $thisweeklistdate) && ($thiscalendarweeklink eq "yes") && ($loglistopenstatus ne "C")) {
						&gm_getloglistvariables;
						$listsubsub = $gmcalendarweekfulldaylinktemplate;
						&entrylistsubsub;
						$calendarweekfull .= $listsubsub;
						$thiscalendarweeklink = "";
					}
				}
			}
		}
	} else {
		$listsubsub = $gmcalendarweekfulldaytemplate;
		$listsubsub =~ s/{{day}}/$currentcountday/g;
		$listsubsub =~ s/{{day}}/$currentcountday/g;
		$listsubsub =~ s/{{month}}/$currentcountmonth/g;
		$listsubsub =~ s/{{monthmonth}}/$currentcountmonthmonth/g;
		$listsubsub =~ s/{{year}}/$currentcountyear/g;
		$listsubsub =~ s/{{yearyear}}/$currentcountyearyear/g;
		$calendarweekfull .= $listsubsub;
	}
	$weekcountfrom++;
} until $weekcountfrom eq "7";

$countfromhere = 1;

do {
	$countfromherepadded = sprintf ("%2d", $countfromhere);
	$countfromherepadded =~ tr/ /0/;
	$thislistdate = "$usethisentrymonthmonth\/$countfromherepadded\/$usethisentryyear";
	if ($loglistdates =~ /$thislistdate/) {
		if ($generateentrypages eq "no") {
			foreach $thisloglistline (@loglistloglines) {
				chomp ($thisloglistline);
				($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
				if ($loglistdate eq $thislistdate) {
					&gm_getloglistvariables;
					$listsubsub = $gmcalendarfullcelltemplate;
					&entrylistsubsub;
					$calendarfull .= $listsubsub;
				}
			}			
		} else {
			$thiscalendarlink = "";
			foreach $thisloglistline (@loglistloglines) {
				chomp ($thisloglistline);
				($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
				if (($loglistdate eq $thislistdate) && ($thiscalendarlink eq "")) {
					unless (($loglistmorestatus eq "N") && ($linktocalendarentries eq "more")) {
						$thiscalendarlink = "yes";
					}
				}
			}
			if ($thiscalendarlink eq "") {
				$listsubsub = $gmcalendarfullcelltemplate;
				$listsubsub =~ s/{{day}}/$countfromhere/g;
				$listsubsub =~ s/{{day}}/$countfromherepadded/g;
				$calendarfull .= $listsubsub;
			} else {
				foreach $thisloglistline (@loglistloglines) {
					chomp ($thisloglistline);
					($loglistnumber, $loglistauthor, $loglistsubject, $loglistdate, $loglisttimeampm, $loglistopenstatus, $loglistmorestatus) = split (/\|/, $thisloglistline);
					if (($loglistdate eq $thislistdate) && ($thiscalendarlink eq "yes") && ($loglistopenstatus ne "C")) {
						&gm_getloglistvariables;
						$listsubsub = $gmcalendarfullcelllinktemplate;
						&entrylistsubsub;
						$calendarfull .= $listsubsub;
						$thiscalendarlink = "";
					}
				}
			}
		}
	} else {
		$listsubsub = $gmcalendarfullcelltemplate;
		$listsubsub =~ s/{{day}}/$countfromhere/g;
		$listsubsub =~ s/{{day}}/$countfromherepadded/g;
		$calendarfull .= $listsubsub;
	}
	if ($calendardataday[$countfromhere] eq "6") { $calendarfull .= "</TR>\n<TR>"; }
	$countfromhere++;
} until $countfromhere > $maxdaysinthismonth;

$endofcaldisplay = 6 - $calendardataday[$maxdaysinthismonth];
$calendarfull .= "$gmcalendarblankcelltemplate" x $endofcaldisplay;
$calendarfull .= $gmcalendartableendingtemplate;

$calendarfull =~ s/{{month}}/$usethisentrymonth/g;
$calendarfull =~ s/{{monthmonth}}/$usethisentrymonthmonth/g;
$calendarfull =~ s/{{year}}/$usethisentryyear/g;
$calendarfull =~ s/{{yearyear}}/$usethisentryyearyear/g;
$calendarfull =~ s/{{monthword}}/$usethisentrymonthword/g;
$calendarfull =~ s/{{monthwordupper}}/$usethisentrymonthwordupper/g;
$calendarfull =~ s/{{monthwordlower}}/$usethisentrymonthwordlower/g;
$calendarfull =~ s/{{monthwordshort}}/$usethisentrymonthwordshort/g;
$calendarfull =~ s/{{monthworduppershort}}/$usethisentrymonthworduppershort/g;
$calendarfull =~ s/{{monthwordlowershort}}/$usethisentrymonthwordlowershort/g;

}

# -----------------
# log the author in
# -----------------

sub gm_login {

if (!(open(CHECKMATE,"gm-counter.cgi"))) {
	&gm_dangermouse("gm-counter.cgi is missing.  Please upload this file to the same directory as all the other Greymatter cgi files, and make sure you CHMOD it to 666.");
}
close(CHECKMATE);

if (!(open(CHECKMATE,"gm-karma.cgi"))) {
	&gm_dangermouse("gm-karma.cgi is missing.  Please upload this file to the same directory as all the other Greymatter cgi files, and make sure you CHMOD it to 755.");
}
close(CHECKMATE);

if (!(open(CHECKMATE,"gm-comments.cgi"))) {
	&gm_dangermouse("gm-comments.cgi is missing.  Please upload this file to the same directory as all the other Greymatter cgi files, and make sure you CHMOD it to 755.");
}
close(CHECKMATE);

if (!(open(CHECKMATE,"gm-upload.cgi"))) {
	&gm_dangermouse("gm-upload.cgi is missing.  Please upload this file to the same directory as all the other Greymatter cgi files, and make sure you CHMOD it to 755.");
}
close(CHECKMATE);

if (!(open(CHECKMATE,"gm-entrylist.cgi"))) {
	&gm_dangermouse("gm-entrylist.cgi is missing.  Please upload this file to the same directory as all the other Greymatter cgi files, and make sure you CHMOD it to 666.");
}
close(CHECKMATE);

if (!(open(CHECKMATE,"gm-cplog.cgi"))) {
	&gm_dangermouse("gm-cplog.cgi is missing.  Please upload this file to the same directory as all the other Greymatter cgi files, and make sure you CHMOD it to 666.");
}
close(CHECKMATE);

if (!(open(CHECKMATE,"gm-authors.cgi"))) {
	&gm_dangermouse("gm-authors.cgi is missing.  Please upload this file to the same directory as all the other Greymatter cgi files, and make sure you CHMOD it to 666.");
}
close(CHECKMATE);

if (!(open(CHECKMATE,"gm-templates.cgi"))) {
	&gm_dangermouse("gm-templates.cgi is missing.  Please upload this file to the same directory as all the other Greymatter cgi files, and make sure you CHMOD it to 666.");
}
close(CHECKMATE);

if (!(open(CHECKMATE,"gm-banlist.cgi"))) {
	&gm_dangermouse("gm-banlist.cgi is missing.  Please upload this file to the same directory as all the other Greymatter cgi files, and make sure you CHMOD it to 666.");
}
close(CHECKMATE);

if ($loginnotice eq "") { $loginnotice = qq(<B><FONT COLOR="#000000">Login Prompt</FONT></B><P>); }

&gm_readconfig;

if ($cookiesallowed eq "no") {
	$getnameandpwcookie = "";
} else {
	$getnameandpwcookie = "<SCRIPT TYPE=\"text/javascript\" LANGUAGE=\"JavaScript\">\n<!--//\ndocument.gmloginform.authorname.value = getCookie(\"gmcookiename\");\ndocument.gmloginform.authorpassword.value = getCookie(\"gmcookiepw\");\ndocument.gmloginform.authorname.focus();\n//-->\n</SCRIPT>";
}

print<<GMLOGIN;

$gmheadtag

$gmframetop
$loginnotice

<FORM ACTION="gm.cgi" METHOD=POST NAME="gmloginform"><TABLE BORDER=0 CELLPADDING=3 CELLSPACING=0><TR><TD ALIGN=RIGHT>$gmfonttag Author:</FONT></TD><TD ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" SIZE=20 NAME="authorname" STYLE="width: 200">$gmfonttag</TD></TR><TR><TD ALIGN=RIGHT>$gmfonttag Password:</FONT></TD><TD ALIGN=LEFT></FONT><INPUT TYPE=PASSWORD CLASS="textinput" SIZE=20 NAME="authorpassword" STYLE="width: 200">$gmfonttag</TD></TR></TABLE><P><INPUT TYPE=SUBMIT CLASS="button" VALUE="Enter" STYLE="background: #D0FFD0; width: 75"><INPUT TYPE=HIDDEN NAME="thomas" VALUE="login"></FORM><P><FONT SIZE=1>"Not knowing when the dawn will come, I open every door."&#151;Emily Dickinson</FONT>
$getnameandpwcookie
$gmframebottom

</BODY>
</HTML>

GMLOGIN

exit;

}

# ------------------
# validate the login
# ------------------

sub gm_validate {

&gm_bancheck;
&gm_readconfig;

$gmvalidated = "no";
$gmentryaccess = "no";
$gmentryeditaccess = "no";
$gmconfigurationaccess = "no";
$gmtemplateaccess = "no";
$gmauthoraccess = "no";
$gmcplogaccess = "no";
$gmrebuildaccess = "no";
$gmbookmarkletaccess = "no";
$gmuploadaccess = "no";
$gmloginaccess = "no";

$IN{'authorname'} =~ s/\|//g;
$IN{'authorpassword'} =~ s/\|//g;
$IN{'authorname'} =~ s/^\s+//;
$IN{'authorname'} =~ s/\s+$//;
$IN{'authorpassword'} =~ s/^\s+//;
$IN{'authorpassword'} =~ s/\s+$//;

if (($IN{'authorname'} eq "") || ($IN{'authorpassword'} eq "")) {
	$loginnotice = qq(<B><FONT COLOR="#0000FF">You left one or more of the fields blank.  Please try again.</FONT></B><P>);
	&gm_writetocplog("<B><FONT COLOR=\"#FF0000\">Invalid login attempt:</FONT></B> One or more fields left blank ($IN{'authorname'} $IN{'authorpassword'})");
	&gm_login;
}

open (FUNNYFEETVALLERY, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
@gmauthordata = <FUNNYFEETVALLERY>;
close (FUNNYFEETVALLERY);

foreach $gmauthordataline (@gmauthordata) {
	chomp ($gmauthordataline);
	@gmauthorinfo = split (/\|/, $gmauthordataline);
	if ($gmauthorinfo[0] eq $IN{'authorname'}) {
		$gmvalidated = "foundname";
		if ($gmauthorinfo[1] eq $IN{'authorpassword'}) {
			$gmvalidated = "yes";
			if ($gmauthorinfo[6] eq "Y") { $gmentryaccess = "yes"; }
			if ($gmauthorinfo[7] eq "Y") { $gmentryeditaccess = "yes"; }
			if ($gmauthorinfo[7] eq "O") { $gmentryeditaccess = "mineonly"; }
			if ($gmauthorinfo[8] eq "Y") { $gmconfigurationaccess = "yes"; }
			if ($gmauthorinfo[9] eq "Y") { $gmtemplateaccess = "yes"; }
			if ($gmauthorinfo[9] eq "O") { $gmtemplateaccess = "hfsonly"; }
			if ($gmauthorinfo[10] eq "Y") { $gmauthoraccess = "yes"; }
			if ($gmauthorinfo[11] eq "Y") { $gmrebuildaccess = "yes"; }
			if ($gmauthorinfo[12] eq "Y") { $gmcplogaccess = "yes"; }
			if ($gmauthorinfo[13] eq "Y") { $gmbookmarkletaccess = "yes"; }
			if ($gmauthorinfo[14] eq "Y") { $gmuploadaccess = "yes"; }
			if ($gmauthorinfo[15] eq "Y") { $gmloginaccess = "yes"; }
		}
	}
}

if ($gmvalidated eq "foundname") {
	$loginnotice = qq(<B><FONT COLOR="#0000FF">The password you entered for that author is incorrect.  Please try again.</FONT></B><P>);
	&gm_writetocplog("<B><FONT COLOR=\"#FF0000\">Invalid login attempt:</FONT></B> Incorrect password ($IN{'authorpassword'}) for $IN{'authorname'}");
	&gm_login;
}

if ($gmvalidated ne "yes") {
	$loginnotice = qq(<B><FONT COLOR="#0000FF">No such author is registered.  Please try again.</FONT></B><P>);
	&gm_writetocplog("<B><FONT COLOR=\"#FF0000\">Invalid login attempt:</FONT></B> No such author as $IN{'authorname'} ($IN{'authorpassword'}) registered");
	&gm_login;
}

}

# --------------------------
# check if this IP is banned
# --------------------------

sub gm_bancheck {

open (FUNNYFEETBABY, "gm-banlist.cgi") || &gm_dangermouse("Can't read the banlist file.  Please make sure that gm-banlist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmbanlist = <FUNNYFEETBABY>;
close (FUNNYFEETBABY);

$currentip = $ENV{'REMOTE_ADDR'};

if ($gmbanlist[0] ne "") {
	foreach $gmbanlistline (@gmbanlist) {
		chomp ($gmbanlistline);
		($checkthisip, $checkthisiphost, $checkthisperson) = split (/\|/, $gmbanlistline);
		if (($currentip =~ /$checkthisip/) && ($checkthisip ne "")) {

			if ($keeplog eq "yes") {
				&date;
				open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
				print FUNNYFEET "<FONT SIZE=1>[$basedate] [$currentip]</FONT> <FONT COLOR=\"#FF0000\"><B>A banned IP ($checkthisip";
				if ($checkthisperson ne "") { print FUNNYFEET ", \"$checkthisperson\""; }
				print FUNNYFEET ") attempted to access this program</B></FONT>\n";
				close (FUNNYFEET);
			}

print<<GMBANNEDNOTICE;

$gmheadtag

$gmframetop
You have been banned from accessing this program.<BR>(IP: $currentip)
$gmframebottom

</BODY>
</HTML>

GMBANNEDNOTICE

exit;

		}
	}
}

}

# ---------------
# write to cp log
# ---------------

sub gm_writetocplog {

my $writetologtext = shift;

if ($keeplog eq "yes") {
	&date;
	open (ITSLOGITSLOG, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	print ITSLOGITSLOG "<FONT SIZE=1>[$basedate] [$authorIP]</FONT> $writetologtext\n";
	close (ITSLOGITSLOG);
}

}

# -----------------------------
# danger will robinson, danger!
# -----------------------------

sub gm_dangermouse {

my $dangerwarning = shift;

print<<GMDANGER;

$gmheadtag

$gmframetop<B><FONT COLOR="#FF0000">Error Notice</FONT></B><P>$dangerwarning$gmframebottom

</BODY>
</HTML>

GMDANGER

exit;

}

1;
