#!/usr/bin/perl

# =============================
# GREYMATTER - Karma Module
# Weblog/Journal Software
# version one point two
# Copyright (c)2000 Noah Grey
# http://noahgrey.com/greysoft/
# =============================

# ***  Your possession of this software indicates that you agree to the terms   ***
# *** specified under the "Copyright & Usage" heading in the "manual.txt" file. ***

use CGI::Carp qw(fatalsToBrowser);

require "gm-library.cgi";

my $getin;
if ($ENV{'REQUEST_METHOD'} eq "GET") { $getin = $ENV{'QUERY_STRING'}; } else { $getin = <STDIN>; }

@pairs = split(/&/, $getin);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$name =~ tr/+/ /;
	$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$IN{$name} = $value;
}

$userip = $ENV{'REMOTE_ADDR'};

&gm_karmabancheck;

&gm_readconfig;
&gm_readtemplates;
&gm_readcounter;

open (FUNNYFEET, "$EntriesPath/$IN{'entry'}.cgi") || &gm_dangermouse("Can't open $EntriesPath/$IN{'entry'}.cgi.  Please make sure your paths are configured correctly and that your entries/archives directory is CHMODed to 777.");
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
&gm_votetwicecheck;
&gm_addkarma;
&gm_freshenafterkarma;

# -------------
# check for ban
# -------------

sub gm_karmabancheck {

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
				print FUNNYFEET ") attempted to cast a $IN{'vote'} karma vote on entry #$IN{'entry'}</B></FONT>\n";
				close (FUNNYFEET);
			}

print "Content-type: text/html\n";

print<<GMBANNEDNOTICE;

$gmheadtag

$gmframetop
You have been banned from voting on this site.<BR>(IP: $userip)
$gmframebottom

</BODY>
</HTML>

GMBANNEDNOTICE

exit;

		}
	}
}

}

# --------------------------------
# check if karma votes can be cast
# --------------------------------

sub gm_allowedcheck {

if (($posttoarchives eq "no") && ($thisentrynumber <= $newarchivenumber)) {

if (($keeplog eq "yes") && ($logkarmaandcomments eq "yes")) {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$userip]</FONT> A $IN{'vote'} karma vote was blocked from being added to archived entry #$IN{'entry'}\n";
	close (FUNNYFEET);
}

print "Content-type: text/html\n";

print<<GMKARMADISALLOWEDNOTICE;

$gmheadtag

$gmframetop
Sorry—karma votes cannot be cast on archived entries.  Please use your browser's Back button to return.
$gmframebottom

</BODY>
</HTML>

GMKARMADISALLOWEDNOTICE

exit;

}

if (($thisentryallowkarma eq "no") || ($thisentryopenstatus eq "closed") || ($allowkarmaorcomments eq "comments") || ($allowkarmaorcomments eq "neither")) {

if (($keeplog eq "yes") && ($logkarmaandcomments eq "yes")) {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$userip]</FONT> A $IN{'vote'} karma vote was blocked from being cast on entry #$IN{'newcommententrynumber'}\n";
	close (FUNNYFEET);
}

print "Content-type: text/html\n";

print<<GMKARMABLOCKEDNOTICE;

$gmheadtag

$gmframetop
Sorry—karma votes cannot be cast on this entry.  Please use your browser's Back button to return.
$gmframebottom

</BODY>
</HTML>

GMKARMABLOCKEDNOTICE

exit;

}

}

# --------------------------------------
# check if this person has already voted
# --------------------------------------

sub gm_votetwicecheck {

@pastkarmavotes = split (/\|/, $entrylines[1]);

$votedtwice = "no";

foreach $googoogajoob (@pastkarmavotes) {

if ($googoogajoob eq $userip) {

if ($allowmultiplekarmavotes eq "yes") {
$votedtwice = "yes";
} else {

if (($keeplog eq "yes") && ($logkarmaandcomments eq "yes")) {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$userip]</FONT> A repeat karma vote ($IN{'vote'}) was blocked from being added to entry #$IN{'entry'}\n";
	close (FUNNYFEET);
}

print "Content-type: text/html\n";

print<<GMVOTETWICEDISALLOWEDNOTICE;

$gmheadtag

$gmframetop
Sorry—you can't vote twice on the same entry.  Please use your browser's Back button to return.
$gmframebottom

</BODY>
</HTML>

GMVOTETWICEDISALLOWEDNOTICE

exit;

}

}

}

}

# ---------------------------
# check if the input is blank
# ---------------------------

