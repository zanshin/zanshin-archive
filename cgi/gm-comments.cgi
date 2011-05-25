#!/usr/bin/perl

# =============================
# GREYMATTER - Comments Module
# Weblog/Journal Software
# version one point two
# Copyright (c)2000 Noah Grey
# http://noahgrey.com/greysoft/
# =============================

# ***  Your possession of this software indicates that you agree to the terms   ***
# *** specified under the "Copyright & Usage" heading in the "manual.txt" file. ***

use CGI::Carp qw(fatalsToBrowser);

require "gm-library.cgi";

read(STDIN, $input, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $input);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$name =~ tr/+/ /;
	$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$IN{$name} = $value;
}

$userip = $ENV{'REMOTE_ADDR'};

&gm_readconfig;
&gm_readtemplates;
&gm_readcounter;

if (($IN{'newcommentbody'} eq "") && ($IN{'newcommentauthor'} eq "") && ($IN{'gmsearch'} eq "")) {
	print "Content-type: text/html\n\n";
	&gm_dangermouse("No valid information was given.");
}

if ($IN{'gmsearch'} ne "") { &gm_searchresults; }

$IN{'newcommentbody'} =~ s/\|\*\|/\n/g;

$IN{'newcommentauthor'} =~ s/<(([^ >]|\n)*)>//g;
$IN{'newcommentemail'} =~ s/<(([^ >]|\n)*)>//g;
$IN{'newcommenthomepage'} =~ s/<(([^ >]|\n)*)>//g;

$IN{'newcommentauthor'} =~ s/{/(/g;
$IN{'newcommentemail'} =~ s/{/(/g;
$IN{'newcommenthomepage'} =~ s/{/(/g;
$IN{'newcommentbody'} =~ s/{/(/g;
$IN{'newcommentauthor'} =~ s/}/)/g;
$IN{'newcommentemail'} =~ s/}/)/g;
$IN{'newcommenthomepage'} =~ s/}/)/g;
$IN{'newcommentbody'} =~ s/}/)/g;
$IN{'newcommentauthor'} =~ s/{/(/g;
$IN{'newcommentemail'} =~ s/{/(/g;
$IN{'newcommenthomepage'} =~ s/{/(/g;
$IN{'newcommentbody'} =~ s/{/(/g;
$IN{'newcommentauthor'} =~ s/}/)/g;
$IN{'newcommentemail'} =~ s/}/)/g;
$IN{'newcommenthomepage'} =~ s/}/)/g;
$IN{'newcommentbody'} =~ s/}/)/g;

$IN{'newcommentauthor'} =~ s/\|//g;
$IN{'newcommentemail'} =~ s/\|//g;
$IN{'newcommenthomepage'} =~ s/\|//g;
$IN{'newcommentbody'} =~ s/\|//g;

$IN{'newcommentauthor'} =~ s/"/\&quot;/g;
$IN{'newcommentemail'} =~ s/"/\&quot;/g;
$IN{'newcommenthomepage'} =~ s/"/\&quot;/g;
$IN{'newcommentbody'} =~ s/"/\&quot;/g;

$IN{'newcommentauthor'} =~ s/^\s+//;
$IN{'newcommentauthor'} =~ s/\s+$//;
$IN{'newcommentemail'} =~ s/^\s+//;
$IN{'newcommentemail'} =~ s/\s+$//;
$IN{'newcommenthomepage'} =~ s/^\s+//;
$IN{'newcommenthomepage'} =~ s/\s+$//;
$IN{'newcommentbody'} =~ s/^\s+//;
$IN{'newcommentbody'} =~ s/\s+$//;

$IN{'newcommentauthor'} =~ s/\n//g;
$IN{'newcommentemail'} =~ s/\n//g;
$IN{'newcommenthomepage'} =~ s/\n//g;
$IN{'newcommentauthor'} =~ s/\r//g;
$IN{'newcommentemail'} =~ s/\r//g;
$IN{'newcommenthomepage'} =~ s/\r//g;

$IN{'newcommentbody'} =~ s/\r//g;
$IN{'newcommentbody'} =~ s/\n/\|\*\|/g;
$IN{'newcommentbody'} =~ s/(\|\*\|\|\*\|){2,}/\|\*\|\|\*\|/g;
$IN{'newcommentbody'} =~ s/\|\*\|\|\*\|\|\*\|/\|\*\|\|\*\|/g;

$temphomepageprefix = substr($IN{'newcommenthomepage'}, 0, 7);
if ($temphomepageprefix ne "http://") { $IN{'newcommenthomepage'} = "http://$IN{'newcommenthomepage'}"; }

if ($IN{'newcommenthomepage'} eq "http://") { $IN{'newcommenthomepage'} = ""; }

&gm_commentbancheck;

$newcommententrynumberpadded = sprintf ("%8d", $IN{'newcommententrynumber'});
$newcommententrynumberpadded =~ tr/ /0/;

open (FUNNYFEET, "$EntriesPath/$newcommententrynumberpadded.cgi") || &gm_dangermouse("Can't open $EntriesPath/$newcommententrynumberpadded.cgi.  Please make sure your paths are configured correctly and that your entries/archives directory is CHMODed to 777.");
@entrylines = <FUNNYFEET>;
close (FUNNYFEET);

$gmcounter = 0;

foreach (@entrylines) {
	chomp ($entrylines[$gmcounter]);
	$gmcounter++;
}

($thisentrynumber, $thisentryauthor, $thisentrysubject, $thisentryweekdaynumber, $thisentrymonth, $thisentryday, $thisentryyearyear, $thisentryhour, $thisentryminute, $thisentrysecond, $thisentryampm, $thisentrypositivekarma, $thisentrynegativekarma, $thisentrycommentsnumber, $thisentryallowkarma, $thisentryallowcomments, $thisentryopenstatus) = split (/\|/, $entrylines[0]);

&gm_allowedcheck;
&gm_blankcheck;

if ($IN{'gmpostpreview'} ne "") {
	&gm_previewcomment;
} else {
	&gm_addcomment;
	&gm_freshenaftercomment;
}

# -------------
# check for ban
# -------------

sub gm_commentbancheck {

open (FUNNYFEET, "gm-banlist.cgi") || &gm_dangermouse("Can't read the banlist file.  Please make sure that gm-banlist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
@gmbanlist = <FUNNYFEET>;
close (FUNNYFEET);

if ($gmbanlist[0] ne "") {
	foreach $gmbanlistline (@gmbanlist) {
		chomp ($gmbanlistline);
		($checkthisip, $checkthisiphost, $checkthisperson) = split (/\|/, $gmbanlistline);
		if ($userip =~ m/$checkthisip/i) {

			if (($keeplog eq "yes") && ($logkarmaandcomments eq "yes")) {
				&date;
				open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
				print FUNNYFEET "<FONT SIZE=1>[$basedate] [$userip]</FONT> <FONT COLOR=\"#FF0000\"><B>A banned IP ($checkthisip/$checkthisiphost";
				if ($checkthisperson ne "") { print FUNNYFEET ", \"$checkthisperson\""; }
				if ($IN{'gmsearch'} ne "") {
					print FUNNYFEET ") attempted to search for \"$IN{'gmsearch'}\"</FONT>\n";
				} else {
					print FUNNYFEET ") attempted to post a comment to entry #$IN{'newcommententrynumber'}</B> ($IN{'newcommentauthor'}: $IN{'newcommentbody'})</FONT>\n";
				}
				close (FUNNYFEET);
			}

print "Content-type: text/html\n\n";

print<<GMBANNEDNOTICE;

$gmheadtag

$gmframetop
You have been banned from using this site.<BR>(IP: $userip)
$gmframebottom

</BODY>
</HTML>

GMBANNEDNOTICE

exit;

		}
	}
}

}

# -------------------------------
# check if comments can be posted
# -------------------------------

sub gm_allowedcheck {

if (($posttoarchives eq "no") && ($thisentrynumber <= $newarchivenumber)) {

if (($keeplog eq "yes") && ($logkarmaandcomments eq "yes")) {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$userip]</FONT> A comment was blocked from being added to archived entry #$IN{'newcommententrynumber'} ($IN{'newcommentauthor'}: $IN{'newcommentbody'})\n";
	close (FUNNYFEET);
}

print "Content-type: text/html\n\n";

print<<GMARCHIVEDISALLOWEDNOTICE;

$gmheadtag

$gmframetop
Sorry—comments cannot be posted to archived entries.  Please use your browser's Back button to return.
$gmframebottom

</BODY>
</HTML>

GMARCHIVEDISALLOWEDNOTICE

exit;

}

if (($thisentryallowcomments eq "no") || ($generateentrypages eq "no") || ($thisentryopenstatus eq "closed") || ($allowkarmaorcomments eq "karma") || ($allowkarmaorcomments eq "neither")) {

if (($keeplog eq "yes") && ($logkarmaandcomments eq "yes")) {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$userip]</FONT> A comment was blocked from being added to entry #$IN{'newcommententrynumber'} ($IN{'newcommentauthor'}: $IN{'newcommentbody'})\n";
	close (FUNNYFEET);
}

print "Content-type: text/html\n\n";

print<<GMCOMMENTBLOCKEDNOTICE;

$gmheadtag

$gmframetop
Sorry—comments cannot be posted to this entry.  Please use your browser's Back button to return.
$gmframebottom

</BODY>
</HTML>

GMCOMMENTBLOCKEDNOTICE

exit;

}

}