sub gm_blankcheck {

if (($IN{'vote'} eq "") || ($IN{'entry'} eq "")) {

print "Content-type: text/html\n";

print<<GMBLANKNOTICE;

$gmheadtag

$gmframetop
Error: Blank fields reported in the karma module input.  Please report to this site's webmaster.
$gmframebottom

</BODY>
</HTML>

GMBLANKNOTICE

exit;

}

}

# ------------------
# add the karma vote
# ------------------

sub gm_addkarma {

if ($IN{'vote'} eq "positive") {
	$thisentrypositivekarma++;
	$newalltimepktotalnumber++;
	unless ($votedtwice eq "yes") { $entrylines[1] .= "|$userip|P"; }
}
if ($IN{'vote'} eq "negative") {
	$thisentrynegativekarma++;
	$newalltimenktotalnumber++;
	unless ($votedtwice eq "yes") { $entrylines[1] .= "|$userip|N"; }
}


$entrylines[0] = "$thisentrynumber|$thisentryauthor|$thisentrysubject|$thisentryweekdaynumber|$thisentrymonth|$thisentryday|$thisentryyearyear|$thisentryhour|$thisentryminute|$thisentrysecond|$thisentryampm|$thisentrypositivekarma|$thisentrynegativekarma|$thisentrycommentsnumber|$thisentryallowkarma|$thisentryallowcomments|$thisentryopenstatus";

$gmcounter = 0;

&date;

open (FUNNYFEET, ">$EntriesPath/$IN{'entry'}.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$IN{'entry'}.cgi.  Please make sure that your paths are configured correctly and that your entries/archives directory is CHMODed to 777.");
foreach $entrynewline (@entrylines) { print FUNNYFEET "$entrynewline\n"; }
close (FUNNYFEET);

}

# ------------------------
# primp, preen, take a bow
# ------------------------

sub gm_freshenafterkarma {

&gm_writecounter;

$aftermath = "$EntriesWebPath/$IN{'entry'}.$entrysuffix";

&gm_getentryvariables($IN{'entry'});

$aftermath = "$LogWebPath/$indexfilename";
$aftermathprefix = substr($indexfilename, 0, 5);

if ($aftermathprefix eq "index") { $aftermath = "$LogWebPath/"; }

if ($thisentryisanarchive eq "yes") {
	$aftermath = "$EntriesWebPath/archive-$thisentrymonthmonth$thisentryyearyear\.$entrysuffix";
}

if ($generateentrypages eq "yes") {
	if ($thisentrymorebody ne "") {
		&gm_formatentry($gmmoreentrypagetemplate);
	} else {
		&gm_formatentry($gmentrypagetemplate);
	}
	open (THISFILE, ">$EntriesPath/$IN{'entry'}.$entrysuffix") || &gm_dangermouse("Can't write to $EntriesPath/$IN{'entry'}.$entrysuffix.  Please make sure that your paths are configured correctly and that your entries/archives directory is CHMODed to 777.");;
	print THISFILE $entryreturn;
	close (THISFILE);
}

if ($thisentryisanarchive eq "no") {
	&gm_generatemainindex;
} else {
	&gm_readcounter;
	$stoppednumber = $newarchivenumber;
	do { &gm_generatearchive($stoppednumber); } until $stoppednumber <= 1;
}

&gm_readconfig;

if (($NotifyForStatus eq "karma") || ($NotifyForStatus eq "both")) {
if ($NotifyEmail ne "") {

&gm_getentryvariables($IN{'entry'});

$sendithere = "$mailprog -t";

@sendestinations = split (/;/, $NotifyEmail);

foreach $destinationow (@sendestinations) {

open (MAIL, "|$sendithere") || &gm_dangermouse("Can't open the mail program at $mailprog.  Please make sure you have this configured correctly.");
print MAIL <<__MAILNOTIFY__;
To: $destinationow
From: $destinationow
Subject: [Greymatter] Notice: Karma Vote Cast

A $IN{'vote'} karma vote has just been cast by $userip IP on entry #$thisentrynumber ($thisentrysubject).  That brings this entry to $thisentrypositivekarma positive and $thisentrynegativekarma negative karma votes for a $thisentrytotalkarma total karma rating.

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
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$userip]</FONT> <I>A $IN{'vote'} karma vote was cast on entry #$thisentrynumber ($thisentrysubject)</I>\n";
	close (FUNNYFEET);
}

print "Location: $aftermath\n\n";

}