# ------------------------------
# check if subj or body is blank
# ------------------------------

sub gm_blankcheck {

if (($IN{'newcommentauthor'} eq "") || ($IN{'newcommentbody'} eq "")) {

print "Content-type: text/html\n\n";

print<<GMBLANKNOTICE;

$gmheadtag

$gmframetop
You left either your name or your comments blank.  Please use your browser's Back button to return.
$gmframebottom

</BODY>
</HTML>

GMBLANKNOTICE

exit;

}

}

# ------------------------------
# preview comment before posting
# ------------------------------

sub gm_previewcomment {

&date;

if ($thisentrymorebody ne "") {
	if ($thisentrynumber <= $newarchivenumber) {
		$commentpreviewpage = $gmmorearchiveentrypagetemplate;
	} else {
		$commentpreviewpage = $gmmoreentrypagetemplate;
	}
} else {
	if ($thisentrynumber <= $newarchivenumber) {
		$commentpreviewpage = $gmarchiveentrypagetemplate;
	} else {
		$commentpreviewpage = $gmentrypagetemplate;
	}
}

&gm_getentryvariables($IN{'newcommententrynumber'});

$thisentrycomments = "";
$thisentrycommentsnumber = 1;
$thispreviewcounter = $thisentrycommentsnumber + 3;

$IN{'newcommentauthor'} =~ s/\&quot;/"/g;
$IN{'newcommentemail'} =~ s/\&quot;/"/g;
$IN{'newcommenthomepage'} =~ s/\&quot;/"/g;
$IN{'newcommentbody'} =~ s/\&quot;/"/g;
$IN{'newcommentbody'} =~ s/\|\*\|/\n/g;

$entrylines[$thispreviewcounter] = "$IN{'newcommentauthor'}|$userip|$IN{'newcommentemail'}|$IN{'newcommenthomepage'}|$wday|$mon|$mday|$JSYear|$hour|$min|$sec|$AMPM|$IN{'newcommentbody'}";

$IN{'newcommentauthor'} =~ s/"/\&quot;/g;
$IN{'newcommentemail'} =~ s/"/\&quot;/g;
$IN{'newcommenthomepage'} =~ s/"/\&quot;/g;
$IN{'newcommentbody'} =~ s/"/\&quot;/g;
$IN{'newcommentbody'} =~ s/\n/\|\*\|/g;

$previewcommentauthor = $IN{'newcommentauthor'};
$previewcommentemail = $IN{'newcommentemail'};
$previewcommenthomepage = $IN{'newcommenthomepage'};
$previewcommentbody = $IN{'newcommentbody'};

&gm_collatecomments;

$commentpreviewpage =~ s/{{commentdivider}}/$gmcommentpreviewdividertemplate/gi;
$commentpreviewpage =~ s/{{entrycommentsform}}/$gmcommentpreviewformtemplate/gi;
$commentpreviewpage =~ s/{{previewcommentauthor}}/$previewcommentauthor/gi;
$commentpreviewpage =~ s/{{previewcommentemail}}/$previewcommentemail/gi;
$commentpreviewpage =~ s/{{previewcommenthomepage}}/$previewcommenthomepage/gi;
$commentpreviewpage =~ s/{{previewcommentbody}}/$previewcommentbody/gi;

&gm_formatentry($commentpreviewpage);

print "Content-type: text/html\n\n";

print<<PREVIEWCOMMENT;

$entryreturn

PREVIEWCOMMENT

exit;

}

# --------------------------
# so add the comment already
# --------------------------

sub gm_addcomment {

$thisentrycommentsnumber++;

$entrylines[0] = "$thisentrynumber|$thisentryauthor|$thisentrysubject|$thisentryweekdaynumber|$thisentrymonth|$thisentryday|$thisentryyearyear|$thisentryhour|$thisentryminute|$thisentrysecond|$thisentryampm|$thisentrypositivekarma|$thisentrynegativekarma|$thisentrycommentsnumber|$thisentryallowkarma|$thisentryallowcomments|$thisentryopenstatus";

$gmcounter = 0;

&date;

open (FUNNYFEET, ">$EntriesPath/$newcommententrynumberpadded.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$newcommententrynumberpadded.cgi.  Please make sure that your paths are configured correctly and that your entries/archives directory is CHMODed to 777.");
foreach $entrynewline (@entrylines) { print FUNNYFEET "$entrynewline\n"; }
print FUNNYFEET "$IN{'newcommentauthor'}|$userip|$IN{'newcommentemail'}|$IN{'newcommenthomepage'}|$wday|$mon|$mday|$JSYear|$hour|$min|$sec|$AMPM|$IN{'newcommentbody'}\n";
close (FUNNYFEET);

}

# ------------------------
# primp, preen, take a bow
# ------------------------

sub gm_freshenaftercomment {

$newalltimecommentstotalnumber++;
&gm_writecounter;

$aftermath = "$EntriesWebPath/$newcommententrynumberpadded.$entrysuffix#comments";

&gm_getentryvariables($IN{'newcommententrynumber'});

if ($thisentrymorebody ne "") {
	if ($thisentrynumber <= $newarchivenumber) {
		&gm_formatentry($gmmorearchiveentrypagetemplate);
	} else {
		&gm_formatentry($gmmoreentrypagetemplate);
	}
} else {
	if ($thisentrynumber <= $newarchivenumber) {
		&gm_formatentry($gmarchiveentrypagetemplate);
	} else {
		&gm_formatentry($gmentrypagetemplate);
	}
}

open (THISFILE, ">$EntriesPath/$thisentrynumberpadded.$entrysuffix") || &gm_dangermouse("Can't write to $EntriesPath/thisentrynumberpadded.$entrysuffix.  Please make sure that your paths are configured correctly and that your entries/archives directory is CHMODed to 777.");;
print THISFILE $entryreturn;
close (THISFILE);

if ($thisentrynumber <= $newarchivenumber) {
	&gm_readcounter;
	$stoppednumber = $newarchivenumber;
	do { &gm_generatearchive($stoppednumber); } until $stoppednumber <= 1;
} else {
	&gm_generatemainindex;
}

&gm_readconfig;

if (($NotifyForStatus eq "comments") || ($NotifyForStatus eq "both")) {
if ($NotifyEmail ne "") {

$formattedcomment = $IN{'newcommentbody'};
$formattedcomment =~ s/\|\*\|/\n/g;
$sendithere = "$mailprog -t";

@sendestinations = split (/;/, $NotifyEmail);

&gm_getentryvariables($IN{'newcommententrynumber'});

foreach $destinationow (@sendestinations) {

open (MAIL, "|$sendithere") || &gm_dangermouse("Can't open the mail program at $mailprog.  Please make sure you have this configured correctly.");
print MAIL <<__MAILNOTIFY__;
To: $destinationow
From: Greymatter <$destinationow>
Subject: [Greymatter] Notice: Comment Posted

A comment has just been posted to entry #$IN{'newcommententrynumber'} ($thisentrysubject).

Name: $IN{'newcommentauthor'} (IP: $userip)
E-Mail: $IN{'newcommentemail'}
Homepage: $IN{'newcommenthomepage'}

Comments: $formattedcomment

Posted to: $aftermath

-----
Greymatter $gmversion
http://noahgrey.com/greysoft/

__MAILNOTIFY__

close(MAIL);

}

}
}

if (($keeplog eq "yes") && ($logkarmaandcomments eq "yes")) {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$userip]</FONT> <I>$IN{'newcommentauthor'} added a comment to entry #$IN{'newcommententrynumber'} ($thisentrysubject)</I>\n";
	close (FUNNYFEET);
}

print "Location: $aftermath\n\n";

}

# --------------
# search results
# --------------

sub gm_searchresults {

$searchmatchescount = 0;
$searchresultbody = "";

$IN{'gmsearch'} =~ s/\|//g;

&gm_readconfig;
&gm_readcounter;
&gm_readtemplates;

$countfromhere = $newentrynumber;

do {

	&gm_getentryvariables($countfromhere);

	unless ($thisentryopenstatus eq "closed") {

		if (($thisentrysubject =~ m/$IN{'gmsearch'}/i) || ($thisentryauthor =~ m/$IN{'gmsearch'}/i) || ($thisentrymainbody =~ m/$IN{'gmsearch'}/i) || ($thisentrymorebody =~ m/$IN{'gmsearch'}/i) || ($thisentrycomments =~ m/$IN{'gmsearch'}/i)) {

			&gm_formatentry($gmsearchresultsentrytemplate);
			$searchresultbody .= $entryreturn;
			$searchmatchescount++;

		}

	}

	$countfromhere--;

} until $countfromhere eq "0";

$searchpage = $gmsearchresultspagetemplate;
$searchpage =~ s/{{searchterm}}/$IN{'gmsearch'}/g;
$searchpage =~ s/{{searchmatches}}/$searchmatchescount/g;
$searchpage =~ s/{{searchresults}}/$searchresultbody/g;
&gm_formatentry($searchpage);

print "Content-type: text/html\n\n";

print<<SHOWSEARCHRESULTS;

$entryreturn

SHOWSEARCHRESULTS

if (($keeplog eq "yes") && ($logkarmaandcomments eq "yes")) {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$userip]</FONT> <I>A search was performed for \"$IN{'gmsearch'}\" ($searchmatchescount matches)</I>\n";
	close (FUNNYFEET);
}

exit;

}
