#!/usr/bin/perl

# =============================
# GREYMATTER - Main Program
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

require "gm-library.cgi";

# ----------------------------------------
# gathering the input & checking for login
# ----------------------------------------

print "Content-type: text/html\n\n";

$authorIP = $ENV{'REMOTE_ADDR'};

$logindeletednotice = "";

if ($ENV{'REQUEST_METHOD'} eq "GET") { $getin = $ENV{'QUERY_STRING'}; } else { $getin = <STDIN>; }

@pairs = split(/&/, $getin);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$name =~ tr/+/ /;
	$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	unless (($name eq "logtext") || ($name eq "loglink")) { $value =~ tr/+/ /; }
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$IN{$name} = $value;
}

&gm_bancheck;
&gm_readconfig;

if ($IN{'thomas'} eq "") { &gm_login; }
if ($IN{'thomas'} eq "Re-Login") { &gm_login; }

&gm_validate;

if ($IN{'thomas'} eq "login") {
	&gm_writetocplog("<B>$IN{'authorname'} logged in</B>");
	&gm_versioncheck;
	&gm_readcounter;
	$statusnote = qq(<B><FONT COLOR="#0000FF">Welcome, $IN{'authorname'}.</FONT></B><P>);
	if ($newentrynumber eq "0") {
		open (FUNNYFEET, "gm-cplog.cgi") || &gm_dangermouse("Can't read the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
		@cploglines = <FUNNYFEET>;
		close (FUNNYFEET);
		$cplogtext = join (" ", @cploglines);
		unless ($cplogtext =~ /successfully performed diagnostics/) {
			$statusnote = qq(<B><FONT COLOR="#0000FF">Welcome to Greymatter!  Please enter Configuration first, check your paths,<BR>and run Diagnostics & Repair to validate your installation.</FONT></B><P>);
		}
	}
	&gm_frontpage;
}

if ($IN{'thomas'} eq "rebuildupdate") { &gm_rebuildupdate; }

if ($IN{'thomas'} eq "Update Now") { &gm_versionupgrading; }

if ($IN{'thomas'} eq "gmbmpost") { &gm_addentrypopup; }

if ($IN{'thomas'} eq "Return To Main Menu") { &gm_frontpage; }

if ($IN{'thomas'} eq "Add A New Entry") { &gm_addentry; }
if ($IN{'thomas'} eq "Edit An Entry") { &gm_editentryselection; }
if ($IN{'thomas'} eq "Configuration") { &gm_configuration; }
if ($IN{'thomas'} eq "Edit Templates") { &gm_edittemplates; }
if ($IN{'thomas'} eq "Edit Authors") { &gm_editauthors; }
if ($IN{'thomas'} eq "Edit Banned IP List") { &gm_editbanlist; }
if ($IN{'thomas'} eq "Add Bookmarklets") { &gm_addbookmarklets; }
if ($IN{'thomas'} eq "Upload Files") { &gm_uploadfiles; }
if ($IN{'thomas'} eq "Rebuild Files") { &gm_rebuildfilesmenu; }
if ($IN{'thomas'} eq "View Control Panel Log") { &gm_viewcplog; }

if ($IN{'thomas'} eq "Add This Entry") { &gm_savenewentry; }
if ($IN{'thomas'} eq "Preview Before Posting") { &gm_previewentry; }

if ($IN{'thomas'} eq "Re-Edit This Entry") {
	if ($IN{'gmbmspecial'} eq "popupblog") { &gm_addentrypopup; } else { &gm_addentry; }
}

if ($IN{'thomas'} eq "Change View") { &gm_editentryselection; }
if ($IN{'thomas'} eq "Search") { &gm_editentryselection; }
if ($IN{'thomas'} eq "Edit Selected Entry") { &gm_editthisentry; }
if ($IN{'thomas'} eq "Open/Close Selected Entry") { &gm_changeentryopenstatus; }
if ($IN{'thomas'} eq "Search And Replace Across All Entries") { &gm_editentrysearchandreplace; }

if ($IN{'thomas'} eq "Edit Selected Comment") { &gm_editselectedcomment; }
if ($IN{'thomas'} eq "Delete Selected Comment") { &gm_deleteselectedcomment; }
if ($IN{'thomas'} eq "Save Changes To This Entry") { &gm_saveentrychanges; }
if ($IN{'thomas'} eq "Select Another Entry") { &gm_editentryselection; }

if ($IN{'thomas'} eq "Return To Entry Selection") { &gm_editentryselection; }

if ($IN{'thomas'} eq "Perform Search And Replace") { &gm_performsearchandreplace; }

if ($IN{'thomas'} eq "Save Changes To This Comment") { &gm_savecommentchanges; }
if ($IN{'thomas'} eq "Return To Entry Editing") { &gm_editthisentry; }

if ($IN{'thomas'} eq "Add New IP") { &gm_addbannedip; }
if ($IN{'thomas'} eq "Delete Selected IP") { &gm_deletebannedip; }

if ($IN{'thomas'} eq "Diagnostics & Repair") { &gm_diagnosticscheck; }
if ($IN{'thomas'} eq "Save Configuration") { &gm_saveconfiguration; }

if ($IN{'thomas'} eq "Perform Diagnostics & Repair") { &gm_diagnosticsperform; }
if ($IN{'thomas'} eq "Return To Configuration") { &gm_configuration; }

if ($IN{'thomas'} eq "Edit Main Index-Related Templates") { &gm_editmainindextemplates; }
if ($IN{'thomas'} eq "Edit Archive-Related Templates") { &gm_editarchivetemplates; }
if ($IN{'thomas'} eq "Edit Entry Page-Related Templates") { &gm_editentrypagetemplates; }
if ($IN{'thomas'} eq "Edit Karma & Comments-Related Templates") { &gm_editkarmacommentstemplates; }
if ($IN{'thomas'} eq "Edit Header, Footer & Sidebar Templates") { &gm_editheaderfootertemplates; }
if ($IN{'thomas'} eq "Edit Miscellaneous Templates") { &gm_editmisctemplates; }

if ($IN{'thomas'} eq "Return To Templates Menu") { &gm_edittemplates; }
if ($IN{'thomas'} eq "Save Template Changes") { &gm_savetemplatechanges; }

if ($IN{'thomas'} eq "Edit Selected Author") { &gm_editselectedauthor; }
if ($IN{'thomas'} eq "Delete Selected Author") { &gm_deleteselectedauthor; }
if ($IN{'thomas'} eq "Create New Author") { &gm_createnewauthor; }

if ($IN{'thomas'} eq "Save Changes To This Author") { &gm_saveauthorchanges; }
if ($IN{'thomas'} eq "Return To Author Panel") { &gm_editauthors; }

if ($IN{'thomas'} eq "Upload This File") { &gm_processupload; }

if ($IN{'thomas'} eq "Rebuild Last Entry Page Only") { &gm_rebuildlastentrypageonly; }
if ($IN{'thomas'} eq "Rebuild Main Index File") { &gm_rebuildmainindexfile; }
if ($IN{'thomas'} eq "Rebuild Main Entry Pages") { &gm_rebuildmainentrypages; }
if ($IN{'thomas'} eq "Rebuild Archive Master Index") { &gm_rebuildarchivemasterindex; }
if ($IN{'thomas'} eq "Rebuild Archive Log Indexes") { &gm_rebuildarchivelogindexes; }
if ($IN{'thomas'} eq "Rebuild Archive Entry Pages") { &gm_rebuildarchiveentrypages; }
if ($IN{'thomas'} eq "Rebuild All Entry Pages") { &gm_rebuildallentrypages; }
if ($IN{'thomas'} eq "Rebuild Connected Files") { &gm_rebuildconnectedfilescheck; }
if ($IN{'thomas'} eq "Rebuild Everything") { &gm_rebuildeverything; }

if ($IN{'thomas'} eq "Clear And Exit") {
	unlink ("$EntriesPath/gmrightclick-$IN{'usethisauthorname'}.reg");
	&gm_frontpage;
}

if ($IN{'thomas'} eq "Reset The Control Panel Log") { &gm_resetcplog; }

if ($IN{'thomas'} eq "Include This Image In A New Entry") { &gm_addentry; }
if ($IN{'thomas'} eq "Include In Entry As A Popup Window") {
	$IN{'newentrymaintext'} = $IN{'newentrypopuptext'};
	&gm_addentry;
}
if ($IN{'thomas'} eq "Include This Link In A New Entry") { &gm_addentry; }

exit;

# ------------------------
# front page - log options
# ------------------------

sub gm_frontpage {

&gm_readconfig;

if (($cgilocalpath eq "") || ($cgiwebpath eq "") || ($LogPath eq "") || ($EntriesPath eq "") || ($LogWebPath eq "") || ($EntriesWebPath eq "")) {

	if (($cgilocalpath eq "") && ($LogPath ne "")) { $cgilocalpath = $LogPath; }
	if (($cgiwebpath eq "") && ($LogWebPath ne "")) { $cgiwebpath = $LogWebPath; }

	if ($cgilocalpath eq "") {
		if ($ENV{'SCRIPT_FILENAME'}) { $cgilocalpath = $ENV{'SCRIPT_FILENAME'}; }
		elsif ($ENV{'PATH_TRANSLATED'}) {
			$cgilocalpath = $ENV{'PATH_TRANSLATED'};
			$cgilocalpath =~ s/\\/\//g; 
		}
		@cgilocalpathtemp = split(/\//, $cgilocalpath);
		pop(@cgilocalpathtemp);
		$cgilocalpath = join("\/", @cgilocalpathtemp);
	}

	@cgipath = split(/\//, $cgilocalpath);
	$cgiwebpathextension = pop(@cgipath);

	if ($cgiwebpath eq "") { $cgiwebpath = "http://$ENV{'HTTP_HOST'}/$cgiwebpathextension"; }

	if ($LogPath eq "") { $LogPath = $cgilocalpath; }
	if ($EntriesPath eq "") { $EntriesPath = ("$cgilocalpath" . "/archives"); }
	if ($LogWebPath eq "") { $LogWebPath = "http://$ENV{'HTTP_HOST'}/$cgiwebpathextension"; }
	if ($EntriesWebPath eq "") { $EntriesWebPath = "http://$ENV{'HTTP_HOST'}/$cgiwebpathextension/archives"; }

	&gm_writeconfig;

}

&gm_validate;

if ($gmloginaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to log in without authorization");
	$loginnotice = qq(<B><FONT COLOR="#FF0000">You don't have access to log in.</FONT></B><P>);
	&gm_login;
}

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Main Menu</FONT></B><P>); }

if (($IN{'authorname'} eq "Alice") && ($IN{'authorpassword'} eq "wonderland")) {
	$setnameandpwcookie = "";
} else {
	$setnameandpwcookie = "<SCRIPT TYPE=\"text/javascript\" LANGUAGE=\"JavaScript\">\n<!--//\nvar now = new Date();\nfixDate(now);\nnow.setTime(now.getTime() + 365 * 24 * 60 * 60 * 1000);\nsetCookie(\"gmcookiename\", \"$IN{'authorname'}\", now);\nsetCookie(\"gmcookiepw\", \"$IN{'authorpassword'}\", now);\n//-->\n</SCRIPT>";
}

if ($cookiesallowed eq "no") {
	$setnameandpwcookie = "";
}

$visityoursitelink = "";

unless (!(open(CHECKMATE,"$LogPath/$indexfilename"))) {
	&gm_readcounter;
	unless ($newentrynumber eq "0") {
		$indexfilenamesmartcheck = "/$indexfilename";
		$indexfilenameprefix = substr($indexfilename, 0, 6);
		if ($indexfilenameprefix eq "index.") { $indexfilenamesmartcheck = "/"; }
		$visityoursitelink = qq(<FORM ACTION="$LogWebPath$indexfilenamesmartcheck" TARGET="NEW">\n<TR><TD VALIGN=TOP ALIGN=CENTER COLSPAN=2>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" VALUE="Visit Your Site" STYLE="background: #D0FFD0; width: 500"><BR>Open your weblog/journal in a new browser window.</FONT></FONT></TD></TR>\n</FORM>);
	}
}
close(CHECKMATE);

print<<GMFRONTPAGE;

$gmheadtag

$gmframetop
$statusnote
$setnameandpwcookie
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<TABLE BORDER=0 CELLPADDING=10 CELLSPACING=0 WIDTH=520>
<TR><TD VALIGN=TOP ALIGN=CENTER COLSPAN=2>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Add A New Entry" STYLE="background: #D0FFD0; width: 500"><BR>Post a new entry to your weblog/journal.</FONT></FONT></TD></TR>

<TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Configuration"><BR>Your site's settings and options.</FONT></FONT></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit An Entry"><BR>Edit and delete entries or comments.</FONT></FONT></TD></TR>

<TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit Templates"><BR>Change your site's layout and appearance.</FONT></FONT></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit Authors"><BR>Edit or add authors to post to your site.</FONT></FONT></TD></TR>

<TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Rebuild Files"><BR>Regenerate part or all of your site.</FONT></FONT></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="View Control Panel Log"><BR>A record of how your site's been used.</FONT></FONT></TD></TR>

<TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Add Bookmarklets"><BR>Post entries with one click (IE 5+ only).</FONT></FONT></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Upload Files"><BR>Upload images or other files to your site.</FONT></FONT></TD></TR>

<TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit Banned IP List"><BR>Ban someone from using your site.</FONT></FONT></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Re-Login"><BR>Re-enter as another author.</FONT></FONT></TD></TR>

</FORM>

$visityoursitelink

</TABLE>
<P>
<FONT SIZE=1>"Our life is what our thoughts make it."&#151;Marcus Aurelius</FONT>
$gmframebottom

</BODY>
</HTML>

GMFRONTPAGE

$statusnote = "";

exit;

}

# ----------------
# templates editor
# ----------------

sub gm_edittemplates {

&gm_validate;

if ($gmtemplateaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the templates without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the templates.</FONT></B><P>);
	&gm_frontpage;
}

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Edit Templates</FONT></B><BR><FONT SIZE=1>Select a group of templates to edit.  Templates control<BR>the layout & format of every aspect of your weblog/journal.</FONT><P>); }

if ($gmtemplateaccess eq "hfsonly") {
	$statusnote .= "<B>You only have access to edit the header, footer & sidebar templates.</B><P>";
}

print<<GMEDITTEMPLATESMENU;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit Main Index-Related Templates" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit Archive-Related Templates" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit Entry Page-Related Templates" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit Karma & Comments-Related Templates" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit Header, Footer & Sidebar Templates" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Edit Miscellaneous Templates" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="width: 320; background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"Art is the imposing of a pattern on experience, and our aesthetic<BR>enjoyment is recognition of the pattern."&#151;A.N. Whitehead</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITTEMPLATESMENU

$statusnote = "";

exit;

}

# -------------------------------
# edit template group: main index
# -------------------------------

sub gm_editmainindextemplates {

&gm_validate;

if (($gmtemplateaccess eq "no") || ($gmtemplateaccess eq "hfsonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the main index templates without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the main index templates.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readtemplates;

&gm_delousealltemplates;

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Editing Main Index-Related Templates</FONT></B><BR><FONT SIZE=1>These are the templates that affect the layout and appearance of your main index.</FONT><P>); }

if ($gmrebuildaccess eq "yes") {
	if ($automaticrebuilddefault eq "yes") {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="index" CHECKED> Automatically rebuild main index after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	} else {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="index"> Automatically rebuild main index after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	}
}

&gm_readcounter;
if ($newentrynumber eq "0") { $autorebuildcheckbox = ""; }

print<<GMEDITMAININDEXTEMPLATES;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="modifiedtemplategroup" VALUE="main index">

<INPUT TYPE=HIDDEN NAME="newentrypagetemplate" VALUE="$gmentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveindextemplate" VALUE="$gmarchiveindextemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrypagetemplate" VALUE="$gmarchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrytemplate" VALUE="$gmarchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newcommentstemplate" VALUE="$gmcommentstemplate">
<INPUT TYPE=HIDDEN NAME="newcommentsformtemplate" VALUE="$gmcommentsformtemplate">
<INPUT TYPE=HIDDEN NAME="newparaseparationtemplate" VALUE="$gmparaseparationtemplate">
<INPUT TYPE=HIDDEN NAME="newkarmaformtemplate" VALUE="$gmkarmaformtemplate">
<INPUT TYPE=HIDDEN NAME="newmoreprefacetemplate" VALUE="$gmmoreprefacetemplate">
<INPUT TYPE=HIDDEN NAME="newmorelinktemplate" VALUE="$gmmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newkarmalinktemplate" VALUE="$gmkarmalinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentslinktemplate" VALUE="$gmcommentslinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthoremailtemplate" VALUE="$gmcommentauthoremailtemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthorhomepagetemplate" VALUE="$gmcommentauthorhomepagetemplate">
<INPUT TYPE=HIDDEN NAME="newcommentdividertemplate" VALUE="$gmcommentdividertemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagetemplate" VALUE="$gmmoreentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrypagetemplate" VALUE="$gmmorearchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newpreviouslinktemplate" VALUE="$gmpreviouslinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextlinktemplate" VALUE="$gmnextlinktemplate">
<INPUT TYPE=HIDDEN NAME="newpreviousmorelinktemplate" VALUE="$gmpreviousmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextmorelinktemplate" VALUE="$gmnextmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newarchivemasterindextemplate" VALUE="$gmarchivemasterindextemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinktemplate" VALUE="$gmlogarchiveslinktemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinktemplate" VALUE="$gmentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagelinktemplate" VALUE="$gmmoreentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkseparatortemplate" VALUE="$gmlogarchiveslinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkseparatortemplate" VALUE="$gmentrypagelinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkmonthseparatortemplate" VALUE="$gmentrypagelinkmonthseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkdayseparatortemplate" VALUE="$gmentrypagelinkdayseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkyearseparatortemplate" VALUE="$gmentrypagelinkyearseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newheadertemplate" VALUE="$gmheadertemplate">
<INPUT TYPE=HIDDEN NAME="newfootertemplate" VALUE="$gmfootertemplate">
<INPUT TYPE=HIDDEN NAME="newsidebartemplate" VALUE="$gmsidebartemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentryseparatortemplate" VALUE="$gmarchiveentryseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrytemplate" VALUE="$gmmorearchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newdatearchivetemplate" VALUE="$gmdatearchivetemplate">

<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkweeklytemplate" VALUE="$gmlogarchiveslinkweeklytemplate">
<INPUT TYPE=HIDDEN NAME="newcustomonetemplate" VALUE="$gmcustomonetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtwotemplate" VALUE="$gmcustomtwotemplate">
<INPUT TYPE=HIDDEN NAME="newcustomthreetemplate" VALUE="$gmcustomthreetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfourtemplate" VALUE="$gmcustomfourtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfivetemplate" VALUE="$gmcustomfivetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomsixtemplate" VALUE="$gmcustomsixtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomseventemplate" VALUE="$gmcustomseventemplate">
<INPUT TYPE=HIDDEN NAME="newcustomeighttemplate" VALUE="$gmcustomeighttemplate">
<INPUT TYPE=HIDDEN NAME="newcustomninetemplate" VALUE="$gmcustomninetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtentemplate" VALUE="$gmcustomtentemplate">
<INPUT TYPE=HIDDEN NAME="newpopuppagetemplate" VALUE="$gmpopuppagetemplate">
<INPUT TYPE=HIDDEN NAME="newpopupcodetemplate" VALUE="$gmpopupcodetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchformtemplate" VALUE="$gmsearchformtemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultspagetemplate" VALUE="$gmsearchresultspagetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultsentrytemplate" VALUE="$gmsearchresultsentrytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartablebeginningtemplate" VALUE="$gmcalendartablebeginningtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartableendingtemplate" VALUE="$gmcalendartableendingtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarblankcelltemplate" VALUE="$gmcalendarblankcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelltemplate" VALUE="$gmcalendarfullcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelllinktemplate" VALUE="$gmcalendarfullcelllinktemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaytemplate" VALUE="$gmcalendarweekfulldaytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaylinktemplate" VALUE="$gmcalendarweekfulldaylinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewdividertemplate" VALUE="$gmcommentpreviewdividertemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewformtemplate" VALUE="$gmcommentpreviewformtemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinknocommentstemplate" VALUE="$gmsmartlinknocommentstemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkonecommenttemplate" VALUE="$gmsmartlinkonecommenttemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkmanycommentstemplate" VALUE="$gmsmartlinkmanycommentstemplate">
<INPUT TYPE=HIDDEN NAME="newlinebreaktemplate" VALUE="$gmlinebreaktemplate">

<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=720>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Main Index Template</B><BR><FONT SIZE=1>The overall template for your main index page&#151;typically the first page that people will see on your weblog/journal.  The {{logbody}} variable is the placeholder that tells Greymatter where you want the body of your log to be inserted, so it must be included somewhere in this template.  The format of the log body is controlled through the templates below.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newindextemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmindextemplate</TEXTAREA>$gmfonttag</FONT></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Index Entry Templates</B><BR><FONT SIZE=1>These templates control how individual entries are listed in the body of your log.  The left template is the format of standard entry listings, and the right template is the format of extended entry listings (entries that contain "more" text).</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Index Entry Template: Standard Entries</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Index Entry Template: Extended Entries</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newentrytemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmentrytemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newmoreentrytemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmmoreentrytemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="entrylistingmorecheck" VALUE="yes"> Make this the same as the template on the left</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#D0D0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Date Grouping Template</B><BR><FONT SIZE=1>When your log is generated, the entry listings for each day are prefaced with a date header; this controls how that date header appears.  Leave this blank if you don't want to group your entry listings in this way.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#D0D0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Entry Separator Template</B><BR><FONT SIZE=1>If you wish, you can have your entry listings divided with a special separator when your log is generated.  Leave this blank if you don't want to include a separator.<BR>&#160;</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newdatetemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmdatetemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newentryseparatortemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmentryseparatortemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD VALIGN=TOP ALIGN=CENTER><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#D0D0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>"Stay At Top" Index Entry Template</B><BR><FONT SIZE=1>Like the index entry templates above, except this will apply to any entry you've marked to stay at the top of your main log (only one entry at a time can be marked as such); use this for any way you might wish to set that apart.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newstayattoptemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmstayattoptemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="entrylistingstayattopcheck" VALUE="yes"> Make this the same as the standard index entry template</FONT></TD></TR></TABLE></TD></TR>

</TABLE>
$autorebuildcheckbox
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Template Changes"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Templates Menu">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"The face is the index of a feeling mind."&#151;George Crabbe</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITMAININDEXTEMPLATES

$statusnote = "";

exit;

}

# -----------------------------
# edit template group: archives
# -----------------------------

sub gm_editarchivetemplates {

&gm_validate;

if (($gmtemplateaccess eq "no") || ($gmtemplateaccess eq "hfsonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the archive templates without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the archive templates.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readtemplates;

&gm_delousealltemplates;

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Editing Archive-Related Templates</FONT></B><BR><FONT SIZE=1>These are the templates that affect the layout and appearance of your archives.</FONT><P>); }

$autorebuildcheckbox = "";

if ($gmrebuildaccess eq "yes") {
	if ($automaticrebuilddefault eq "yes") {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="archiveindexes" CHECKED> Automatically rebuild archive master index and log indexes after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	} else {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="archiveindexes"> Automatically rebuild archive master index and log indexes after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	}
}

&gm_readcounter;
if ($newentrynumber eq "0") { $autorebuildcheckbox = ""; }

print<<GMEDITARCHIVETEMPLATES;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="modifiedtemplategroup" VALUE="archive">

<INPUT TYPE=HIDDEN NAME="newindextemplate" VALUE="$gmindextemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagetemplate" VALUE="$gmentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrypagetemplate" VALUE="$gmarchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newentrytemplate" VALUE="$gmentrytemplate">
<INPUT TYPE=HIDDEN NAME="newstayattoptemplate" VALUE="$gmstayattoptemplate">
<INPUT TYPE=HIDDEN NAME="newdatetemplate" VALUE="$gmdatetemplate">
<INPUT TYPE=HIDDEN NAME="newcommentstemplate" VALUE="$gmcommentstemplate">
<INPUT TYPE=HIDDEN NAME="newcommentsformtemplate" VALUE="$gmcommentsformtemplate">
<INPUT TYPE=HIDDEN NAME="newparaseparationtemplate" VALUE="$gmparaseparationtemplate">
<INPUT TYPE=HIDDEN NAME="newkarmaformtemplate" VALUE="$gmkarmaformtemplate">
<INPUT TYPE=HIDDEN NAME="newmoreprefacetemplate" VALUE="$gmmoreprefacetemplate">
<INPUT TYPE=HIDDEN NAME="newmorelinktemplate" VALUE="$gmmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newkarmalinktemplate" VALUE="$gmkarmalinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentslinktemplate" VALUE="$gmcommentslinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthoremailtemplate" VALUE="$gmcommentauthoremailtemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthorhomepagetemplate" VALUE="$gmcommentauthorhomepagetemplate">
<INPUT TYPE=HIDDEN NAME="newcommentdividertemplate" VALUE="$gmcommentdividertemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrytemplate" VALUE="$gmmoreentrytemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagetemplate" VALUE="$gmmoreentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrypagetemplate" VALUE="$gmmorearchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newpreviouslinktemplate" VALUE="$gmpreviouslinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextlinktemplate" VALUE="$gmnextlinktemplate">
<INPUT TYPE=HIDDEN NAME="newpreviousmorelinktemplate" VALUE="$gmpreviousmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextmorelinktemplate" VALUE="$gmnextmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinktemplate" VALUE="$gmlogarchiveslinktemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinktemplate" VALUE="$gmentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagelinktemplate" VALUE="$gmmoreentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkseparatortemplate" VALUE="$gmlogarchiveslinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkseparatortemplate" VALUE="$gmentrypagelinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkmonthseparatortemplate" VALUE="$gmentrypagelinkmonthseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkdayseparatortemplate" VALUE="$gmentrypagelinkdayseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkyearseparatortemplate" VALUE="$gmentrypagelinkyearseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newheadertemplate" VALUE="$gmheadertemplate">
<INPUT TYPE=HIDDEN NAME="newfootertemplate" VALUE="$gmfootertemplate">
<INPUT TYPE=HIDDEN NAME="newsidebartemplate" VALUE="$gmsidebartemplate">
<INPUT TYPE=HIDDEN NAME="newentryseparatortemplate" VALUE="$gmentryseparatortemplate">

<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkweeklytemplate" VALUE="$gmlogarchiveslinkweeklytemplate">
<INPUT TYPE=HIDDEN NAME="newcustomonetemplate" VALUE="$gmcustomonetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtwotemplate" VALUE="$gmcustomtwotemplate">
<INPUT TYPE=HIDDEN NAME="newcustomthreetemplate" VALUE="$gmcustomthreetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfourtemplate" VALUE="$gmcustomfourtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfivetemplate" VALUE="$gmcustomfivetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomsixtemplate" VALUE="$gmcustomsixtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomseventemplate" VALUE="$gmcustomseventemplate">
<INPUT TYPE=HIDDEN NAME="newcustomeighttemplate" VALUE="$gmcustomeighttemplate">
<INPUT TYPE=HIDDEN NAME="newcustomninetemplate" VALUE="$gmcustomninetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtentemplate" VALUE="$gmcustomtentemplate">
<INPUT TYPE=HIDDEN NAME="newpopuppagetemplate" VALUE="$gmpopuppagetemplate">
<INPUT TYPE=HIDDEN NAME="newpopupcodetemplate" VALUE="$gmpopupcodetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchformtemplate" VALUE="$gmsearchformtemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultspagetemplate" VALUE="$gmsearchresultspagetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultsentrytemplate" VALUE="$gmsearchresultsentrytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartablebeginningtemplate" VALUE="$gmcalendartablebeginningtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartableendingtemplate" VALUE="$gmcalendartableendingtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarblankcelltemplate" VALUE="$gmcalendarblankcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelltemplate" VALUE="$gmcalendarfullcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelllinktemplate" VALUE="$gmcalendarfullcelllinktemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaytemplate" VALUE="$gmcalendarweekfulldaytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaylinktemplate" VALUE="$gmcalendarweekfulldaylinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewdividertemplate" VALUE="$gmcommentpreviewdividertemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewformtemplate" VALUE="$gmcommentpreviewformtemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinknocommentstemplate" VALUE="$gmsmartlinknocommentstemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkonecommenttemplate" VALUE="$gmsmartlinkonecommenttemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkmanycommentstemplate" VALUE="$gmsmartlinkmanycommentstemplate">
<INPUT TYPE=HIDDEN NAME="newlinebreaktemplate" VALUE="$gmlinebreaktemplate">

<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=720>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Archive Master Index Template</B><BR><FONT SIZE=1>If you wish, you can keep a master index of your archives&#151;an index page in your entries/archives directory intended for linking to all the archives (both the monthly/weekly logs and the individual entry pages) of your site.  You can use variables such as {{logarchivelist}} and {{logentrylist}} here (or anywhere) to generate those list links; check the manual for more information about those variables.  If you don't wish to keep an archive master index, you can disable it in Configuration.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newarchivemasterindextemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmarchivemasterindextemplate</TEXTAREA>$gmfonttag</FONT></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Archive Log Index Template</B><BR><FONT SIZE=1>Archive log index files are the archives of your log; this is like the main index except that the log archives are generated in monthly or weekly installments, each installment showing the full log for that given month or week.  As with the main index, {{logbody}} (or {{archivebody}}) is the placeholder that tells Greymatter where to put the body of your log.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newarchiveindextemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmarchiveindextemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="archivelogindexcheck" VALUE="yes"> Make this the same as the main index template</FONT></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Log Archive Entry Templates</B><BR><FONT SIZE=1>These templates control how individual entries are listed in the body of your log; these work the same as the main index versions, except this controls how they appear in the log archives instead.  The left template is the format of standard entry listings, and the right template is the format of extended entry listings (entries that contain "more" text).</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Archive Entry Template: Standard Entries</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Archive Entry Template: Extended Entries</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newarchiveentrytemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmarchiveentrytemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="archiveentrylistingcheck" VALUE="yes"> Make this the same as the main index version</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newmorearchiveentrytemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmmorearchiveentrytemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="archiveentrylistingmorecheck" VALUE="yes"> Make this the same as the main index version</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#D0D0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Archive Date Grouping Template</B><BR><FONT SIZE=1>When your log is generated, the entry listings for each day are prefaced with a date header; this controls how that date header appears.  This works the same as it does on the main index, except this is how the date header will appear in your log archives.  Leave this blank if you don't want to group your entry listings in this way.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#D0D0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Archive Entry Separator Template</B><BR><FONT SIZE=1>If you wish, you can have your entry listings divided with a special separator when your log is generated.  This works the same as it does on the main index, except this is the separator for entries in your log archives.  Leave this blank if you don't want to include a separator.<BR>&#160;</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newdatearchivetemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmdatearchivetemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="archivedateheadercheck" VALUE="yes"> Make this the same as the main index version</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newarchiveentryseparatortemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmarchiveentryseparatortemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="archiveentryseparatorcheck" VALUE="yes"> Make this the same as the main index version</FONT></FONT></TD></TR></TABLE></TD></TR>

</TABLE>
$autorebuildcheckbox
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Template Changes"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Templates Menu">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"History never looks like history when you're living through it."&#151;John Gardner</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITARCHIVETEMPLATES

$statusnote = "";

exit;

}

# --------------------------------
# edit template group: entry pages
# --------------------------------

sub gm_editentrypagetemplates {

&gm_validate;

if (($gmtemplateaccess eq "no") || ($gmtemplateaccess eq "hfsonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the entry page templates without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the entry page templates.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readtemplates;

&gm_delousealltemplates;

if ($statusnote eq "") { $statusnote = qq(<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=720><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B><FONT COLOR="#000000">Editing Entry Page-Related Templates</FONT></B><BR><FONT SIZE=1>These are the templates that affect the layout and appearance of the pages for your individual entries (as opposed to the Index Entry templates, in the Main Index and Archive template groups, which customise how entries appear in the body of your log).  If you have "Generate pages for individual entries" disabled in Configuration, you can ignore these templates.</FONT></TD></TR></TABLE><P>); }

$autorebuildcheckbox = "";

if ($gmrebuildaccess eq "yes") {
	if ($automaticrebuilddefault eq "yes") {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="entrypages" CHECKED> Automatically rebuild all entry pages after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	} else {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="entrypages"> Automatically rebuild all entry pages after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	}
}

&gm_readcounter;
if ($newentrynumber eq "0") { $autorebuildcheckbox = ""; }

print<<GMEDITENTRYPAGETEMPLATES;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="modifiedtemplategroup" VALUE="entry page">

<INPUT TYPE=HIDDEN NAME="newindextemplate" VALUE="$gmindextemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveindextemplate" VALUE="$gmarchiveindextemplate">
<INPUT TYPE=HIDDEN NAME="newentrytemplate" VALUE="$gmentrytemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrytemplate" VALUE="$gmarchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newstayattoptemplate" VALUE="$gmstayattoptemplate">
<INPUT TYPE=HIDDEN NAME="newdatetemplate" VALUE="$gmdatetemplate">
<INPUT TYPE=HIDDEN NAME="newcommentstemplate" VALUE="$gmcommentstemplate">
<INPUT TYPE=HIDDEN NAME="newcommentsformtemplate" VALUE="$gmcommentsformtemplate">
<INPUT TYPE=HIDDEN NAME="newparaseparationtemplate" VALUE="$gmparaseparationtemplate">
<INPUT TYPE=HIDDEN NAME="newkarmaformtemplate" VALUE="$gmkarmaformtemplate">
<INPUT TYPE=HIDDEN NAME="newmoreprefacetemplate" VALUE="$gmmoreprefacetemplate">
<INPUT TYPE=HIDDEN NAME="newmorelinktemplate" VALUE="$gmmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newkarmalinktemplate" VALUE="$gmkarmalinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentslinktemplate" VALUE="$gmcommentslinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthoremailtemplate" VALUE="$gmcommentauthoremailtemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthorhomepagetemplate" VALUE="$gmcommentauthorhomepagetemplate">
<INPUT TYPE=HIDDEN NAME="newcommentdividertemplate" VALUE="$gmcommentdividertemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrytemplate" VALUE="$gmmoreentrytemplate">
<INPUT TYPE=HIDDEN NAME="newpreviouslinktemplate" VALUE="$gmpreviouslinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextlinktemplate" VALUE="$gmnextlinktemplate">
<INPUT TYPE=HIDDEN NAME="newpreviousmorelinktemplate" VALUE="$gmpreviousmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextmorelinktemplate" VALUE="$gmnextmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newarchivemasterindextemplate" VALUE="$gmarchivemasterindextemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinktemplate" VALUE="$gmlogarchiveslinktemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinktemplate" VALUE="$gmentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagelinktemplate" VALUE="$gmmoreentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkseparatortemplate" VALUE="$gmlogarchiveslinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkseparatortemplate" VALUE="$gmentrypagelinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkmonthseparatortemplate" VALUE="$gmentrypagelinkmonthseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkdayseparatortemplate" VALUE="$gmentrypagelinkdayseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkyearseparatortemplate" VALUE="$gmentrypagelinkyearseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newheadertemplate" VALUE="$gmheadertemplate">
<INPUT TYPE=HIDDEN NAME="newfootertemplate" VALUE="$gmfootertemplate">
<INPUT TYPE=HIDDEN NAME="newsidebartemplate" VALUE="$gmsidebartemplate">
<INPUT TYPE=HIDDEN NAME="newentryseparatortemplate" VALUE="$gmentryseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentryseparatortemplate" VALUE="$gmarchiveentryseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrytemplate" VALUE="$gmmorearchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newdatearchivetemplate" VALUE="$gmdatearchivetemplate">

<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkweeklytemplate" VALUE="$gmlogarchiveslinkweeklytemplate">
<INPUT TYPE=HIDDEN NAME="newcustomonetemplate" VALUE="$gmcustomonetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtwotemplate" VALUE="$gmcustomtwotemplate">
<INPUT TYPE=HIDDEN NAME="newcustomthreetemplate" VALUE="$gmcustomthreetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfourtemplate" VALUE="$gmcustomfourtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfivetemplate" VALUE="$gmcustomfivetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomsixtemplate" VALUE="$gmcustomsixtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomseventemplate" VALUE="$gmcustomseventemplate">
<INPUT TYPE=HIDDEN NAME="newcustomeighttemplate" VALUE="$gmcustomeighttemplate">
<INPUT TYPE=HIDDEN NAME="newcustomninetemplate" VALUE="$gmcustomninetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtentemplate" VALUE="$gmcustomtentemplate">
<INPUT TYPE=HIDDEN NAME="newpopuppagetemplate" VALUE="$gmpopuppagetemplate">
<INPUT TYPE=HIDDEN NAME="newpopupcodetemplate" VALUE="$gmpopupcodetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchformtemplate" VALUE="$gmsearchformtemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultspagetemplate" VALUE="$gmsearchresultspagetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultsentrytemplate" VALUE="$gmsearchresultsentrytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartablebeginningtemplate" VALUE="$gmcalendartablebeginningtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartableendingtemplate" VALUE="$gmcalendartableendingtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarblankcelltemplate" VALUE="$gmcalendarblankcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelltemplate" VALUE="$gmcalendarfullcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelllinktemplate" VALUE="$gmcalendarfullcelllinktemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaytemplate" VALUE="$gmcalendarweekfulldaytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaylinktemplate" VALUE="$gmcalendarweekfulldaylinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewdividertemplate" VALUE="$gmcommentpreviewdividertemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewformtemplate" VALUE="$gmcommentpreviewformtemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinknocommentstemplate" VALUE="$gmsmartlinknocommentstemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkonecommenttemplate" VALUE="$gmsmartlinkonecommenttemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkmanycommentstemplate" VALUE="$gmsmartlinkmanycommentstemplate">
<INPUT TYPE=HIDDEN NAME="newlinebreaktemplate" VALUE="$gmlinebreaktemplate">

<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=720>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Entry Page Template: Current Standard Entries</B><BR><FONT SIZE=1>This template controls how the individual pages for your current regular entries (non-archived entries without "more" text) will be formatted.  The {{entrymainbody}} and {{entrymorebody}} variables specify where the body of your standard and extended text (if any) will respectively appear.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newentrypagetemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmentrypagetemplate</TEXTAREA>$gmfonttag</FONT></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Entry Page Template: Current Extended Entries</B><BR><FONT SIZE=1>Like the above, except this applies to current extended entries (non-archived entries *with* "more" text).</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newmoreentrypagetemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmmoreentrypagetemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="entrymorepagecheck" VALUE="yes"> Make this the same as the above template (current standard entries)</FONT></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Entry Page Template: Archived Standard Entries</B><BR><FONT SIZE=1>Like the above, except this applies to archived entries (entries too old to be listed on the main log) without "more" text.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newarchiveentrypagetemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmarchiveentrypagetemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="entryarchivepagecheck" VALUE="yes"> Make this the same as the top template (current standard entries)</FONT></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Entry Page Template: Archived Extended Entries</B><BR><FONT SIZE=1>Like the above, except this applies to archived entries (entries too old to be listed on the main log) *with* "more" text.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newmorearchiveentrypagetemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmmorearchiveentrypagetemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="entrymorearchivepagecheck" VALUE="yes"> Make this the same as the previous template (archived standard entries)</FONT></TD></TR>

</TABLE>
$autorebuildcheckbox
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Template Changes"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Templates Menu">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"One of the few remaining freedoms we have is the blank page; no one can prescribe how we should fill it."&#151;James Kelman</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITENTRYPAGETEMPLATES

$statusnote = "";

exit;

}

# -------------------------------------
# edit template group: karma & comments
# -------------------------------------

sub gm_editkarmacommentstemplates {

&gm_validate;

if (($gmtemplateaccess eq "no") || ($gmtemplateaccess eq "hfsonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the karma & comments templates without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the karma & comments templates.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readtemplates;

&gm_delousealltemplates;

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Editing Karma & Comments-Related Templates</FONT></B><BR><FONT SIZE=1>These are the templates that affect all elements relating to karma voting and comment posting; if you have<BR>either or both of those disabled, you can ignore the templates relating to them.  All these templates<BR>affect things that will not appear on entries for which karma voting and/or comment posting is disabled.</FONT><P>); }

$autorebuildcheckbox = "";

if ($gmrebuildaccess eq "yes") {
	if ($automaticrebuilddefault eq "yes") {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="everything" CHECKED> Automatically rebuild all files after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	} else {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="everything"> Automatically rebuild all files after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	}
}

&gm_readcounter;
if ($newentrynumber eq "0") { $autorebuildcheckbox = ""; }

print<<GMEDITKARMACOMMENTSTEMPLATES;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="modifiedtemplategroup" VALUE="karma & comments">

<INPUT TYPE=HIDDEN NAME="newindextemplate" VALUE="$gmindextemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagetemplate" VALUE="$gmentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveindextemplate" VALUE="$gmarchiveindextemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrypagetemplate" VALUE="$gmarchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newentrytemplate" VALUE="$gmentrytemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrytemplate" VALUE="$gmarchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newstayattoptemplate" VALUE="$gmstayattoptemplate">
<INPUT TYPE=HIDDEN NAME="newdatetemplate" VALUE="$gmdatetemplate">
<INPUT TYPE=HIDDEN NAME="newparaseparationtemplate" VALUE="$gmparaseparationtemplate">
<INPUT TYPE=HIDDEN NAME="newmoreprefacetemplate" VALUE="$gmmoreprefacetemplate">
<INPUT TYPE=HIDDEN NAME="newmorelinktemplate" VALUE="$gmmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrytemplate" VALUE="$gmmoreentrytemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagetemplate" VALUE="$gmmoreentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrypagetemplate" VALUE="$gmmorearchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newpreviouslinktemplate" VALUE="$gmpreviouslinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextlinktemplate" VALUE="$gmnextlinktemplate">
<INPUT TYPE=HIDDEN NAME="newpreviousmorelinktemplate" VALUE="$gmpreviousmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextmorelinktemplate" VALUE="$gmnextmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newarchivemasterindextemplate" VALUE="$gmarchivemasterindextemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinktemplate" VALUE="$gmlogarchiveslinktemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinktemplate" VALUE="$gmentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagelinktemplate" VALUE="$gmmoreentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkseparatortemplate" VALUE="$gmlogarchiveslinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkseparatortemplate" VALUE="$gmentrypagelinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkmonthseparatortemplate" VALUE="$gmentrypagelinkmonthseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkdayseparatortemplate" VALUE="$gmentrypagelinkdayseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkyearseparatortemplate" VALUE="$gmentrypagelinkyearseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newheadertemplate" VALUE="$gmheadertemplate">
<INPUT TYPE=HIDDEN NAME="newfootertemplate" VALUE="$gmfootertemplate">
<INPUT TYPE=HIDDEN NAME="newsidebartemplate" VALUE="$gmsidebartemplate">
<INPUT TYPE=HIDDEN NAME="newentryseparatortemplate" VALUE="$gmentryseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentryseparatortemplate" VALUE="$gmarchiveentryseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrytemplate" VALUE="$gmmorearchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newdatearchivetemplate" VALUE="$gmdatearchivetemplate">

<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkweeklytemplate" VALUE="$gmlogarchiveslinkweeklytemplate">
<INPUT TYPE=HIDDEN NAME="newcustomonetemplate" VALUE="$gmcustomonetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtwotemplate" VALUE="$gmcustomtwotemplate">
<INPUT TYPE=HIDDEN NAME="newcustomthreetemplate" VALUE="$gmcustomthreetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfourtemplate" VALUE="$gmcustomfourtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfivetemplate" VALUE="$gmcustomfivetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomsixtemplate" VALUE="$gmcustomsixtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomseventemplate" VALUE="$gmcustomseventemplate">
<INPUT TYPE=HIDDEN NAME="newcustomeighttemplate" VALUE="$gmcustomeighttemplate">
<INPUT TYPE=HIDDEN NAME="newcustomninetemplate" VALUE="$gmcustomninetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtentemplate" VALUE="$gmcustomtentemplate">
<INPUT TYPE=HIDDEN NAME="newpopuppagetemplate" VALUE="$gmpopuppagetemplate">
<INPUT TYPE=HIDDEN NAME="newpopupcodetemplate" VALUE="$gmpopupcodetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchformtemplate" VALUE="$gmsearchformtemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultspagetemplate" VALUE="$gmsearchresultspagetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultsentrytemplate" VALUE="$gmsearchresultsentrytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartablebeginningtemplate" VALUE="$gmcalendartablebeginningtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartableendingtemplate" VALUE="$gmcalendartableendingtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarblankcelltemplate" VALUE="$gmcalendarblankcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelltemplate" VALUE="$gmcalendarfullcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelllinktemplate" VALUE="$gmcalendarfullcelllinktemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaytemplate" VALUE="$gmcalendarweekfulldaytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaylinktemplate" VALUE="$gmcalendarweekfulldaylinktemplate">
<INPUT TYPE=HIDDEN NAME="newlinebreaktemplate" VALUE="$gmlinebreaktemplate">

<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=720>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>{{karmalink}} and {{commentslink}} Templates</B><BR><FONT SIZE=1>These templates are what will appear wherever the {{karmalink}} and {{commentslink}} are used, but only when called for; the contents of {{commentslink}} will only appear on entries for which comments can be posted to, and the same with {{karmalink}}.  The default approach is to use {{karmalink}} to contain the links for voting on karma and {{commentslink}} for a link to your entry's comments, but you can use these templates to set anything that will appear, wherever you insert their respective variables, only for entries with karma or comments enabled respectively.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{karmalink}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{commentslink}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newkarmalinktemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmkarmalinktemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcommentslinktemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmcommentslinktemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#D0D0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Comment Appearance Template</B><BR><FONT SIZE=1>Whenever comments are added to your entries, this is the template which the comments will be formatted by.<BR>&#160;<BR>&#160;</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#D0D0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{entrycommentsform}} Posting Form</B><BR><FONT SIZE=1>This is the form  by which visitors can add comments (appearing whereever {{entrycommentsform}} is used).  You can change the form's design, but the "NAME", "VALUE" and "ACTION" values must remain the same.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcommentstemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmcommentstemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcommentsformtemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmcommentsformtemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#D0D0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{commentdivider}} Template</B><BR><FONT SIZE=1>The {{commentdivider}} variable (whatever you set below) will only appear if at least one comment has been posted to that entry; for example, if you want to have something that says "This entry has received X comments" in an entry, but don't want that to appear if there haven't been any comments posted to it yet.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#D0D0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{karmaform}} Template</B><BR><FONT SIZE=1>Just like {{karmalink}} above, this will only appear on karma-enabled entries; this is intended to allow a handling of karma voting on individual entry pages distinct from the main log, if you wish to do that.<BR>&#160;<BR>&#160;</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcommentdividertemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmcommentdividertemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newkarmaformtemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmkarmaformtemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Comment Previewing Templates</B><BR><FONT SIZE=1>If you allow visitors to preview their comments before posting them (to enable this, add a &lt;INPUT TYPE=SUBMIT NAME="gmpostpreview" VALUE="Preview Your Comment"&gt; button [the "value" text can be changed to whatever you wish, as long as you keep the NAME="gmpostpreview" part] to your entry comments form, if it's not there already), these templates control what special information will appear (the comment is shown to the user as it would appear in your entry's page).  The Preview Divider is what will appear in the preview where {{commentdivider}} (see above) is, and the Confirmation Form takes the place of {{entrycommentsform}} above.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Preview Divider Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Confirmation Form Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcommentpreviewdividertemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmcommentpreviewdividertemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcommentpreviewformtemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmcommentpreviewformtemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=3><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>{{commentstatussmart}} Templates</B><BR><FONT SIZE=1>If you wish, you can customise the text or other output that {{commentstatussmart}} generates when there are no comments, only one comment, or more than one comment, respectively.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=33%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=229 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Output for<BR>no comments</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=34%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=229 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Output for<BR>one comment</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=33%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=229 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Output for two<BR>or more comments</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newsmartlinknocommentstemplate" COLS=26 ROWS=5 WRAP=VIRTUAL STYLE="width: 233">$gmsmartlinknocommentstemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newsmartlinkonecommenttemplate" COLS=26 ROWS=5 WRAP=VIRTUAL STYLE="width: 233">$gmsmartlinkonecommenttemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newsmartlinkmanycommentstemplate" COLS=26 ROWS=5 WRAP=VIRTUAL STYLE="width: 233">$gmsmartlinkmanycommentstemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>{{commentauthoremail}} and {{commentauthorhomepage}} Templates</B><BR><FONT SIZE=1>When used in the Comment Appearance template, these varibles are what will appear whenever an e-mail or homepage address, respectively, has been given by that author of that comment; this is useful, for example, if you want to set up little icons or somesuch that will appear with someone's comment when they give their e-mail or homepage address.  The simplest approach, though, is to ignore these altogether and use {{commentauthorsmartlink}} instead.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{commentauthoremail}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{commentauthorhomepage}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcommentauthoremailtemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmcommentauthoremailtemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcommentauthorhomepagetemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmcommentauthorhomepagetemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

</TABLE>
$autorebuildcheckbox
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Template Changes"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Templates Menu">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"We all shine on, like the moon and the stars and the sun."&#151;John Lennon, "Instant Karma!"</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITKARMACOMMENTSTEMPLATES

$statusnote = "";

exit;

}

# ---------------------------------------------
# edit template group: header, footer & sidebar
# ---------------------------------------------

sub gm_editheaderfootertemplates {

&gm_validate;

if ($gmtemplateaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the header, footer & sidebar templates without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the header, footer & sidebar templates.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readtemplates;

&gm_delousealltemplates;

if ($statusnote eq "") { $statusnote = qq(<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=720><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B><FONT COLOR="#000000">Editing Header, Footer & Sidebar (& Custom) Templates</FONT></B><BR><FONT SIZE=1>If you want to have something&#151;certain text, graphics, formatting, etc.&#151;that appears across all your pages, but you don't want to have to modify all the templates each time you change them, simply use the Header, Footer and Sidebar templates below, or any of the ten custom templates.  Their contents will be inserted wherever the respective variables appear in your templates.</FONT></TD></TR></TABLE><P>); }

$autorebuildcheckbox = "";

if ($gmrebuildaccess eq "yes") {
	if ($automaticrebuilddefault eq "yes") {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="everything" CHECKED> Automatically rebuild all files after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	} else {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="everything"> Automatically rebuild all files after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	}
}

&gm_readcounter;
if ($newentrynumber eq "0") { $autorebuildcheckbox = ""; }

print<<GMEDITHEADERFOOTERTEMPLATES;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="modifiedtemplategroup" VALUE="header, footer & sidebar">

<INPUT TYPE=HIDDEN NAME="newindextemplate" VALUE="$gmindextemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagetemplate" VALUE="$gmentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveindextemplate" VALUE="$gmarchiveindextemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrypagetemplate" VALUE="$gmarchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newentrytemplate" VALUE="$gmentrytemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrytemplate" VALUE="$gmarchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newstayattoptemplate" VALUE="$gmstayattoptemplate">
<INPUT TYPE=HIDDEN NAME="newdatetemplate" VALUE="$gmdatetemplate">
<INPUT TYPE=HIDDEN NAME="newcommentstemplate" VALUE="$gmcommentstemplate">
<INPUT TYPE=HIDDEN NAME="newcommentsformtemplate" VALUE="$gmcommentsformtemplate">
<INPUT TYPE=HIDDEN NAME="newparaseparationtemplate" VALUE="$gmparaseparationtemplate">
<INPUT TYPE=HIDDEN NAME="newkarmaformtemplate" VALUE="$gmkarmaformtemplate">
<INPUT TYPE=HIDDEN NAME="newmoreprefacetemplate" VALUE="$gmmoreprefacetemplate">
<INPUT TYPE=HIDDEN NAME="newmorelinktemplate" VALUE="$gmmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newkarmalinktemplate" VALUE="$gmkarmalinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentslinktemplate" VALUE="$gmcommentslinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthoremailtemplate" VALUE="$gmcommentauthoremailtemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthorhomepagetemplate" VALUE="$gmcommentauthorhomepagetemplate">
<INPUT TYPE=HIDDEN NAME="newcommentdividertemplate" VALUE="$gmcommentdividertemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrytemplate" VALUE="$gmmoreentrytemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagetemplate" VALUE="$gmmoreentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrypagetemplate" VALUE="$gmmorearchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newpreviouslinktemplate" VALUE="$gmpreviouslinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextlinktemplate" VALUE="$gmnextlinktemplate">
<INPUT TYPE=HIDDEN NAME="newpreviousmorelinktemplate" VALUE="$gmpreviousmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newnextmorelinktemplate" VALUE="$gmnextmorelinktemplate">
<INPUT TYPE=HIDDEN NAME="newarchivemasterindextemplate" VALUE="$gmarchivemasterindextemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinktemplate" VALUE="$gmlogarchiveslinktemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinktemplate" VALUE="$gmentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagelinktemplate" VALUE="$gmmoreentrypagelinktemplate">
<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkseparatortemplate" VALUE="$gmlogarchiveslinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkseparatortemplate" VALUE="$gmentrypagelinkseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkmonthseparatortemplate" VALUE="$gmentrypagelinkmonthseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkdayseparatortemplate" VALUE="$gmentrypagelinkdayseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagelinkyearseparatortemplate" VALUE="$gmentrypagelinkyearseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newentryseparatortemplate" VALUE="$gmentryseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentryseparatortemplate" VALUE="$gmarchiveentryseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrytemplate" VALUE="$gmmorearchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newdatearchivetemplate" VALUE="$gmdatearchivetemplate">

<INPUT TYPE=HIDDEN NAME="newlogarchiveslinkweeklytemplate" VALUE="$gmlogarchiveslinkweeklytemplate">
<INPUT TYPE=HIDDEN NAME="newpopuppagetemplate" VALUE="$gmpopuppagetemplate">
<INPUT TYPE=HIDDEN NAME="newpopupcodetemplate" VALUE="$gmpopupcodetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchformtemplate" VALUE="$gmsearchformtemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultspagetemplate" VALUE="$gmsearchresultspagetemplate">
<INPUT TYPE=HIDDEN NAME="newsearchresultsentrytemplate" VALUE="$gmsearchresultsentrytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartablebeginningtemplate" VALUE="$gmcalendartablebeginningtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendartableendingtemplate" VALUE="$gmcalendartableendingtemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarblankcelltemplate" VALUE="$gmcalendarblankcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelltemplate" VALUE="$gmcalendarfullcelltemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarfullcelllinktemplate" VALUE="$gmcalendarfullcelllinktemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaytemplate" VALUE="$gmcalendarweekfulldaytemplate">
<INPUT TYPE=HIDDEN NAME="newcalendarweekfulldaylinktemplate" VALUE="$gmcalendarweekfulldaylinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewdividertemplate" VALUE="$gmcommentpreviewdividertemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewformtemplate" VALUE="$gmcommentpreviewformtemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinknocommentstemplate" VALUE="$gmsmartlinknocommentstemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkonecommenttemplate" VALUE="$gmsmartlinkonecommenttemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkmanycommentstemplate" VALUE="$gmsmartlinkmanycommentstemplate">
<INPUT TYPE=HIDDEN NAME="newlinebreaktemplate" VALUE="$gmlinebreaktemplate">

<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=720>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Header Template</B><BR><FONT SIZE=1>Whatever you put here will appear wherever {{header}} is used in your other templates.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newheadertemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmheadertemplate</TEXTAREA>$gmfonttag</FONT></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Footer Template</B><BR><FONT SIZE=1>Whatever you put here will appear wherever {{footer}} is used in your other templates.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newfootertemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmfootertemplate</TEXTAREA>$gmfonttag</FONT></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2>$gmfonttag<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Sidebar Template</B><BR><FONT SIZE=1>Whatever you put here will appear wherever {{sidebar}} is used in your other templates.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE><P></FONT><TEXTAREA NAME="newsidebartemplate" COLS=86 ROWS=30 WRAP=VIRTUAL STYLE="width: 720">$gmsidebartemplate</TEXTAREA>$gmfonttag</FONT></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Miscellaneous Custom Templates</B><BR><FONT SIZE=1>Whatever you put in any of the templates below will appear wherever their respective variables are used.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customone}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customtwo}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomonetemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomonetemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomtwotemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomtwotemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customthree}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customfour}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomthreetemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomthreetemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomfourtemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomfourtemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customfive}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customsix}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomfivetemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomfivetemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomsixtemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomsixtemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customseven}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customeight}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomseventemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomseventemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomeighttemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomeighttemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customnine}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{customten}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomninetemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomninetemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcustomtentemplate" COLS=41 ROWS=20 WRAP=VIRTUAL STYLE="width: 355">$gmcustomtentemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

</TABLE>
$autorebuildcheckbox
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Template Changes"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Templates Menu">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"When you make eyes in place of an eye, a hand in place of a hand, a foot in place of a foot,<BR>an image in place of an image, then you will enter the kingdom."&#151;Gospel of Thomas 22:38</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITHEADERFOOTERTEMPLATES

$statusnote = "";

exit;

}

# ----------------------------------
# edit template group: miscellaneous
# ----------------------------------

sub gm_editmisctemplates {

&gm_validate;

if (($gmtemplateaccess eq "no") || ($gmtemplateaccess eq "hfsonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the miscellaneous templates without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the miscellaneous templates.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readtemplates;

&gm_delousealltemplates;

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Editing Miscellaneous Templates</FONT></B><BR><FONT SIZE=1>All the templates affecting things that didn't fit into the other categories.</FONT><P>); }

$autorebuildcheckbox = "";

if ($gmrebuildaccess eq "yes") {
	if ($automaticrebuilddefault eq "yes") {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="everything" CHECKED> Automatically rebuild all files after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	} else {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="everything"> Automatically rebuild all files after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	}
}

&gm_readcounter;
if ($newentrynumber eq "0") { $autorebuildcheckbox = ""; }

print<<GMEDITMISCTEMPLATES;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="modifiedtemplategroup" VALUE="miscellaneous">

<INPUT TYPE=HIDDEN NAME="newindextemplate" VALUE="$gmindextemplate">
<INPUT TYPE=HIDDEN NAME="newentrypagetemplate" VALUE="$gmentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveindextemplate" VALUE="$gmarchiveindextemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrypagetemplate" VALUE="$gmarchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newentrytemplate" VALUE="$gmentrytemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentrytemplate" VALUE="$gmarchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newstayattoptemplate" VALUE="$gmstayattoptemplate">
<INPUT TYPE=HIDDEN NAME="newdatetemplate" VALUE="$gmdatetemplate">
<INPUT TYPE=HIDDEN NAME="newcommentstemplate" VALUE="$gmcommentstemplate">
<INPUT TYPE=HIDDEN NAME="newcommentsformtemplate" VALUE="$gmcommentsformtemplate">
<INPUT TYPE=HIDDEN NAME="newkarmaformtemplate" VALUE="$gmkarmaformtemplate">
<INPUT TYPE=HIDDEN NAME="newkarmalinktemplate" VALUE="$gmkarmalinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentslinktemplate" VALUE="$gmcommentslinktemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthoremailtemplate" VALUE="$gmcommentauthoremailtemplate">
<INPUT TYPE=HIDDEN NAME="newcommentauthorhomepagetemplate" VALUE="$gmcommentauthorhomepagetemplate">
<INPUT TYPE=HIDDEN NAME="newcommentdividertemplate" VALUE="$gmcommentdividertemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrytemplate" VALUE="$gmmoreentrytemplate">
<INPUT TYPE=HIDDEN NAME="newmoreentrypagetemplate" VALUE="$gmmoreentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrypagetemplate" VALUE="$gmmorearchiveentrypagetemplate">
<INPUT TYPE=HIDDEN NAME="newarchivemasterindextemplate" VALUE="$gmarchivemasterindextemplate">
<INPUT TYPE=HIDDEN NAME="newheadertemplate" VALUE="$gmheadertemplate">
<INPUT TYPE=HIDDEN NAME="newfootertemplate" VALUE="$gmfootertemplate">
<INPUT TYPE=HIDDEN NAME="newsidebartemplate" VALUE="$gmsidebartemplate">
<INPUT TYPE=HIDDEN NAME="newentryseparatortemplate" VALUE="$gmentryseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newarchiveentryseparatortemplate" VALUE="$gmarchiveentryseparatortemplate">
<INPUT TYPE=HIDDEN NAME="newmorearchiveentrytemplate" VALUE="$gmmorearchiveentrytemplate">
<INPUT TYPE=HIDDEN NAME="newdatearchivetemplate" VALUE="$gmdatearchivetemplate">

<INPUT TYPE=HIDDEN NAME="newcustomonetemplate" VALUE="$gmcustomonetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtwotemplate" VALUE="$gmcustomtwotemplate">
<INPUT TYPE=HIDDEN NAME="newcustomthreetemplate" VALUE="$gmcustomthreetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfourtemplate" VALUE="$gmcustomfourtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomfivetemplate" VALUE="$gmcustomfivetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomsixtemplate" VALUE="$gmcustomsixtemplate">
<INPUT TYPE=HIDDEN NAME="newcustomseventemplate" VALUE="$gmcustomseventemplate">
<INPUT TYPE=HIDDEN NAME="newcustomeighttemplate" VALUE="$gmcustomeighttemplate">
<INPUT TYPE=HIDDEN NAME="newcustomninetemplate" VALUE="$gmcustomninetemplate">
<INPUT TYPE=HIDDEN NAME="newcustomtentemplate" VALUE="$gmcustomtentemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewdividertemplate" VALUE="$gmcommentpreviewdividertemplate">
<INPUT TYPE=HIDDEN NAME="newcommentpreviewformtemplate" VALUE="$gmcommentpreviewformtemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinknocommentstemplate" VALUE="$gmsmartlinknocommentstemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkonecommenttemplate" VALUE="$gmsmartlinkonecommenttemplate">
<INPUT TYPE=HIDDEN NAME="newsmartlinkmanycommentstemplate" VALUE="$gmsmartlinkmanycommentstemplate">

<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=720>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>{{previouslink}} And {{nextlink}} Templates</B><BR><FONT SIZE=1>If there is a previous or next entry (ignoring closed entries, of course) preceding or following the given entry, these will appear; these variables are intended for use in the entry page templates, for including links to the previous or next entry (if applicable).  {{previousmorelink}} and {{nextmorelink}} work the same way, except that they link only to the previous or next extended entry (entries with "more" text).</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{previouslink}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{nextlink}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newpreviouslinktemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmpreviouslinktemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newnextlinktemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmnextlinktemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{previousmorelink}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{nextmorelink}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newpreviousmorelinktemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmpreviousmorelinktemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="previousmorelinkcheck" VALUE="yes"> Make this the same as the {{previouslink}} template</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newnextmorelinktemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmnextmorelinktemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="nextmorelinkcheck" VALUE="yes"> Make this the same as the {{nextlink}} template</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>List Variable Templates</B><BR><FONT SIZE=1>The variables {{logarchivelist}} and {{logentrylist}} (and the variants thereof; check the manual for more information) are used for automatically generating lists of links&#151;whether on your archive master index, or anywhere else&#151;to your log archives and your individual entry pages; these templates set the formatting of those links.  The first two templates apply to the {{logentrylist}} variable and its variants, formatting the links to standard and extended entries respectively; the Log Archive Links Templates apply to the {{logarchivelist}} variable, which generates links to the monthly/weekly log archive files (whichever of the two is used depends on whether you have weekly or monthly archiving enabled).</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Log Archives Link Template: Weekly</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Log Archives Link Template: Monthly</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newlogarchiveslinkweeklytemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmlogarchiveslinkweeklytemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newlogarchiveslinktemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmlogarchiveslinktemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Entry List Link Template: Standard</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Entry List Link Template: Extended</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newentrypagelinktemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmentrypagelinktemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newmoreentrypagelinktemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmmoreentrypagelinktemplate</TEXTAREA>$gmfonttag</FONT><BR>$gmfonttag<FONT SIZE=1><INPUT TYPE=CHECKBOX NAME="moreentrylistlinkcheck" VALUE="yes"> Make this the same as the template on the left</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>List Variable Templates: Link Separators</B><BR><FONT SIZE=1>Going along with the list variable templates above, these specify how the links are to be separated when the lists are built for their respective variables.  Use the day, month, and year separators for entry lists if you wish to separate the listings for each individual day, month, or year; leave them blank to keep the entry lists continuous.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Entry List Link Separator</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Log Archives Link Separator</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newentrypagelinkseparatortemplate" COLS=41 ROWS=5 WRAP=VIRTUAL STYLE="width: 355">$gmentrypagelinkseparatortemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newlogarchiveslinkseparatortemplate" COLS=41 ROWS=5 WRAP=VIRTUAL STYLE="width: 355">$gmlogarchiveslinkseparatortemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=33%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=229 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Entry List:<BR>Day Separator</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=34%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=229 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Entry List:<BR>Month Separator</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=33%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=229 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Entry List:<BR>Year Separator</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newentrypagelinkdayseparatortemplate" COLS=26 ROWS=5 WRAP=VIRTUAL STYLE="width: 233">$gmentrypagelinkdayseparatortemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newentrypagelinkmonthseparatortemplate" COLS=26 ROWS=5 WRAP=VIRTUAL STYLE="width: 233">$gmentrypagelinkmonthseparatortemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newentrypagelinkyearseparatortemplate" COLS=26 ROWS=5 WRAP=VIRTUAL STYLE="width: 233">$gmentrypagelinkyearseparatortemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Search Templates</B><BR><FONT SIZE=1>These templates control the built-in ability for visitors to search through your site entries (just add {{searchform}} to a template to insert the search form there).  The Search Form template is the form by which visitors can perform the search; the Search Item Results template formats the appearance of each item returned by the search result; and finally, the Search Results Page template is for the full page that your visitors will see displaying all the search results.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Search Form Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Search Item Results Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newsearchformtemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmsearchformtemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newsearchresultsentrytemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmsearchresultsentrytemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Search Results Page Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER COLSPAN=2></FONT><TEXTAREA NAME="newsearchresultspagetemplate" COLS=86 ROWS=15 WRAP=VIRTUAL STYLE="width: 720">$gmsearchresultspagetemplate</TEXTAREA>$gmfonttag</FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Calendar Templates</B><BR><FONT SIZE=1>These control the layout and appearance of monthly or weekly calendars made with the 	{{calendar}} or {{calendarweek}} variables respectively.  The first five are for monthly calendars (with 	{{calendar}}); you can specify the formatting of the beginning and end of the table, and how each kind of cell (cells without a day, cells with an unlinked day, and cells with a linked day) will appear.  The last two are for weekly calendars ({{calendarweek}}) and their linked or unlinked days.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{calendar}}: Beginning of table</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{calendar}}: Ending of table</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcalendartablebeginningtemplate" COLS=41 ROWS=5 WRAP=VIRTUAL STYLE="width: 355">$gmcalendartablebeginningtemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcalendartableendingtemplate" COLS=41 ROWS=5 WRAP=VIRTUAL STYLE="width: 355">$gmcalendartableendingtemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=33%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=229 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{calendar}}:<BR>Blank cell</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=34%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=229 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{calendar}}:<BR>Day cell without link</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=33%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=229 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{calendar}}:<BR>Day cell with link</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcalendarblankcelltemplate" COLS=26 ROWS=5 WRAP=VIRTUAL STYLE="width: 233">$gmcalendarblankcelltemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcalendarfullcelltemplate" COLS=26 ROWS=5 WRAP=VIRTUAL STYLE="width: 233">$gmcalendarfullcelltemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcalendarfullcelllinktemplate" COLS=26 ROWS=5 WRAP=VIRTUAL STYLE="width: 233">$gmcalendarfullcelllinktemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{calendarweek}}: Day without link</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{calendarweek}}: Day with link</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcalendarweekfulldaytemplate" COLS=41 ROWS=5 WRAP=VIRTUAL STYLE="width: 355">$gmcalendarweekfulldaytemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newcalendarweekfulldaylinktemplate" COLS=41 ROWS=5 WRAP=VIRTUAL STYLE="width: 355">$gmcalendarweekfulldaylinktemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>{{popup}} Templates</B><BR><FONT SIZE=1>These templates control the code associated with the {{popup}} variable for making popup windows; the Popup Code template is for the code that calls the window, and the Popup Window template is for the HTML file to be generated for the window.  (The popup-related variables&#151;{{popuptitle}} etc.&#151;will only work in these two templates.)</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Popup Code Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Popup Window Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newpopupcodetemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmpopupcodetemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newpopuppagetemplate" COLS=41 ROWS=10 WRAP=VIRTUAL STYLE="width: 355">$gmpopuppagetemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#D0D0FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Line & Paragraph Separators</B><BR><FONT SIZE=1>The line separator is whatever will be inserted whenever there's a line break in the body of an entry's text; the paragraph separator is used for a double-line break (a paragraph break).  These apply both to entries and to comments.</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Line Separator</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Paragraph Separator</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newlinebreaktemplate" COLS=41 ROWS=3 WRAP=VIRTUAL STYLE="width: 355">$gmlinebreaktemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newparaseparationtemplate" COLS=41 ROWS=3 WRAP=VIRTUAL STYLE="width: 355">$gmparaseparationtemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER COLSPAN=2> &#160; </TD></TR>

<TR><TD VALIGN=BOTTOM ALIGN=CENTER COLSPAN=2><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=10 WIDTH=100%><TR><TD COLSPAN=2><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#FFD0D0"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>{{morepreface}} And {{morelink}} Templates (no longer recommended)</B><BR><FONT SIZE=1>Meant for use in the Index and Log Archive Entry templates, to specify links or other text/code to appear only for extended entries.  These are no longer recommended for use; it's simpler and more flexible now to distinguish standard and extended entries with their separate templates, so these are no longer necessary (but are kept here for compatibility purposes).</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{morepreface}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD><TD VALIGN=TOP ALIGN=CENTER WIDTH=50%><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=351 BGCOLOR="#E0F0FF"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>{{morelink}} Template</B></FONT></TD></TR></TABLE></TD></TR></TABLE></TD></TR><TR><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newmoreprefacetemplate" COLS=41 ROWS=3 WRAP=VIRTUAL STYLE="width: 355">$gmmoreprefacetemplate</TEXTAREA>$gmfonttag</FONT></TD><TD VALIGN=TOP ALIGN=CENTER></FONT><TEXTAREA NAME="newmorelinktemplate" COLS=41 ROWS=3 WRAP=VIRTUAL STYLE="width: 355">$gmmorelinktemplate</TEXTAREA>$gmfonttag</FONT></FONT></TD></TR></TABLE></TD></TR>

</TABLE>
$autorebuildcheckbox
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Template Changes"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Templates Menu">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"God does not play dice with the universe."&#151;Albert Einstein</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITMISCTEMPLATES

$statusnote = "";

exit;

}

# -------------------------
# save the template changes
# -------------------------

sub gm_savetemplatechanges {

&gm_validate;

if ($gmtemplateaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the templates without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the templates.</FONT></B><P>);
	&gm_frontpage;
}

$IN{'newindextemplate'} = &relouse($IN{'newindextemplate'});
$IN{'newentrypagetemplate'} = &relouse($IN{'newentrypagetemplate'});
$IN{'newarchiveindextemplate'} = &relouse($IN{'newarchiveindextemplate'});
$IN{'newarchiveentrypagetemplate'} = &relouse($IN{'newarchiveentrypagetemplate'});
$IN{'newentrytemplate'} = &relouse($IN{'newentrytemplate'});
$IN{'newarchiveentrytemplate'} = &relouse($IN{'newarchiveentrytemplate'});
$IN{'newstayattoptemplate'} = &relouse($IN{'newstayattoptemplate'});
$IN{'newdatetemplate'} = &relouse($IN{'newdatetemplate'});
$IN{'newcommentstemplate'} = &relouse($IN{'newcommentstemplate'});
$IN{'newcommentsformtemplate'} = &relouse($IN{'newcommentsformtemplate'});
$IN{'newparaseparationtemplate'} = &relouse($IN{'newparaseparationtemplate'});
$IN{'newkarmaformtemplate'} = &relouse($IN{'newkarmaformtemplate'});
$IN{'newmoreprefacetemplate'} = &relouse($IN{'newmoreprefacetemplate'});
$IN{'newmorelinktemplate'} = &relouse($IN{'newmorelinktemplate'});
$IN{'newkarmalinktemplate'} = &relouse($IN{'newkarmalinktemplate'});
$IN{'newcommentslinktemplate'} = &relouse($IN{'newcommentslinktemplate'});
$IN{'newcommentauthoremailtemplate'} = &relouse($IN{'newcommentauthoremailtemplate'});
$IN{'newcommentauthorhomepagetemplate'} = &relouse($IN{'newcommentauthorhomepagetemplate'});
$IN{'newcommentdividertemplate'} = &relouse($IN{'newcommentdividertemplate'});
$IN{'newmoreentrytemplate'} = &relouse($IN{'newmoreentrytemplate'});
$IN{'newmoreentrypagetemplate'} = &relouse($IN{'newmoreentrypagetemplate'});
$IN{'newmorearchiveentrypagetemplate'} = &relouse($IN{'newmorearchiveentrypagetemplate'});
$IN{'newpreviouslinktemplate'} = &relouse($IN{'newpreviouslinktemplate'});
$IN{'newnextlinktemplate'} = &relouse($IN{'newnextlinktemplate'});
$IN{'newpreviousmorelinktemplate'} = &relouse($IN{'newpreviousmorelinktemplate'});
$IN{'newnextmorelinktemplate'} = &relouse($IN{'newnextmorelinktemplate'});
$IN{'newarchivemasterindextemplate'} = &relouse($IN{'newarchivemasterindextemplate'});
$IN{'newlogarchiveslinktemplate'} = &relouse($IN{'newlogarchiveslinktemplate'});
$IN{'newentrypagelinktemplate'} = &relouse($IN{'newentrypagelinktemplate'});
$IN{'newmoreentrypagelinktemplate'} = &relouse($IN{'newmoreentrypagelinktemplate'});
$IN{'newlogarchiveslinkseparatortemplate'} = &relouse($IN{'newlogarchiveslinkseparatortemplate'});
$IN{'newentrypagelinkseparatortemplate'} = &relouse($IN{'newentrypagelinkseparatortemplate'});
$IN{'newentrypagelinkmonthseparatortemplate'} = &relouse($IN{'newentrypagelinkmonthseparatortemplate'});
$IN{'newentrypagelinkdayseparatortemplate'} = &relouse($IN{'newentrypagelinkdayseparatortemplate'});
$IN{'newentrypagelinkyearseparatortemplate'} = &relouse($IN{'newentrypagelinkyearseparatortemplate'});
$IN{'newheadertemplate'} = &relouse($IN{'newheadertemplate'});
$IN{'newfootertemplate'} = &relouse($IN{'newfootertemplate'});
$IN{'newsidebartemplate'} = &relouse($IN{'newsidebartemplate'});
$IN{'newcustomlinktemplate'} = "";
$IN{'newentryseparatortemplate'} = &relouse($IN{'newentryseparatortemplate'});
$IN{'newarchiveentryseparatortemplate'} = &relouse($IN{'newarchiveentryseparatortemplate'});
$IN{'newmorearchiveentrytemplate'} = &relouse($IN{'newmorearchiveentrytemplate'});
$IN{'newdatearchivetemplate'} = &relouse($IN{'newdatearchivetemplate'});

$IN{'newlogarchiveslinkweeklytemplate'} = &relouse($IN{'newlogarchiveslinkweeklytemplate'});
$IN{'newcustomonetemplate'} = &relouse($IN{'newcustomonetemplate'});
$IN{'newcustomtwotemplate'} = &relouse($IN{'newcustomtwotemplate'});
$IN{'newcustomthreetemplate'} = &relouse($IN{'newcustomthreetemplate'});
$IN{'newcustomfourtemplate'} = &relouse($IN{'newcustomfourtemplate'});
$IN{'newcustomfivetemplate'} = &relouse($IN{'newcustomfivetemplate'});
$IN{'newcustomsixtemplate'} = &relouse($IN{'newcustomsixtemplate'});
$IN{'newcustomseventemplate'} = &relouse($IN{'newcustomseventemplate'});
$IN{'newcustomeighttemplate'} = &relouse($IN{'newcustomeighttemplate'});
$IN{'newcustomninetemplate'} = &relouse($IN{'newcustomninetemplate'});
$IN{'newcustomtentemplate'} = &relouse($IN{'newcustomtentemplate'});
$IN{'newpopuppagetemplate'} = &relouse($IN{'newpopuppagetemplate'});
$IN{'newpopupcodetemplate'} = &relouse($IN{'newpopupcodetemplate'});
$IN{'newsearchformtemplate'} = &relouse($IN{'newsearchformtemplate'});
$IN{'newsearchresultspagetemplate'} = &relouse($IN{'newsearchresultspagetemplate'});
$IN{'newsearchresultsentrytemplate'} = &relouse($IN{'newsearchresultsentrytemplate'});
$IN{'newcalendartablebeginningtemplate'} = &relouse($IN{'newcalendartablebeginningtemplate'});
$IN{'newcalendartableendingtemplate'} = &relouse($IN{'newcalendartableendingtemplate'});
$IN{'newcalendarblankcelltemplate'} = &relouse($IN{'newcalendarblankcelltemplate'});
$IN{'newcalendarfullcelltemplate'} = &relouse($IN{'newcalendarfullcelltemplate'});
$IN{'newcalendarfullcelllinktemplate'} = &relouse($IN{'newcalendarfullcelllinktemplate'});
$IN{'newcalendarweekblankdaytemplate'} = "";
$IN{'newcalendarweekfulldaytemplate'} = &relouse($IN{'newcalendarweekfulldaytemplate'});
$IN{'newcalendarweekfulldaylinktemplate'} = &relouse($IN{'newcalendarweekfulldaylinktemplate'});
$IN{'newcommentpreviewdividertemplate'} = &relouse($IN{'newcommentpreviewdividertemplate'});
$IN{'newcommentpreviewformtemplate'} = &relouse($IN{'newcommentpreviewformtemplate'});
$IN{'newsmartlinknocommentstemplate'} = &relouse($IN{'newsmartlinknocommentstemplate'});
$IN{'newsmartlinkonecommenttemplate'} = &relouse($IN{'newsmartlinkonecommenttemplate'});
$IN{'newsmartlinkmanycommentstemplate'} = &relouse($IN{'newsmartlinkmanycommentstemplate'});
$IN{'newlinebreaktemplate'} = &relouse($IN{'newlinebreaktemplate'});

if (($IN{'newcustomlinktemplate'} ne "") && ((substr($IN{'newcustomlinktemplate'}, 0, 1)) ne " ")) {
	$IN{'newcustomlinktemplate'} = " $IN{'newcustomlinktemplate'}";
}

if ($IN{'entrylistingmorecheck'} eq "yes") { $IN{'newmoreentrytemplate'} = $IN{'newentrytemplate'}; }
if ($IN{'entrylistingstayattopcheck'} eq "yes") { $IN{'newstayattoptemplate'} = $IN{'newentrytemplate'}; }
if ($IN{'archivelogindexcheck'} eq "yes") { $IN{'newarchiveindextemplate'} = $IN{'newindextemplate'}; }
if ($IN{'archiveentrylistingcheck'} eq "yes") { $IN{'newarchiveentrytemplate'} = $IN{'newentrytemplate'}; }
if ($IN{'archiveentrylistingmorecheck'} eq "yes") { $IN{'newmorearchiveentrytemplate'} = $IN{'newmoreentrytemplate'}; }
if ($IN{'archivedateheadercheck'} eq "yes") { $IN{'newdatearchivetemplate'} = $IN{'newdatetemplate'}; }
if ($IN{'archiveentryseparatorcheck'} eq "yes") { $IN{'newarchiveentryseparatortemplate'} = $IN{'newentryseparatortemplate'}; }
if ($IN{'entrymorepagecheck'} eq "yes") { $IN{'newmoreentrypagetemplate'} = $IN{'newentrypagetemplate'}; }
if ($IN{'entryarchivepagecheck'} eq "yes") { $IN{'newarchiveentrypagetemplate'} = $IN{'newentrypagetemplate'}; }
if ($IN{'entrymorearchivepagecheck'} eq "yes") { $IN{'newmorearchiveentrypagetemplate'} = $IN{'newarchiveentrypagetemplate'}; }
if ($IN{'previousmorelinkcheck'} eq "yes") { $IN{'newpreviousmorelinktemplate'} = $IN{'newpreviouslinktemplate'}; }
if ($IN{'nextmorelinkcheck'} eq "yes") { $IN{'newnextmorelinktemplate'} = $IN{'newnextlinktemplate'}; }

if ($IN{'moreentrylistlinkcheck'} eq "yes") { $IN{'newmoreentrypagelinktemplate'} = $IN{'newentrypagelinktemplate'}; }

open (FUNNYFEETRELEASE, ">gm-templates.cgi") || &gm_dangermouse("Can't write the templates file.  Please make sure that gm-templates.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEETRELEASE "$IN{'newindextemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newentrypagetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newarchiveindextemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newarchiveentrypagetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newentrytemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newarchiveentrytemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newstayattoptemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newdatetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcommentstemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcommentsformtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newparaseparationtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newkarmaformtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newmoreprefacetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newmorelinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newkarmalinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcommentslinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcommentauthoremailtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcommentauthorhomepagetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcommentdividertemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newmoreentrytemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newmoreentrypagetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newmorearchiveentrypagetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newpreviouslinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newnextlinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newpreviousmorelinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newnextmorelinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newarchivemasterindextemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newlogarchiveslinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newentrypagelinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newmoreentrypagelinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newlogarchiveslinkseparatortemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newentrypagelinkseparatortemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newentrypagelinkmonthseparatortemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newentrypagelinkdayseparatortemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newentrypagelinkyearseparatortemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newheadertemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newfootertemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newsidebartemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomlinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newentryseparatortemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newarchiveentryseparatortemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newmorearchiveentrytemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newdatearchivetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newlogarchiveslinkweeklytemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomonetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomtwotemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomthreetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomfourtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomfivetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomsixtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomseventemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomeighttemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomninetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcustomtentemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newpopuppagetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newpopupcodetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newsearchformtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newsearchresultspagetemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newsearchresultsentrytemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcalendartablebeginningtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcalendartableendingtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcalendarblankcelltemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcalendarfullcelltemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcalendarfullcelllinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcalendarweekblankdaytemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcalendarweekfulldaytemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcalendarweekfulldaylinktemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcommentpreviewdividertemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newcommentpreviewformtemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newsmartlinknocommentstemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newsmartlinkonecommenttemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newsmartlinkmanycommentstemplate'}\n";
print FUNNYFEETRELEASE "$IN{'newlinebreaktemplate'}\n";
close (FUNNYFEETRELEASE);

$statusnote = qq(<B><FONT COLOR="#0000FF">The $IN{'modifiedtemplategroup'} templates have been modified.  Be sure to rebuild<BR>your files to make these changes take effect throughout your site.</FONT></B><P>);

&gm_writetocplog("$IN{'authorname'} modified the $IN{'modifiedtemplategroup'} templates");

if ($IN{'autorebuild'} eq "index") { &gm_rebuildmainindexfile; }
if ($IN{'autorebuild'} eq "archiveindexes") { &gm_rebuildarchivelogindexes; }
if ($IN{'autorebuild'} eq "entrypages") { &gm_rebuildallentrypages; }
if ($IN{'autorebuild'} eq "everything") { &gm_rebuildeverything; }

&gm_edittemplates;

}

# ---------------------------
# view the greymatter logfile
# ---------------------------

sub gm_viewcplog {

&gm_validate;

if ($gmcplogaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to view the control panel log without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to view the control panel log.</FONT></B><P>);
	&gm_frontpage;
}

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Control Panel Log</FONT></B><P>); }

print<<GMVIEWLOGTOP;

$gmheadtag

$gmframetop
$statusnote
<P ALIGN=LEFT>
GMVIEWLOGTOP

open (FUNNYFEET, "gm-cplog.cgi");
@gmlogfile = <FUNNYFEET>;
close (FUNNYFEET);

foreach $gmlogfileline (@gmlogfile) {
	chomp ($gmlogfileline);
	print "$gmlogfileline<BR>";
}

&date;
&gm_readcounter;

if ($newentrynumber ne "0") {
	$newalltimetotalkarmanumber = $newalltimepktotalnumber - $newalltimenktotalnumber;
	$newalltimetotalkarmavotes = $newalltimepktotalnumber + $newalltimenktotalnumber;
	$entriesonmainnumber = $newentrynumber - $newarchivenumber;
	$karmavotesonaverage = sprintf("%.1f", ($newalltimetotalkarmavotes / $newentrynumber));
	$commentspostedonaverage = sprintf("%.1f", ($newalltimecommentstotalnumber / $newentrynumber));
} else {
	$newalltimetotalkarmanumber = 0;
	$newalltimetotalkarmavotes = 0;
	$entriesonmainnumber = 0;
	$karmavotesonaverage = 0;
	$commentspostedonaverage = 0;
}

print<<GMVIEWLOGBOTTOM;
</P>
<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=0 BGCOLOR="#EEF8FF"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag <B>Site Stats as of $basedate</B><P><FONT SIZE=1>$newentrynumber entries currently online ($newalltimeopenentriesnumber open and $newalltimeclosedentriesnumber closed) with $newarchivenumber archived and $entriesonmainnumber marked as current<BR>$newalltimetotalkarmavotes karma votes cast ($karmavotesonaverage on average per entry) with $newalltimepktotalnumber positive and $newalltimenktotalnumber negative for a total karma rating of $newalltimetotalkarmanumber<BR>$newalltimecommentstotalnumber total comments posted ($commentspostedonaverage on average per entry)</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE>
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #FFD0D0" VALUE="Reset The Control Panel Log">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"When stepping into the stream of consciousness, don't slip on the rocks."<BR>&#151;Siddharta Gautama (the Buddha)</FONT>
$gmframebottom
GMVIEWLOGBOTTOM

exit;

}

# ----------------------------
# clear the greymatter logfile
# ----------------------------

sub gm_resetcplog {

&gm_validate;

if ($gmcplogaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to clear the control panel log without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to clear the control panel log.</FONT></B><P>);
	&gm_frontpage;
}

open (FUNNYFEET, ">gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEET "";
close (FUNNYFEET);

&gm_writetocplog("$IN{'authorname'} cleared this control panel log");

$statusnote = qq(<B><FONT COLOR="#0000FF">The control panel log has been cleared.</FONT></B><P>);

&gm_frontpage;

}

# --------------
# authors editor
# --------------

sub gm_editauthors {

&gm_validate;

if ($gmauthoraccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the authors without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the authors.</FONT></B><P>);
	&gm_frontpage;
}

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Author Panel</FONT></B><BR><FONT SIZE=1>Select an author to edit their information and/or access, or to delete them altogether.</FONT><P>); }

open (FUNNYFEET, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmauthordata = <FUNNYFEET>;
close (FUNNYFEET);

print<<GMEDITAUTHORBEGINNING;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 WIDTH=100% BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=4 CELLSPACING=1 WIDTH=100%>
<TR><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag <FONT SIZE=1><B>Select</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Author<BR>Name</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Can<BR>post?</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Can<BR>edit?</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Can<BR>config?</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Edit<BR>temp's?</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Edit<BR>auth's?</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Can<BR>reb'ld?</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>View<BR>CP log?</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Use<BR>b'lets?</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Upload<BR>files?</B></FONT></FONT></TD><TD VALIGN=BOTTOM ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag<FONT SIZE=1><B>Can<BR>login?</B></FONT></FONT></TD></TR>

GMEDITAUTHORBEGINNING

$alicewarning = "";
$alternateauthorrowone = "#EEF8FF";
$alternateauthorrowtwo = "#F8F8FF";
$alternateauthorrow = $alternateauthorrowone;

foreach $gmauthordataline (@gmauthordata) {
	if ($alternateauthorrow eq $alternateauthorrowone) {
		$alternateauthorrow = $alternateauthorrowtwo;
	} else {
		$alternateauthorrow = $alternateauthorrowone;
	}
	chomp ($gmauthordataline);
	@gmauthorinfo = split (/\|/, $gmauthordataline);
	if (($gmauthorinfo[0] eq "Alice") && ($gmauthorinfo[1] eq "wonderland")) {
		$alicewarning = "<P><B>Be sure to create your own author and delete Alice!</B>"
	}
	print qq(<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP><INPUT TYPE=RADIO NAME="selectedauthor" VALUE="$gmauthorinfo[0]"></TD><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag$gmauthorinfo[0]</FONT></TD>);
	if ($gmauthorinfo[6] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	if ($gmauthorinfo[7] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} elsif ($gmauthorinfo[7] eq "O") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Own</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	if ($gmauthorinfo[8] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	if ($gmauthorinfo[9] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} elsif ($gmauthorinfo[9] eq "O") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag HFS</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	if ($gmauthorinfo[10] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	if ($gmauthorinfo[11] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	if ($gmauthorinfo[12] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	if ($gmauthorinfo[13] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	if ($gmauthorinfo[14] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	if ($gmauthorinfo[15] eq "Y") {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag Yes</FONT></TD>);
	} else {
		print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="$alternateauthorrow" NOWRAP>$gmfonttag No</FONT></TD>);
	}
	print "</TR>\n";
}

print<<GMEDITAUTHORSBOTTOM;

</TABLE></TD></TR></TABLE>
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Edit Selected Author"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #FFD0D0" VALUE="Delete Selected Author">
$alicewarning
<P>
<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=10 CELLSPACING=0 BGCOLOR="#D0E0FF" WIDTH=680><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B>Register A New Author</B><BR><FONT SIZE=1>
Create a new account for someone to have access to Greymatter with (giving an e-mail or homepage is optional).  You can specify whether the author is created having access to everything, to nothing, or to post & edit their own entries only; you can then customise their access further by editing their account above after it's been created.</FONT><P>Name: <INPUT TYPE=TEXT CLASS="textinput" SIZE=25 NAME="newauthorname"> &#160; &#160; Password: <INPUT TYPE=PASSWORD CLASS="textinput" SIZE=25 NAME="newauthorpassword"><P>E-Mail: <INPUT TYPE=TEXT CLASS="textinput" SIZE=30 NAME="newauthoremail"> &#160; &#160; Homepage: <INPUT TYPE=TEXT CLASS="textinput" SIZE=30 NAME="newauthorhomepage" VALUE="http://"><P><B>Default Author Access</B><BR><INPUT TYPE=RADIO NAME="newauthoraccess" VALUE="all" CHECKED> All access &#160; <INPUT TYPE=RADIO NAME="newauthoraccess" VALUE="none"> No access<BR><INPUT TYPE=RADIO NAME="newauthoraccess" VALUE="postedit"> Post & edit their own entries only<P><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas"  STYLE="background: #D0FFD0" VALUE="Create New Author"></FONT></TD></TR></TABLE></TD></TR></TABLE>
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"All the world is queer save me and thee; and sometimes I think thee is a little queer."&#151;old Quaker saying</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITAUTHORSBOTTOM

$statusnote = "";

exit;

}

# -------------------
# create a new author
# -------------------

sub gm_createnewauthor {

&gm_validate;

if ($gmauthoraccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to create a new author without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to create a new author.</FONT></B><P>);
	&gm_frontpage;
}

if (($IN{'newauthorname'} eq "") || ($IN{'newauthorpassword'} eq "")) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You left either the name or password fields blank.  Please try again.</FONT></B><P>);
	&gm_editauthors;
}

if (($IN{'newauthorname'} =~ /^\s+/) || ($IN{'newauthorpassword'} =~ /^\s+/) || ($IN{'newauthorname'} =~ /\s+$/) || ($IN{'newauthorpassword'} =~ /\s+$/)) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You cannot have a space at the beginning or end<BR>of the author name or password.  Please try again.</FONT></B><P>);
	&gm_editauthors;
}

$IN{'newauthorname'} =~ s/ /THISISASPACE/g;
$IN{'newauthorpassword'} =~ s/ /THISISASPACE/g;

if (($IN{'newauthorname'} =~ /\W/) || ($IN{'newauthorpassword'} =~ /\W/)) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">The author name or password cannot contain non-alphanumeric characters<BR>(characters other than letters, numbers or spaces).  Please try again.</FONT></B><P>);
	&gm_editauthors;
}

$IN{'newauthorname'} =~ s/THISISASPACE/ /g;
$IN{'newauthorpassword'} =~ s/THISISASPACE/ /g;

$IN{'newauthoremail'} =~ s/^\s+//;
$IN{'newauthoremail'} =~ s/\s+$//;
$IN{'newauthorhomepage'} =~ s/^\s+//;
$IN{'newauthorhomepage'} =~ s/\s+$//;

if ($IN{'newauthorhomepage'} eq "http://") { $IN{'newauthorhomepage'} = ""; }

open (FUNNYFEET, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmauthordata = <FUNNYFEET>;
close (FUNNYFEET);

foreach $gmauthordataline (@gmauthordata) {
	chomp ($gmauthordataline);
	@gmauthorinfo = split (/\|/, $gmauthordataline);
	if ($IN{'newauthorname'} eq $gmauthorinfo[0]) {
		&gm_writetocplog("$IN{'authorname'} attempted to add an author that is already registered ($IN{'newauthorname'})");
		$statusnote = qq(<B><FONT COLOR="#FF0000">That author is already registered.</FONT></B><P>);
		&gm_editauthors;
	}
}

$temphomepageprefix = substr($IN{'newauthorhomepage'}, 0, 7);
if ($temphomepageprefix ne "http://") { $IN{'newauthorhomepage'} = "http://$IN{'newauthorhomepage'}"; }

if ($IN{'newauthorhomepage'} eq "http://") { $IN{'newauthorhomepage'} = ""; }

&date;

if ($IN{'newauthoraccess'} eq "all") {
	$newauthorline = "$IN{'newauthorname'}|$IN{'newauthorpassword'}|$IN{'newauthoremail'}|$IN{'newauthorhomepage'}|$montwo\/$mdaytwo\/$JSYear|0|Y|Y|Y|Y|Y|Y|Y|Y|Y|Y";
} elsif ($IN{'newauthoraccess'} eq "postedit") {
	$newauthorline = "$IN{'newauthorname'}|$IN{'newauthorpassword'}|$IN{'newauthoremail'}|$IN{'newauthorhomepage'}|$montwo\/$mdaytwo\/$JSYear|0|Y|O|N|N|N|N|N|Y|N|Y";
} else {
	$newauthorline = "$IN{'newauthorname'}|$IN{'newauthorpassword'}|$IN{'newauthoremail'}|$IN{'newauthorhomepage'}|$montwo\/$mdaytwo\/$JSYear|0|N|N|N|N|N|N|N|N|N|N";
}

open (FUNNYFEET, ">>gm-authors.cgi") || &gm_dangermouse("Can't write to the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEET "$newauthorline\n";
close (FUNNYFEET);

open (FUNNYFEET, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmauthordata = <FUNNYFEET>;
close (FUNNYFEET);

@gmauthordatasorted = sort { lc($a) cmp lc ($b) } @gmauthordata;

open (FUNNYFEET, ">gm-authors.cgi") || &gm_dangermouse("Can't write to the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
foreach $gmauthordataline (@gmauthordatasorted) {
	chomp ($gmauthordataline);
	print FUNNYFEET "$gmauthordataline\n";
}
close (FUNNYFEET);

&gm_writetocplog("$IN{'authorname'} registered a new author ($IN{'newauthorname'})");

$statusnote = qq(<B><FONT COLOR="#0000FF">$IN{'newauthorname'} has been added to the author database.</FONT></B><P>);

&gm_editauthors;

}

# ----------------
# delete an author
# ----------------

sub gm_deleteselectedauthor {

&gm_validate;

if ($gmauthoraccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to delete an author ($IN{'selectedauthor'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to delete authors.</FONT></B><P>);
	&gm_frontpage;
}

open (FUNNYFEET, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmauthordata = <FUNNYFEET>;
close (FUNNYFEET);

$authorfound = "no";

foreach $gmauthordataline (@gmauthordata) {
	chomp ($gmauthordataline);
	@gmauthorinfo = split (/\|/, $gmauthordataline);
	if ($IN{'selectedauthor'} eq $gmauthorinfo[0]) { $authorfound = "yes"; }
}

if ($authorfound ne "yes") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must select an author first.</FONT></B><P>);
	&gm_editauthors;
}

$authoramount = scalar(@gmauthordata);

if ($authoramount eq "1") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You can't delete the only remaining author!</FONT></B><P>);
	&gm_editauthors;
}

open (FUNNYFEET, ">gm-authors.cgi") || &gm_dangermouse("Can't write to the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
foreach $gmauthordataline (@gmauthordata) {
	chomp ($gmauthordataline);
	@gmauthorinfo = split (/\|/, $gmauthordataline);
	if ($IN{'selectedauthor'} ne $gmauthorinfo[0]) { print FUNNYFEET "$gmauthordataline\n"; }
}
close (FUNNYFEET);

if ($IN{'selectedauthor'} eq $IN{'authorname'}) {
	&gm_writetocplog("$IN{'authorname'} deleted himself/herself in a sudden fit of existentialism");
} else {
	&gm_writetocplog("$IN{'authorname'} deleted an author ($IN{'selectedauthor'})");
}

if ($IN{'selectedauthor'} eq $IN{'authorname'}) {
	$loginnotice = qq(<B><FONT COLOR="#0000FF">Please re-enter under your new author name and password.</FONT></B><P>);
	&gm_login;
	} else {
	$statusnote = qq(<B><FONT COLOR="#0000FF">$IN{'selectedauthor'} has been deleted.</FONT></B><P>);
	&gm_editauthors;
}

}

# -----------------
# editing an author
# -----------------

sub gm_editselectedauthor {

&gm_validate;

if ($gmauthoraccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the authors without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the authors.</FONT></B><P>);
	&gm_frontpage;
}

open (FUNNYFEET, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmauthordata = <FUNNYFEET>;
close (FUNNYFEET);

$authorfound = "no";

$gmcounter = 0;
$gmauthordatanumber = 0;

foreach $gmauthordataline (@gmauthordata) {
	chomp ($gmauthordataline);
	@gmauthorinfo = split (/\|/, $gmauthordataline);
	if ($IN{'selectedauthor'} eq $gmauthorinfo[0]) {
		$gmauthordatanumber = $gmcounter;
		$authorfound = "yes";
	}
	$gmcounter++;
}

if ($authorfound ne "yes") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must select an author first.</FONT></B><P>);
	&gm_editauthors;
}

@gmselectedauthorinfo = split (/\|/, $gmauthordata[$gmauthordatanumber]);

if ($gmselectedauthorinfo[3] eq "") { $gmselectedauthorinfo[3] = "http://"; }

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Editing $gmselectedauthorinfo[0]'s Info & Access</FONT></B><P>); }

print<<GMEDITSELECTEDAUTHORTOP;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="authororiginalname" VALUE="$gmselectedauthorinfo[0]">
<INPUT TYPE=HIDDEN NAME="authororiginalpassword" VALUE="$gmselectedauthorinfo[1]">
<INPUT TYPE=HIDDEN NAME="authororiginaldate" VALUE="$gmselectedauthorinfo[4]">
<INPUT TYPE=HIDDEN NAME="authororiginalentries" VALUE="$gmselectedauthorinfo[5]">
<INPUT TYPE=HIDDEN NAME="editedauthornumber" VALUE="$gmauthordatanumber">
<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1>
<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Name:</FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT BGCOLOR="#FFFFFF"><INPUT TYPE=TEXT CLASS="textinput" NAME="editedname" VALUE="$gmselectedauthorinfo[0]" SIZE=20></TD></TR>
<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Password:</FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT BGCOLOR="#FFFFFF"><INPUT TYPE=PASSWORD CLASS="textinput" NAME="editedpassword" VALUE="$gmselectedauthorinfo[1]" SIZE=20></TD></TR>
<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag E-Mail:</FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT BGCOLOR="#FFFFFF"><INPUT TYPE=TEXT CLASS="textinput" NAME="editedemail" VALUE="$gmselectedauthorinfo[2]" SIZE=20></TD></TR>
<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Homepage:</FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT BGCOLOR="#FFFFFF"><INPUT TYPE=TEXT CLASS="textinput" NAME="editedhomepage" VALUE="$gmselectedauthorinfo[3]" SIZE=20></TD></TR>

GMEDITSELECTEDAUTHORTOP

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can post new entries?:</FONT></TD>);

if ($gmselectedauthorinfo[6] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedentryaccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editedentryaccess" VALUE="N"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedentryaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedentryaccess" VALUE="N" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can edit entries?:</FONT></TD>);

if ($gmselectedauthorinfo[7] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedentryeditaccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editedentryeditaccess" VALUE="N"> No<BR><INPUT TYPE=RADIO NAME="editedentryeditaccess" VALUE="O"> Only their own entries</FONT></TD></TR>\n);
} elsif ($gmselectedauthorinfo[7] eq "O") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedentryeditaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedentryeditaccess" VALUE="N"> No<BR><INPUT TYPE=RADIO NAME="editedentryeditaccess" VALUE="O" CHECKED> Only their own entries</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedentryeditaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedentryeditaccess" VALUE="N" CHECKED> No<BR><INPUT TYPE=RADIO NAME="editedentryeditaccess" VALUE="O"> Only their own entries</FONT></TD></TR>\n);
}

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can configure?:</FONT></TD>);

if ($gmselectedauthorinfo[8] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedconfigureaccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editedconfigureaccess" VALUE="N"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedconfigureaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedconfigureaccess" VALUE="N" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can edit templates?:</FONT></TD>);

if ($gmselectedauthorinfo[9] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedtemplateaccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editedtemplateaccess" VALUE="N"> No<BR><INPUT TYPE=RADIO NAME="editedtemplateaccess" VALUE="O"> Only header/footer/sidebar</FONT></TD></TR>\n);
} elsif ($gmselectedauthorinfo[9] eq "O") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedtemplateaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedtemplateaccess" VALUE="N"> No<BR><INPUT TYPE=RADIO NAME="editedtemplateaccess" VALUE="O" CHECKED> Only header/footer/sidebar</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedtemplateaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedtemplateaccess" VALUE="N" CHECKED> No<BR><INPUT TYPE=RADIO NAME="editedtemplateaccess" VALUE="O"> Only header/footer/sidebar</FONT></TD></TR>\n);
}

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can edit authors?:</FONT></TD>);

if ($gmselectedauthorinfo[10] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedauthoraccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editedauthoraccess" VALUE="N"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedauthoraccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedauthoraccess" VALUE="N" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can rebuild files?:</FONT></TD>);

if ($gmselectedauthorinfo[11] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedrebuildaccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editedrebuildaccess" VALUE="N"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedrebuildaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedrebuildaccess" VALUE="N" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can view CP log?:</FONT></TD>);

if ($gmselectedauthorinfo[12] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedcplogaccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editedcplogaccess" VALUE="N"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedcplogaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedcplogaccess" VALUE="N" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can use bookmarklets?:</FONT></TD>);

if ($gmselectedauthorinfo[13] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedbookmarkletaccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editedbookmarkletaccess" VALUE="N"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedbookmarkletaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedbookmarkletaccess" VALUE="N" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can upload files?:</FONT></TD>);

if ($gmselectedauthorinfo[14] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editeduploadaccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editeduploadaccess" VALUE="N"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editeduploadaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editeduploadaccess" VALUE="N" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR><TD VALIGN=MIDDLE ALIGN=RIGHT BGCOLOR="#FFFFFF">$gmfonttag Can login to gm.cgi?:</FONT></TD>);

if ($gmselectedauthorinfo[15] eq "Y") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedloginaccess" VALUE="Y" CHECKED> Yes <INPUT TYPE=RADIO NAME="editedloginaccess" VALUE="N"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFFF">$gmfonttag<INPUT TYPE=RADIO NAME="editedloginaccess" VALUE="Y"> Yes <INPUT TYPE=RADIO NAME="editedloginaccess" VALUE="N" CHECKED> No</FONT></TD></TR>\n);
}

print<<GMEDITSELECTEDAUTHORBOTTOM;

</TABLE></TD></TR></TABLE>
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Changes To This Author"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Author Panel">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"I always wanted to be somebody, but I should have been more specific."&#151;Lily Tomlin</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITSELECTEDAUTHORBOTTOM

exit;

}

# -------------------------
# save changes to an author
# -------------------------

sub gm_saveauthorchanges {

&gm_validate;

if ($gmauthoraccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to modify an author ($IN{'authororiginalname'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to delete authors.</FONT></B><P>);
	&gm_frontpage;
}

$IN{'editedname'} =~ s/\|//g;
$IN{'editedpassword'} =~ s/\|//g;
$IN{'editedemail'} =~ s/\|//g;
$IN{'editedhomepage'} =~ s/\|//g;

$IN{'editedname'} =~ s/^\s+//;
$IN{'editedname'} =~ s/\s+$//;
$IN{'editedpassword'} =~ s/^\s+//;
$IN{'editedpassword'} =~ s/\s+$//;

if (($IN{'editedname'} eq "") || ($IN{'editedpassword'} eq "")) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You left either the name or password fields blank.  Please try again.</FONT></B><P>);
	&gm_editauthors;
}

open (FUNNYFEET, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmauthordata = <FUNNYFEET>;
close (FUNNYFEET);

$gmnamesduplicate = "no";

foreach $gmauthordataline (@gmauthordata) {
	@gmauthordatainfo = split (/\|/, $gmauthordataline);
	if (($IN{'authororiginalname'} ne $IN{'editedname'}) && ($gmauthordatainfo[0] eq $IN{'editedname'})) { 
		&gm_writetocplog("$IN{'authorname'} attempted to add a duplicate of $IN{'editedname'} via $IN{'authororiginalname'}");
		$statusnote = qq(<B><FONT COLOR="#FF0000">You can't add a duplicate of another author.</FONT></B><P>);
		&gm_editauthors;
	}
}

if (($IN{'editedname'} ne $IN{'authororiginalname'}) && ($keeplog eq "yes")) {
	if ($IN{'authorname'} eq $IN{'authororiginalname'}) {
		&gm_writetocplog("$IN{'authorname'} changed his/her own name to $IN{'editedname'}");
	} else {
		&gm_writetocplog("$IN{'authorname'} changed $IN{'authororiginalname'}'s name to $IN{'editedname'}");
	}
}

$temphomepageprefix = substr($IN{'editedhomepage'}, 0, 7);
if ($temphomepageprefix ne "http://") { $IN{'editedhomepage'} = "http://$IN{'editedhomepage'}"; }

if ($IN{'editedhomepage'} eq "http://") { $IN{'editedhomepage'} = ""; }

open (FUNNYFEET, ">gm-authors.cgi") || &gm_dangermouse("Can't write to the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
foreach $gmauthordataline (@gmauthordata) {
	chomp ($gmauthordataline);
	@gmauthorinfo = split (/\|/, $gmauthordataline);
	if ($IN{'authororiginalname'} ne $gmauthorinfo[0]) {
		print FUNNYFEET "$gmauthordataline\n";
	} else {
		print FUNNYFEET "$IN{'editedname'}|$IN{'editedpassword'}|$IN{'editedemail'}|$IN{'editedhomepage'}|$IN{'authororiginaldate'}|$IN{'authororiginalentries'}|$IN{'editedentryaccess'}|$IN{'editedentryeditaccess'}|$IN{'editedconfigureaccess'}|$IN{'editedtemplateaccess'}|$IN{'editedauthoraccess'}|$IN{'editedrebuildaccess'}|$IN{'editedcplogaccess'}|$IN{'editedbookmarkletaccess'}|$IN{'editeduploadaccess'}|$IN{'editedloginaccess'}\n";
	}
}
close (FUNNYFEET);

if ($IN{'authororiginalname'} eq $IN{'authorname'}) {
	$IN{'authorname'} = $IN{'editedname'};
	$IN{'authorpassword'} = $IN{'editedpassword'};
}

if ($IN{'authorname'} eq $IN{'editedname'}) {
	&gm_writetocplog("$IN{'authorname'} edited his/her own info/access");
} else {
	&gm_writetocplog("$IN{'authorname'} edited $IN{'editedname'}'s info/access");
}

$statusnote = qq(<B><FONT COLOR="#0000FF">$IN{'editedname'}'s info/access has been edited.</FONT></B><P>);
&gm_editauthors;

}

# ------------------
# configuration menu
# ------------------

sub gm_configuration {

&gm_validate;

if ($gmconfigurationaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to configure this program without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to configure this program.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readconfig;

&date;

$censorlist = &delouse($censorlist);
$otherfilelist = &delouse($otherfilelist);

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Configuration Options</FONT></B><P>); }

print<<GMCONFIGMENUTOP;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=700>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#FFFFD0" COLSPAN=2>$gmfonttag<B>Path Configuration</B><BR><FONT SIZE=1>Your paths tell Greymatter where to look for things on your site; local paths are relative to your server, and the website paths are their respective pointers on the web.  Each of these paths MUST be correctly set for Greymatter to work correctly; if you can't seem to set them right, use virtual paths (with "." and "../") instead; read the Troubleshooting section of the manual for more information.  It's a good idea to run "Diagnostics & Repair" after saving changes to your paths.</FONT></FONT></TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=100%>$gmfonttag<B>Local Log Path:</B><BR><FONT SIZE=1>The main weblog/journal directory on your account, where your main index file is.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedlogpath" VALUE="$LogPath" SIZE=30 STYLE="width: 400">$gmfonttag</TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=100%>$gmfonttag<B>Local Entries/Archives Path:</B><BR><FONT SIZE=1>The directory on your account where your entry files (current and archived) are to be stored.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedentriespath" VALUE="$EntriesPath" SIZE=30 STYLE="width: 400">$gmfonttag</TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=100%>$gmfonttag<B>Local CGI Path:</B><BR><FONT SIZE=1>The place on your account where you keep all your Greymatter CGI files ("gm*.cgi").</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedcgilocalpath" VALUE="$cgilocalpath" SIZE=30 STYLE="width: 400">$gmfonttag</TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=100%>$gmfonttag<B>Website Log Path:</B><BR><FONT SIZE=1>The website address of the directory where your main index file is.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedlogwebpath" VALUE="$LogWebPath" SIZE=30 STYLE="width: 400">$gmfonttag</TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=100%>$gmfonttag<B>Website Entries Path:</B><BR><FONT SIZE=1>The website address of the directory where all your entries are to be stored.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedentrieswebpath" VALUE="$EntriesWebPath" SIZE=30 STYLE="width: 400" WIDTH=100%>$gmfonttag</TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT>$gmfonttag<B>Website CGI Path:</B><BR><FONT SIZE=1>The website address of the directory where all your Greymatter CGI files are kept.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedcgiwebpath" VALUE="$cgiwebpath" SIZE=30 STYLE="width: 400">$gmfonttag</TD></TR>

</TABLE></TD></TR></TABLE>

<P>

<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=700>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#D0D0FF" COLSPAN=2>$gmfonttag<B>Index & Archive Options</B><BR><FONT SIZE=1>Options relating to your main index and your archives.</FONT></FONT></TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Index filename:</B><BR><FONT SIZE=1>The filename of your log/journal's main index.  If you enable "Keep archive master index", Greymatter will create that file in the archives directory with the same filename.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=350></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedindexfilename" VALUE="$indexfilename" SIZE=15 STYLE="width: 200">$gmfonttag</TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>.suffix to entry files:</B><BR><FONT SIZE=1>If you have "Generate pages for individual entries" enabled, this is the suffix those pages will have.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedentrysuffix" VALUE="$entrysuffix" SIZE=15 STYLE="width: 200">$gmfonttag</TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>.suffix to log archives:</B><BR><FONT SIZE=1>If you have "Keep monthly/weekly log archives" enabled, this is the suffix those log archive files will have.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedlogarchivesuffix" VALUE="$logarchivesuffix" SIZE=15 STYLE="width: 200">$gmfonttag</TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Days to keep on main index:</B><BR><FONT SIZE=1>The number of days' worth of entries Greymatter will list on your main index before scrolling them off.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedindexdays" VALUE="$indexdays" SIZE=5 MAXLENGTH=5>$gmfonttag</TD></TR>

GMCONFIGMENUTOP

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Generate pages for individual entries?</B><BR><FONT SIZE=1>Specifies whether you want individual entries to have their own pages.  Comments are disabled if this is turned off.</FONT></FONT></TD>);

if ($generateentrypages eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedgenerateentrypages" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedgenerateentrypages" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedgenerateentrypages" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedgenerateentrypages" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Keep archive master index?</B><BR><FONT SIZE=1>If enabled, Greymatter will keep an index (with the same filename as above) in your entries/archives directory, intended to be an overview of all your archives.</FONT></FONT></TD>);

if ($keeparchivemasterindex eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedkeeparchivemasterindex" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedkeeparchivemasterindex" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedkeeparchivemasterindex" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedkeeparchivemasterindex" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Keep monthly/weekly log archives?</B><BR><FONT SIZE=1>If enabled, Greymatter will keep archive files of your log in monthly or weekly installments in your entries/archives directory.</FONT></FONT></TD>);

if ($keepmonthlyarchives eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedkeepmonthlyarchives" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedkeepmonthlyarchives" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedkeepmonthlyarchives" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedkeepmonthlyarchives" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Keep main index and archive log<BR>indexes concurrent with each other?</B><BR><FONT SIZE=1>If enabled, both new and archived entries will be listed in the monthly/weekly archives; if disabled, Greymatter won't list entries there until they've scrolled off the main index.  For simplicity's sake, it's a good idea leave this on.</FONT></FONT></TD>);

if ($concurrentmainandarchives eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedconcurrentmainandarchives" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedconcurrentmainandarchives" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedconcurrentmainandarchives" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedconcurrentmainandarchives" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Archive by month or week?</B><BR><FONT SIZE=1>If "Keep monthly/weekly log archives" is enabled, this specifies whether the log archives will be generated by the month or by the week.</FONT></FONT></TD>);

if ($archiveformat eq "week") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedarchiveformat" VALUE="month"> Monthly &#160; <INPUT TYPE=RADIO NAME="editedarchiveformat" VALUE="week" CHECKED> Weekly</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedarchiveformat" VALUE="month" CHECKED> Monthly &#160; <INPUT TYPE=RADIO NAME="editedarchiveformat" VALUE="week"> Weekly</FONT></TD></TR>\n);
}

print qq(</TABLE></TD></TR></TABLE>

<P>

<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=700>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#D0D0FF" COLSPAN=2>$gmfonttag<B>E-Mail Options</B><BR><FONT SIZE=1>Options relating to e-mail setup and notification.  If you don't plan to have Greymatter send you e-mails, you can safely ignore the "E-Mail Program Location" and "E-Mail(s) to send notices to" fields.</FONT></FONT></TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=100%>$gmfonttag<B>E-Mail Program Location:</B><BR><FONT SIZE=1>The pointer to the mail program (usually Sendmail) on your account.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedmailprog" VALUE="$mailprog" SIZE=30 STYLE="width: 400">$gmfonttag</TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=100%>$gmfonttag<B>E-Mail(s) to send notices to:</B><BR><FONT SIZE=1>The e-mail addresses you want all notifications (if any) to be sent to.  Separate multiple e-mail addresses with semicolons.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editednotifyemail" VALUE="$NotifyEmail" SIZE=30 STYLE="width: 400">$gmfonttag</TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=100%>$gmfonttag<B>Send e-mail notifications for:</B><BR><FONT SIZE=1>Indicates whether you want Greymatter to send e-mails notifying you of new karma votes, new comment postings, both karma and comments, or to disable e-mail notification altogether.</FONT></FONT></TD>);

if ($NotifyForStatus eq "karma") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="karma" CHECKED> New karma votes &#160; <INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="comments"> New comments<BR><INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="neither"> Neither</FONT></TD></TR>\n);
} elsif ($NotifyForStatus eq "comments") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="karma"> New karma votes &#160; <INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="comments" CHECKED> New comments<BR><INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="neither"> Neither</FONT></TD></TR>\n);
} elsif ($NotifyForStatus eq "both") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="karma"> New karma votes &#160; <INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="comments"> New comments<BR><INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="both" CHECKED> Both &#160; <INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="neither"> Neither</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="karma"> New karma votes &#160; <INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="comments"> New comments<BR><INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editednotifyforstatus" VALUE="neither" CHECKED> Neither</FONT></TD></TR>\n);
}

print qq(</TABLE></TD></TR></TABLE>

<P>

<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=700>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#D0D0FF" COLSPAN=2>$gmfonttag<B>Karma & Comments Options</B><BR><FONT SIZE=1>Options relating to karma voting and comment posting.  Obviously, certain options can be ignored if you have their respective functions disabled (for example, if you disable comments or have "Generate pages for individual entries" turned off, none of the options relating to comments will have any effect).</FONT></FONT></TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Allow karma voting and/or comment posting?</B><BR><FONT SIZE=1>Specifies whether you want to permit voting on karma, posting comments, both, or neither, on your site.  You can leave them enabled and still turn karma or comments on or off for individual entries; to disable either or both will override that for ALL entries.</FONT></FONT></TD>);

if ($allowkarmaorcomments eq "karma") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="karma" CHECKED> Karma only &#160; <INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="comments"> Comments only<BR><INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="neither"> Neither</FONT></TD></TR>\n);
} elsif ($allowkarmaorcomments eq "comments") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="karma"> Karma only &#160; <INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="comments" CHECKED> Comments only<BR><INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="neither"> Neither</FONT></TD></TR>\n);
} elsif ($allowkarmaorcomments eq "both") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="karma"> Karma only <INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="comments"> Comments only<BR><INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="both" CHECKED> Both <INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="neither"> Neither</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="karma"> Karma only &#160; <INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="comments"> Comments only<BR><INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editedallowkarmaorcomments" VALUE="neither" CHECKED> Neither</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Order of comments on entry pages:</B><BR><FONT SIZE=1>The order in which you want comments displayed.  If "ascending", they'll be listed from newest to oldest, with the newest comment at the top; if "descending", from first to last, with the first comment at the top.</FONT></FONT></TD>);

if ($commentsorder eq "ascending") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcommentsorder" VALUE="ascending" CHECKED> Ascending &#160; <INPUT TYPE=RADIO NAME="editedcommentsorder" VALUE="descending"> Descending</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcommentsorder" VALUE="ascending"> Ascending &#160; <INPUT TYPE=RADIO NAME="editedcommentsorder" VALUE="descending" CHECKED> Descending</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Can post comments and vote on karma in archives?</B><BR><FONT SIZE=1>If enabled, visitors can cast karma votes or post comments (if applicable) on entries no longer listed on the main index.  Enabling this may slow down your site over time.</FONT></FONT></TD>);

if ($posttoarchives eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedposttoarchives" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedposttoarchives" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedposttoarchives" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedposttoarchives" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Karma voting on by default?</B><BR><FONT SIZE=1>Specifies whether "Allow karma voting on this entry" is preselected to "Yes" or "No" by default on the "Add a new entry" screen.</FONT></FONT></TD>);

if ($allowkarmadefault eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowkarmadefault" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedallowkarmadefault" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowkarmadefault" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedallowkarmadefault" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Comment posting on by default?</B><BR><FONT SIZE=1>Specifies whether "Allow comments to be posted to this entry" is preselected to "Yes" or "No" by default on the "Add a new entry" screen.</FONT></FONT></TD>);

if ($allowcommentsdefault eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowcommentsdefault" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedallowcommentsdefault" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowcommentsdefault" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedallowcommentsdefault" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>HTML allowed in comments?</B><BR><FONT SIZE=1>Indicates whether you want to allow visitors to include HTML codes in their comments, or to have Greymatter strip them out.  You can also specify whether only the codes for links, bold and italics can be included, or just the codes for links.</FONT></FONT></TD>);

if ($allowhtmlincomments eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="yes" CHECKED> All HTML allowed &#160; <INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="no"> No HTML allowed<BR><INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="linkboldital"> Linking, Bold & Italic code only<BR><INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="linkonly"> Linking code only</FONT></TD></TR>\n);
} elsif ($allowhtmlincomments eq "linkboldital") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="yes"> All HTML allowed &#160; <INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="no"> No HTML allowed<BR><INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="linkboldital" CHECKED> Linking, Bold & Italic code only<BR><INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="linkonly"> Linking code only</FONT></TD></TR>\n);
} elsif ($allowhtmlincomments eq "linkonly") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="yes"> All HTML allowed &#160; <INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="no"> No HTML allowed<BR><INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="linkboldital"> Linking, Bold & Italic code only<BR><INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="linkonly" CHECKED> Linking code only</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="yes"> All HTML allowed &#160; <INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="no" CHECKED> No HTML allowed<BR><INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="linkboldital"> Linking, Bold & Italic code only<BR><INPUT TYPE=RADIO NAME="editedallowhtmlincomments" VALUE="linkonly"> Linking code only</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Auto-link URLs in comments?</B><BR><FONT SIZE=1>If enabled, Greymatter will automatically link to any website or e-mail addresses that users post in their comments (unless you've enabled linking above and they've already linked the website/e-mail address themselves).</FONT></FONT></TD>);

if ($autolinkurls eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedautolinkurls" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedautolinkurls" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedautolinkurls" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedautolinkurls" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Strip new lines from comments?</B><BR><FONT SIZE=1>If enabled, all line and paragraph breaks are stripped when displaying visitors' comments, turning them into unbroken blocks of text; if disabled, Greymatter preserves the visitors' original formatting.</FONT></FONT></TD>);

if ($striplinesfromcomments eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedstriplinesfromcomments" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedstriplinesfromcomments" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedstriplinesfromcomments" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedstriplinesfromcomments" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Allow multiple karma votes from same IP?</B><BR><FONT SIZE=1>If enabled, the same visitor could cast multiple karma votes on the same entry; if disabled, only one vote per visitor is allowed.</FONT></FONT></TD>);

if ($allowmultiplekarmavotes eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowmultiplekarmavotes" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedallowmultiplekarmavotes" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedallowmultiplekarmavotes" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedallowmultiplekarmavotes" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Mention it in the control panel log when<BR>comments and karma votes are added?</B><BR><FONT SIZE=1>Enable this if you want Greymatter to mention all new comments and karma votes in the control panel log.</FONT></FONT></TD>);

if ($logkarmaandcomments eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedlogkarmaandcomments" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedlogkarmaandcomments" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedlogkarmaandcomments" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedlogkarmaandcomments" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(</TABLE></TD></TR></TABLE>

<P>

<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=700>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#D0D0FF" COLSPAN=2>$gmfonttag<B>Date & Time Options</B><BR><FONT SIZE=1>Miscellaneous options regarding to dates & times.  Use the wide variety date and time variables in your templates to fine-tune how you want the date and time to appear on your site.</FONT></FONT></TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Server Offset Time:</B><BR><FONT SIZE=1>As of this moment, Greymatter reads your time as <B>$hour\:$mintwo $AMPM</B>.  If this is incorrect, specify the number of hours to add or subtract from this time (to subtract, make it a negative number, with a minus in front of it).</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedoffsettime" VALUE="$serveroffset" SIZE=5 MAXLENGTH=3>$gmfonttag</TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Your Time Zone:</B><BR><FONT SIZE=1>The time zone you live in.  This is what will appear wherever you use the {{timezone}} variable in your templates.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedtimezone" VALUE="$timezone" SIZE=5 MAXLENGTH=5>$gmfonttag</TD></TR>

</TABLE></TD></TR></TABLE>

<P>

<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=700>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#D0D0FF" COLSPAN=2>$gmfonttag<B>File Uploading Options</B><BR><FONT SIZE=1>Options relating to uploading files from within Greymatter.</FONT></FONT></TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Allowed File Types:</B><BR><FONT SIZE=1>If you only wish to allow certain types of files to be uploaded, enter their file suffixes here.  Separate allowed file types by semicolons (for example, "jpg;gif;zip").  Leave this blank to allow any type of file to be uploaded.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editeduploadfilesallowed" VALUE="$uploadfilesallowed" SIZE=20 STYLE="width: 320">$gmfonttag</TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Maximum Filesize Allowed:</B><BR><FONT SIZE=1>If you don't wish to allow files larger than a certain size to be uploaded, specify that limit here (in KB/kilobytes).  Leave this on "0" to allow files of any size to be uploaded.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editeduploadfilesizelimit" VALUE="$uploadfilesizelimit" SIZE=5 MAXLENGTH=5>$gmfonttag KB</TD></TR>

</TABLE></TD></TR></TABLE>

<P>

<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=700>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#D0D0FF" COLSPAN=2>$gmfonttag<B>Censoring Options</B><BR><FONT SIZE=1>Words or phrases you want to censor on your site (if any), and where to censor them.<BR>Censored terms will be turned into "*" asterisks.</FONT></FONT></TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Enable censoring?</B><BR><FONT SIZE=1>Specifies whether you want any words or phrases in your censor list to appear censored for entries, comments, or both.  Leave it on "Neither" to disable censorship.</FONT></FONT></TD>);

if ($censorenabled eq "entries") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="entries" CHECKED> Entries only &#160; <INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="comments"> Comments only<BR><INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="neither"> Neither</FONT></TD></TR>\n);
} elsif ($censorenabled eq "comments") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="entries"> Entries only &#160; <INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="comments" CHECKED> Comments only<BR><INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="neither"> Neither</FONT></TD></TR>\n);
} elsif ($censorenabled eq "both") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="entries"> Entries only &#160; <INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="comments"> Comments only<BR><INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="both" CHECKED> Both &#160; <INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="neither"> Neither</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="entries"> Entries only &#160; <INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="comments"> Comments only<BR><INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editedcensorenabled" VALUE="neither" CHECKED> Neither</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Censor List</B><BR><FONT SIZE=1>Enter any words or phrases you want to censor, separated by lines (press return after each word/phrase).  Use [brackets] around words/phrases to censor the term only if it's not part of another word/phrase; for example, censoring the word hell would render hell as **** and shell as s****, but censoring [hell] would only turn hell by itself into asterisks, and leave the word shell alone.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><TEXTAREA NAME="editedcensorlist" COLS=25 ROWS=6 WRAP=VIRTUAL STYLE="width: 320">$censorlist</TEXTAREA>$gmfonttag</FONT></TD></TR>

</TABLE></TD></TR></TABLE>

<P>

<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=700>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#D0D0FF" COLSPAN=2>$gmfonttag<B>Connect Other Files (Advanced Users Only)</B><BR><FONT SIZE=1>If you wish, you can connect other files on your account to Greymatter, and have them treated as if they were one of Greymatter's regular index files; for example, using {{header}} or {{footer}} in another file to insert your Greymatter header or footer into that file.  (You'll need to edit & upload these files to your account outside Greymatter.)  This is <B>only recommended for advanced users</B> that are already comfortable using Greymatter.</FONT></FONT></TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Filename List</B><BR><FONT SIZE=1>To connect a file to Greymatter, <B>CHMOD it to 666</B>&#151;making sure it contains whatever Greymatter variables you wish&#151;and enter its filename on the right; place each filename on separate lines.  If the file isn't in the same directory as gm.cgi, then use virtual paths relative to where it's running from.  For example, if you want to connect "test.htm" and it's in the directory above gm.cgi, you'd use ../test.htm; or, if you run gm.cgi from /here/cgi-bin and test.htm was in /there/log, you'd use ../../there/log ("../" means to go up one directory).  Greymatter will automatically create a "pattern" file in your entries directory for each filename, and whenever you reupload a changed file, Greymatter will automatically update its stored pattern for that file.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><TEXTAREA NAME="editedotherfilelist" COLS=25 ROWS=10 WRAP=VIRTUAL STYLE="width: 320">$otherfilelist</TEXTAREA>$gmfonttag</FONT></TD></TR>

<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Update them when adding entries?</B><BR><FONT SIZE=1>If "Yes", then Greymatter will automatically update any of the connected files above when new entries are added; if not, they'll only be updated whenever you rebuild them (either specifically, or by rebuilding everything).</FONT></FONT></TD>);

if ($otherfilelistentryrebuild eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedotherfilelistentryrebuild" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedotherfilelistentryrebuild" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedotherfilelistentryrebuild" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedotherfilelistentryrebuild" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(</TABLE></TD></TR></TABLE>

<P>

<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=700>

<TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#D0D0FF" COLSPAN=2>$gmfonttag<B>Miscellaneous Options</B></FONT></TD></TR>

<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Enable cookies?</B><BR><FONT SIZE=1>By default, Greymatter keeps a cookie on your browser that remembers your name and password, so you don't have to type them in each time you log on.  To disable and delete Greymatter's cookies, select "No" and check the checkbox.</FONT></FONT></TD>);

if ($cookiesallowed eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcookiesallowed" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedcookiesallowed" VALUE="no"> No);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcookiesallowed" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedcookiesallowed" VALUE="no" CHECKED> No);
}

print qq(<BR><INPUT TYPE=CHECKBOX NAME="editeddeletecookies" VALUE="yes"> Delete cookies set by Greymatter?</FONT></TD></TR>\n<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Keep control panel log?</B><BR><FONT SIZE=1>Specifies whether you want Greymatter to keep its internal log of all activity; disable this if you want to shut it off.</FONT></FONT></TD>);

if ($keeplog eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedkeeplog" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedkeeplog" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedkeeplog" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedkeeplog" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Allow "easy formatting"?</B><BR><FONT SIZE=1>With "easy formatting", bold text, italics & underlining can be done easily by bracketing text with two **asterisks**, \\\\backslashes\\\\ or __underlines__ respectively.  You can specify whether this is enabled in entries, comments, or both; if disabled, the characters won't be converted.</FONT></FONT></TD>);

if ($inlineformatting eq "entries") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="entries" CHECKED> Entries only &#160; <INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="comments"> Comments only<BR><INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="neither"> Neither</FONT></TD></TR>\n);
} elsif ($inlineformatting eq "comments") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="entries"> Entries only &#160; <INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="comments" CHECKED> Comments only<BR><INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="neither"> Neither</FONT></TD></TR>\n);
} elsif ($inlineformatting eq "both") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="entries"> Entries only &#160; <INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="comments"> Comments only<BR><INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="both" CHECKED> Both &#160; <INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="neither"> Neither</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="entries"> Entries only &#160; <INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="comments"> Comments only<BR><INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="both"> Both &#160; <INPUT TYPE=RADIO NAME="editedinlineformatting" VALUE="neither" CHECKED> Neither</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Default entry list view:</B><BR><FONT SIZE=1>This specifies which view will be the default when you go to the Edit An Entry selection menu.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<SELECT NAME="editeddefaultentrylistview" CLASS="selectlist">\n);

if ($defaultentrylistview eq "main") {
	if ($indexdays eq "1") {
		print qq(<OPTION VALUE="main" SELECTED> Current entries \($indexdays day\)\n);
	} else {
		print qq(<OPTION VALUE="main" SELECTED> Current entries \($indexdays days\)\n);
	}
} else {
	if ($indexdays eq "1") {
		print qq(<OPTION VALUE="main"> Current entries \($indexdays day\)\n);
	} else {
		print qq(<OPTION VALUE="main"> Current entries \($indexdays days\)\n);
	}
}

if ($defaultentrylistview eq "onlyyou") {
	print qq(<OPTION VALUE="onlyyou" SELECTED> All entries by you\n);
} else {
	print qq(<OPTION VALUE="onlyyou"> All entries by you\n);
}

if ($defaultentrylistview eq "more") {
	print qq(<OPTION VALUE="more" SELECTED> All extended entries\n);
} else {
	print qq(<OPTION VALUE="more"> All extended entries\n);
}

if ($defaultentrylistview eq "open") {
	print qq(<OPTION VALUE="open" SELECTED> All open entries\n);
} else {
	print qq(<OPTION VALUE="open"> All open entries\n);
}

if ($defaultentrylistview eq "closed") {
	print qq(<OPTION VALUE="closed" SELECTED> All closed entries\n);
} else {
	print qq(<OPTION VALUE="closed"> All closed entries\n);
}

if ($defaultentrylistview eq "all") {
	print qq(<OPTION VALUE="all" SELECTED> All entries\n);
} else {
	print qq(<OPTION VALUE="all"> All entries\n);
}

print qq(</SELECT></FONT></TD></TR>\n<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Order of list links:</B><BR><FONT SIZE=1>The order in which you want links to be displayed in log list variables&#151;check the manual for more information on those.  If "ascending", the links will be listed from newest to oldest, with the newest entry at the top; if "descending", from first to last, with the first entry at the top.</FONT></FONT></TD>);

if ($entrylistsortorder eq "ascending") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedentrylistsortorder" VALUE="ascending" CHECKED> Ascending &#160; <INPUT TYPE=RADIO NAME="editedentrylistsortorder" VALUE="descending"> Descending</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedentrylistsortorder" VALUE="ascending"> Ascending &#160; <INPUT TYPE=RADIO NAME="editedentrylistsortorder" VALUE="descending" CHECKED> Descending</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Log entry list variable number:</B><BR><FONT SIZE=1>The number of entries to link to, starting from the most recent, whenever the "number" variant of the log entrylist variables (for example, if this is set to 5, using {{logmoreentrylist number}} would generate a list of links to the five most recent extended entries).  Check the manual for more information on those variables.</FONT></FONT></TD><TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="editedentrylistcountnumber" VALUE="$entrylistcountnumber" SIZE=5 MAXLENGTH=5>$gmfonttag</TD></TR>\n);

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Link to entries in {{logentrylist comments}} only if comments are active?</B><BR><FONT SIZE=1>If you use {{logentrylist comments}} and its related variables (see the manual for more information), this specifies whether to list only entries to which comments can still be posted.</FONT></FONT></TD>);

if ($commententrylistonlyifokay eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcommententrylistonlyifokay" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedcommententrylistonlyifokay" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedcommententrylistonlyifokay" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedcommententrylistonlyifokay" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#FFFFFF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>Entries to link to in 	{{calendar}}:</B><BR><FONT SIZE=1>Whenever you use {{calendar}} or {{calendarweek}} to generate tables linking to your entries, this specifies whether you want to link to the most recent entry for that day, or to link only to extended entries.  (It won't generate links at all if "Generate pages for individual entries" is turned off.)</FONT></FONT></TD>);

if ($linktocalendarentries eq "all") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedlinktocalendarentries" VALUE="all" CHECKED> Always link to entry for that calendar day<BR><INPUT TYPE=RADIO NAME="editedlinktocalendarentries" VALUE="more"> Link only to extended entries</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedlinktocalendarentries" VALUE="all"> Always link to entry for that calendar day<BR><INPUT TYPE=RADIO NAME="editedlinktocalendarentries" VALUE="more" CHECKED> Link only to extended entries</FONT></TD></TR>\n);
}

print qq(<TR BGCOLOR="#F8F8FF"><TD VALIGN=MIDDLE ALIGN=RIGHT WIDTH=50%>$gmfonttag<B>"Automatically rebuild" selected by default?</B><BR><FONT SIZE=1>Selects whether the option to automatically rebuild files after saving changes to templates or entries is prechecked by default.  (Authors without access to rebuilding files won't see this option.)</FONT></FONT></TD>);

if ($automaticrebuilddefault eq "yes") {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedautomaticrebuilddefault" VALUE="yes" CHECKED> Yes &#160; <INPUT TYPE=RADIO NAME="editedautomaticrebuilddefault" VALUE="no"> No</FONT></TD></TR>\n);
} else {
	print qq(<TD VALIGN=MIDDLE ALIGN=CENTER WIDTH=50%>$gmfonttag<INPUT TYPE=RADIO NAME="editedautomaticrebuilddefault" VALUE="yes"> Yes &#160; <INPUT TYPE=RADIO NAME="editedautomaticrebuilddefault" VALUE="no" CHECKED> No</FONT></TD></TR>\n);
}

print<<GMCONFIGMENUBOTTOM;

</TABLE></TD></TR></TABLE>
<P>
<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=10 CELLSPACING=0 BGCOLOR="#FFD0D0"><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<FONT SIZE=1><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Diagnostics & Repair"></TD></TR></TABLE></TD></TR></TABLE>
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Configuration"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">

</FORM>
<P>
<FONT SIZE=1>"It's better to change your shoes than to carpet the world."&#151;Stuart Smalley</FONT>
$gmframebottom

</BODY>
</HTML>

GMCONFIGMENUBOTTOM

$statusnote = "";

exit;

}

# ----------------
# save config file
# ----------------

sub gm_saveconfiguration {

&gm_validate;

if ($gmconfigurationaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to save changes to the config file without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to change the config file.</FONT></B><P>);
	&gm_frontpage;
}

chomp ($IN{'editedcensorlist'});
$IN{'editedcensorlist'} = &relouse($IN{'editedcensorlist'});
chomp ($IN{'editedotherfilelist'});
$IN{'editedotherfilelist'} = &relouse($IN{'editedotherfilelist'});

$IN{'editedlogpath'} = &configdelouse($IN{'editedlogpath'});
$IN{'editedentriespath'} = &configdelouse($IN{'editedentriespath'});
$IN{'editedlogwebpath'} = &configdelouse($IN{'editedlogwebpath'});
$IN{'editedentrieswebpath'} = &configdelouse($IN{'editedentrieswebpath'});
$IN{'editednotifyemail'} = &configdelouse($IN{'editednotifyemail'});
$IN{'editedindexfilename'} = &configdelouse($IN{'editedindexfilename'});
$IN{'editedentrysuffix'} = &configdelouse($IN{'editedentrysuffix'});
$IN{'editedindexdays'} = &configdelouse($IN{'editedindexdays'});
$IN{'editedoffsettime'} = &configdelouse($IN{'editedoffsettime'});
$IN{'editedtimezone'} = &configdelouse($IN{'editedtimezone'});
$IN{'editedmailprog'} = &configdelouse($IN{'editedmailprog'});
$IN{'editedcgilocalpath'} = &configdelouse($IN{'editedcgilocalpath'});
$IN{'editedcgiwebpath'} = &configdelouse($IN{'editedcgiwebpath'});
$IN{'editedentrylistcountnumber'} = &configdelouse($IN{'editedentrylistcountnumber'});
$IN{'editedlogarchivesuffix'} = &configdelouse($IN{'editedlogarchivesuffix'});

$IN{'editedcensorlist'} =~ s/^\s+//;
$IN{'editedcensorlist'} =~ s/\s+$//;
$IN{'editedotherfilelist'} =~ s/^\s+//;
$IN{'editedotherfilelist'} =~ s/^\s+//;

$IN{'editedentrysuffix'} =~ s/\.//g;
$IN{'editednotifyemail'} =~ s/ //g;
$IN{'editedlogarchivesuffix'} =~ s/\.//g;

if (($IN{'editedlogpath'} eq "") || ($IN{'editedentriespath'} eq "") || ($IN{'editedlogwebpath'} eq "") || ($IN{'editedentrieswebpath'} eq "") || ($IN{'editedindexfilename'} eq "") || ($IN{'editedentrysuffix'} eq "") || ($IN{'editedindexdays'} eq "") || ($IN{'editedoffsettime'} eq "") || ($IN{'editedtimezone'} eq "") || ($IN{'editedcgilocalpath'} eq "") || ($IN{'editedcgiwebpath'} eq "") || ($IN{'editedentrylistcountnumber'} eq "") || ($IN{'editedlogarchivesuffix'} eq "")) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You left one or more of the required fields blank.  Please try again.</FONT></B><P>);
	&gm_configuration;
}

if ($IN{'editedindexdays'} =~ /\D/) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">"Days to keep on main index" must be a number.</FONT></B><P>);
	&gm_configuration;
}

if ($IN{'editedoffsettime'} =~ /\D/) {
	unless ($IN{'editedoffsettime'} =~ /-/) {
		$statusnote = qq(<B><FONT COLOR="#FF0000">"Server Offset Time" must be a number.</FONT></B><P>);
		&gm_configuration;
	}
}

if ($IN{'editeduploadfilesizelimit'} eq "") { $IN{'editeduploadfilesizelimit'} = 0; }

if ($IN{'editeduploadfilesizelimit'} =~ /\D/) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">"Maximum Filesize Allowed" must be a number.</FONT></B><P>);
	&gm_configuration;
}

if (($IN{'editednotifyemail'} ne "") && ($IN{'editedmailprog'} eq "")) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must give your server's e-mail program location<BR>if you're going to have e-mail notification enabled.</FONT></B><P>);
	&gm_configuration;
}

if (($IN{'editednotifyemail'} eq "") && ($IN{'editednotifyforstatus'} ne "neither")) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must give an e-mail address to receive e-mail notifications.</FONT></B><P>);
	&gm_configuration;
}

if ($IN{'editedentrylistcountnumber'} =~ /\D/) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">"Log entry list variable number" must be a number.</FONT></B><P>);
	&gm_configuration;
}

$IN{'editeduploadfilesallowed'} =~ s/;/SEMICOLON/g;

if ($IN{'editeduploadfilesallowed'} =~ /\W/) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">"Allowed File Types" must only contain alphanumeric characters (besides semicolons).</FONT></B><P>);
	&gm_configuration;
}

$IN{'editeduploadfilesallowed'} =~ s/SEMICOLON/;/g;

if ($IN{'editedindexdays'} < 1) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">"Days to keep on main index" must be set to at least one!</FONT></B><P>);
	&gm_configuration;
}

if (substr($IN{'editedlogpath'}, -1) eq "/") { chop ($IN{'editedlogpath'}) };
if (substr($IN{'editedentriespath'}, -1) eq "/") { chop ($IN{'editedentriespath'}) };
if (substr($IN{'editedcgilocalpath'}, -1) eq "/") { chop ($IN{'editedcgilocalpath'}) };
if (substr($IN{'editedlogwebpath'}, -1) eq "/") { chop ($IN{'editedlogwebpath'}) };
if (substr($IN{'editedentrieswebpath'}, -1) eq "/") { chop ($IN{'editedentrieswebpath'}) };
if (substr($IN{'editedcgiwebpath'}, -1) eq "/") { chop ($IN{'editedcgiwebpath'}) };

open (FUNNYFEET, ">gm-config.cgi") || &gm_dangermouse("Can't write to the configuration file.  Please make sure that gm-config.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEET "$IN{'editedlogpath'}\n";
print FUNNYFEET "$IN{'editedentriespath'}\n";
print FUNNYFEET "$IN{'editedlogwebpath'}\n";
print FUNNYFEET "$IN{'editedentrieswebpath'}\n";
print FUNNYFEET "$IN{'editednotifyemail'}\n";
print FUNNYFEET "$IN{'editedindexfilename'}\n";
print FUNNYFEET "$IN{'editedentrysuffix'}\n";
print FUNNYFEET "$IN{'editedindexdays'}\n";
print FUNNYFEET "$IN{'editedoffsettime'}\n";
print FUNNYFEET "$IN{'editedtimezone'}\n";
print FUNNYFEET "$IN{'editedkeeplog'}\n";
print FUNNYFEET "$IN{'editedposttoarchives'}\n";
print FUNNYFEET "$IN{'editedallowkarmadefault'}\n";
print FUNNYFEET "$IN{'editedallowcommentsdefault'}\n";
print FUNNYFEET "$IN{'editedcommentsorder'}\n";
print FUNNYFEET "$IN{'editedgenerateentrypages'}\n";
print FUNNYFEET "$IN{'editedallowhtmlincomments'}\n";
print FUNNYFEET "$IN{'editedlogkarmaandcomments'}\n";
print FUNNYFEET "$IN{'editedmailprog'}\n";
print FUNNYFEET "$IN{'editednotifyforstatus'}\n";
print FUNNYFEET "$IN{'editedautolinkurls'}\n";
print FUNNYFEET "$IN{'editedstriplinesfromcomments'}\n";
print FUNNYFEET "$IN{'editedallowmultiplekarmavotes'}\n";
print FUNNYFEET "$gmversion\n";
print FUNNYFEET "$IN{'editedcgilocalpath'}\n";
print FUNNYFEET "$IN{'editedcgiwebpath'}\n";
print FUNNYFEET "$IN{'editedconcurrentmainandarchives'}\n";
print FUNNYFEET "$IN{'editedkeeparchivemasterindex'}\n";
print FUNNYFEET "$IN{'editedentrylistsortorder'}\n";
print FUNNYFEET "$IN{'editedallowkarmaorcomments'}\n";
print FUNNYFEET "$IN{'editedentrylistcountnumber'}\n";
print FUNNYFEET "$IN{'editedcookiesallowed'}\n";
print FUNNYFEET "$IN{'editedlogarchivesuffix'}\n";
print FUNNYFEET "$IN{'editedcensorlist'}\n";
print FUNNYFEET "$IN{'editedcensorenabled'}\n";
print FUNNYFEET "$IN{'editedkeepmonthlyarchives'}\n";
print FUNNYFEET "$IN{'editeddefaultentrylistview'}\n";
print FUNNYFEET "$IN{'editedlinktocalendarentries'}\n";
print FUNNYFEET "$IN{'editedautomaticrebuilddefault'}\n";
print FUNNYFEET "$IN{'editedcommententrylistonlyifokay'}\n";
print FUNNYFEET "$IN{'editedotherfilelist'}\n";
print FUNNYFEET "$IN{'editedotherfilelistentryrebuild'}\n";
print FUNNYFEET "$IN{'editedarchiveformat'}\n";
print FUNNYFEET "$IN{'editedinlineformatting'}\n";
print FUNNYFEET "$IN{'editeduploadfilesallowed'}\n";
print FUNNYFEET "$IN{'editeduploadfilesizelimit'}\n";
close (FUNNYFEET);

if (($keeplog eq "no") && ($IN{'editedkeeplog'} eq "yes")) {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$authorIP]</FONT> $IN{'authorname'} let this log get its groove back\n<FONT SIZE=1>[$basedate] [$authorIP]</FONT> $IN{'authorname'} edited the config file\n";
	close (FUNNYFEET);
}

if ($IN{'editedkeeplog'} eq "no") {
	&gm_writetocplog("$IN{'authorname'} edited the config file\n<FONT SIZE=1>[$basedate] [$authorIP]</FONT> $IN{'authorname'} decided to stop this log from getting down with its bad-ass self");
} else {
	&gm_writetocplog("$IN{'authorname'} edited the config file");
}

$statusnote = qq(<B><FONT COLOR="#0000FF">The config file has been updated.  Be sure to rebuild your files<BR>for the changes to take effect on your site, if appropriate.</FONT></B><P>);

if ($IN{'editeddeletecookies'} eq "yes") {
	$statusnote .= "\n<SCRIPT TYPE=\"text/javascript\" LANGUAGE=\"JavaScript\">\n<!--//\ndeleteCookie(\"gmcookiename\");\ndeleteCookie(\"gmcookiepw\");\n//-->\n</SCRIPT>";
}

&gm_frontpage;

}

# -------------------
# edit banned ip list
# -------------------

sub gm_editbanlist {

&gm_validate;

if ($gmconfigurationaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit the ban list without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit the ban list.</FONT></B><P>);
	&gm_frontpage;
}

if ($statusnote eq "") { $statusnote = qq(<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=460><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B><FONT COLOR="#000000">Edit Banned IP List</FONT></B><BR><FONT SIZE=1>Anyone matching an IP address that you have listed here will be unable to vote or post comments on your site; you can optionally add names to them to help you remember who you've banned.  You can also ban partial IPs (for example, banning 12.34.56 would ban someone at 12.34.56.78 as well as 12.34.56.89).</FONT></TD></TR></TABLE><P>); }

print<<GMBANLISTMENUTOP;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<SELECT CLASS="selectlist" NAME="editedbanlist" SIZE=10>

GMBANLISTMENUTOP

open (FUNNYFEET, "gm-banlist.cgi") || &gm_dangermouse("Can't read the banlist file.  Please make sure that gm-banlist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmbanlist = <FUNNYFEET>;
close (FUNNYFEET);

foreach $gmbanlistline (@gmbanlist) {
	chomp ($gmbanlistline);
	$gmbanlistline =~ s/</\&lt;/g;
	$gmbanlistline =~ s/>/\&gt;/g;
	$gmbanlistline =~ s/"/\&quot;/g;
	($gmbannedip, $gmbannediphost, $gmbannedperson) = split (/\|/, $gmbanlistline);
	print qq(<OPTION VALUE="$gmbanlistline">$gmbannedip/$gmbannediphost);
	if ($gmbannedperson ne "") { print " ($gmbannedperson)"; }
	print "\n";
}

print<<GMBANLISTMENUBOTTOM;

</SELECT>
<P>
New IP to ban: <INPUT TYPE=TEXT CLASS="textinput" MAXLENGTH=15 NAME="editednewbannedip" SIZE=15>
<BR>
Banned person's name (optional): <INPUT TYPE=TEXT CLASS="textinput" NAME="editednewbannedperson" SIZE=15>
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Add New IP"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #FFD0D0" VALUE="Delete Selected IP">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>
"Why have those banish'd and forbidden legs dared once
<BR>
to touch a dust of England's ground?"&#151;Shakespeare
</FONT>
$gmframebottom

</BODY>
</HTML>

GMBANLISTMENUBOTTOM

$statusnote = "";

exit;

}

# -------------------------
# add an ip to the ban list
# -------------------------

sub gm_addbannedip {

&gm_validate;

if ($gmconfigurationaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to add an IP ($IN{'editednewbannedip'}) to the ban list without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to add an IP to the ban list.</FONT></B><P>);
	&gm_frontpage;
}

$IN{'editednewbannedip'} =~ s/\n//g;
$IN{'editednewbannedip'} =~ s/\|//g;
$IN{'editednewbannedperson'} =~ s/\n//g;
$IN{'editednewbannedperson'} =~ s/\|//g;

if ($IN{'editednewbannedip'} eq "") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must enter the IP you want to add to the ban list.</FONT></B><P>);
	&gm_editbanlist;
}

open (FUNNYFEET, "gm-banlist.cgi") || &gm_dangermouse("Can't read the banlist file.  Please make sure that gm-banlist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmbanlist = <FUNNYFEET>;
close (FUNNYFEET);

$gmcounter = 0;

foreach (@gmbanlist) {
	chomp ($gmbanlist[$gmcounter]);
	($checkthisip, $checkthisiphost, $checkthisperson) = split (/\|/, $gmbanlist[$gmcounter]);
	if ($checkthisip eq $IN{'editednewbannedip'}) {
		$statusnote = qq(<B><FONT COLOR="#FF0000">That IP is already in the ban list.</FONT></B><P>);
		&gm_editbanlist;
	}
	$gmcounter++;
}

$newbannediphost = $IN{'editednewbannedip'};

$gmbanlist[$gmcounter] = "$IN{'editednewbannedip'}|$newbannediphost|$IN{'editednewbannedperson'}";

@gmbanlistsorted = sort { $a <=> $b } @gmbanlist;

open (FUNNYFEET, ">gm-banlist.cgi") || &gm_dangermouse("Can't write to the banlist file.  Please make sure that gm-banlist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
foreach $gmnewbanlistline (@gmbanlistsorted) { print FUNNYFEET "$gmnewbanlistline\n"; }
close (FUNNYFEET);

if ($keeplog eq "yes") {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$authorIP]</FONT> $IN{'authorname'} added an IP ($IN{'editednewbannedip'}";
	if ($IN{'editednewbannedperson'} ne "") { print FUNNYFEET ", \"$IN{'editednewbannedperson'}\""; }
	print FUNNYFEET ") to the ban list\n";
	close (FUNNYFEET);
}

$statusnote = qq(<B><FONT COLOR="#0000FF">$IN{'editednewbannedip'} has been added to the ban list.</FONT></B><P>);
&gm_editbanlist;

}

# ------------------------------
# delete an ip from the ban list
# ------------------------------

sub gm_deletebannedip {

&gm_validate;

if ($gmconfigurationaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to delete an IP ($IN{'editedbanlist'}) to the ban list without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to delete an IP from the ban list.</FONT></B><P>);
	&gm_frontpage;
}

chomp($IN{'editedbanlist'});

if ($IN{'editedbanlist'} eq "") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must select the IP you want to delete from the ban list.</FONT></B><P>);
	&gm_editbanlist;
}

open (FUNNYFEET, "gm-banlist.cgi") || &gm_dangermouse("Can't read the banlist file.  Please make sure that gm-banlist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmbanlist = <FUNNYFEET>;
close (FUNNYFEET);

$deletedthisbannedip = "";
$deletedthisbannediphost = "";
$deletedthisbannedperson = "";

open (FUNNYFEET, ">gm-banlist.cgi") || &gm_dangermouse("Can't write to the banlist file.  Please make sure that gm-banlist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
foreach $gmbanlistline (@gmbanlist) {
	chomp($gmbanlistline);
	if ($gmbanlistline eq $IN{'editedbanlist'}) {
		($checkthisip, $checkthisiphost, $checkthisperson) = split (/\|/, $gmbanlistline);
		$deletedthisbannedip = $checkthisip;
		$deletedthisbannediphost = $checkthisiphost;
		$deletedthisbannedperson = $checkthisperson;
	}
	if ($gmbanlistline ne $IN{'editedbanlist'}) { print FUNNYFEET "$gmbanlistline\n"; }
}
close (FUNNYFEET);

if ($keeplog eq "yes") {
	&date;
	open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
	print FUNNYFEET "<FONT SIZE=1>[$basedate] [$authorIP]</FONT> $IN{'authorname'} deleted an IP ($deletedthisbannedip";
	if ($deletedthisbannedperson ne "") { print FUNNYFEET ", \"$deletedthisbannedperson\""; }
	print FUNNYFEET ") from the ban list\n";
	close (FUNNYFEET);
}

$statusnote = qq(<B><FONT COLOR="#0000FF">$deletedthisbannedip has been deleted from the ban list.</FONT></B><P>);
&gm_editbanlist;

}

# ---------------
# add a new entry
# ---------------

sub gm_addentry {

&gm_validate;

if ($gmentryaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to add an entry without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to add entries.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readcounter;

if ($newentrynumber eq "0") {
	open (FUNNYFEET, "gm-cplog.cgi") || &gm_dangermouse("Can't read the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
	@cploglines = <FUNNYFEET>;
	close (FUNNYFEET);
	$cplogtext = join (" ", @cploglines);
	unless ($cplogtext =~ /successfully performed diagnostics/) {
		$statusnote = qq(<B><FONT COLOR="#FF0000">Please run "Diagnostics & Repair" in the Configuration screen before posting your first entry.</FONT></B><P>);
		&gm_frontpage;
	}
}

if ($statusnote eq "") {
	$statusnote = qq(<B><FONT COLOR="#000000">Add A New Entry</FONT></B><BR><FONT SIZE=1>This is the form by which you add new entries to your weblog/journal.  You can make this either a standard or extended entry;<BR>standard entries contain only main text (the first box), while extended entries also have "more" text (the second box).<BR>Standard & extended entries can be handled and formatted in distinct ways via your templates.</FONT><P>);
}

if ($IN{'newentrysubject'} ne "") { $IN{'newentrysubject'} = &delouse($IN{'newentrysubject'}); }
if ($IN{'newentrymaintext'} ne "") { $IN{'newentrymaintext'} = &delouse($IN{'newentrymaintext'}); }
if ($IN{'newentrymoretext'} ne "") { $IN{'newentrymoretext'} = &delouse($IN{'newentrymoretext'}); }

print<<GMADDENTRYTOP;

$gmheadtagtwo

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0><TR><TD ALIGN=RIGHT>$gmfonttag<B>Subject:</B></FONT></TD><TD ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="newentrysubject" VALUE="$IN{'newentrysubject'}" SIZE=50 STYLE="width: 550">$gmfonttag</TD></TR></TABLE>
<P>
<B>Main Entry Text</B>
<BR>
</FONT><TEXTAREA NAME="newentrymaintext" COLS=86 ROWS=15 WRAP=VIRTUAL STYLE="width: 720">$IN{'newentrymaintext'}</TEXTAREA>$gmfonttag
<P>
<B>Extended ("More") Entry Text&#151;Optional</B>
<BR>
</FONT><TEXTAREA NAME="newentrymoretext" COLS=86 ROWS=15 WRAP=VIRTUAL STYLE="width: 720">$IN{'newentrymoretext'}</TEXTAREA>$gmfonttag
<P>
<SCRIPT TYPE="text/javascript" LANGUAGE="JavaScript">
<!--//
if ((parseInt(navigator.appVersion) >= 4) && (navigator.appName == "Microsoft Internet Explorer")) {
	document.write("<FONT SIZE=1>Shortcut keys: CTRL-SHIFT-A to add a link, CTRL-SHIFT-B to bold selected text,<BR>CTRL-SHIFT-I to italicise, CTRL-SHIFT-U to underline</FONT><P>");
}
//-->
</SCRIPT>
<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0 WIDTH=716 BGCOLOR="#FFFFD0"><TR><TD VALIGN=TOP ALIGN=CENTER>$gmfonttag<B>Entry Options</B><BR><FONT SIZE=1>If you wish to enable or disable karma voting and/or comment posting for this entry, you can specify it below (use Configuration to set whether those are on or off by default), unless you've disabled karma or comments altogether.  You can also specify whether to keep an entry permanently at the top of your main log (you can edit the entry later to turn that off).</FONT></FONT></TD></TR></TABLE></TD></TR></TABLE>
<P>

GMADDENTRYTOP

if (($allowkarmaorcomments eq "karma") || ($allowkarmaorcomments eq "both")) {
	print qq(Allow karma voting on this entry: );
	if ($allowkarmadefault eq "yes") {
		print qq(<INPUT TYPE=RADIO NAME="newentryallowkarma" VALUE="yes" CHECKED> Yes <INPUT TYPE=RADIO NAME="newentryallowkarma" VALUE="no"> No\n);
	} else {
		print qq(<INPUT TYPE=RADIO NAME="newentryallowkarma" VALUE="yes"> Yes <INPUT TYPE=RADIO NAME="newentryallowkarma" VALUE="no" CHECKED> No\n);
	}
} else {
	print qq(<INPUT TYPE=HIDDEN NAME="newentryallowkarma" VALUE="no">\n);
}

if ($allowkarmaorcomments eq "both") { print "<BR>\n"; }

if (($allowkarmaorcomments eq "comments") || ($allowkarmaorcomments eq "both")) {
	print qq(Allow comments to be posted to this entry: );
	if ($allowcommentsdefault eq "yes") {
		print qq(<INPUT TYPE=RADIO NAME="newentryallowcomments" VALUE="yes" CHECKED> Yes <INPUT TYPE=RADIO NAME="newentryallowcomments" VALUE="no"> No\n);
	} else {
		print qq(<INPUT TYPE=RADIO NAME="newentryallowcomments" VALUE="yes"> Yes <INPUT TYPE=RADIO NAME="newentryallowcomments" VALUE="no" CHECKED> No\n);
	}
} else {
	print qq(<INPUT TYPE=HIDDEN NAME="newentryallowcomments" VALUE="no">\n);
}

print<<GMADDENTRYBOTTOM;

<BR>
Keep this entry at the top of the main log: <INPUT TYPE=RADIO NAME="newentrystayattop" VALUE="yes"> Yes <INPUT TYPE=RADIO NAME="newentrystayattop" VALUE="no" CHECKED> No
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Preview Before Posting"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Add This Entry">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>"You must have chaos in your soul to give birth to a dancing star."&#151;Friedrich Nietzsche</FONT>
$gmframebottom

</BODY>
</HTML>

GMADDENTRYBOTTOM

exit;

}

# -------------------------------
# add a new entry - popup version
# -------------------------------

sub gm_addentrypopup {

&gm_validate;

if (($gmentryaccess ne "yes") || ($gmbookmarkletaccess ne "yes")) {
	&gm_writetocplog("$IN{'authorname'} attempted to add an entry via popup without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to add entries via the popup window.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readcounter;

if ($newentrynumber eq "0") {
	open (FUNNYFEET, "gm-cplog.cgi") || &gm_dangermouse("Can't read the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
	@cploglines = <FUNNYFEET>;
	close (FUNNYFEET);
	$cplogtext = join (" ", @cploglines);
	unless ($cplogtext =~ /successfully performed diagnostics/) {
		$statusnote = qq(<B><FONT COLOR="#FF0000">Please run "Diagnostics & Repair" in the Configuration screen before posting your first entry.</FONT></B><P>);
		&gm_frontpage;
	}
}

if ($statusnote eq "") {
	$statusnote = qq(<B><FONT COLOR="#000000">Greymatter Pop-Up Posting Window</FONT></B><P>);
}

$popupincludetext = qq(<A HREF="$IN{'loglink'}">$IN{'loglinktitle'}</A>);

if ($IN{'logtext'} ne "") { $popupincludetext .= "\n\n$IN{'logtext'}"; }

if ($IN{'newentrysubject'} ne "") { $IN{'newentrysubject'} = &delouse($IN{'newentrysubject'}); }
if ($IN{'newentrymaintext'} ne "") {
	$IN{'newentrymaintext'} = &delouse($IN{'newentrymaintext'});
} else {
	$IN{'newentrymaintext'} = $popupincludetext;
}
if ($IN{'newentrymoretext'} ne "") { $IN{'newentrymoretext'} = &delouse($IN{'newentrymoretext'}); }

print<<GMADDENTRYPOPUPTOP;

$gmheadtagtwo
$gmframetoptwo
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="gmbmspecial" VALUE="popupblog">
<TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0><TR><TD ALIGN=RIGHT>$gmfonttag<B>Subject:</B></FONT></TD><TD ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="newentrysubject" VALUE="$IN{'newentrysubject'}" SIZE=25 STYLE="width: 450">$gmfonttag</TD></TR></TABLE>
<P>
<B>Main Entry Text</B>
<BR>
</FONT><TEXTAREA NAME="newentrymaintext" COLS=50 ROWS=12 WRAP=VIRTUAL STYLE="width: 590">$IN{'newentrymaintext'}</TEXTAREA>$gmfonttag
<P>
<B>Extended ("More") Entry Text&#151;Optional</B>
<BR>
</FONT><TEXTAREA NAME="newentrymoretext" COLS=50 ROWS=12 WRAP=VIRTUAL STYLE="width: 590">$IN{'newentrymoretext'}</TEXTAREA>$gmfonttag
<P>
<SCRIPT TYPE="text/javascript" LANGUAGE="JavaScript">
<!--//
if ((parseInt(navigator.appVersion) >= 4) && (navigator.appName == "Microsoft Internet Explorer")) {
	document.write("<FONT SIZE=1>Shortcut keys: CTRL-SHIFT-A to add a link, CTRL-SHIFT-B to bold selected text,<BR>CTRL-SHIFT-I to italicise, CTRL-SHIFT-U to underline</FONT><P>");
}
//-->
</SCRIPT>
<P>

GMADDENTRYPOPUPTOP

if (($allowkarmaorcomments eq "karma") || ($allowkarmaorcomments eq "both")) {
	print qq(Allow karma voting on this entry: );
	if ($allowkarmadefault eq "yes") {
		print qq(<INPUT TYPE=RADIO NAME="newentryallowkarma" VALUE="yes" CHECKED> Yes <INPUT TYPE=RADIO NAME="newentryallowkarma" VALUE="no"> No\n);
	} else {
		print qq(<INPUT TYPE=RADIO NAME="newentryallowkarma" VALUE="yes"> Yes <INPUT TYPE=RADIO NAME="newentryallowkarma" VALUE="no" CHECKED> No\n);
	}
} else {
	print qq(<INPUT TYPE=HIDDEN NAME="newentryallowkarma" VALUE="no">\n);
}

if ($allowkarmaorcomments eq "both") { print "<BR>\n"; }

if (($allowkarmaorcomments eq "comments") || ($allowkarmaorcomments eq "both")) {
	print qq(Allow comments to be posted to this entry: );
	if ($allowcommentsdefault eq "yes") {
		print qq(<INPUT TYPE=RADIO NAME="newentryallowcomments" VALUE="yes" CHECKED> Yes <INPUT TYPE=RADIO NAME="newentryallowcomments" VALUE="no"> No\n);
	} else {
		print qq(<INPUT TYPE=RADIO NAME="newentryallowcomments" VALUE="yes"> Yes <INPUT TYPE=RADIO NAME="newentryallowcomments" VALUE="no" CHECKED> No\n);
	}
} else {
	print qq(<INPUT TYPE=HIDDEN NAME="newentryallowcomments" VALUE="no">\n);
}

print<<GMADDENTRYPOPUPBOTTOM;

<BR>
Keep this entry at the top of the main log: <INPUT TYPE=RADIO NAME="newentrystayattop" VALUE="yes"> Yes <INPUT TYPE=RADIO NAME="newentrystayattop" VALUE="no" CHECKED> No
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Preview Before Posting"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Add This Entry">
</FORM>
$gmframebottomtwo

</BODY>
</HTML>

GMADDENTRYPOPUPBOTTOM

exit;

}

# ----------------------------
# preview entry before posting
# ----------------------------

sub gm_previewentry {

&gm_validate;

if ($gmentryaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to add an entry without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to add entries.</FONT></B><P>);
	&gm_frontpage;
}

$newentrysubject = &relouse($IN{'newentrysubject'});
$newentrymaintext = &relouse($IN{'newentrymaintext'});
$newentrymoretext = &relouse($IN{'newentrymoretext'});

$newentrysubjectdeloused = &delouse($newentrysubject);
$newentrymaintextdeloused = &delouse($newentrymaintext);
$newentrymoretextdeloused = &delouse($newentrymoretext);
$newentrysubjectdeloused =~ s/\n/\|\*\|/g;
$newentrymaintextdeloused =~ s/\n/\|\*\|/g;
$newentrymoretextdeloused =~ s/\n/\|\*\|/g;

$newentrymaintext =~ s/\|\*\|/<BR>/g;
$newentrymoretext =~ s/\|\*\|/<BR>/g;
$newentrymaintext =~ s/\n/<BR>/g;
$newentrymoretext =~ s/\n/<BR>/g;
$newentrymaintext =~ s/<BR><BR>/<\/P><P ALIGN=JUSTIFY>/g;
$newentrymoretext =~ s/<BR><BR>/<\/P><P ALIGN=JUSTIFY>/g;

&gm_readcounter;

unless ($newentrynumber < 1) {
	&gm_getentryvariables($newentrynumber);
	&gm_formatentry($newentrymaintext);
	$newentrymaintext = $entryreturn;
	unless ($newentrymoretext eq "") {
		&gm_formatentry($newentrymoretext);
		$newentrymoretext = $entryreturn;
	}
}

$showmoretext = "";
if ($newentrymoretext ne "") { $showmoretext = "</P><P ALIGN=CENTER><CENTER>\n<B>[extended text]</B>\n</CENTER></P><P ALIGN=JUSTIFY>\n$newentrymoretext\n"; }

if ($statusnote eq "") {
	if ($newentrysubject ne "") {
		$statusnote = qq(<B><FONT COLOR="#000000">Previewing "$newentrysubject"</FONT></B><BR><FONT SIZE=1>Click "Add This Entry" below to add this entry to your site, or click "Re-Edit This Entry" to re-edit it.</FONT><P>);
	} else {
		$statusnote = qq(<B><FONT COLOR="#000000">Previewing New Entry</FONT></B><BR><FONT SIZE=1>Click "Add This Entry" below to add this entry to your site, or click "Re-Edit This Entry" to re-edit it.</FONT><P>);
	}
}

print<<GMPREVIEWENTRY;

$gmheadtag

$gmframetop
$statusnote
<P ALIGN=JUSTIFY>
$newentrymaintext
$showmoretext
</P><P ALIGN=CENTER><CENTER>
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="newentrysubject" VALUE="$newentrysubjectdeloused">
<INPUT TYPE=HIDDEN NAME="newentrymaintext" VALUE="$newentrymaintextdeloused">
<INPUT TYPE=HIDDEN NAME="newentrymoretext" VALUE="$newentrymoretextdeloused">
<INPUT TYPE=HIDDEN NAME="newentryallowkarma" VALUE="$IN{'newentryallowkarma'}">
<INPUT TYPE=HIDDEN NAME="newentryallowcomments" VALUE="$IN{'newentryallowcomments'}">
<INPUT TYPE=HIDDEN NAME="newentrystayattop" VALUE="$IN{'newentrystayattop'}">
<INPUT TYPE=HIDDEN NAME="gmbmspecial" VALUE="$IN{'gmbmspecial'}">
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Re-Edit This Entry"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Add This Entry">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<FONT SIZE=1>"The future is not something we enter. The future is something we create."&#151;Leonard Sweet</FONT>
</CENTER></P>
$gmframebottom

</BODY>
</HTML>

GMPREVIEWENTRY

exit;

}

# ------------------
# save the new entry
# ------------------

sub gm_savenewentry {

&gm_validate;

if ($gmentryaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to add an entry without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to add entries.</FONT></B><P>);
	&gm_frontpage;
}

$IN{'newentrysubject'} = &configdelouse($IN{'newentrysubject'});
$IN{'newentrysubject'} = &relouse($IN{'newentrysubject'});
$IN{'newentrymaintext'} = &relouse($IN{'newentrymaintext'});
$IN{'newentrymoretext'} = &relouse($IN{'newentrymoretext'});

if ($IN{'newentrymaintext'} eq "") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You left the main text field blank.  Please try again.</FONT></B><P>);
	if ($IN{'gmbmspecial'} eq "popupblog") { &gm_addentrypopup; } else { &gm_addentry; }
}

&gm_readcounter;

$newentrynumber++;

$newentrynumberpadded = sprintf ("%8d", $newentrynumber);
$newentrynumberpadded =~ tr/ /0/;

&gm_readconfig;
&date;

$basedate = "$montwo\/$mdaytwo\/$shortyear $hourtwo\:$mintwo $AMPM";

open (FUNNYFEET, ">$EntriesPath/$newentrynumberpadded.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$newentrynumberpadded.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEET "$newentrynumber|$IN{'authorname'}|$IN{'newentrysubject'}|$wday|$mon|$mday|$JSYear|$hour|$min|$sec|$AMPM|0|0|0|$IN{'newentryallowkarma'}|$IN{'newentryallowcomments'}|open\n";
print FUNNYFEET "0.0.0.0|I\n";
print FUNNYFEET "$IN{'newentrymaintext'}\n";
print FUNNYFEET "$IN{'newentrymoretext'}\n";
close (FUNNYFEET);

chmod (0666, "$EntriesPath/$newentrynumberpadded.cgi");

open (FUNNYFEET, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entrylist file.  Please make sure that gm-entrylist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@originalentrylist = <FUNNYFEET>;
close (FUNNYFEET);

$newentrytempmorestatus = "N";
if ($IN{'newentrymoretext'} ne "") { $newentrytempmorestatus = "Y"; }

open (FUNNYFEET, ">gm-entrylist.cgi") || &gm_dangermouse("Can't write to the entrylist file.  Please make sure that gm-entrylist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEET "$newentrynumber|$IN{'authorname'}|$IN{'newentrysubject'}|$montwo\/$mdaytwo\/$shortyear|$hourtwo\:$mintwo $AMPM|O|$newentrytempmorestatus\n";
foreach $originalentrylistline (@originalentrylist) {
	chomp ($originalentrylistline);
	print FUNNYFEET "$originalentrylistline\n";
}
close (FUNNYFEET);

if ($IN{'newentrystayattop'} eq "yes") { $newstayattopnumber = $newentrynumber; }

$newalltimeopenentriesnumber++;

&gm_writecounter;

if ($generateentrypages eq "yes") {

	&gm_readconfig;
	&gm_getentryvariables($newentrynumber);

	if ($thisentryopenstatus eq "open") {
		if ($thisentrymorebody ne "") {
			&gm_formatentry($gmmoreentrypagetemplate);
		} else {
			&gm_formatentry($gmentrypagetemplate);
		}
		open (THISFILE, ">$EntriesPath/$thisentrynumberpadded.$entrysuffix") || &gm_dangermouse("Can't write file to $EntriesPath/$thisentrynumberpadded.$entrysuffix - please run Diagnostics & Repair in the Configuration screen.");
		print THISFILE $entryreturn;
		close (THISFILE);
		chmod (0666, "$EntriesPath/$newentrynumberpadded.$entrysuffix");
	} else {
		unlink ("$EntriesPath/$thisentrynumberpadded.$entrysuffix");
	}

	if ($newentrynumber ne "1") {
		$updatepreviousnumber = $newentrynumber - 1;
		&gm_getentryvariables($updatepreviousnumber);
		if ($thisentryopenstatus eq "open") {
			if ($updatepreviousnumber <= $newarchivenumber) {
				if ($thisentrymorebody ne "") {
					&gm_formatentry($gmmorearchiveentrypagetemplate);
				} else {
					&gm_formatentry($gmarchiveentrypagetemplate);
				}
			} else {
				if ($thisentrymorebody ne "") {
					&gm_formatentry($gmmoreentrypagetemplate);
				} else {
					&gm_formatentry($gmentrypagetemplate);
				}
			}
			open (THISFILE, ">$EntriesPath/$thisentrynumberpadded.$entrysuffix") || &gm_dangermouse("Can't write file to $EntriesPath/$thisentrynumberpadded.$entrysuffix - please run Diagnostics & Repair in the Configuration screen.");
			print THISFILE $entryreturn;
			close (THISFILE);
			chmod (0666, "$EntriesPath/$newentrynumberpadded.$entrysuffix");
		} else {
			unlink ("$EntriesPath/$thisentrynumberpadded.$entrysuffix");
		}
	}

}

&gm_generatemainindex;

&gm_readcounter;

if (($newarchivenumber ne "0") || ($concurrentmainandarchives eq "yes")) {

	if (($generateentrypages eq "yes") && ($newarchivenumber ne "0")) {
		&gm_getentryvariables($newarchivenumber);
		$originaldaymarker = "$thisentryday $thisentrymonth";
		$currentdaymarker = $originaldaymarker;
		$markercount = $newarchivenumber;
		do {
			if ($thisentryopenstatus eq "open") {
				if ($thisentrymorebody ne "") {
					&gm_formatentry($gmmorearchiveentrypagetemplate);
				} else {
					&gm_formatentry($gmarchiveentrypagetemplate);
				}
				open (THISFILE, ">$EntriesPath/$thisentrynumberpadded.$entrysuffix") || &gm_dangermouse("Can't write file to $EntriesPath/$thisentrynumberpadded.$entrysuffix - please run Diagnostics & Repair in the Configuration screen.");
				print THISFILE $entryreturn;
				close (THISFILE);
				chmod (0666, "$EntriesPath/$newentrynumberpadded.$entrysuffix");
			} else {
				unlink ("$EntriesPath/$thisentrynumberpadded.$entrysuffix");
			}
			$markercount--;
			if ($markercount eq "0") {
				$currentdaymarker = "finis";
			} else {
				&gm_getentryvariables($markercount);
				$currentdaymarker = "$thisentryday $thisentrymonth";
			}
		} until $currentdaymarker ne $originaldaymarker;
	}

	if ($concurrentmainandarchives eq "yes") { $newarchivenumber = $newentrynumber; }
	unless ($keepmonthlyarchives eq "no") { &gm_generatearchive($newarchivenumber); }
	&gm_readcounter;

}

if ($keeparchivemasterindex eq "yes") {
	if ($newarchivenumber ne "0") {
		&gm_getentryvariables($newarchivenumber);
	} else {
		&gm_getentryvariables($newentrynumber);
	}
	&gm_formatentry($gmarchivemasterindextemplate);
	open (THISFILE, ">$EntriesPath/$indexfilename") || &gm_dangermouse("Can't write to $EntriesPath/$indexfilename.  Please make sure your paths are configured correctly, that the entries/archives directory is CHMODed to 777, and that $EntriesPath/$indexfilename is CHMODed to 666; also try running Diagnostics & Repair from the Configuration screen.");
	print THISFILE $entryreturn;
	close (THISFILE);
	chmod (0666, "$EntriesPath/$indexfilename");
}

open (FUNNYFEET, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmauthordata = <FUNNYFEET>;
close (FUNNYFEET);

open (FUNNYFEET, ">gm-authors.cgi") || &gm_dangermouse("Can't write to the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
foreach $gmauthordataline (@gmauthordata) {
	chomp ($gmauthordataline);
	($checkthisname, $checkthispassword, $checkthisemail, $checkthishomepage, $checkthisoriginaldate, $checkthisentrycount, $checkthisentryaccess, $checkthisentryeditaccess, $checkthisconfigureaccess, $checkthistemplateaccess, $checkthisauthoraccess, $checkthisrebuildaccess, $checkthiscplogaccess, $checkthisbookmarkletaccess, $checkthisuploadaccess, $checkthisloginaccess) = split (/\|/, $gmauthordataline);
	if ($checkthisname eq $IN{'authorname'}) { $checkthisentrycount++; }
	print FUNNYFEET "$checkthisname|$checkthispassword|$checkthisemail|$checkthishomepage|$checkthisoriginaldate|$checkthisentrycount|$checkthisentryaccess|$checkthisentryeditaccess|$checkthisconfigureaccess|$checkthistemplateaccess|$checkthisauthoraccess|$checkthisrebuildaccess|$checkthiscplogaccess|$checkthisbookmarkletaccess|$checkthisuploadaccess|$checkthisloginaccess\n";
}
close (FUNNYFEET);

$recordentrysubject = $IN{'newentrysubject'};
if ($recordentrysubject eq "") { $recordentrysubject = "[no subject]"; }

if ($IN{'gmbmspecial'} eq "popupblog") {
	&gm_writetocplog("$IN{'authorname'} added a new entry (#$newentrynumber\: $recordentrysubject) via popup");
} else {
	&gm_writetocplog("$IN{'authorname'} added a new entry (#$newentrynumber\: $recordentrysubject)");
}

if (($otherfilelist ne "") && ($otherfilelistentryrebuild eq "yes") && ($IN{'gmbmspecial'} ne "popupblog")) {
	$IN{'rebuilding'} = "connectedaftersave";
	$IN{'rebuildfrom'} = "connected";
	&gm_rebuildupdate;
}

if ($IN{'gmbmspecial'} eq "popupblog") {

$indexfilenamesmartcheck = "/$indexfilename";
$indexfilenameprefix = substr($indexfilename, 0, 6);
if ($indexfilenameprefix eq "index.") { $indexfilenamesmartcheck = "/"; }

print<<GMPOPUPNOTICE;

$gmheadtag

$gmframetoptwo<B><FONT COLOR="#0000FF">Your new entry has been added to <A HREF="$LogWebPath$indexfilenamesmartcheck" TARGET="NEW"><FONT COLOR="#0000FF">your site</FONT></A>.</FONT></B><P><A HREF="javascript:window.close();">Click here to close this window.</A>$gmframebottomtwo

</BODY>
</HTML>

GMPOPUPNOTICE

exit;

}

$statusnote = qq(<B><FONT COLOR="#0000FF">Your new entry has been added.</FONT></B><P>);
&gm_frontpage;

}

# ------------------
# rebuild files menu
# ------------------

sub gm_rebuildfilesmenu {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild the files without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild the files.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readcounter;

if ($newentrynumber eq "0") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">There are no entries yet!</FONT></B><P>);
	&gm_frontpage;
}

if ($statusnote eq "") { $statusnote = qq(<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=380><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag<B><FONT COLOR="#000000">Rebuild Files</FONT></B><BR><FONT SIZE=1>If you've made any changes that will have a visible impact on your site (such as changing the templates, closing/reopening an entry, etc), you may want to rebuild the relevant files so that the changes will be immediately visible&#151;note that whenever you add a new entry, Greymatter automatically updates the relevant files.</FONT></TD></TR></TABLE><P>); }

$rebuildconnectedfilesbutton = "";

if ($otherfilelist ne "") {
	$rebuildconnectedfilesbutton = qq(<P>\n<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Rebuild Connected Files" STYLE="width: 320">);
}

print<<GMREBUILDMENU;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Rebuild Last Entry Page Only" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Rebuild Main Index File" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Rebuild Main Entry Pages" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Rebuild Archive Master Index" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Rebuild Archive Log Indexes" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Rebuild Archive Entry Pages" STYLE="width: 320">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Rebuild All Entry Pages" STYLE="width: 320">
$rebuildconnectedfilesbutton
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Rebuild Everything" STYLE="width: 320">
<P>
<FONT SIZE=1>
After clicking, expect a wait of up to several minutes, depending<BR>on how much is being rebuilt.  <B>DO NOT INTERRUPT GREYMATTER</B><BR>while it's rebuilding, or you could damage your files.
</FONT>
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>
"The most merciful thing in the world is the inability of the
<BR>
human mind to correlate all its contents."&#151;H.P. Lovecraft
</FONT>
$gmframebottom

</BODY>
</HTML>

GMREBUILDMENU

$statusnote = "";

exit;

}

# ---------------------------
# rebuild the main index file
# ---------------------------

sub gm_rebuildmainindexfile {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild the main index file without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild the main index file.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readcounter;

if ($newentrynumber eq "0") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">There are no entries yet.</FONT></B><P>);
	&gm_frontpage;
}

&gm_generatemainindex;

&gm_writetocplog("$IN{'authorname'} rebuilt the main index file");

if ($IN{'autorebuild'} eq "index") {
	$statusnote = qq(<B><FONT COLOR="#0000FF">The $IN{'modifiedtemplategroup'} templates have been<BR>modified and the main index file has been rebuilt.</FONT></B><P>);
	&gm_edittemplates;
} else {
	$statusnote = qq(<B><FONT COLOR="#0000FF">The main index file has been rebuilt.</FONT></B><P>);
	&gm_frontpage;
}

}

# ----------------------------
# rebuild last entry page only
# ----------------------------

sub gm_rebuildlastentrypageonly {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild the last entry page without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild the last entry page.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readconfig;

if ($generateentrypages ne "yes") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">Entry page generation is currently disabled.</FONT></B><P>);
	&gm_rebuildfilesmenu;
}

&gm_readcounter;
&gm_readtemplates;

if ($newentrynumber eq "0") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">There are no entries yet.</FONT></B><P>);
	&gm_frontpage;
}

&gm_getentryvariables($newentrynumber);

if ($thisentryopenstatus eq "open") {
	if ($thisentrymorebody ne "") {
		&gm_formatentry($gmmoreentrypagetemplate);
	} else {
		&gm_formatentry($gmentrypagetemplate);
	}
	open (THISFILE, ">$EntriesPath/$thisentrynumberpadded.$entrysuffix") || &gm_dangermouse("Can't write to $EntriesPath/$thisentrynumberpadded.$entrysuffix.  Please make sure that your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
	print THISFILE $entryreturn;
	close (THISFILE);
	chmod (0666, "$EntriesPath/$thisentrynumberpadded.$entrysuffix");
} else {
	unlink ("$EntriesPath/$thisentrynumberpadded.$entrysuffix");
}

&gm_writetocplog("$IN{'authorname'} rebuilt the last entry page");

$statusnote = qq(<B><FONT COLOR="#0000FF">The last entry page has been rebuilt.</FONT></B><P>);
&gm_frontpage;

}

# ------------------------
# rebuild main entry files
# ------------------------

sub gm_rebuildmainentrypages {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild the main entry pages without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild the main entry pages.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readconfig;

if ($generateentrypages ne "yes") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">Entry page generation is currently disabled.</FONT></B><P>);
	&gm_rebuildfilesmenu;
}

&gm_readcounter;
&gm_readtemplates;

if ($newentrynumber eq "0") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">There are no entries yet.</FONT></B><P>);
	&gm_frontpage;
}

$IN{'rebuilding'} = "mainentries";
$IN{'rebuildfrom'} = $newarchivenumber + 1;

&gm_rebuildupdate;

}

# ----------------------------
# rebuild archive master index
# ----------------------------

sub gm_rebuildarchivemasterindex {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild the archive master index without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild the archive master index.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readconfig;
&gm_readcounter;
&gm_readtemplates;

if ($keeparchivemasterindex eq "no") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">"Keep archive master index" is currently disabled.</FONT></B><P>);
	&gm_frontpage;
}

if ($newarchivenumber ne "0") {
	&gm_getentryvariables($newarchivenumber);
} else {
	&gm_getentryvariables($newentrynumber);
}

&gm_formatentry($gmarchivemasterindextemplate);

open (THISFILE, ">$EntriesPath/$indexfilename") || &gm_dangermouse("Can't write to $EntriesPath/$indexfilename.  Please make sure your paths are configured correctly, that the entries/archives directory is CHMODed to 777, and that $EntriesPath/$indexfilename is CHMODed to 666; also try running Diagnostics & Repair from the Configuration screen.");
print THISFILE $entryreturn;
close (THISFILE);

chmod (0666, "$EntriesPath/$indexfilename");

&gm_writetocplog("$IN{'authorname'} rebuilt the archive master index");

$statusnote = qq(<B><FONT COLOR="#0000FF">The archive master index has been rebuilt.</FONT></B><P>);
&gm_frontpage;

}

# ---------------------------
# rebuild archive log indexes
# ---------------------------

sub gm_rebuildarchivelogindexes {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild the archive log indexes without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild the archive log indexes.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readconfig;
&gm_readcounter;
&gm_readtemplates;

if (($IN{'autorebuild'} eq "archiveindexes") && ($keeparchivemasterindex ne "no")) {
	if ($newarchivenumber ne "0") {
		&gm_getentryvariables($newarchivenumber);
	} else {
		&gm_getentryvariables($newentrynumber);
	}
	&gm_formatentry($gmarchivemasterindextemplate); 
	open (THISFILE, ">$EntriesPath/$indexfilename") || &gm_dangermouse("Can't write to $EntriesPath/$indexfilename.  Please make sure your paths are configured correctly, that the entries/archives directory is CHMODed to 777, and that $EntriesPath/$indexfilename is CHMODed to 666; also try running Diagnostics & Repair from the Configuration screen.");
	print THISFILE $entryreturn;
	close (THISFILE);
}

if ($keepmonthlyarchives eq "no") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">Log archives are currently disabled.</FONT></B><P>);
	if ($IN{'autorebuild'} eq "archiveindexes") {
		$statusnote = qq(<B><FONT COLOR="#FF0000">The $IN{'modifiedtemplategroup'} templates have been modified.</FONT></B><P>);
	}
	&gm_frontpage;
}

if (($newarchivenumber eq "0") && ($concurrentmainandarchives ne "yes")) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">There are no archive log indexes yet.</FONT></B><P>);
	if ($IN{'autorebuild'} eq "archiveindexes") {
		$statusnote = qq(<B><FONT COLOR="#FF0000">The $IN{'modifiedtemplategroup'} templates have been modified.</FONT></B><P>);
	}
	&gm_frontpage;
}

unlink glob("$EntriesPath/archive-*.$entrysuffix");
unlink glob("$EntriesPath/archive-*.$logarchivesuffix");

if ($concurrentmainandarchives eq "yes") { $newarchivenumber = $newentrynumber; }

$stoppednumber = $newarchivenumber;
do { &gm_generatearchive($stoppednumber); } until $stoppednumber <= 1;

&gm_writetocplog("$IN{'authorname'} rebuilt the archive log indexes");

if ($IN{'autorebuild'} eq "archiveindexes") {
	$statusnote = qq(<B><FONT COLOR="#0000FF">The $IN{'modifiedtemplategroup'} templates have been<BR>modified and the archive indexes have been rebuilt.</FONT></B><P>);
	&gm_edittemplates;
} else {
	$statusnote = qq(<B><FONT COLOR="#0000FF">The archive log indexes have been rebuilt.</FONT></B><P>);
	&gm_frontpage;
}

}

# ---------------------------
# rebuild archive entry pages
# ---------------------------

sub gm_rebuildarchiveentrypages {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild the archive entry pages without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild the archive entry pages.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readconfig;
&gm_readcounter;
&gm_readtemplates;

if ($newarchivenumber eq "0") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">There are no archives yet.</FONT></B><P>);
	&gm_frontpage;
}

if ($generateentrypages eq "no") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">Entry page generation is currently disabled.</FONT></B><P>);
	&gm_rebuildfilesmenu;
}

$IN{'rebuilding'} = "archivefiles";
$IN{'rebuildfrom'} = "1";

&gm_rebuildupdate;

}

# -----------------------
# rebuild all entry pages
# -----------------------

sub gm_rebuildallentrypages {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild the entry pages without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild the entry pages.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readconfig;

if ($generateentrypages ne "yes") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">Entry page generation is currently disabled.</FONT></B><P>);
	&gm_rebuildfilesmenu;
}

&gm_readcounter;
&gm_readtemplates;

if ($newentrynumber eq "0") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">There are no entries yet.</FONT></B><P>);
	&gm_frontpage;
}

unlink glob("$EntriesPath/archive-*.$entrysuffix");

$IN{'rebuilding'} = "entryfiles";
$IN{'rebuildfrom'} = "1";

&gm_rebuildupdate;

}

# -------------------------------
# rebuild connected files - check
# -------------------------------

sub gm_rebuildconnectedfilescheck {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild the connected files without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild the connected files.</FONT></B><P>);
	&gm_frontpage;
}

if ($otherfilelist eq "") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">There are no connected files to rebuild.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readconfig;
&gm_readcounter;
&gm_readtemplates;

$IN{'rebuilding'} = "connected";
$IN{'rebuildfrom'} = "connected";

&gm_rebuildupdate;

}

# ------------------
# rebuild everything
# ------------------

sub gm_rebuildeverything {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild all the files without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild all the files.</FONT></B><P>);
	&gm_frontpage;
}

unlink glob("$EntriesPath/*.reg");
unlink glob("$EntriesPath/archive-*.$entrysuffix");
unlink glob("$EntriesPath/archive-*.$logarchivesuffix");

$IN{'rebuilding'} = "everything";
$IN{'rebuildfrom'} = "index";

&gm_rebuildupdate;

}

# ------------------------------
# edit an entry - selection menu
# ------------------------------

sub gm_editentryselection {

&gm_validate;

if ($gmentryeditaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit entries without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit entries.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readcounter;

if ($newentrynumber eq "0") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">There are no entries yet!</FONT></B><P>);
	&gm_frontpage;
}

if ($IN{'entryselectionview'} eq "") { $IN{'entryselectionview'} = $defaultentrylistview; }

$searchingfortext = "";

if ($IN{'entrysearch'} ne "") {
	$searchingfortext = qq(<P>\n<FONT COLOR="#0000FF"><B>All entries containing "$IN{'entrysearch'}"</B></FONT>\n<P>\n);
	$IN{'entryselectionview'} = "searchresults";
	$IN{'entrysearch'} = &relouse($IN{'entrysearch'});
}

if ($statusnote eq "") {
	$statusnote = qq(<B><FONT COLOR="#000000">Entry Selection</FONT></B><BR><FONT SIZE=1>Select an entry to edit or review.  "Closed" entries are considered deleted<BR>and are no longer visible on your site, but can be reopened at any time.</FONT><P>);
}

if ($gmentryeditaccess eq "mineonly") {
	$statusnote .= qq(<B>You only have access to edit your own entries.</B><P>);
}

open (FUNNYFEET, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entrylist file.  Please make sure that gm-entrylist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@gmentrylist = <FUNNYFEET>;
close (FUNNYFEET);

if ($IN{'sortby'} eq "subject") {
	@gmentrylist = sort {
		@a_fields = split /\|/, $a;
		@b_fields = split /\|/, $b;
		lc($a_fields[2]) cmp lc($b_fields[2]) || $b_fields[0] <=> $a_fields[0];
	} @gmentrylist;
}

if ($IN{'sortby'} eq "author") {
	@gmentrylist = sort {
		@a_fields = split /\|/, $a;
		@b_fields = split /\|/, $b;
		lc($a_fields[1]) cmp lc($b_fields[1]) || $b_fields[0] <=> $a_fields[0];
	} @gmentrylist;
}

print<<GMEDITENTRYSELECTIONMENUTOP;

$gmheadtag

$gmframetop
$statusnote
$searchingfortext
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="thomas" VALUE="Edit An Entry">
<SELECT CLASS="selectlist" NAME="entryselectionlist" SIZE=15>

GMEDITENTRYSELECTIONMENUTOP

$gmentrydatemarker = "nyet";
$liststayattopnotice = "";
$listclosedentrynotice = "";
$listmoreentrynotice = "";
$listsecondblank = "yes";

foreach $gmentrylistline (@gmentrylist) {
	chomp ($gmentrylistline);
	($listentrynumber, $listentryauthor, $listentrysubject, $listentrydate, $listentrytime, $listentryopenstatus, $listentrymorestatus) = split (/\|/, $gmentrylistline);

	if ($IN{'entryselectionview'} eq "searchresults") {
		$containsearch = "no";
		if ($listofaffectedentries ne "") {
			foreach $checkforthisentry (@affectedentrylist) {
				if ($checkforthisentry eq $listentrynumber) { $containsearch = "yes"; }
			}
		} else {
			&gm_getentryvariables($listentrynumber);
			if (($thisentryauthor =~ m/$IN{'entrysearch'}/i) || ($thisentrysubject =~ m/$IN{'entrysearch'}/i) || ($thisentrymainbody =~ m/$IN{'entrysearch'}/i) || ($thisentrymorebody =~ m/$IN{'entrysearch'}/i) || ($thisentrycomments =~ m/$IN{'entrysearch'}/i)) {
				$containsearch = "yes";
			}
		}
	}

	if ($listentrysubject eq "") { $listentrysubject = "(no subject)"; }

	if (($listentrynumber eq $newstayattopnumber) && ($listentryopenstatus eq "C") && ($listentrymorestatus eq "Y")) {
		unless (($listentryauthor ne $IN{'authorname'}) && ($IN{'entryselectionview'} eq "onlyyou")) {
		unless (($IN{'entryselectionview'} eq "searchresults") && ($containsearch eq "no")) {
			print qq(<OPTION VALUE="$listentrynumber">‡ † * [$listentrydate $listentrytime] $listentrynumber\: $listentrysubject \($listentryauthor\)\n);
			$liststayattopnotice = "‡ = Entry currently marked to stay at the top of the main index.";
			$listclosedentrynotice = "† = Closed entry.";
			$listmoreentrynotice = "* = Extended entry (contains \"more\" text).";
			$listsecondblank = "no";
		}
		}
	} elsif (($listentrynumber eq $newstayattopnumber) && ($listentryopenstatus eq "C")) {
		unless (($listentryauthor ne $IN{'authorname'}) && ($IN{'entryselectionview'} eq "onlyyou")) {
		unless (($IN{'entryselectionview'} eq "searchresults") && ($containsearch eq "no")) {
			print qq(<OPTION VALUE="$listentrynumber">‡ † [$listentrydate $listentrytime] $listentrynumber\: $listentrysubject \($listentryauthor\)\n);
			$liststayattopnotice = "‡ = Entry currently marked to stay at the top of the main index.";
			$listclosedentrynotice = "† = Closed entry.";
			$listsecondblank = "no";
		}
		}
	} elsif (($listentrynumber eq $newstayattopnumber) && ($listentrymorestatus eq "Y")) {
		unless (($listentryauthor ne $IN{'authorname'}) && ($IN{'entryselectionview'} eq "onlyyou")) {
		unless (($IN{'entryselectionview'} eq "searchresults") && ($containsearch eq "no")) {
			print qq(<OPTION VALUE="$listentrynumber">‡ * [$listentrydate $listentrytime] $listentrynumber\: $listentrysubject \($listentryauthor\)\n);
			$liststayattopnotice = "‡ = Entry currently marked to stay at the top of the main index.";
			$listmoreentrynotice = "* = Extended entry (contains \"more\" text).";
			$listsecondblank = "no";
		}
		}
	} elsif ($listentrynumber eq $newstayattopnumber) {
		unless (($listentryauthor ne $IN{'authorname'}) && ($IN{'entryselectionview'} eq "onlyyou")) {
		unless (($IN{'entryselectionview'} eq "searchresults") && ($containsearch eq "no")) {
			print qq(<OPTION VALUE="$listentrynumber">‡ [$listentrydate $listentrytime] $listentrynumber\: $listentrysubject \($listentryauthor\)\n);
			$liststayattopnotice = "‡ = Entry currently marked to stay at the top of the main index.";
			$listsecondblank = "no";
		}
		}
	} elsif (($listentrymorestatus eq "Y") && ($listentryopenstatus eq "C")) {
		unless (($listentryauthor ne $IN{'authorname'}) && ($IN{'entryselectionview'} eq "onlyyou")) {
		unless (($IN{'entryselectionview'} eq "searchresults") && ($containsearch eq "no")) {
			if (($IN{'entryselectionview'} eq "searchresults") || ($IN{'entryselectionview'} eq "onlyyou") || ($IN{'entryselectionview'} eq "more") || ($IN{'entryselectionview'} eq "closed") || ($IN{'entryselectionview'} eq "all") || ($IN{'entryselectionview'} eq "main")) {
				unless (($listentrynumber <= $newarchivenumber) && ($IN{'entryselectionview'} eq "main")) {
					print qq(<OPTION VALUE="$listentrynumber">† * [$listentrydate $listentrytime] $listentrynumber\: $listentrysubject \($listentryauthor\)\n);
					$listclosedentrynotice = "† = Closed entry.";
					$listmoreentrynotice = "* = Extended entry (contains \"more\" text).";
					$listsecondblank = "no";
				}
			}
		}
		}
	} elsif ($listentrymorestatus eq "Y") {
		unless (($listentryauthor ne $IN{'authorname'}) && ($IN{'entryselectionview'} eq "onlyyou")) {
		unless (($IN{'entryselectionview'} eq "searchresults") && ($containsearch eq "no")) {
			if (($IN{'entryselectionview'} eq "searchresults") || ($IN{'entryselectionview'} eq "onlyyou") || ($IN{'entryselectionview'} eq "more") || ($IN{'entryselectionview'} eq "open") || ($IN{'entryselectionview'} eq "all") || ($IN{'entryselectionview'} eq "main")) {
				unless (($listentrynumber <= $newarchivenumber) && ($IN{'entryselectionview'} eq "main")) {
					print qq(<OPTION VALUE="$listentrynumber">* [$listentrydate $listentrytime] $listentrynumber\: $listentrysubject \($listentryauthor\)\n);
					$listmoreentrynotice = "* = Extended entry (contains \"more\" text).";
					$listsecondblank = "no";
				}
			}
		}
		}
	} elsif ($listentryopenstatus eq "C") {
		unless (($listentryauthor ne $IN{'authorname'}) && ($IN{'entryselectionview'} eq "onlyyou")) {
		unless (($IN{'entryselectionview'} eq "searchresults") && ($containsearch eq "no")) {
			if (($IN{'entryselectionview'} eq "searchresults") || ($IN{'entryselectionview'} eq "onlyyou") || ($IN{'entryselectionview'} eq "closed") || ($IN{'entryselectionview'} eq "all") || ($IN{'entryselectionview'} eq "main")) {
				unless (($listentrynumber <= $newarchivenumber) && ($IN{'entryselectionview'} eq "main")) {
					print qq(<OPTION VALUE="$listentrynumber">† [$listentrydate $listentrytime] $listentrynumber\: $listentrysubject \($listentryauthor\)\n);
					$listclosedentrynotice = "† = Closed entry.";
					$listsecondblank = "no";
				}
			}
		}
		}
	} else {
		unless (($listentryauthor ne $IN{'authorname'}) && ($IN{'entryselectionview'} eq "onlyyou")) {
		unless (($IN{'entryselectionview'} eq "searchresults") && ($containsearch eq "no")) {
			if (($IN{'entryselectionview'} eq "searchresults") || ($IN{'entryselectionview'} eq "onlyyou") || ($IN{'entryselectionview'} eq "open") || ($IN{'entryselectionview'} eq "all") || ($IN{'entryselectionview'} eq "main")) {
				unless (($listentrynumber <= $newarchivenumber) && ($IN{'entryselectionview'} eq "main")) {
					print qq(<OPTION VALUE="$listentrynumber">[$listentrydate $listentrytime] $listentrynumber\: $listentrysubject \($listentryauthor\)\n);
					$listsecondblank = "no";
				}
			}
		}
		}
	}

}

print qq(</SELECT>\n<P>\n<INPUT TYPE=TEXT NAME="entrysearch" CLASS="textinput" SIZE=25 STYLE="width: 350"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Search" STYLE="width: 70; height: 22">\n<P>List: <SELECT NAME="entryselectionview" CLASS="selectlist">\n);

if ($IN{'entryselectionview'} eq "searchresults") {
	print qq(<OPTION VALUE="$defaultentrylistview" SELECTED> \(Search results\)\n);
}

if ($IN{'entryselectionview'} eq "main") {
	if ($indexdays eq "1") {
		print qq(<OPTION VALUE="main" SELECTED> Current entries \($indexdays day\)\n);
	} else {
		print qq(<OPTION VALUE="main" SELECTED> Current entries \($indexdays days\)\n);
	}
} else {
	if ($indexdays eq "1") {
		print qq(<OPTION VALUE="main"> Current entries \($indexdays day\)\n);
	} else {
		print qq(<OPTION VALUE="main"> Current entries \($indexdays days\)\n);
	}
}

if ($IN{'entryselectionview'} eq "onlyyou") {
	print qq(<OPTION VALUE="onlyyou" SELECTED> All entries by you\n);
} else {
	print qq(<OPTION VALUE="onlyyou"> All entries by you\n);
}

if ($IN{'entryselectionview'} eq "more") {
	print qq(<OPTION VALUE="more" SELECTED> All extended entries\n);
} else {
	print qq(<OPTION VALUE="more"> All extended entries\n);
}

if ($IN{'entryselectionview'} eq "open") {
	print qq(<OPTION VALUE="open" SELECTED> All open entries\n);
} else {
	print qq(<OPTION VALUE="open"> All open entries\n);
}

if ($IN{'entryselectionview'} eq "closed") {
	print qq(<OPTION VALUE="closed" SELECTED> All closed entries\n);
} else {
	print qq(<OPTION VALUE="closed"> All closed entries\n);
}

if ($IN{'entryselectionview'} eq "all") {
	print qq(<OPTION VALUE="all" SELECTED> All entries\n);
} else {
	print qq(<OPTION VALUE="all"> All entries\n);
}


$listnotice = "";

if (($liststayattopnotice ne "") && ($listmoreentrynotice ne "") && ($listclosedentrynotice ne "")) {
	$listnotice = "<FONT SIZE=1>$liststayattopnotice\n<BR>\n$listmoreentrynotice\n<BR>\n$listclosedentrynotice</FONT>\n<P>";
} elsif (($liststayattopnotice ne "") && ($listmoreentrynotice ne "")) {
	$listnotice = "<FONT SIZE=1>$liststayattopnotice\n<BR>\n$listmoreentrynotice</FONT>\n<P>";
} elsif (($liststayattopnotice ne "") && ($listclosedentrynotice ne "")) {
	$listnotice = "<FONT SIZE=1>$liststayattopnotice\n<BR>\n$listclosedentrynotice</FONT>\n<P>";
} elsif ($liststayattopnotice ne "") {
	$listnotice = "<FONT SIZE=1>$liststayattopnotice</FONT>\n<P>";
} elsif (($listmoreentrynotice ne "") && ($listclosedentrynotice ne "")) {
	$listnotice = "<FONT SIZE=1>$listmoreentrynotice\n<BR>\n$listclosedentrynotice</FONT>\n<P>";
} elsif ($listmoreentrynotice ne "") {
	$listnotice = "<FONT SIZE=1>$listmoreentrynotice</FONT>\n<P>";
} elsif ($listclosedentrynotice ne "") {
	$listnotice = "<FONT SIZE=1>$listclosedentrynotice</FONT>\n<P>";
}

print qq(</SELECT> &#160; <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Change View" STYLE="width: 100; height: 22">\n<P>Sort by: );

if ($IN{'sortby'} eq "subject") {
	print qq(<INPUT TYPE=RADIO NAME="sortby" VALUE="date"> Date &#160; <INPUT TYPE=RADIO NAME="sortby" VALUE="subject" CHECKED> Subject &#160; <INPUT TYPE=RADIO NAME="sortby" VALUE="author"> Author);
} elsif ($IN{'sortby'} eq "author") {
	print qq(<INPUT TYPE=RADIO NAME="sortby" VALUE="date"> Date &#160; <INPUT TYPE=RADIO NAME="sortby" VALUE="subject"> Subject &#160; <INPUT TYPE=RADIO NAME="sortby" VALUE="author" CHECKED> Author);
} else {
	print qq(<INPUT TYPE=RADIO NAME="sortby" VALUE="date" CHECKED> Date &#160; <INPUT TYPE=RADIO NAME="sortby" VALUE="subject"> Subject &#160; <INPUT TYPE=RADIO NAME="sortby" VALUE="author"> Author);
}

print<<GMEDITENTRYSELECTIONMENUBOTTOM;

<P>
$listnotice
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Edit Selected Entry"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #FFD0D0" VALUE="Open/Close Selected Entry">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0; width: 485" VALUE="Search And Replace Across All Entries">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>
"We must be the change we wish to see in the world."&#151;Gandhi
</FONT>
</CENTER>
$gmframebottom

</BODY>
</HTML>

GMEDITENTRYSELECTIONMENUBOTTOM

$statusnote = "";

exit;

}

# ------------------------------------
# editing entries - search and replace
# ------------------------------------

sub gm_editentrysearchandreplace {

&gm_validate;

if ($gmentryeditaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to perform a search-and-replace without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to perform a search-and-replace.</FONT></B><P>);
	&gm_frontpage;
}

if ($gmentryeditaccess eq "mineonly") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must have access to edit all entries to do this.</FONT></B><P>);
	&gm_editentryselection;
}

if ($statusnote eq "") {
	$statusnote = qq(<B><FONT COLOR="#000000">Search And Replace</FONT></B><BR><FONT SIZE=1>Enter whatever exact text or other information you wish to search across entries for in the<BR>first box, and whatever you wish to replace it with in the second box (leave the Replace<BR>box blank to delete all instances of your search term).  Keep in mind that a search-and-replace<BR>will make permanent changes to the contents of ALL entries that contain your search term.</FONT><P>);
}

print<<GMEDITENTRYSEARCHREPLACE;

$gmheadtag

$gmframetop
$statusnote
<CENTER>
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0><TR><TD VALIGN=MIDDLE ALIGN=RIGHT>$gmfonttag<B>Search For:</B></FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="srsearchterm" SIZE=40 STYLE="width: 400">$gmfonttag</TD></TR><TR><TD VALIGN=MIDDLE ALIGN=RIGHT>$gmfonttag<B>Replace With:</B></FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="srreplaceterm" SIZE=40 STYLE="width: 400">$gmfonttag</TD></TR></TABLE>
<P>
<INPUT TYPE=CHECKBOX NAME="srcaseinsensitive" VALUE="yes"> Make "Search For" term case-insensitive?
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0; width: 485" VALUE="Perform Search And Replace">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Entry Selection"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>
"Search others for their virtues, thyself for thy vices."&#151;Benjamin Franklin
</FONT>
</CENTER>
$gmframebottom

</BODY>
</HTML>

GMEDITENTRYSEARCHREPLACE

$statusnote = "";

exit;

}

# --------------------------
# perform search and replace
# --------------------------

sub gm_performsearchandreplace {

&gm_validate;

if ($gmentryeditaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to perform a search-and-replace without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to perform a search-and-replace.</FONT></B><P>);
	&gm_frontpage;
}

if ($gmentryeditaccess eq "mineonly") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must have access to edit all entries to do this.</FONT></B><P>);
	&gm_editentryselection;
}

&gm_readcounter;

$currententrycounter = $newentrynumber;
$entriesaffected = 0;
$listofaffectedentries = "";
$rebuildentrylist = "no";

do {

	$currententrycounterpadded = sprintf ("%8d", $currententrycounter);
	$currententrycounterpadded =~ tr/ /0/;

	open (FUNNYFEET, "$EntriesPath/$currententrycounterpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$currententrycounterpadded.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777, or try running Diagnostics & Repair in the Configuration screen.");
	@entrylines = <FUNNYFEET>;
	close (FUNNYFEET);

	$gmcounter = 0;
	$resaveentry = "no";

	chomp ($entrylines[0]);
	($thisentrynumber, $thisentryauthor, $thisentrysubject, $thisentryweekdaynumber, $thisentrymonth, $thisentryday, $thisentryyearyear, $thisentryhour, $thisentryminute, $thisentrysecond, $thisentryampm, $thisentrypositivekarma, $thisentrynegativekarma, $thisentrycommentsnumber, $thisentryallowkarma, $thisentryallowcomments, $thisentryopenstatus) = split (/\|/, $entrylines[0]);

	if ($IN{'srcaseinsensitive'} eq "yes") {
		if ($thisentrysubject =~ m/$IN{'srsearchterm'}/i) {
			$thisentrysubject =~ s/$IN{'srsearchterm'}/$IN{'srreplaceterm'}/ig;
			$entrylines[0] = "$thisentrynumber|$thisentryauthor|$thisentrysubject|$thisentryweekdaynumber|$thisentrymonth|$thisentryday|$thisentryyearyear|$thisentryhour|$thisentryminute|$thisentrysecond|$thisentryampm|$thisentrypositivekarma|$thisentrynegativekarma|$thisentrycommentsnumber|$thisentryallowkarma|$thisentryallowcomments|$thisentryopenstatus";
			$resaveentry = "yes";
			$rebuildentrylist = "yes";
		}
	} else {
		if ($thisentrysubject =~ m/$IN{'srsearchterm'}/) {
			$thisentrysubject =~ s/$IN{'srsearchterm'}/$IN{'srreplaceterm'}/g;
			$entrylines[0] = "$thisentrynumber|$thisentryauthor|$thisentrysubject|$thisentryweekdaynumber|$thisentrymonth|$thisentryday|$thisentryyearyear|$thisentryhour|$thisentryminute|$thisentrysecond|$thisentryampm|$thisentrypositivekarma|$thisentrynegativekarma|$thisentrycommentsnumber|$thisentryallowkarma|$thisentryallowcomments|$thisentryopenstatus";
			$resaveentry = "yes";
			$rebuildentrylist = "yes";
		}
	}

	foreach (@entrylines) {
		chomp ($entrylines[$gmcounter]);
		unless (($gmcounter eq "0") || ($gmcounter eq "1")) {
			if ($IN{'srcaseinsensitive'} eq "yes") {
				if ($entrylines[$gmcounter] =~ m/$IN{'srsearchterm'}/i) {
					$entrylines[$gmcounter] =~ s/$IN{'srsearchterm'}/$IN{'srreplaceterm'}/ig;
					$resaveentry = "yes";
				}
			} else {
				if ($entrylines[$gmcounter] =~ m/$IN{'srsearchterm'}/) {
					$entrylines[$gmcounter] =~ s/$IN{'srsearchterm'}/$IN{'srreplaceterm'}/g;
					$resaveentry = "yes";
				}
			}
		}
		$gmcounter++;
	}

	if ($resaveentry eq "yes") {
		open (FUNNYFEET, ">$EntriesPath/$currententrycounterpadded.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$currententrycounterpadded.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777, or try running Diagnostics & Repair in the Configuration screen.");
		foreach $thisistheline (@entrylines) {
			print FUNNYFEET "$thisistheline\n";
		}
		close (FUNNYFEET);
		$entriesaffected++;
		$listofaffectedentries .= "$currententrycounter|";
	}

	$currententrycounter--;

} until $currententrycounter eq "0";

if ($rebuildentrylist eq "yes") {
	$checkentrycounter = $newentrynumber;
	$rebuiltentrylist = "";
	do {
		$checkentrycounterpadded = sprintf ("%8d", $checkentrycounter);
		$checkentrycounterpadded =~ tr/ /0/;
		&gm_getentryvariables($checkentrycounter);
		$checkentryopenstatus = "O";
		$checkentrymorestatus = "N";
		if ($thisentryopenstatus eq "closed") { $checkentryopenstatus = "C"; }
		if ($thisentrymorebody ne "") { $checkentrymorestatus = "Y"; }
		$rebuiltentrylist .= "$thisentrynumber|$thisentryauthor|$thisentrysubject|$thisentrymonthmonth\/$thisentrydayday\/$thisentryyear|$thisentryhourhour\:$thisentryminuteminute $thisentryampm|$checkentryopenstatus|$checkentrymorestatus\n";
		$checkentrycounter--;
	} until $checkentrycounter eq "0";
	open (FUNNYFEET, ">gm-entrylist.cgi") || &gm_dangermouse("Can't write to gm-entrylist.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666.");
	print FUNNYFEET $rebuiltentrylist;
	close (FUNNYFEET);
}

if ($listofaffectedentries ne "") {
	chop ($listofaffectedentries);
	@affectedentrylist = split (/\|/, $listofaffectedentries);
}

if ($entriesaffected eq "0") {
	&gm_writetocplog("$IN{'authorname'} searched all entries for \"$IN{'srsearchterm'}\" and replaced it with \"$IN{'srreplaceterm'}\" (no entries affected)");
	$statusnote = qq(<B><FONT COLOR="#FF0000">The search term was not found.</FONT></B><P>);
	$IN{'entryselectionview'} = "searchresults";
	&gm_editentryselection;
} elsif ($entriesaffected eq "1") {
	&gm_writetocplog("$IN{'authorname'} searched all entries for \"$IN{'srsearchterm'}\" and replaced it with \"$IN{'srreplaceterm'}\" (1 entry affected)");
	$statusnote = qq(<B><FONT COLOR="#0000FF">The search-and-replace was completed successfully \(1 entry affected\).<BR>The affected entry is listed below.</FONT></B><P>);
	$IN{'entryselectionview'} = "searchresults";
	&gm_editentryselection;
} else {
	&gm_writetocplog("$IN{'authorname'} searched all entries for \"$IN{'srsearchterm'}\" and replaced it with \"$IN{'srreplaceterm'}\" ($entriesaffected entries affected)");
	$statusnote = qq(<B><FONT COLOR="#0000FF">The search-and-replace was completed successfully \($entriesaffected entries affected\).<BR>All affected entries are listed below.</FONT></B><P>);
	$IN{'entryselectionview'} = "searchresults";
	&gm_editentryselection;
}

}

# -----------------------------------
# edit an entry - main editing screen
# -----------------------------------

sub gm_editthisentry {

&gm_validate;

if ($gmentryeditaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit entry #$IN{'entryselectionlist'} without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit entries.</FONT></B><P>);
	&gm_frontpage;
}

if ($IN{'entryselectionlist'} eq "") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must select an entry to edit.</FONT></B><P>);
	&gm_editentryselection;
}

&gm_readconfig;
&gm_readtemplates;
&gm_readcounter;

$thisentrynumberpadded = sprintf ("%8d", $IN{'entryselectionlist'});
$thisentrynumberpadded =~ tr/ /0/;

open (FUNNYFEET, "$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
@entrylines = <FUNNYFEET>;
close (FUNNYFEET);

$gmcounter = 0;

foreach (@entrylines) {
	chomp ($entrylines[$gmcounter]);
	$entrylines[$gmcounter] =~ s/\|\*\|/\n/g;
	$gmcounter++;
}

($thisentrynumber, $thisentryauthor, $thisentrysubject, $thisentryweekdaynumber, $thisentrymonth, $thisentryday, $thisentryyearyear, $thisentryhour, $thisentryminute, $thisentrysecond, $thisentryampm, $thisentrypositivekarma, $thisentrynegativekarma, $thisentrycommentsnumber, $thisentryallowkarma, $thisentryallowcomments, $thisentryopenstatus) = split (/\|/, $entrylines[0]);

if (($IN{'authorname'} ne $thisentryauthor) && ($gmentryeditaccess eq "mineonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to edit entry #$IN{'entryselectionlist'} (by $thisentryauthor) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit entries you didn't create.</FONT></B><P>);
	&gm_editentryselection;
}

# chomp ($thisentryopenstatus);

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

$thisentrymainbody = $entrylines[2];
$thisentrymorebody = $entrylines[3];
$thisentrymainbody = &delouse($thisentrymainbody);
$thisentrymorebody = &delouse($thisentrymorebody);
$thisentrysubject = &delouse($thisentrysubject);

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000"><B>Editing Entry #$thisentrynumber: Posted by $thisentryauthor @ $thisentrymonthmonth/$thisentrydayday/$thisentryyearyear $thisentryhourhour\:$thisentryminuteminute\:$thisentrysecondsecond $thisentryampm</B></FONT></B><P>); }

$autorebuildcheckbox = "";

if ($gmrebuildaccess eq "yes") {
	if ($automaticrebuilddefault eq "yes") {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="indexandentry" CHECKED> Automatically rebuild main index and this entry's page after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	} else {
		$autorebuildcheckbox = qq(<P>\n<INPUT TYPE=CHECKBOX NAME="autorebuild" VALUE="indexandentry"> Automatically rebuild main index and this entry's page after saving\n<BR>\n<FONT SIZE=1>After clicking Save, expect a wait of up to several minutes if leaving this box checked.<BR>DO NOT interrupt Greymatter while it's rebuilding!</FONT>);
	}
}

print<<GMENTRYEDITTOP;

$gmheadtagtwo

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="revisedentrynumber" VALUE="$thisentrynumber">
<INPUT TYPE=HIDDEN NAME="revisedentryauthor" VALUE="$thisentryauthor">
<INPUT TYPE=HIDDEN NAME="entryselectionview" VALUE="$IN{'entryselectionview'}">
<TABLE BORDER=0 CELLPADDING=5 CELLSPACING=0><TR><TD ALIGN=RIGHT>$gmfonttag<B>Subject:</B></FONT></TD><TD ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="revisedentrysubject" VALUE="$thisentrysubject" SIZE=45 STYLE="width: 550">$gmfonttag</TD></TR></TABLE>
<P>
<B>Main Entry Text</B>
<BR>
</FONT><TEXTAREA NAME="revisedentrymaintext" COLS=86 ROWS=15 WRAP=VIRTUAL STYLE="width: 720">$thisentrymainbody</TEXTAREA>$gmfonttag
<P>
<B>Extended ("More") Entry Text</B>
<BR>
</FONT><TEXTAREA NAME="revisedentrymoretext" COLS=86 ROWS=15 WRAP=VIRTUAL STYLE="width: 720">$thisentrymorebody</TEXTAREA>$gmfonttag
<P>
<SCRIPT TYPE="text/javascript" LANGUAGE="JavaScript">
<!--//
if ((parseInt(navigator.appVersion) >= 4) && (navigator.appName == "Microsoft Internet Explorer")) {
	document.write("<FONT SIZE=1>Shortcut keys: CTRL-SHIFT-A to add a link, CTRL-SHIFT-B to bold selected text,<BR>CTRL-SHIFT-I to italicise, CTRL-SHIFT-U to underline</FONT><P>");
}
//-->
</SCRIPT>

GMENTRYEDITTOP

if ($thisentrycommentsnumber ne "0") {

print qq(<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=1 WIDTH=720><TR><TD VALIGN=MIDDLE ALIGN=CENTER BGCOLOR="#B0B0D0">$gmfonttag <B><FONT SIZE=1>Select</FONT></B></TD><TD VALIGN=MIDDLE ALIGN=LEFT BGCOLOR="#B0B0D0" WIDTH=100%>$gmfonttag <B><FONT SIZE=1>Comment</FONT></B></TD></TR>);

$commentcounter = 4;
$commentcountermax = $thisentrycommentsnumber + 3;

$alternatecommentrowone = "#EEF8FF";
$alternatecommentrowtwo = "#F8F8FF";
$alternatecommentrow = $alternatecommentrowone;

do {

if ($alternatecommentrow eq $alternatecommentrowone) {
	$alternatecommentrow = $alternatecommentrowtwo;
} else {
	$alternatecommentrow = $alternatecommentrowone;
}

$thiscommentnumber = $commentcounter - 3;

($thiscommentauthor, $thiscommentauthorip, $thiscommentauthoremailabsolute, $thiscommentauthorhomepageabsolute, $thiscommentweekdaynumber, $thiscommentmonth, $thiscommentday, $thiscommentyearyear, $thiscommenthour, $thiscommentminute, $thiscommentsecond, $thiscommentampm, $thiscommenttext) = split (/\|/, $entrylines[$commentcounter]);

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

$thiscommenttext =~ s/</\&lt;/g;
$thiscommenttext =~ s/>/\&gt;/g;
$thiscommenttext =~ s/\|\*\|/\n/g;
$thiscommenttext =~ s/\n/<BR>/g;
$thiscommenttext =~ s/<BR><BR>/<P>/g;
# $thiscommenttext =~ s/  / &#160;/g;

print qq(<TR><TD VALIGN=TOP ALIGN=CENTER BGCOLOR="$alternatecommentrow"><INPUT TYPE=RADIO NAME="revisedentrycommentselection" VALUE="$thiscommentnumber"></TD><TD VALIGN=MIDDLE ALIGN=LEFT BGCOLOR="$alternatecommentrow">
$gmfonttag\<B>#$thiscommentnumber\: Posted by $thiscommentauthor ($thiscommentauthorip) @ $thiscommentmonthmonth/$thiscommentdayday/$thiscommentyearyear $thiscommenthourhour\:$thiscommentminuteminute\:$thiscommentsecondsecond $thiscommentampm</B><P>$thiscommenttext);

if (($thiscommentauthoremailabsolute ne "") && ($thiscommentauthorhomepageabsolute ne "")) {
	print qq(<P>----------<BR>E-Mail: <A HREF="mailto:$thiscommentauthoremailabsolute">$thiscommentauthoremailabsolute</A><BR>Homepage: <A HREF="$thiscommentauthorhomepageabsolute">$thiscommentauthorhomepageabsolute</A>);
} else {
	if ($thiscommentauthoremailabsolute ne "") {
		print qq(<P>----------<BR>E-Mail: <A HREF="mailto:$thiscommentauthoremailabsolute">$thiscommentauthoremailabsolute</A>);
	}
	if ($thiscommentauthorhomepageabsolute ne "") {
		print qq(<P>----------<BR>Homepage: <A HREF="$thiscommentauthorhomepageabsolute">$thiscommentauthorhomepageabsolute</A>);
	}
}

print qq(</FONT></TD></TR>);

$commentcounter++;

} until $commentcounter > $commentcountermax;

print qq(</TABLE></TD></TR></TABLE>\n<P><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Edit Selected Comment"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #FFD0D0" VALUE="Delete Selected Comment">\n<P>\n);

}

if ($thisentrypositivekarma ne "0") {
	print qq(<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=0 BGCOLOR="#D0D0FF" WIDTH=658><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag Positive karma votes from (IPs): );

	$karmatempipline = "";
	@karmatempiptally = split (/\|/, $entrylines[1]);

	$gmcounter = 0;

	foreach (@karmatempiptally) {
		if ($karmatempiptally[$gmcounter] eq "P") { $karmatempipline .= "$karmatempiptally[$gmcounter - 1], "; }
		$gmcounter++;
	}

	substr($karmatempipline, -2, 2) = "";

	print qq($karmatempipline \($thisentrypositivekarma total\)</FONT></TD></TR></TABLE></TD></TR></TABLE>\n<P>\n);
}

if ($thisentrynegativekarma ne "0") {
	print qq(<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=7 CELLSPACING=0 BGCOLOR="#D0D0D0" WIDTH=658><TR><TD VALIGN=MIDDLE ALIGN=CENTER>$gmfonttag Negative karma votes from (IPs): );

	$karmatempipline = "";
	@karmatempiptally = split (/\|/, $entrylines[1]);

	$gmcounter = 0;

	foreach (@karmatempiptally) {
		if ($karmatempiptally[$gmcounter] eq "N") { $karmatempipline .= "$karmatempiptally[$gmcounter - 1], "; }
		$gmcounter++;
	}

	substr($karmatempipline, -2, 2) = "";

	print qq($karmatempipline \($thisentrynegativekarma total\)</FONT></TD></TR></TABLE></TD></TR></TABLE>\n<P>\n);
}

if (($allowkarmaorcomments eq "karma") || ($allowkarmaorcomments eq "both")) {
	if ($thisentryallowkarma eq "yes") {
		print qq(Allow karma voting on this entry: <INPUT TYPE=RADIO NAME="revisedentryallowkarma" VALUE="yes" CHECKED> Yes <INPUT TYPE=RADIO NAME="revisedentryallowkarma" VALUE="no"> No\n);
	} else {
		print qq(Allow karma voting on this entry: <INPUT TYPE=RADIO NAME="revisedentryallowkarma" VALUE="yes"> Yes <INPUT TYPE=RADIO NAME="revisedentryallowkarma" VALUE="no" CHECKED> No\n);
	}
} else {
	print qq(<INPUT TYPE=HIDDEN NAME="revisedentryallowkarma" VALUE="no">\n);
}

if ($allowkarmaorcomments eq "both") { print "<BR>\n"; }

if (($allowkarmaorcomments eq "comments") || ($allowkarmaorcomments eq "both")) {
	if ($thisentryallowcomments eq "yes") {
		print qq(Allow comments to be posted to this entry: <INPUT TYPE=RADIO NAME="revisedentryallowcomments" VALUE="yes" CHECKED> Yes <INPUT TYPE=RADIO NAME="revisedentryallowcomments" VALUE="no"> No\n<BR>\n);
	} else {
		print qq(Allow comments to be posted to this entry: <INPUT TYPE=RADIO NAME="revisedentryallowcomments" VALUE="yes"> Yes <INPUT TYPE=RADIO NAME="revisedentryallowcomments" VALUE="no" CHECKED> No\n<BR>\n);
	}
} else {
	print qq(<INPUT TYPE=HIDDEN NAME="revisedentryallowkarma" VALUE="no">\n);
}

if ($newstayattopnumber eq $thisentrynumber) {
	print qq(Keep this entry at the top of the main page: <INPUT TYPE=RADIO NAME="revisedentrystayattop" VALUE="yes" CHECKED> Yes <INPUT TYPE=RADIO NAME="revisedentrystayattop" VALUE="no"> No\n<BR>\n);
} else {
	print qq(Keep this entry at the top of the main page: <INPUT TYPE=RADIO NAME="revisedentrystayattop" VALUE="yes"> Yes <INPUT TYPE=RADIO NAME="revisedentrystayattop" VALUE="no" CHECKED> No\n<BR>\n);
}

if ($thisentryopenstatus eq "open") {
	print qq(This entry is: <INPUT TYPE=RADIO NAME="revisedentryopenstatus" VALUE="open" CHECKED> Open <INPUT TYPE=RADIO NAME="revisedentryopenstatus" VALUE="closed"> Closed\n);
} else {
	print qq(This entry is: <INPUT TYPE=RADIO NAME="revisedentryopenstatus" VALUE="open"> Open <INPUT TYPE=RADIO NAME="revisedentryopenstatus" VALUE="closed" CHECKED> Closed\n);
}

print<<GMENTRYEDITBOTTOM;

$autorebuildcheckbox
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Changes To This Entry"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Select Another Entry">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>
"Always changing; everything for good, nothing for nothing."&#151;Flying Hawk, Sioux Chief
</FONT>
$gmframebottom

</BODY>
</HTML>

GMENTRYEDITBOTTOM

exit;

}

# ----------------------------
# save changes to edited entry
# ----------------------------

sub gm_saveentrychanges {

&gm_validate;

if ($gmentryeditaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit entry #$IN{'revisedentrynumber'} without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit entries.</FONT></B><P>);
	&gm_frontpage;
}

if (($IN{'authorname'} ne $IN{'revisedentryauthor'}) && ($gmentryeditaccess eq "mineonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to edit entry #$IN{'entryselectionlist'} (by $IN{'revisedentryauthor'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit entries you didn't create.</FONT></B><P>);
	&gm_editentryselection;
}

$IN{'revisedentrysubject'} = &configdelouse($IN{'revisedentrysubject'});

if ($IN{'revisedentrymaintext'} eq "") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You left the main text field blank.  Please try again.</FONT></B><P>);
	$IN{'entryselectionlist'} = $IN{'revisedentrynumber'};
	&gm_editthisentry;
}

&gm_readconfig;
&gm_readtemplates;
&gm_readcounter;

$thisentrynumberpadded = sprintf ("%8d", $IN{'revisedentrynumber'});
$thisentrynumberpadded =~ tr/ /0/;

open (FUNNYFEET, "$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
@entrylines = <FUNNYFEET>;
close (FUNNYFEET);

$gmcounter = 0;

foreach (@entrylines) {
	chomp ($entrylines[$gmcounter]);
	$gmcounter++;
}

($thisentrynumber, $thisentryauthor, $thisentrysubject, $thisentryweekdaynumber, $thisentrymonth, $thisentryday, $thisentryyearyear, $thisentryhour, $thisentryminute, $thisentrysecond, $thisentryampm, $thisentrypositivekarma, $thisentrynegativekarma, $thisentrycommentsnumber, $thisentryallowkarma, $thisentryallowcomments, $thisentryopenstatus) = split (/\|/, $entrylines[0]);

chomp ($thisentryopenstatus);

if (($thisentryopenstatus eq "open") && ($IN{'revisedentryopenstatus'} eq "closed")) {
	$newalltimeopenentriesnumber--;
	$newalltimeclosedentriesnumber++;
}

if (($thisentryopenstatus eq "closed") && ($IN{'revisedentryopenstatus'} eq "open")) {
	$newalltimeopenentriesnumber++;
	$newalltimeclosedentriesnumber--;
}

$thisentryyear = substr($thisentryyearyear, -2, 2);

@months = ("null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
@weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");

$thisentryweekday = $weekdays[$thisentryweekdaynumber];
$thisentrymonthword = $months[$thisentrymonth];

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

$IN{'revisedentrysubject'} = &configdelouse($IN{'revisedentrysubject'});
$IN{'revisedentrysubject'} = &relouse($IN{'revisedentrysubject'});
$IN{'revisedentrymaintext'} = &relouse($IN{'revisedentrymaintext'});
$IN{'revisedentrymoretext'} = &relouse($IN{'revisedentrymoretext'});

open (FUNNYFEET, ">$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEET "$thisentrynumber|$thisentryauthor|$IN{'revisedentrysubject'}|$thisentryweekdaynumber|$thisentrymonth|$thisentryday|$thisentryyearyear|$thisentryhour|$thisentryminute|$thisentrysecond|$thisentryampm|$thisentrypositivekarma|$thisentrynegativekarma|$thisentrycommentsnumber|$IN{'revisedentryallowkarma'}|$IN{'revisedentryallowcomments'}|$IN{'revisedentryopenstatus'}\n";
print FUNNYFEET "$entrylines[1]\n";
print FUNNYFEET "$IN{'revisedentrymaintext'}\n";
print FUNNYFEET "$IN{'revisedentrymoretext'}\n";

if ($thisentrycommentsnumber ne "0") {

	$commentcounter = 4;
	$commentcountermax = $thisentrycommentsnumber + 3;

	do {
	
	unless ($entrylines[$commentcounter] eq "") { print FUNNYFEET "$entrylines[$commentcounter]\n"; }

	$commentcounter++;

	} until $commentcounter > $commentcountermax;

}

close (FUNNYFEET);

open (FUNNYFEET, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entrylist file.  Please make sure that gm-entrylist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@originalentrylist = <FUNNYFEET>;
close (FUNNYFEET);

$revisedentrymorestatus = "N";
if ($IN{'revisedentrymoretext'} ne "") { $revisedentrymorestatus = "Y"; }
$revisedentrymarkopen = "O";
if ($IN{'revisedentryopenstatus'} eq "closed") { $revisedentrymarkopen = "C"; }

open (FUNNYFEET, ">gm-entrylist.cgi") || &gm_dangermouse("Can't write to the entrylist file.  Please make sure that gm-entrylist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
foreach $thisentrylistline (@originalentrylist) {
	chomp ($thisentrylistline);
	($thisentrylistnumber, $thisentrylistauthor, $thisentrylistsubject, $thisentrylistdate, $thisentrylisttime, $thisentrylistopenstatus, $thisentrylistmorestatus) = split (/\|/, $thisentrylistline);
	if ($thisentrylistnumber eq $IN{'revisedentrynumber'}) {
		print FUNNYFEET "$IN{'revisedentrynumber'}|$thisentrylistauthor|$IN{'revisedentrysubject'}|$thisentrylistdate|$thisentrylisttime|$revisedentrymarkopen|$revisedentrymorestatus\n";
	} else {
		print FUNNYFEET "$thisentrylistline\n";
	}
}
close (FUNNYFEET);

if (($IN{'revisedentrystayattop'} eq "no") && ($newstayattopnumber eq $thisentrynumber)) { $newstayattopnumber = 0; }

if ($IN{'revisedentrystayattop'} eq "yes") { $newstayattopnumber = $thisentrynumber; }

&gm_writecounter;

$recordentrysubject = $IN{'revisedentrysubject'};
if ($recordentrysubject eq "") { $recordentrysubject = "[no subject]"; }

&gm_writetocplog("$IN{'authorname'} edited an entry (#$IN{'revisedentrynumber'}: $recordentrysubject)");

if ($IN{'autorebuild'} eq "indexandentry") {
	&gm_readconfig;
	&gm_readcounter;
	&gm_readtemplates;
	&gm_generatemainindex;
	&gm_getentryvariables($IN{'revisedentrynumber'});
	if (($thisentryopenstatus eq "open") && ($generateentrypages eq "yes")) {
		if ($thisentrymorebody ne "") {
			&gm_formatentry($gmmoreentrypagetemplate);
		} else {
			&gm_formatentry($gmentrypagetemplate);
		}
		open (THISFILE, ">$EntriesPath/$thisentrynumberpadded.$entrysuffix") || &gm_dangermouse("Can't write to $EntriesPath/$thisentrynumberpadded.$entrysuffix.  Please make sure that your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
		print THISFILE $entryreturn;
		close (THISFILE);
		chmod (0666, "$EntriesPath/$thisentrynumberpadded.$entrysuffix");
	} else {
		unlink ("$EntriesPath/$thisentrynumberpadded.$entrysuffix");
	}
	$statusnote = qq(<B><FONT COLOR="#0000FF">Entry #$IN{'revisedentrynumber'} ($recordentrysubject) has been edited<BR>and the main index & this entry's page have been rebuilt.</FONT></B><P>);
} else {
	$statusnote = qq(<B><FONT COLOR="#0000FF">Entry #$IN{'revisedentrynumber'} ($recordentrysubject) has been edited.<BR>Be sure to rebuild your files for the changes to be visible on your site.</FONT></B><P>);
}

&gm_frontpage;

}

# ------------------------
# change entry open status
# ------------------------

sub gm_changeentryopenstatus {

&gm_validate;

if ($gmentryeditaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to change the open/closed status on entry #$IN{'revisedentrynumber'} without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to open/close entries.</FONT></B><P>);
	&gm_frontpage;
}

if ($IN{'entryselectionlist'} eq "") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must select an entry to open or close.</FONT></B><P>);
	&gm_editentryselection;
}

&gm_readconfig;
&gm_readtemplates;
&gm_readcounter;

$thisentrynumberpadded = sprintf ("%8d", $IN{'entryselectionlist'});
$thisentrynumberpadded =~ tr/ /0/;

open (FUNNYFEET, "$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
@entrylines = <FUNNYFEET>;
close (FUNNYFEET);

$gmcounter = 0;

foreach (@entrylines) {
	chomp ($entrylines[$gmcounter]);
	$gmcounter++;
}

($thisentrynumber, $thisentryauthor, $thisentrysubject, $thisentryweekdaynumber, $thisentrymonth, $thisentryday, $thisentryyearyear, $thisentryhour, $thisentryminute, $thisentrysecond, $thisentryampm, $thisentrypositivekarma, $thisentrynegativekarma, $thisentrycommentsnumber, $thisentryallowkarma, $thisentryallowcomments, $thisentryopenstatus) = split (/\|/, $entrylines[0]);

if (($IN{'authorname'} ne $thisentryauthor) && ($gmentryeditaccess eq "mineonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to change the open/closed status on entry #$IN{'entryselectionlist'} (by $thisentryauthor) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to open/close entries you didn't create.</FONT></B><P>);
	&gm_editentryselection;
}

if ($thisentryopenstatus eq "open") {
	$newalltimeopenentriesnumber--;
	$newalltimeclosedentriesnumber++;
	$thisentryopenstatus = "closed";
} else {
	$newalltimeopenentriesnumber++;
	$newalltimeclosedentriesnumber--;
	$thisentryopenstatus = "open";
}

$gmcounter = 0;

&gm_writecounter;

open (FUNNYFEET, ">$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
print FUNNYFEET "$thisentrynumber|$thisentryauthor|$thisentrysubject|$thisentryweekdaynumber|$thisentrymonth|$thisentryday|$thisentryyearyear|$thisentryhour|$thisentryminute|$thisentrysecond|$thisentryampm|$thisentrypositivekarma|$thisentrynegativekarma|$thisentrycommentsnumber|$thisentryallowkarma|$thisentryallowcomments|$thisentryopenstatus\n";
foreach (@entrylines) {
	unless ($gmcounter eq "0") { print FUNNYFEET "$entrylines[$gmcounter]\n"; }
	$gmcounter++;
}
close (FUNNYFEET);

open (FUNNYFEET, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entrylist file.  Please make sure that gm-entrylist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
@originalentrylist = <FUNNYFEET>;
close (FUNNYFEET);

open (FUNNYFEET, ">gm-entrylist.cgi") || &gm_dangermouse("Can't write to the entrylist file.  Please make sure that gm-entrylist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
foreach $thisentrylistline (@originalentrylist) {
	chomp ($thisentrylistline);
	($thisentrylistnumber, $thisentrylistauthor, $thisentrylistsubject, $thisentrylistdate, $thisentrylisttime, $thisentrylistopenstatus, $thisentrylistmorestatus) = split (/\|/, $thisentrylistline);
	if ($thisentrylistnumber eq $thisentrynumber) {
		if ($thisentrylistopenstatus eq "O") {
			$thisentrylistopenstatus = "C";
		} else {
			$thisentrylistopenstatus = "O";
		}
		print FUNNYFEET "$thisentrylistnumber|$thisentrylistauthor|$thisentrylistsubject|$thisentrylistdate|$thisentrylisttime|$thisentrylistopenstatus|$thisentrylistmorestatus\n";
	} else {
		print FUNNYFEET "$thisentrylistline\n";
	}
}
close (FUNNYFEET);

if ($thisentryopenstatus eq "open") {
	&gm_writetocplog("$IN{'authorname'} reopened an entry (#$thisentrynumber: $thisentrysubject)");
} else {
	&gm_writetocplog("$IN{'authorname'} closed an entry (#$thisentrynumber: $thisentrysubject)");
}

if ($thisentryopenstatus eq "open") {
	$statusnote = qq(<B><FONT COLOR="#0000FF">Entry #$thisentrynumber ($thisentrysubject) has been reopened.<BR>Be sure to rebuild your files for the changes to be visible on your site.</FONT></B><P>);
} else {
	$statusnote = qq(<B><FONT COLOR="#0000FF">Entry #$thisentrynumber ($thisentrysubject) has been closed.<BR>Be sure to rebuild your files for the changes to be visible on your site.</FONT></B><P>);
}

&gm_editentryselection;

}

# -----------------------
# delete selected comment
# -----------------------

sub gm_deleteselectedcomment {

&gm_validate;

if ($gmentryeditaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to delete a comment from entry #$IN{'revisedentrynumber'} ($IN{'revisedentrysubject'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to delete comments.</FONT></B><P>);
	&gm_frontpage;
}

if ($IN{'revisedentrycommentselection'} eq "") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must select a comment to be deleted.</FONT></B><P>);
	&gm_editthisentry;
}

if (($IN{'authorname'} ne $IN{'revisedentryauthor'}) && ($gmentryeditaccess eq "mineonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to delete a comment from entry #$IN{'entryselectionlist'} (by $IN{'revisedentryauthor'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to delete comments from entries you didn't create.</FONT></B><P>);
	&gm_editentryselection;
}

$deleteme = $IN{'revisedentrycommentselection'} + 3;

$thisentrynumberpadded = sprintf ("%8d", $IN{'revisedentrynumber'});
$thisentrynumberpadded =~ tr/ /0/;

open (FUNNYFEET, "$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure that your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
@entrylines = <FUNNYFEET>;
close (FUNNYFEET);

($thisentrynumber, $thisentryauthor, $thisentrysubject, $thisentryweekdaynumber, $thisentrymonth, $thisentryday, $thisentryyearyear, $thisentryhour, $thisentryminute, $thisentrysecond, $thisentryampm, $thisentrypositivekarma, $thisentrynegativekarma, $thisentrycommentsnumber, $thisentryallowkarma, $thisentryallowcomments, $thisentryopenstatus) = split (/\|/, $entrylines[0]);

if (($IN{'authorname'} ne $IN{'revisedentryauthor'} ) && ($gmentryeditaccess eq "mineonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to delete entry #$IN{'entryselectionlist'} (by $IN{'revisedentryauthor'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to delete entries you didn't create.</FONT></B><P>);
	&gm_editentryselection;
}

$thisentrycommentsnumber--;

$entrylines[0] = "$thisentrynumber|$thisentryauthor|$thisentrysubject|$thisentryweekdaynumber|$thisentrymonth|$thisentryday|$thisentryyearyear|$thisentryhour|$thisentryminute|$thisentrysecond|$thisentryampm|$thisentrypositivekarma|$thisentrynegativekarma|$thisentrycommentsnumber|$thisentryallowkarma|$thisentryallowcomments|$thisentryopenstatus";

$entrylines[$deleteme] = "*DELETED*";

open (FUNNYFEET, ">$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure that your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
foreach $revisedentryline (@entrylines) {
	chomp ($revisedentryline);
	unless ($revisedentryline eq "*DELETED*") { print FUNNYFEET "$revisedentryline\n"; }
}
close (FUNNYFEET);

&gm_readcounter;

$newalltimecommentstotalnumber--;

&gm_writecounter;

&gm_writetocplog("$IN{'authorname'} deleted a comment from entry #$IN{'revisedentrynumber'} ($IN{'revisedentrysubject'})");

$statusnote = qq(<B><FONT COLOR="#0000FF">The comment has been deleted.</FONT></B><P>);

$IN{'entryselectionlist'} = $IN{'revisedentrynumber'};

&gm_editthisentry;

}

# ---------------------
# edit selected comment
# ---------------------

sub gm_editselectedcomment {

&gm_validate;

if ($gmentryeditaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit comment #$IN{'revisedentrycommentselection'} in entry #$IN{'revisedentrynumber'} ($IN{'revisedentrysubject'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit comments.</FONT></B><P>);
	&gm_frontpage;
}

if ($IN{'revisedentrycommentselection'} eq "") {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You must select a comment to be edited.</FONT></B><P>);
	$IN{'entryselectionlist'} = $IN{'revisedentrynumber'};
	&gm_editthisentry;
}

if (($IN{'authorname'} ne $IN{'revisedentryauthor'}) && ($gmentryeditaccess eq "mineonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to edit a comment in entry #$IN{'entryselectionlist'} (by $IN{'revisedentryauthor'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit comments in entries you didn't create.</FONT></B><P>);
	&gm_editentryselection;
}

$thisentrynumberpadded = sprintf ("%8d", $IN{'revisedentrynumber'});
$thisentrynumberpadded =~ tr/ /0/;

$editme = $IN{'revisedentrycommentselection'} + 3;

open (FUNNYFEET, "$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure that your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
@entrylines = <FUNNYFEET>;
close (FUNNYFEET);

chomp ($entrylines[$editme]);

$entrylines[$editme] =~ s/\|\*\|/\n/g;

($thiscommentauthor, $thiscommentauthorip, $thiscommentauthoremailabsolute, $thiscommentauthorhomepageabsolute, $thiscommentweekdaynumber, $thiscommentmonth, $thiscommentday, $thiscommentyearyear, $thiscommenthour, $thiscommentminute, $thiscommentsecond, $thiscommentampm, $thiscommenttext) = split (/\|/, $entrylines[$editme]);

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
$thiscommenttext = &delouse($thiscommenttext);

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Editing Comment #$IN{'revisedentrycommentselection'} In Entry #$IN{'revisedentrynumber'} ($IN{'revisedentrysubject'})</FONT></B>\n<BR>\nPosted @ $thiscommentmonthmonth/$thiscommentdayday/$thiscommentyearyear $thiscommenthourhour\:$thiscommentminuteminute\:$thiscommentsecondsecond $thiscommentampm<P>); }

print<<GMEDITCOMMENT;

$gmheadtag

$gmframetop
$statusnote
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="revisedentryauthor" VALUE="$IN{'revisedentryauthor'}">
<INPUT TYPE=HIDDEN NAME="revisedentrynumber" VALUE="$IN{'revisedentrynumber'}">
<INPUT TYPE=HIDDEN NAME="revisedentrysubject" VALUE="$IN{'revisedentrysubject'}">
<INPUT TYPE=HIDDEN NAME="entryselectionlist" VALUE="$IN{'revisedentrynumber'}">
<INPUT TYPE=HIDDEN NAME="revisedentrycommentselection" VALUE="$IN{'revisedentrycommentselection'}">
<TABLE BORDER=0 CELLPADDING=3 CELLSPACING=0><TR><TD VALIGN=MIDDLE ALIGN=RIGHT>$gmfonttag<B>Author:</B></FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="revisedentrycommentauthor" VALUE="$thiscommentauthor" SIZE=45 STYLE="width: 550">$gmfonttag</TD></TR><TR><TD VALIGN=MIDDLE ALIGN=RIGHT>$gmfonttag<B>E-Mail:</B></FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="revisedentrycommentauthoremail" VALUE="$thiscommentauthoremailabsolute" SIZE=45 STYLE="width: 550">$gmfonttag</TD></TR><TR><TD VALIGN=MIDDLE ALIGN=RIGHT>$gmfonttag<B>Homepage:</B></FONT></TD><TD VALIGN=MIDDLE ALIGN=LEFT></FONT><INPUT TYPE=TEXT CLASS="textinput" NAME="revisedentrycommentauthorhomepage" VALUE="$thiscommentauthorhomepageabsolute" SIZE=45 STYLE="width: 550">$gmfonttag</TD></TR></TABLE>
<P>
<B>Comment Text</B>
<BR>
</FONT><TEXTAREA NAME="revisedentrycommenttext" COLS=86 ROWS=15 WRAP=VIRTUAL STYLE="width: 720">$thiscommenttext</TEXTAREA>$gmfonttag
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Save Changes To This Comment"> <INPUT TYPE=RESET CLASS="button" STYLE="background: #FFD0D0" VALUE="Undo Changes Since Last Save">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Entry Editing">
<P>
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<P>
<FONT SIZE=1>
"All good men are happy when they choose to be their own authors. Those who choose to have
<BR>
others edit their pathways, must live on the edge of another man's sword."&#151;Julie Arabi
</FONT>
$gmframebottom

</BODY>
</HTML>

GMEDITCOMMENT

exit;

}

# --------------------
# save comment changes
# --------------------

sub gm_savecommentchanges {

&gm_validate;

if ($gmentryeditaccess eq "no") {
	&gm_writetocplog("$IN{'authorname'} attempted to edit comment #$IN{'revisedentrycommentselection'} in entry #$IN{'revisedentrynumber'} ($IN{'revisedentrysubject'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit comments.</FONT></B><P>);
	&gm_frontpage;
}

if (($IN{'authorname'} ne $IN{'revisedentryauthor'}) && ($gmentryeditaccess eq "mineonly")) {
	&gm_writetocplog("$IN{'authorname'} attempted to edit comment #$IN{'revisedentrycommentselection'} in entry #$IN{'entryselectionlist'} (by $IN{'revisedentryauthor'}) without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to edit comments in entries you didn't create.</FONT></B><P>);
	&gm_editentryselection;
}

$IN{'entryselectionlist'} = $IN{'revisedentrynumber'};

$IN{'revisedentrycommentauthor'} = &configdelouse($IN{'revisedentrycommentauthor'});
$IN{'revisedentrycommentauthoremail'} = &configdelouse($IN{'revisedentrycommentauthoremail'});
$IN{'revisedentrycommentauthorhomepage'} = &configdelouse($IN{'revisedentrycommentauthorhomepage'});
$IN{'revisedentrycommenttext'} = &relouse($IN{'revisedentrycommenttext'});

if (($IN{'revisedentrycommentauthor'} eq "") || ($IN{'revisedentrycommenttext'} eq "")) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You left either the comment author or text blank.  Please try again.</FONT></B><P>);
	&gm_editselectedcomment;
}

$thisentrynumberpadded = sprintf ("%8d", $IN{'revisedentrynumber'});
$thisentrynumberpadded =~ tr/ /0/;

open (FUNNYFEET, "$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't read $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure that your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
@entrylines = <FUNNYFEET>;
close (FUNNYFEET);

$editme = $IN{'revisedentrycommentselection'} + 3;

chomp ($entrylines[$editme]);

($thiscommentauthor, $thiscommentauthorip, $thiscommentauthoremailabsolute, $thiscommentauthorhomepageabsolute, $thiscommentweekdaynumber, $thiscommentmonth, $thiscommentday, $thiscommentyearyear, $thiscommenthour, $thiscommentminute, $thiscommentsecond, $thiscommentampm, $thiscommenttext) = split (/\|/, $entrylines[$editme]);

$entrylines[$editme] = "$IN{'revisedentrycommentauthor'}|$thiscommentauthorip|$IN{'revisedentrycommentauthoremail'}|$IN{'revisedentrycommentauthorhomepage'}|$thiscommentweekdaynumber|$thiscommentmonth|$thiscommentday|$thiscommentyearyear|$thiscommenthour|$thiscommentminute|$thiscommentsecond|$thiscommentampm|$IN{'revisedentrycommenttext'}";

$gmcounter = 0;

open (FUNNYFEET, ">$EntriesPath/$thisentrynumberpadded.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$thisentrynumberpadded.cgi.  Please make sure that your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
foreach (@entrylines) {
	chomp ($entrylines[$gmcounter]);
	print FUNNYFEET "$entrylines[$gmcounter]\n";
	$gmcounter++;
}
close (FUNNYFEET);

&gm_writetocplog("$IN{'authorname'} edited comment #$IN{'revisedentrycommentselection'} in entry #$IN{'revisedentrynumber'} ($IN{'revisedentrysubject'})");

$statusnote = qq(<B><FONT COLOR="#0000FF">Comment #$IN{'revisedentrycommentselection'} has been edited.  Be sure to rebuild your files<BR>to make the changes visible on that entry's page.</FONT></B><P>);

&gm_editthisentry;

}

# ----------------------------
# diagnostics & repair - check
# ----------------------------

sub gm_diagnosticscheck {

&gm_validate;

if ($gmconfigurationaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to perform diagnostics & repair without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to perform diagnostics & repair.</FONT></B><P>);
	&gm_frontpage;
}

print<<GMDIAGNOSTICSCHECK;

$gmheadtag
$gmframetop
<B>Diagnostics & Repair</B>
<P>
This will check file access and permissions for your Greymatter installation, correctly CHMOD all files (if it can; you will need to do this manually if Greymatter can't do this automatically), repair any missing entries or corrupt counter files, and rebuild your entry list.  If you are installing Greymatter for the first time, if you've changed your path settings and want to verify them, or if you believe an important configuration file might be corrupt, click below to run diagnostics and rebuilding operations on your Greymatter setup.  Running this will not alter your files.  <B>Note:</B> This will verify your Local paths, but it cannot verify your Website paths.<P>Please wait for several moments after clicking (or even minutes if you have a large number of entries).<BR><B>DO NOT interrupt this procedure once started!</B><P><FORM ACTION="gm.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}"><TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0 BGCOLOR="#000000"><TR><TD><TABLE BORDER=0 CELLPADDING=10 CELLSPACING=0 BGCOLOR="#FFD0D0"><TR><TD VALIGN=MIDDLE ALIGN=CENTER><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Perform Diagnostics & Repair"></FONT></TD></TR></TABLE></TD></TR></TABLE><P><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Configuration"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF"></FORM><P><FONT SIZE=1>"The body must be repaired and supported, if we would preserve the mind in all its vigor."&#151;Pliny the Younger</FONT>
$gmframebottom

</BODY>
</HTML>

GMDIAGNOSTICSCHECK

exit;

}

# ------------------------------
# diagnostics & repair - perform
# ------------------------------

sub gm_diagnosticsperform {

&gm_validate;

if ($gmconfigurationaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to perform diagnostics & repair without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to perform diagnostics & repair.</FONT></B><P>);
	&gm_frontpage;
}

$docreport = "<UL>\n";

open (NOWHEREMAN, "$cgilocalpath/gm-authors.cgi") || &gm_dangermouse("Can't read $cgilocalpath/gm-authors.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
@nowherefile = <NOWHEREMAN>;
close (NOWHEREMAN);

chmod (0666, "gm-authors.cgi");

open (NOWHEREMAN, ">$cgilocalpath/gm-authors.cgi") || &gm_dangermouse("Can't write to $cgilocalpath/gm-authors.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
print NOWHEREMAN @nowherefile;
close (NOWHEREMAN);

open (NOWHEREMAN, "$cgilocalpath/gm-banlist.cgi") || &gm_dangermouse("Can't read $cgilocalpath/gm-banlist.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
@nowherefile = <NOWHEREMAN>;
close (NOWHEREMAN);

chmod (0666, "gm-banlist.cgi");

open (NOWHEREMAN, ">$cgilocalpath/gm-banlist.cgi") || &gm_dangermouse("Can't write to $cgilocalpath/gm-banlist.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
print NOWHEREMAN @nowherefile;
close (NOWHEREMAN);

open (NOWHEREMAN, "$cgilocalpath/gm-config.cgi") || &gm_dangermouse("Can't read $cgilocalpath/gm-config.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
@nowherefile = <NOWHEREMAN>;
close (NOWHEREMAN);

chmod (0666, "gm-config.cgi");

open (NOWHEREMAN, ">$cgilocalpath/gm-config.cgi") || &gm_dangermouse("Can't write to $cgilocalpath/gm-config.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
print NOWHEREMAN @nowherefile;
close (NOWHEREMAN);

open (NOWHEREMAN, "$cgilocalpath/gm-counter.cgi") || &gm_dangermouse("Can't read $cgilocalpath/gm-counter.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
@nowherefile = <NOWHEREMAN>;
close (NOWHEREMAN);

chmod (0666, "gm-counter.cgi");

open (NOWHEREMAN, ">$cgilocalpath/gm-counter.cgi") || &gm_dangermouse("Can't write to $cgilocalpath/gm-counter.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
print NOWHEREMAN @nowherefile;
close (NOWHEREMAN);

open (NOWHEREMAN, "$cgilocalpath/gm-cplog.cgi") || &gm_dangermouse("Can't read $cgilocalpath/gm-cplog.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
@nowherefile = <NOWHEREMAN>;
close (NOWHEREMAN);

chmod (0666, "gm-cplog.cgi");

open (NOWHEREMAN, ">$cgilocalpath/gm-cplog.cgi") || &gm_dangermouse("Can't write to $cgilocalpath/gm-cplog.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
print NOWHEREMAN @nowherefile;
close (NOWHEREMAN);

open (NOWHEREMAN, "$cgilocalpath/gm-entrylist.cgi") || &gm_dangermouse("Can't read $cgilocalpath/gm-entrylist.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
@nowherefile = <NOWHEREMAN>;
close (NOWHEREMAN);

chmod (0666, "gm-entrylist.cgi");

open (NOWHEREMAN, ">$cgilocalpath/gm-entrylist.cgi") || &gm_dangermouse("Can't write to $cgilocalpath/gm-entrylist.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
print NOWHEREMAN @nowherefile;
close (NOWHEREMAN);

open (NOWHEREMAN, "$cgilocalpath/gm-templates.cgi") || &gm_dangermouse("Can't read $cgilocalpath/gm-templates.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
@nowherefile = <NOWHEREMAN>;
close (NOWHEREMAN);

chmod (0666, "gm-templates.cgi");

open (NOWHEREMAN, ">$cgilocalpath/gm-templates.cgi") || &gm_dangermouse("Can't write to $cgilocalpath/gm-templates.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
print NOWHEREMAN @nowherefile;
close (NOWHEREMAN);

$docreport .= "<LI> All config files are readable/writeable and are CHMODed correctly\n";

if (!(open(NOWHEREMAN,"$cgilocalpath/gm-karma.cgi"))) {
	&gm_dangermouse("Can't find $cgilocalpath/gm-karma.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 755, and that your Local CGI Path is pointing to the correct place.");
}
close(NOWHEREMAN);

if (!(open(NOWHEREMAN,"$cgilocalpath/gm-comments.cgi"))) {
	&gm_dangermouse("Can't find $cgilocalpath/gm-comments.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 755, and that your Local CGI Path is pointing to the correct place.");
}
close(NOWHEREMAN);

if (!(open(NOWHEREMAN,"$cgilocalpath/gm-upload.cgi"))) {
	&gm_dangermouse("Can't find $cgilocalpath/gm-upload.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 755, and that your Local CGI Path is pointing to the correct place.");
}
close(NOWHEREMAN);

if (!(open(NOWHEREMAN,"$cgilocalpath/gm-library.cgi"))) {
	&gm_dangermouse("Can't find $cgilocalpath/gm-library.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666, and that your Local CGI Path is pointing to the correct place.");
}
close(NOWHEREMAN);

$docreport .= "<LI> The local CGI path is correctly configured and all essential files are there\n";

open (NOWHEREMAN, ">$EntriesPath/gm-testfile.txt") || &gm_dangermouse("Can't create files in $EntriesPath.  Make sure the entries/archives path is correctly configured and that this directory is CHMODed to 777.");
print NOWHEREMAN "test";
close (NOWHEREMAN);

unlink ("$EntriesPath/gm-testfile.txt") || &gm_dangermouse("Can't delete the gm-testfile.txt file created in $EntriesPath.  Your server may not support this operation.");

$docreport .= "<LI> The entries/archives path is readable/writeable and is CHMODed correctly\n";

chmod (0666, "$EntriesPath/$indexfilename");

unless (!(open(NOWHERETEMP,"$EntriesPath/$indexfilename"))) {

	open (NOWHEREMAN, "$EntriesPath/$indexfilename") || &gm_dangermouse("Can't read $EntriesPath/$indexfilename.  Make sure the entries/archives path is correctly configured and CHMODed to 777, the index filename is correctly specified under Configuration, and that this file is CHMODed to 666.");
	@nowhereland = <NOWHEREMAN>;
	close (NOWHEREMAN);

	open (NOWHEREMAN, ">$EntriesPath/$indexfilename") || &gm_dangermouse("Can't write to $EntriesPath/$indexfilename.  Make sure the entries/archives path is correctly configured and CHMODed to 777, the index filename is correctly specified under Configuration, and that this file is CHMODed to 666.");
	print NOWHEREMAN @nowhereland;
	close (NOWHEREMAN);

$docreport .= "<LI> The archive index file is readable/writeable and is CHMODed correctly\n";

}

close(NOWHERETEMP);

&gm_readcounter;

$oldentrynumbercount = $newentrynumber;
$countentriesfromhere = 5000;
$foundtopentry = "no";		

do {
	$countentriesfromherepadded = sprintf ("%8d", $countentriesfromhere);
	$countentriesfromherepadded =~ tr/ /0/;
	if (-e "$EntriesPath/$countentriesfromherepadded.cgi") {
		$newentrynumber = $countentriesfromhere;
		$foundtopentry = "yes";
	}
	$countentriesfromhere--;
	if ($countentriesfromhere eq "0") {
		$newentrynumber = 0;
		$foundtopentry = "yes";
	}
} until $foundtopentry eq "yes";

&gm_writecounter;

if ($oldentrynumbercount ne $newentrynumber) {
	$docreport .= "<LI> The counter was successfully repaired\n";
	&gm_generatemainindex;
}

if ($newentrynumber ne "0") {
	$checkentrycounter = $newentrynumber;
	$docreportentryappend = "no";
	do {
		$checkentrycounterpadded = sprintf ("%8d", $checkentrycounter);
		$checkentrycounterpadded =~ tr/ /0/;
		$makedummyentry = "no";
		if (!(open(ENTRYCHECK,"$EntriesPath/$checkentrycounterpadded.cgi"))) { $makedummyentry = "yes";	}
		close(ENTRYCHECK);
		if (($makedummyentry eq "yes") && ($checkentrycounter ne "0")) {
			&date;
			$thisnewwday = $wday;
			$thisnewmon = $mon;
			$thisnewmday = $mday;
			$thisnewyear = $JSYear;
			$thisnewhour = $hour;
			$thisnewmin = $min;
			$thisnewsec = $sec;
			$thisnewampm = $AMPM;
			if ($checkentrycounter ne $newentrynumber) {
				$nextentrynumber = $thisentrynumber + 1;
				$nextentrynumberpadded = sprintf ("%8d", $nextentrynumber);
				$nextentrynumberpadded =~ tr/ /0/;
				open (FUNNYFEET, "$EntriesPath/$nextentrynumberpadded.cgi") || &gm_dangermouse("Can't open $EntriesPath/$nextentrynumberpadded.cgi - this file may be missing or corrupt, especially if you've tried to add new entries or start using Greymatter with an incorrect installation.  Please run Diagnostics & Repair in the Configuration screen.");
				@nextentrylines = <FUNNYFEET>;
				close (FUNNYFEET);
				($nextentrynumber, $nextentryauthor, $nextentrysubject, $nextentryweekdaynumber, $nextentrymonth, $nextentryday, $nextentryyearyear, $nextentryhour, $nextentryminute, $nextentrysecond, $nextentryampm, $nextentrypositivekarma, $nextentrynegativekarma, $nextentrycommentsnumber, $nextentryallowkarma, $nextentryallowcomments, $nextentryopenstatus) = split (/\|/, $nextentrylines[0]);
				$thisnewwday = $nextentryweekdaynumber;
				$thisnewmon = $nextentrymonth;
				$thisnewmday = $nextentryday;
				$thisnewyear = $nextentryyearyear;
				$thisnewhour = $nextentryhour;
				$thisnewmin = $nextentryminute;
				$thisnewsec = $nextentrysecond;
				$thisnewampm = $nextentryampm;
			} elsif ($checkentrycounter ne "1") {
				$previousentrynumber = $thisentrynumber - 1;
				$previousentrynumberpadded = sprintf ("%8d", $previousentrynumber);
				$previousentrynumberpadded =~ tr/ /0/;
				open (FUNNYFEET, "$EntriesPath/$previousentrynumberpadded.cgi") || &gm_dangermouse("Can't open $EntriesPath/$previousentrynumberpadded.cgi - this file may be missing or corrupt, especially if you've tried to add new entries or start using Greymatter with an incorrect installation.  Please run Diagnostics & Repair in the Configuration screen.");
				@previousentrylines = <FUNNYFEET>;
				close (FUNNYFEET);
				($previousentrynumber, $previousentryauthor, $previousentrysubject, $previousentryweekdaynumber, $previousentrymonth, $previousentryday, $previousentryyearyear, $previousentryhour, $previousentryminute, $previousentrysecond, $previousentryampm, $previousentrypositivekarma, $previousentrynegativekarma, $previousentrycommentsnumber, $previousentryallowkarma, $previousentryallowcomments, $previousentryopenstatus) = split (/\|/, $previousentrylines[0]);
				$thisnewwday = $previousentryweekdaynumber;
				$thisnewmon = $previousentrymonth;
				$thisnewmday = $previousentryday;
				$thisnewyear = $previousentryyearyear;
				$thisnewhour = $previousentryhour;
				$thisnewmin = $previousentryminute;
				$thisnewsec = $previousentrysecond;
				$thisnewampm = $previousentryampm;
			}
			open (FUNNYFEET, ">$EntriesPath/$checkentrycounterpadded.cgi") || &gm_dangermouse("Can't write to $EntriesPath/$checkentrycounterpadded.cgi.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777.");
			print FUNNYFEET "$checkentrycounter|Greymatter|*Repaired*|$thisnewwday|$thisnewmon|$thisnewmday|$thisnewyear|$thisnewhour|$thisnewmin|$thisnewsec|$thisnewampm|0|0|0|no|no|closed\n";
			print FUNNYFEET "0.0.0.0|I\n";
			print FUNNYFEET "This entry was detected by Greymatter during Diagnostics & Repair as being missing or corrupt.  This is a dummy entry only.  DO NOT reopen this entry.\n";
			print FUNNYFEET "\n";
			close (FUNNYFEET);
			$docreportentryappend = "yes";
			$docreport .= "<LI> Entry #$checkentrycounter was detected as being missing or corrupt and was successfully replaced (it is recommended that you go to the Rebuild Files screen now and click \"Rebuild Everything\")\n";
		}
		chmod (0666, "$EntriesPath/$checkentrycounterpadded.cgi");
		$checkentrycounter--;
	} until $checkentrycounter eq "0";
	$docreport .= "<LI> All entry files are working correctly\n";
}

if ($newentrynumber ne "0") {
	$checkentrycounter = $newentrynumber;
	$rebuiltentrylist = "";
	do {
		$checkentrycounterpadded = sprintf ("%8d", $checkentrycounter);
		$checkentrycounterpadded =~ tr/ /0/;
		&gm_getentryvariables($checkentrycounter);
		$checkentryopenstatus = "O";
		$checkentrymorestatus = "N";
		if ($thisentryopenstatus eq "closed") { $checkentryopenstatus = "C"; }
		if ($thisentrymorebody ne "") { $checkentrymorestatus = "Y"; }
		$rebuiltentrylist .= "$thisentrynumber|$thisentryauthor|$thisentrysubject|$thisentrymonthmonth\/$thisentrydayday\/$thisentryyear|$thisentryhourhour\:$thisentryminuteminute $thisentryampm|$checkentryopenstatus|$checkentrymorestatus\n";
		$checkentrycounter--;
	} until $checkentrycounter eq "0";
	open (FUNNYFEET, ">gm-entrylist.cgi") || &gm_dangermouse("Can't write to gm-entrylist.cgi.  Make sure this file is in the same directory as all your Greymatter CGI files and is CHMODed to 666.");
	print FUNNYFEET $rebuiltentrylist;
	close (FUNNYFEET);
	$docreport .= "<LI> The entry list was successfully rebuilt\n"
}

open (NOWHEREMAN, "$LogPath/$indexfilename") || &gm_dangermouse("Can't read $LogPath/$indexfilename.  Make sure the log path is correctly configured, the index filename is correctly specified under Configuration, and that this file is CHMODed to 666.");
@nowhereland = <NOWHEREMAN>;
close (NOWHEREMAN);

chmod (0666, "$LogPath/$indexfilename");

open (NOWHEREMAN, ">$LogPath/$indexfilename") || &gm_dangermouse("Can't write to $LogPath/$indexfilename.  Make sure the log path is correctly configured, the index filename is correctly specified under Configuration, and that this file is CHMODed to 666.");
print NOWHEREMAN @nowhereland;
close (NOWHEREMAN);

$docreport .= "<LI> The main index file is readable/writeable and is CHMODed correctly\n";

if ($otherfilelist ne "") {
	@connectedfilelist = split (/\|\*\|/, $otherfilelist);
	foreach $usethisfilename (@connectedfilelist) {
		open (NOWHEREMAN, "$usethisfilename") || &gm_dangermouse("Can't open $usethisfilename.  Please make sure that this file exists and is CHMODed to 666, or else remove it from your list of connected files in configuration.");
		@connectedfilelines = <NOWHEREMAN>;
		close (NOWHEREMAN);
		chmod (0666, "$usethisfilename");
		open (NOWHEREMAN, ">$usethisfilename") || &gm_dangermouse("Can't write to $usethisfilename.  Please make sure that this file exists and is CHMODed to 666, or else remove it from your list of connected files in configuration.");
		print NOWHEREMAN @connectedfilelines;
		close (NOWHEREMAN);
	}
	$docreport .= "<LI> All connected files are readable/writeable and are CHMODed correctly\n";
}

&date;
open (FUNNYFEET, ">>gm-cplog.cgi") || &gm_dangermouse("Can't write to the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
print FUNNYFEET "<FONT SIZE=1>[$basedate] [$authorIP]</FONT> $IN{'authorname'} successfully performed diagnostics & repair\n";
close (FUNNYFEET);

print<<GMDIAGNOSTICSFINISHED;

$gmheadtag
$gmframetop
<FONT COLOR="#0000FF"><B>Diagnostics & Repair Complete</B></FONT>
<P>
All operations were completed successfully.  Greymatter successfully checked and/or performed the following:
<P>
<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0><TR><TD ALIGN=LEFT>$gmfonttag$docreport</FONT></TD></TR></TABLE>
<P>
<FORM ACTION="gm.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}"><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Configuration"> <INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF"></FORM></P><P ALIGN=CENTER><FONT SIZE=1>"Old houses mended, cost little less than new before they're ended."&#151;Colley Cibber</FONT>
$gmframebottom

</BODY>
</HTML>

GMDIAGNOSTICSFINISHED

exit;

}

# ----------------
# add bookmarklets
# ----------------

sub gm_addbookmarklets {

&gm_validate;

if ($gmbookmarkletaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to add bookmarklets without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to use bookmarklets.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readcounter;

if ($newentrynumber eq "0") {
	open (FUNNYFEET, "gm-cplog.cgi") || &gm_dangermouse("Can't read the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
	@cploglines = <FUNNYFEET>;
	close (FUNNYFEET);
	$cplogtext = join (" ", @cploglines);
	unless ($cplogtext =~ /successfully performed diagnostics/) {
		$statusnote = qq(<B><FONT COLOR="#FF0000">Please run "Diagnostics & Repair" in the Configuration screen before adding bookmarklets.</FONT></B><P>);
		&gm_frontpage;
	}
}

if (($IN{'authorname'} eq "Alice") && ($IN{'authorpassword'} eq "wonderland")) {
	$statusnote = qq(<B><FONT COLOR="#FF0000">You can't add bookmarklets under the default account.<BR>Create a new author account for yourself first.</FONT></B><P>);
	&gm_frontpage;
}

$gmbookmarkletline = "@=\"javascript:doc=external.menuArguments.document;lt=escape(doc.selection.createRange().text);loglink=escape(doc.location.href);loglinktitle=escape(doc.title);wingm=window.open('";
$gmbookmarkletline .= $cgiwebpath;
$gmbookmarkletline .= "/gm.cgi?thomas=gmbmpost&authorname=";
$gmbookmarkletline .= $IN{'authorname'};
$gmbookmarkletline .= "&authorpassword=";
$gmbookmarkletline .= $IN{'authorpassword'};
$gmbookmarkletline .= "&logtext='+lt+'&loglink='+loglink+'&loglinktitle='+loglinktitle,'gmwindow','scrollbars=yes,width=660,height=460,left=75,top=75,status=yes,resizable=yes');wingm.focus();\"";

$usethisauthorname = int(rand 999999) + 1;

open (FUNNYFEET, ">$EntriesPath/gmrightclick-$usethisauthorname.reg") || &gm_dangermouse("Can't write to $EntriesPath/gmrightclick.reg.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777, or try running Diagnostics & Repair in the Configuration screen.");
print FUNNYFEET "REGEDIT4\n";
print FUNNYFEET "[HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\MenuExt\\Post To &Greymatter]\n";
print FUNNYFEET "$gmbookmarkletline\n";
print FUNNYFEET "\"contexts\"=hex:31";
close (FUNNYFEET);

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Add Bookmarklets (Internet Explorer 5+ Only)</FONT></B><P>); }

&gm_readconfig;

&gm_writetocplog("$IN{'authorname'} added a bookmarklet");

print<<GMADDBOOKMARKLETS;

$gmheadtag

$gmframetop
$statusnote
<SCRIPT TYPE="text/javascript" LANGUAGE="JavaScript">
<!--
function installrightclickposting() {
	if (confirm("This will update your Windows registry.  Are you sure?")) location.href="$EntriesWebPath/gmrightclick-$usethisauthorname.reg"
}
-->
</SCRIPT>
<P ALIGN=JUSTIFY>
Installing bookmarklets makes for the quickest and most convenient way to "blog" new items, allowing you to post new entries to Greymatter with one mouse-click while surfing anywhere on the web.  After installing a bookmarklet, clicking the new "Post To Greymatter" menu or toolbar button in your browser will load Greymatter in a pop-up window containing a link to the website you're currently visiting all ready to go in your new entry, plus any text from the website that you may have highlighted.  (These bookmarklets are currently only verified to work on Internet Explorer 5 or higher.  Also, since bookmarklets contain your Greymatter name and password, you may wish to be careful about installing these if you share your computer with others.)
</P><P ALIGN=JUSTIFY>
To install the standard bookmarklet, just drag the following link to your browser's menu or toolbar:
</P><P ALIGN=CENTER><CENTER>
<B><A HREF="javascript:lt=document.selection.createRange().text;void(gmwindow=window.open('$cgiwebpath/gm.cgi?thomas=gmbmpost&authorname=$IN{'authorname'}&authorpassword=$IN{'authorpassword'}&logtext='+escape(lt)+'&loglink='+escape(location.href)+'&loglinktitle='+escape(document.title),'gmwindow','scrollbars=yes,width=660,height=460,left=75,top=75,resizable=yes,status=yes'));gmwindow.focus();">Post To Greymatter</A></B>
</CENTER></P><P ALIGN=JUSTIFY>
Even more conveniently, you can also install it to your right-click menu (IE Windows users only).  To do this, click on the link below to update your Windows registry with the new menu option.  After clicking OK, select "Open this file from its current location" to install.
</P><P ALIGN=CENTER><CENTER>
<B><A HREF="javascript:installrightclickposting()">Install Right-Click Menu Access</A></B>
</CENTER></P><P ALIGN=JUSTIFY>
Finally, click Clear And Exit, and shut down Internet Explorer; you should see the new option in your right-click menu once you restart IE.  (Should you wish to uninstall this later, you'll need to edit your Windows registry.  To do this, select "Run..." from the start menu, type in "regedit", expand the directories until you reach "\\HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\MenuExt", right click the "Post To &Greymatter" option, and click Delete.  As always, be careful about editing the registry&#151;you can mess up your computer if you do this wrong.)
</P><P ALIGN=JUSTIFY>
And that's that!  You should now have the bookmarklets installed and working correctly, allowing one-click automatic logging to Greymatter from anywhere on the web.  Enjoy.  =)
</P><P ALIGN=CENTER><CENTER>
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=HIDDEN NAME="usethisauthorname" VALUE="$usethisauthorname">
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Clear And Exit">
</FORM>
<FONT SIZE=1>"We aim above the mark to hit the mark."&#151;R.W. Emerson</FONT>
</CENTER></P>
$gmframebottom

</BODY>
</HTML>

GMADDBOOKMARKLETS

exit;

}

# ------------
# upload files
# ------------

sub gm_uploadfiles {

&gm_validate;

if ($gmuploadaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to upload files without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to upload files.</FONT></B><P>);
	&gm_frontpage;
}

&gm_readcounter;

if ($newentrynumber eq "0") {
	open (FUNNYFEET, "gm-cplog.cgi") || &gm_dangermouse("Can't read the control panel log.  Please make sure that gm-cplog.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files; also try running Diagnostics & Repair from the Configuration screen.");
	@cploglines = <FUNNYFEET>;
	close (FUNNYFEET);
	$cplogtext = join (" ", @cploglines);
	unless ($cplogtext =~ /successfully performed diagnostics/) {
		$statusnote = qq(<B><FONT COLOR="#FF0000">Please run "Diagnostics & Repair" in the Configuration screen before uploading files.</FONT></B><P>);
		&gm_frontpage;
	}
}

if ($uploadfilesallowed ne "") {
	$howmanyfiletypes = 0;
	@uploadfiletypesallowed = split (/;/, $uploadfilesallowed);
	foreach $thisfiletype (@uploadfiletypesallowed) {
		$allowthesefiletypes .= ".$thisfiletype, ";
	}
	$allowthesefiletypes =~ s/, .(\w+), $/ and .$1/;
	$allowthesefiletypes =~ s/, $//;
}

if (($uploadfilesallowed ne "") && ($uploadfilesizelimit ne "0")) {
	$specialuploadtext = "Only $allowthesefiletypes files may currently be uploaded,<BR>and no file larger than $uploadfilesizelimit\k may be uploaded.<P>";
} elsif ($uploadfilesallowed ne "") {
	$specialuploadtext = "Only $allowthesefiletypes files may currently be uploaded.<P>";
} elsif ($uploadfilesizelimit ne "0") {
	$specialuploadtext = "No file larger than $uploadfilesizelimit\k may currently be uploaded.<P>";
} else {
	$specialuploadtext = "";
}

if ($statusnote eq "") { $statusnote = qq(<B><FONT COLOR="#000000">Upload Files</FONT></B><P>Use the prompt below to browse your computer for a file to upload directly to your account.<BR>(If you don't see the prompt, then your browser doesn't support this feature.)  All files<BR>will be uploaded to your entries/archives directory; after uploading, you can then have<BR>a link to download the file or display the image in a new entry if you wish.<P>$specialuploadtext); }

&gm_readconfig;

$insertauthorname = $IN{'authorname'};
$insertauthorpassword = $IN{'authorpassword'};

print<<GMUPLOADFILES;

$gmheadtag

$gmframetop
$statusnote
<SCRIPT TYPE="text/javascript" LANGUAGE="JavaScript1.2">
<!--//
document.write('<FORM ENCTYPE="multipart/form-data" ACTION="gm-upload.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$insertauthorname"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$insertauthorpassword"><INPUT TYPE=FILE CLASS="textinput" NAME="uploadfile-01" SIZE="40"><P><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Upload This File"></FORM><P>');
//-->
</SCRIPT>
<FORM ACTION="gm.cgi" METHOD=POST>
<INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}">
<INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}">
<INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF">
</FORM>
<FONT SIZE=1>"Our life is composed greatly from dreams, from the unconscious, and they must be brought<BR>into connection with action. They must be woven together."&#151;Anaïs Nin</FONT>
$gmframebottom
</BODY>
</HTML>

GMUPLOADFILES

exit;

}

# ----------------
# version checking
# ----------------

sub gm_versioncheck {

if ($versionsetup ne $gmversion) {

print<<GMVERSIONCHECKTOP;

$gmheadtag
$gmframetop

GMVERSIONCHECKTOP

if ($versionsetup eq "one point zero") {
	print qq(Greymatter has detected that you are upgrading from version 1.0.  Some of your files will need to be updated now.  After Greymatter is done updating, you might want to review your configuration and customize the templates; many new templates are included which could affect your site.<P><B>Important notes:</B> If you have an index page in your archives directory, Greymatter will, by default, overwrite it with its new archive index, so you may want to <B>make a backup of that file</B> first; you'll also need to make sure that file is CHMODed to 666, or simply delete that file instead.  There is also a new gm-upload.cgi file that you'll have to upload with your other Greymatter CGI files and CHMOD to 755, if you haven't already.<P><FORM ACTION="gm.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}"><INPUT TYPE=HIDDEN NAME="oldsetupversion" VALUE="$versionsetup"><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Update Now"></FORM><P><FONT SIZE=1>"We must always change, renew, rejuvenate ourselves."&#151;Goethe</FONT>);
} elsif ($versionsetup eq "1.1") {
	print qq(Greymatter has detected that you are upgrading from version 1.1.  Some of your files will need to be updated now.  After Greymatter is done updating, you might want to review the new configuration and template options; it's also <I>strongly recommended</I> that you "Rebuild Everything" right after it finishes updating.  Finally, be sure to upload the new gm-upload.cgi with your other Greymatter CGI files and CHMOD it to 755, if you haven't already.<P><FORM ACTION="gm.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}"><INPUT TYPE=HIDDEN NAME="oldsetupversion" VALUE="$versionsetup"><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Update Now"></FORM><P><FONT SIZE=1>"We must always change, renew, rejuvenate ourselves."&#151;Goethe</FONT>);
} elsif ($versionsetup eq "1.2") {
	print qq(Greymatter has detected that you are upgrading from version 1.2.  This is a minor upgrade release and no changes will be made to your files.<P><FORM ACTION="gm.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}"><INPUT TYPE=HIDDEN NAME="oldsetupversion" VALUE="$versionsetup"><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Update Now"></FORM><P><FONT SIZE=1>"We must always change, renew, rejuvenate ourselves."&#151;Goethe</FONT>);
} elsif ($versionsetup eq "1.21") {
	print qq(Greymatter has detected that you are upgrading from version 1.21.  This is a minor upgrade release and no changes will be made to your files.<P><FORM ACTION="gm.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}"><INPUT TYPE=HIDDEN NAME="oldsetupversion" VALUE="$versionsetup"><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Update Now"></FORM><P><FONT SIZE=1>"We must always change, renew, rejuvenate ourselves."&#151;Goethe</FONT>);
} elsif ($versionsetup eq "1.21a") {
	print qq(Greymatter has detected that you are upgrading from version 1.21a.  This is a minor upgrade release and no changes will be made to your files.<P><FORM ACTION="gm.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}"><INPUT TYPE=HIDDEN NAME="oldsetupversion" VALUE="$versionsetup"><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" STYLE="background: #D0FFD0" VALUE="Update Now"></FORM><P><FONT SIZE=1>"We must always change, renew, rejuvenate ourselves."&#151;Goethe</FONT>);
} else {
	print qq(<B>ERROR:</B> Greymatter could not determine the version setup.  Please make sure that Greymatter is installed correctly.  Try reuploading the gm-config.cgi file that came with Greymatter and try logging in again; you'll need to reconfigure your Configuration settings.);
}

print<<GMVERSIONCHECKBOTTOM;

$gmframebottom

</BODY>
</HTML>

GMVERSIONCHECKBOTTOM

exit;

}

}

# -----------------
# version upgrading
# -----------------

sub gm_versionupgrading {

if ($IN{'oldsetupversion'} eq "one point zero") {
	open (FUNNYFEET, "gm-entrylist.cgi") || &gm_dangermouse("Can't read the entrylist file.  Please make sure that gm-entrylist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	@tempnewentrylist = <FUNNYFEET>;
	close (FUNNYFEET);
	open (FUNNYFEETWO, ">gm-entrylist.cgi") || &gm_dangermouse("Can't write to the entrylist file.  Please make sure that gm-entrylist.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	foreach $tempnewentrylistline (@tempnewentrylist) {
		chomp ($tempnewentrylistline);
		($templistnumber, $templistauthorname, $templistsubject, $templistdate, $templisttime, $templistopenstatus) = split (/\|/, $tempnewentrylistline);
		$templistopenstatus = "O";
		if ($templistopenstatus eq "closed") { $templistopenstatus = "C"; }
		$templistmorestatus = "N";
		&gm_getentryvariables($templistnumber);
		if ($thisentrymorebody ne "") { $templistmorestatus = "Y"; }
		print FUNNYFEETWO "$templistnumber|$templistauthorname|$templistsubject|$templistdate|$templisttime|$templistopenstatus|$templistmorestatus\n";
	}
	close (FUNNYFEETWO);
	&gm_readtemplates;
	$gmentrytemplate =~ s/\n/\|\*\|/g;
	$gmentrypagetemplate =~ s/\n/\|\*\|/g;
	$gmarchiveentrypagetemplate =~ s/\n/\|\*\|/g;
	$gmarchiveentrytemplate =~ s/\n/\|\*\|/g;
	$gmdatetemplate =~ s/\n/\|\*\|/g;
	open (FUNNYFEETHREE, ">>gm-templates.cgi");
	print FUNNYFEETHREE "$gmentrytemplate\n";
	print FUNNYFEETHREE "$gmentrypagetemplate\n";
	print FUNNYFEETHREE "$gmarchiveentrypagetemplate\n";
	print FUNNYFEETHREE qq([{{pagepreviouslink}}Previous entry: "{{previousentrysubject}}"</A>]\n);
	print FUNNYFEETHREE qq([{{pagenextlink}}Next entry: "{{nextentrysubject}}"</A>]\n);
	print FUNNYFEETHREE qq([{{pagemorepreviouslink}}Previous extended entry: "{{previousmoreentrysubject}}"</A>]\n);
	print FUNNYFEETHREE qq([{{pagemorenextlink}}Next extended entry: "{{nextmoreentrysubject}}"</A>]\n);
	print FUNNYFEETHREE qq(<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">|*|<HTML>|*|<HEAD>|*|<TITLE>My Archives</TITLE>|*|<META NAME="Generator" CONTENT="Greymatter 1.1">|*|</HEAD>|*||*|<BODY BGCOLOR="#FFFFFF">|*||*|<P ALIGN=CENTER>|*|{{header}}|*|</P><P ALIGN=CENTER>|*|<FONT SIZE=4><B>My Archives</B></FONT>|*|</P>|*||*|<P ALIGN=CENTER>|*|<B>Log Archives</B>|*|</P><P ALIGN=CENTER>|*|{{logarchivelist}}|*|</P><P ALIGN=CENTER>|*|<B>Entries</B>|*|</P><P ALIGN=CENTER>|*|{{logentrylist}}|*|</P>|*||*|<P ALIGN=CENTER>|*|[{{pageindexlink}}Main Index</A>]|*|</P><P ALIGN=CENTER>|*|{{gmicon}}|*|</P><P ALIGN=CENTER>|*|{{footer}}|*|</P>|*||*|</BODY>|*|</HTML>\n);
	print FUNNYFEETHREE qq({{pagearchivelogindexlink}}Log Archives: {{monthword}} {{yearyear}}</A>\n);
	print FUNNYFEETHREE qq({{pagelink}}{{monthmonth}}/{{dayday}}/{{yearyear}}: {{entrysubject}}</A>\n);
	print FUNNYFEETHREE qq(<B>{{pagelink}}{{monthmonth}}/{{dayday}}/{{yearyear}}: {{entrysubject}}</A></B>\n);
	print FUNNYFEETHREE qq( / \n);
	print FUNNYFEETHREE qq(<BR>\n);
	print FUNNYFEETHREE "<P>\n";
	print FUNNYFEETHREE "<BR>\n";
	print FUNNYFEETHREE "<P>\n";
	print FUNNYFEETHREE "\n";
	print FUNNYFEETHREE "\n";
	print FUNNYFEETHREE "\n";
	print FUNNYFEETHREE qq( onMouseOver="window.status='{{monthmonth}}/{{dayday}}/{{yearyear}}: {{entrysubject}}';return true" onMouseOut="window.status='';return true"\n);
	print FUNNYFEETHREE "\n";
	print FUNNYFEETHREE "\n";
	print FUNNYFEETHREE "$gmarchiveentrytemplate\n";
	print FUNNYFEETHREE "$gmdatetemplate\n";
	close (FUNNYFEETHREE);
	open (FUNNYFEETFOUR, ">>gm-config.cgi");
	print FUNNYFEETFOUR "yes\n";
	print FUNNYFEETFOUR "ascending\n";
	print FUNNYFEETFOUR "both\n";
	print FUNNYFEETFOUR "10\n";
	close (FUNNYFEETFOUR);
	&gm_readconfig;
	$versionsetup = $gmversion;
	&gm_writeconfig;
}

if (($IN{'oldsetupversion'} eq "one point zero") || ($IN{'oldsetupversion'} eq "1.1")) {
	&gm_readtemplates;
	open (LAUGHINGFEET, "gm-templates.cgi") || &gm_dangermouse("Can't read the templates file.  Please make sure that gm-templates.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	@gmtemplateline = <LAUGHINGFEET>;
	close (LAUGHINGFEET);
	open (LAUGHINGFEETONE, ">gm-templates.cgi") || &gm_dangermouse("Can't write to the templates file.  Please make sure that gm-templates.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	foreach $thistemplateline (@gmtemplateline) {
		chomp ($thistemplateline);
		unless ($thistemplateline eq "") {
			$authoremaillinkreplacement = qq(<A HREF="mailto:{{authoremail}}">);
			$authorhomepagelinkreplacement = qq(<A HREF="mailto:{{authorhomepage}}">);
			$commentauthoremaillinkreplacement = qq(<A HREF="mailto:{{commentauthoremailabsolute}}">);
			$commentauthorhomepagelinkreplacement = qq(<A HREF="mailto:{{commentauthorhomepageabsolute}}">);
			$commentspostlinkreplacement = qq(<A HREF="{{commentspostlink}}"$gmcustomlinktemplate>);
			$pagelinkreplacement = qq(<A HREF="{{pagelink}}"$gmcustomlinktemplate>);
			$pageindexlinkreplacement = qq(<A HREF="{{pageindexlink}}">);
			$pagearchiveindexlinkreplacement = qq(<A HREF="{{pagearchiveindexlink}}">);
			$pagearchivelogindexlinkreplacement = qq(<A HREF="{{pagearchivelogindexlink}}">);
			$pagenextlinkreplacement = qq(<A HREF="{{nextpagelink}}" onMouseOver="window.status='{{nextmonthmonth}}/{{nextdayday}}/{{nextyear}}: {{nextentrysubject}}';return true" onMouseOut="window.status='';return true">);
			$pagenextmorelinkreplacement = qq(<A HREF="{{nextmorepagelink}}" onMouseOver="window.status='{{nextmoremonthmonth}}/{{nextmoredayday}}/{{nextmoreyear}}: {{nextmoreentrysubject}}';return true" onMouseOut="window.status='';return true">);
			$pagepreviouslinkreplacement = qq(<A HREF="{{previouspagelink}}" onMouseOver="window.status='{{previousmonthmonth}}/{{previousdayday}}/{{previousyear}}: {{previousentrysubject}}';return true" onMouseOut="window.status='';return true">);
			$pagepreviousmorelinkreplacement = qq(<A HREF="{{previousmorepagelink}}" onMouseOver="window.status='{{previousmoremonthmonth}}/{{previousmoredayday}}/{{previousmoreyear}}: {{previousmoreentrysubject}}';return true" onMouseOut="window.status='';return true">);
			$pagesmartindexlinkreplacement = qq(<A HREF="{{pagesmartindexlink}}">);
			$pagepositivekarmalinkreplacement = qq(<A HREF="{{positivekarmalink}}" onMouseOver="window.status='Cast a positive vote on this entry';return true" onMouseOut="window.status='';return true">);
			$pagenegativekarmalinkreplacement = qq(<A HREF="{{negativekarmalink}}" onMouseOver="window.status='Cast a negative vote on this entry';return true" onMouseOut="window.status='';return true">);
			$thistemplateline =~ s/{{authoremaillink}}/$authoremaillinkreplacement/ig;
			$thistemplateline =~ s/{{authorhomepagelink}}/$authorhomepagelinkreplacement/ig;
			$thistemplateline =~ s/{{commentauthoremaillink}}/$commentauthoremaillinkreplacement/ig;
			$thistemplateline =~ s/{{commentauthorhomepagelink}}/$commentauthorhomepagelinkreplacement/ig;
			$thistemplateline =~ s/{{commentspostlink}}/$commentspostlinkreplacement/ig;
			$thistemplateline =~ s/{{pagelink}}/$pagelinkreplacement/ig;
			$thistemplateline =~ s/{{pageindexlink}}/$pageindexlinkreplacement/ig;
			$thistemplateline =~ s/{{pagearchiveindexlink}}/$pagearchiveindexlinkreplacement/ig;
			$thistemplateline =~ s/{{pagearchivelogindexlink}}/$pagearchivelogindexlinkreplacement/ig;
			$thistemplateline =~ s/{{pagenextlink}}/$pagenextlinkreplacement/ig;
			$thistemplateline =~ s/{{pagenextmorelink}}/$pagenextmorelinkreplacement/ig;
			$thistemplateline =~ s/{{pagepreviouslink}}/$pagepreviouslinkreplacement/ig;
			$thistemplateline =~ s/{{pagepreviousmorelink}}/$pagepreviousmorelinkreplacement/ig;
			$thistemplateline =~ s/{{pagemorepreviouslink}}/$pagepreviousmorelinkreplacement/ig;
			$thistemplateline =~ s/{{pagemorenextlink}}/$pagepreviousmorelinkreplacement/ig;
			$thistemplateline =~ s/{{pagesmartindexlink}}/$pagesmartindexlinkreplacement/ig;
			$thistemplateline =~ s/{{positivekarmalink}}/$pagepositivekarmalinkreplacement/ig;
			$thistemplateline =~ s/{{negativekarmalink}}/$pagenegativekarmalinkreplacement/ig;
		}
		print LAUGHINGFEETONE "$thistemplateline\n";
	}
	close (LAUGHINGFEETONE);
	&gm_readtemplates;
	$gmindextemplate = &relouse($gmindextemplate);
	$gmentrypagetemplate = &relouse($gmentrypagetemplate);
	$gmarchiveindextemplate = &relouse($gmarchiveindextemplate);
	$gmarchiveentrypagetemplate = &relouse($gmarchiveentrypagetemplate);
	$gmentrytemplate = &relouse($gmentrytemplate);
	$gmarchiveentrytemplate = &relouse($gmarchiveentrytemplate);
	$gmstayattoptemplate = &relouse($gmstayattoptemplate);
	$gmdatetemplate = &relouse($gmdatetemplate);
	$gmcommentstemplate = &relouse($gmcommentstemplate);
	$gmcommentsformtemplate = &relouse($gmcommentsformtemplate);
	$gmparaseparationtemplate = &relouse($gmparaseparationtemplate);
	$gmkarmaformtemplate = &relouse($gmkarmaformtemplate);
	$gmmoreprefacetemplate = &relouse($gmmoreprefacetemplate);
	$gmmorelinktemplate = &relouse($gmmorelinktemplate);
	$gmkarmalinktemplate = &relouse($gmkarmalinktemplate);
	$gmcommentslinktemplate = &relouse($gmcommentslinktemplate);
	$gmcommentauthoremailtemplate = &relouse($gmcommentauthoremailtemplate);
	$gmcommentauthorhomepagetemplate = &relouse($gmcommentauthorhomepagetemplate);
	$gmcommentdividertemplate = &relouse($gmcommentdividertemplate);
	$gmmoreentrytemplate = &relouse($gmmoreentrytemplate);
	$gmmoreentrypagetemplate = &relouse($gmmoreentrypagetemplate);
	$gmmorearchiveentrypagetemplate = &relouse($gmmorearchiveentrypagetemplate);
	$gmpreviouslinktemplate = &relouse($gmpreviouslinktemplate);
	$gmnextlinktemplate = &relouse($gmnextlinktemplate);
	$gmpreviousmorelinktemplate = &relouse($gmpreviousmorelinktemplate);
	$gmnextmorelinktemplate = &relouse($gmnextmorelinktemplate);
	$gmarchivemasterindextemplate = &relouse($gmarchivemasterindextemplate);
	$gmlogarchiveslinktemplate = &relouse($gmlogarchiveslinktemplate);
	$gmentrypagelinktemplate = &relouse($gmentrypagelinktemplate);
	$gmmoreentrypagelinktemplate = &relouse($gmmoreentrypagelinktemplate);
	$gmlogarchiveslinkseparatortemplate = &relouse($gmlogarchiveslinkseparatortemplate);
	$gmentrypagelinkseparatortemplate = &relouse($gmentrypagelinkseparatortemplate);
	$gmentrypagelinkmonthseparatortemplate = "";
	$gmentrypagelinkdayseparatortemplate = "";
	$gmentrypagelinkyearseparatortemplate = "";
	$gmheadertemplate = &relouse($gmheadertemplate);
	$gmfootertemplate = &relouse($gmfootertemplate);
	$gmsidebartemplate = &relouse($gmsidebartemplate);
	$gmcustomlinktemplate = "";
	$gmentryseparatortemplate = &relouse($gmentryseparatortemplate);
	$gmarchiveentryseparatortemplate = &relouse($gmarchiveentryseparatortemplate);
	$gmmorearchiveentrytemplate = &relouse($gmmorearchiveentrytemplate);
	$gmdatearchivetemplate = &relouse($gmdatearchivetemplate);
	open (LAUGHINGFEETTWO, ">gm-templates.cgi") || &gm_dangermouse("Can't write to the templates file.  Please make sure that gm-templates.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	print LAUGHINGFEETTWO "$gmindextemplate\n";
	print LAUGHINGFEETTWO "$gmentrypagetemplate\n";
	print LAUGHINGFEETTWO "$gmarchiveindextemplate\n";
	print LAUGHINGFEETTWO "$gmarchiveentrypagetemplate\n";
	print LAUGHINGFEETTWO "$gmentrytemplate\n";
	print LAUGHINGFEETTWO "$gmarchiveentrytemplate\n";
	print LAUGHINGFEETTWO "$gmstayattoptemplate\n";
	print LAUGHINGFEETTWO "$gmdatetemplate\n";
	print LAUGHINGFEETTWO "$gmcommentstemplate\n";
	print LAUGHINGFEETTWO "$gmcommentsformtemplate\n";
	print LAUGHINGFEETTWO "$gmparaseparationtemplate\n";
	print LAUGHINGFEETTWO "$gmkarmaformtemplate\n";
	print LAUGHINGFEETTWO "$gmmoreprefacetemplate\n";
	print LAUGHINGFEETTWO "$gmmorelinktemplate\n";
	print LAUGHINGFEETTWO "$gmkarmalinktemplate\n";
	print LAUGHINGFEETTWO "$gmcommentslinktemplate\n";
	print LAUGHINGFEETTWO "$gmcommentauthoremailtemplate\n";
	print LAUGHINGFEETTWO "$gmcommentauthorhomepagetemplate\n";
	print LAUGHINGFEETTWO "$gmcommentdividertemplate\n";
	print LAUGHINGFEETTWO "$gmmoreentrytemplate\n";
	print LAUGHINGFEETTWO "$gmmoreentrypagetemplate\n";
	print LAUGHINGFEETTWO "$gmmorearchiveentrypagetemplate\n";
	print LAUGHINGFEETTWO "$gmpreviouslinktemplate\n";
	print LAUGHINGFEETTWO "$gmnextlinktemplate\n";
	print LAUGHINGFEETTWO "$gmpreviousmorelinktemplate\n";
	print LAUGHINGFEETTWO "$gmnextmorelinktemplate\n";
	print LAUGHINGFEETTWO "$gmarchivemasterindextemplate\n";
	print LAUGHINGFEETTWO "$gmlogarchiveslinktemplate\n";
	print LAUGHINGFEETTWO "$gmentrypagelinktemplate\n";
	print LAUGHINGFEETTWO "$gmmoreentrypagelinktemplate\n";
	print LAUGHINGFEETTWO "$gmlogarchiveslinkseparatortemplate\n";
	print LAUGHINGFEETTWO "$gmentrypagelinkseparatortemplate\n";
	print LAUGHINGFEETTWO "\n";
	print LAUGHINGFEETTWO "\n";
	print LAUGHINGFEETTWO "\n";
	print LAUGHINGFEETTWO "$gmheadertemplate\n";
	print LAUGHINGFEETTWO "$gmfootertemplate\n";
	print LAUGHINGFEETTWO "$gmsidebartemplate\n";
	print LAUGHINGFEETTWO "\n";
	print LAUGHINGFEETTWO "$gmentryseparatortemplate\n";
	print LAUGHINGFEETTWO "$gmarchiveentryseparatortemplate\n";
	print LAUGHINGFEETTWO "$gmmorearchiveentrytemplate\n";
	print LAUGHINGFEETTWO "$gmdatearchivetemplate\n";
	print LAUGHINGFEETTWO qq(<A HREF="{{pagearchivelogindexlink}}">{{weekbeginningmonthmonth}}/{{weekbeginningdayday}}/{{weekbeginningyearyear}} to {{weekendingmonthmonth}}/{{weekendingdayday}}/{{weekendingyearyear}}</A>\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq(<HTML>|*|<HEAD>|*|<TITLE>{{monthmonth}}/{{dayday}}/{{year}}: {{popuptitle}}</TITLE>|*|<META NAME="Generator" CONTENT="Greymatter {{gmversion}}">|*|</HEAD>|*||*|<BODY BGCOLOR="#000000" TOPMARGIN=0 LEFTMARGIN=0 MARGINHEIGHT=0 MARGINWIDTH=0 onBlur="window.close\(\)">|*||*|<IMG BORDER=0 SRC="{{entrieswebpath}}/{{popupfile}}" ALT="{{popuptitle}}" HEIGHT={{popupheight}} WIDTH={{popupwidth}}>|*||*|</BODY>|*|</HTML>\n);
	print LAUGHINGFEETTWO qq(<A HREF="#" onMouseOver="window.status='{{monthmonth}}/{{dayday}}/{{year}}: {{popuptitle}} \(opens popup window\)';return true" onMouseOut="window.status='';return true" onClick="window.open\('{{entrieswebpath}}/{{popuphtmlfile}}','{{randomnumber 1111-9999}}','width={{popupwidth}},height={{popupheight}},directories=no,location=no,menubar=no,scrollbars=no,status=no,toolbar=no,resizable=no,left=0,top=0,screenx=50,screeny=50'\);return false">\n);
	print LAUGHINGFEETTWO qq(<FORM ACTION="{{cgiwebpath}}/gm-comments.cgi" METHOD=POST><INPUT TYPE=TEXT NAME="gmsearch" SIZE=20> <INPUT TYPE=SUBMIT VALUE="Search"></FORM>\n);
	print LAUGHINGFEETTWO qq(<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">|*|<HTML>|*|<HEAD>|*|<TITLE>Search Results</TITLE>|*|<META NAME="Generator" CONTENT="Greymatter {{gmversion}}">|*|</HEAD>|*||*|<BODY BGCOLOR="#FFFFFF">|*||*|<P ALIGN=CENTER>|*|<B>Search results for "{{searchterm}}" \({{searchmatches}} matches\)</B>|*|</P>|*||*|{{searchresults}}|*||*|<P ALIGN=CENTER>|*|[<A HREF="{{pageindexlink}}">Return To Main Index</A>]|*|</P><P ALIGN=CENTER>|*|{{gmicon}}|*|</P>|*||*|</BODY>|*|</HTML>\n);
	print LAUGHINGFEETTWO qq(<P ALIGN=JUSTIFY><BLOCKQUOTE>|*|<A HREF="{{pagelink}}">{{monthmonth}}/{{dayday}}/{{yearyear}}: {{entrysubject}}</A>|*|<P ALIGN=JUSTIFY><BLOCKQUOTE><I>|*|{{entrymainbodyfirstwords 10}}...|*|</I></BLOCKQUOTE></P>|*|</BLOCKQUOTE></P>\n);
	print LAUGHINGFEETTWO qq(<TABLE BORDER=2 CELLPADDING=5 CELLSPACING=0><TR><TD ALIGN=CENTER COLSPAN=7>{{monthword}} {{yearyear}}</TD></TR><TR><TD ALIGN=CENTER>S</TD><TD ALIGN=CENTER>M</TD><TD ALIGN=CENTER>T</TD><TD ALIGN=CENTER>W</TD><TD ALIGN=CENTER>T</TD><TD ALIGN=CENTER>F</TD><TD ALIGN=CENTER>S</TD></TR>\n);
	print LAUGHINGFEETTWO qq(</TABLE>\n);
	print LAUGHINGFEETTWO qq(<TD ALIGN=CENTER>&#160;</TD>\n);
	print LAUGHINGFEETTWO qq(<TD ALIGN=CENTER>{{day}}</TD>\n);
	print LAUGHINGFEETTWO qq(<TD ALIGN=CENTER><A HREF="{{pagelink}}">{{day}}</A></TD>\n);
	print LAUGHINGFEETTWO qq(\n);
	print LAUGHINGFEETTWO qq( [{{day}}] \n);
	print LAUGHINGFEETTWO qq( [<A HREF="{{pagelink}}">{{day}}</A>] \n);
	print LAUGHINGFEETTWO qq(<A NAME="comments">|*||*|<P ALIGN=CENTER>|*|<B>Previewing Your Comment</B>|*|</P>|*|\n);
	print LAUGHINGFEETTWO qq(<P ALIGN=CENTER>|*|A preview of your new comment is shown above as it will appear on this page.  Click "Post This Comment" below to post it, or click the back button on your browser to re-edit it.|*|</P><P ALIGN=CENTER><CENTER>|*|<FORM ACTION="{{cgiwebpath}}/gm-comments.cgi" METHOD=POST>|*|<INPUT TYPE=HIDDEN NAME="newcommententrynumber" VALUE="{{entrynumber}}">|*|<INPUT TYPE=HIDDEN NAME="newcommentauthor" VALUE="{{previewcommentauthor}}">|*|<INPUT TYPE=HIDDEN NAME="newcommentemail" VALUE="{{previewcommentemail}}">|*|<INPUT TYPE=HIDDEN NAME="newcommenthomepage" VALUE="{{previewcommenthomepage}}">|*|<INPUT TYPE=HIDDEN NAME="newcommentbody" VALUE="{{previewcommentbody}}">|*|<INPUT TYPE=SUBMIT VALUE="Post This Comment">|*|</FORM>|*|</CENTER></P>\n);
	print LAUGHINGFEETTWO qq(No Comments\n);
	print LAUGHINGFEETTWO qq(1 Comment\n);
	print LAUGHINGFEETTWO qq({{commentsnumber}} comments\n);
	print LAUGHINGFEETTWO qq(<BR>\n);
	close (LAUGHINGFEETTWO);
	&gm_readconfig;
	$versionsetup = $gmversion;
	$cookiesallowed = "yes";
	$logarchivesuffix = $entrysuffix;
	$censorlist = "";
	$censorenabled = "neither";
	$keepmonthlyarchives = "yes";
	$defaultentrylistview = "main";
	$linktocalendarentries = "all";
	$automaticrebuilddefault = "yes";
	$commententrylistonlyifokay = "yes";
	$otherfilelist = "";
	$otherfilelistentryrebuild = "no";
	$archiveformat = "month";
	$inlineformatting = "entries";
	$uploadfilesallowed = "";
	$uploadfilesizelimit = "0";
	&gm_writeconfig;
	open (LAUGHINGFEETTHREE, "gm-authors.cgi") || &gm_dangermouse("Can't read the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	@gmauthorupgradedata = <LAUGHINGFEETTHREE>;
	close (LAUGHINGFEETTHREE);
	open (LAUGHINGFEETFOUR, ">gm-authors.cgi") || &gm_dangermouse("Can't write to the authors file.  Please make sure that gm-authors.cgi is CHMODed to 666 and is in the same place as all your other Greymatter CGI files.");
	foreach $thisupgradeauthorline (@gmauthorupgradedata) {
		chomp ($thisupgradeauthorline);
		unless ($thisupgradeauthorline eq "") {
			($thisupgradeauthorname, $thisupgradeauthorpassword, $thisupgradeauthoremail, $thisupgradeauthorhomepage, $thisupgradeauthordate, $thisupgradeauthorposts, $thisupgradeauthorentryaccess, $thisupgradeauthorentryeditaccess, $thisupgradeauthorconfigurationaccess, $thisupgradeauthortemplateaccess, $thisupgradeauthorauthoraccess, $thisupgradeauthorrebuildaccess, $thisupgradeauthorcplogaccess) = split (/\|/, $thisupgradeauthorline);
			$thisupgradeauthorbookmarkletaccess = "N";
			$thusupgradeauthoruploadaccess = "N";
			$thisupgradeauthorloginaccess = "Y";
			if ($thisupgradeauthorentryaccess eq "Y") { $thisupgradeauthorbookmarkletaccess = "Y"; }
			if ($thisupgradeauthorconfigurationaccess eq "Y") { $thisupgradeauthoruploadaccess = "Y"; }
			print LAUGHINGFEETFOUR "$thisupgradeauthorname|$thisupgradeauthorpassword|$thisupgradeauthoremail|$thisupgradeauthorhomepage|$thisupgradeauthordate|$thisupgradeauthorposts|$thisupgradeauthorentryaccess|$thisupgradeauthorentryeditaccess|$thisupgradeauthorconfigurationaccess|$thisupgradeauthortemplateaccess|$thisupgradeauthorauthoraccess|$thisupgradeauthorrebuildaccess|$thisupgradeauthorcplogaccess|$thisupgradeauthorbookmarkletaccess|$thisupgradeauthoruploadaccess|$thisupgradeauthorloginaccess\n";
		}
	}
	close (LAUGHINGFEETFOUR);
}

&gm_readconfig;
$versionsetup = $gmversion;
&gm_writeconfig;

&gm_writetocplog("<B><FONT COLOR=\"#0000FF\">$IN{'authorname'} upgraded Greymatter from an older version ($IN{'oldsetupversion'}) to a newer version ($gmversion)</FONT></B>");

$statusnote = qq(<B><FONT COLOR="#0000FF">Upgrade complete!  Welcome back, $IN{'authorname'}.</FONT></B><P>);

&gm_frontpage;

}

# ----------------------
# rebuild update process
# ----------------------

sub gm_rebuildupdate {

&gm_validate;

if ($gmrebuildaccess ne "yes") {
	&gm_writetocplog("$IN{'authorname'} attempted to rebuild files without authorization");
	$statusnote = qq(<B><FONT COLOR="#FF0000">You don't have access to rebuild files.</FONT></B><P>);
	&gm_frontpage;
}

$usethisauthorname = $IN{'authorname'};
$usethisauthorpassword = $IN{'authorpassword'};
$usethisauthorname =~ s/ /\+/g;
$usethisauthorpassword =~ s/ /\+/g;

$nowrebuild = "";
$whatimdoing = "Error";

&gm_readconfig;
&gm_readcounter;
&gm_readtemplates;

if ($IN{'rebuildfrom'} eq "index") {

	&gm_generatemainindex;
	$whatimdoing = "Rebuilt main index.  Now rebuilding log archives...";
	$nowrebuild = "logarchives";

} elsif ($IN{'rebuildfrom'} eq "logarchives") {

	if (($newarchivenumber ne "0") || ($concurrentmainandarchives eq "yes")) {
		if ($keepmonthlyarchives ne "no") {
			if ($concurrentmainandarchives eq "yes") { $newarchivenumber = $newentrynumber; }
			$stoppednumber = $newarchivenumber;
			do { &gm_generatearchive($stoppednumber); } until $stoppednumber <= 1;
			&gm_readcounter;
		}
	}
	$whatimdoing = "Rebuilt log archives.  Now rebuilding archive master index...";
	$nowrebuild = "masterindex";

} elsif ($IN{'rebuildfrom'} eq "masterindex") {

	if (($keeparchivemasterindex eq "yes") && ($newentrynumber ne "0")) {
		if ($newarchivenumber ne "0") {
			&gm_getentryvariables($newarchivenumber);
		} else {
			&gm_getentryvariables($newentrynumber);
		}
		&gm_formatentry($gmarchivemasterindextemplate);
		open (THISARCHIVEFILE, ">$EntriesPath/$indexfilename") || &gm_dangermouse("Can't write to $EntriesPath/$indexfilename.  Please make sure your paths are configured correctly, that the entries/archives directory is CHMODed to 777, and that $EntriesPath/$indexfilename is CHMODed to 666; also try running Diagnostics & Repair from the Configuration screen.");
		print THISARCHIVEFILE $entryreturn;
		close (THISARCHIVEFILE);
		chmod (0666, "$EntriesPath/$indexfilename");
	}
	if ($otherfilelist ne "") {
		$whatimdoing = "Rebuilt archive master index.  Now rebuilding connected files...";
		$nowrebuild = "connected";
	} else {
		$whatimdoing = "Rebuilt archive master index.  Now rebuilding entry files...";
		$nowrebuild = "1";
	}

} elsif ($IN{'rebuildfrom'} eq "connected") {

	if ($otherfilelist ne "") {
		&gm_rebuildconnectedfiles;
		if ($connectedfilesdone eq "yes") {
			$whatimdoing = "Rebuilt connected files.  Now rebuilding entry files...";
			$nowrebuild = "1";
			if (($IN{'rebuilding'} eq "connected") || ($IN{'rebuilding'} eq "connectedaftersave")) {
				$nowrebuild = "done";
			}
		} else {
			$connectpercentdone = int( ($IN{'connectednumber'} / $#connectedfilelist) * 100 );
			$whatimdoing = "Rebuilding connected files ($connectpercentdone% done)...";
			$nowrebuild = "connected";
		}
	} else {
		$whatimdoing = "Now rebuilding entry files...";
		$nowrebuild = "1";
	}

} else {

	unless (($IN{'rebuilding'} eq "connected") || ($IN{'rebuilding'} eq "connectedaftersave")) {
	if (($generateentrypages eq "yes") && ($newentrynumber ne "0")) {
		$currentcount = $IN{'rebuildfrom'};
		$counttohere = $currentcount + 19;
		if ($IN{'rebuildfrom'} eq "archivefiles") {
			if ($counttohere > $newarchivenumber) { $counttohere = $newarchivenumber; }
		} else {
			if ($counttohere > $newentrynumber) { $counttohere = $newentrynumber; }
		}
		do {
			&gm_getentryvariables($currentcount);
			if ($thisentryopenstatus eq "open") {
				if ($currentcount <= $newarchivenumber) {
					if ($thisentrymorebody ne "") {
						&gm_formatentry($gmmorearchiveentrypagetemplate);
					} else {
						&gm_formatentry($gmarchiveentrypagetemplate);
					}
				} else {
					if ($thisentrymorebody ne "") {
						&gm_formatentry($gmmoreentrypagetemplate);
					} else {
						&gm_formatentry($gmentrypagetemplate);
					}
				}
				open (THISENTRYFILE, ">$EntriesPath/$thisentrynumberpadded.$entrysuffix") || &gm_dangermouse("Can't write to $EntriesPath/$thisentrynumberpadded.$entrysuffix.  Please make sure that your entries/archives directory is correctly configured and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
				print THISENTRYFILE $entryreturn;
				close (THISENTRYFILE);
				chmod (0666, "$EntriesPath/$thisentrynumberpadded.$entrysuffix");
			} else {
				unlink ("$EntriesPath/$thisentrynumberpadded.$entrysuffix");
			}
			unless ($currentcount eq $counttohere) { $currentcount++; }
		} until $currentcount eq $counttohere;
		$percentdone = int( ($counttohere / $newentrynumber) * 100 );
		$whatimdoing = "Rebuilt entry pages: $IN{'rebuildfrom'} to $counttohere ($percentdone% done)...";
		if ($counttohere eq $newentrynumber) {
			&gm_getentryvariables($newentrynumber);
			if ($thisentryopenstatus eq "open") {
				if ($thisentrymorebody ne "") {
					&gm_formatentry($gmmoreentrypagetemplate);
				} else {
					&gm_formatentry($gmentrypagetemplate);
				}
				open (THISFILE, ">$EntriesPath/$thisentrynumberpadded.$entrysuffix") || &gm_dangermouse("Can't write to $EntriesPath/$thisentrynumberpadded.$entrysuffix.  Please make sure that your entries/archives directory is configured correctly and is CHMODed to 777; also try running Diagnostics & Repair from the Configuration screen.");
				print THISFILE $entryreturn;
				close (THISFILE);
				chmod (0666, "$EntriesPath/$thisentrynumberpadded.$entrysuffix");
			} else {
				unlink ("$EntriesPath/$thisentrynumberpadded.$entrysuffix");
			}
			$nowrebuild = "done";
		} else {
			$nowrebuild = $counttohere;
		}
	} else {
		$nowrebuild = "done";
	}
	}

}

$metarefreshtag = qq(<META http-equiv="REFRESH" content="1; URL=gm.cgi?authorname=$usethisauthorname&authorpassword=$usethisauthorpassword&thomas=rebuildupdate&rebuilding=$IN{'rebuilding'}&rebuildfrom=$nowrebuild&connectednumber=$IN{'connectednumber'}">);

if (($nowrebuild eq "") || ($nowrebuild eq "done")) {
	if ($IN{'rebuilding'} eq "everything") {
		$statusnote = qq(<B><FONT COLOR="#0000FF">All the files have been rebuilt.</FONT></B>);
		&gm_writetocplog("$IN{'authorname'} rebuilt all the files");
	} elsif ($IN{'rebuilding'} eq "entryfiles") {
		$statusnote = qq(<B><FONT COLOR="#0000FF">All the entry pages have been rebuilt.</FONT></B>);
		&gm_writetocplog("$IN{'authorname'} rebuilt all the entry pages");
	} elsif ($IN{'rebuilding'} eq "archivefiles") {
		$statusnote = qq(<B><FONT COLOR="#0000FF">All the archive entry pages have been rebuilt.</FONT></B>);
		&gm_writetocplog("$IN{'authorname'} rebuilt all the archive entry pages");
	} elsif ($IN{'rebuilding'} eq "mainentries") {
		$statusnote = qq(<B><FONT COLOR="#0000FF">All the main entry pages have been rebuilt.</FONT></B>);
		&gm_writetocplog("$IN{'authorname'} rebuilt all the main entry pages");
	} elsif ($IN{'rebuilding'} eq "connected") {
		$statusnote = qq(<B><FONT COLOR="#0000FF">All the connected files have been rebuilt.</FONT></B>);
		&gm_writetocplog("$IN{'authorname'} rebuilt all the connected files");
	} elsif ($IN{'rebuilding'} eq "connectedaftersave") {
		$statusnote = qq(<B><FONT COLOR="#0000FF">Your new entry has been added.</FONT></B>);
	} else {
		$statusnote = qq(<B><FONT COLOR="#0000FF">All relevant files have been rebuilt.</FONT></B>);
		&gm_writetocplog("$IN{'authorname'} rebuilt unknown files");
	}
	$whatimdoing = qq($statusnote<P><FORM ACTION="gm.cgi" METHOD=POST><INPUT TYPE=HIDDEN NAME="authorname" VALUE="$IN{'authorname'}"><INPUT TYPE=HIDDEN NAME="authorpassword" VALUE="$IN{'authorpassword'}"><INPUT TYPE=SUBMIT CLASS="button" NAME="thomas" VALUE="Return To Main Menu" STYLE="background: #D0D0FF"></FORM><P><FONT SIZE=1>"Man must not demolish, but build; he must raise temples where mankind<BR>may come and partake of the purest pleasure."&#151;Goethe</FONT>);
	$metarefreshtag = "";
}

if ($IN{'rebuilding'} eq "everything") {
	$statusnote = qq(<B><FONT COLOR="#000000">Rebuilding Everything</FONT></B><P>);
} elsif ($IN{'rebuilding'} eq "entryfiles") {
	$statusnote = qq(<B><FONT COLOR="#000000">Rebuilding Entry Pages</FONT></B><P>);
} elsif ($IN{'rebuilding'} eq "archivefiles") {
	$statusnote = qq(<B><FONT COLOR="#000000">Rebuilding Archive Entry Pages</FONT></B><P>);
} elsif ($IN{'rebuilding'} eq "mainentries") {
	$statusnote = qq(<B><FONT COLOR="#000000">Rebuilding Main Entry Pages</FONT></B><P>);
} elsif ($IN{'rebuilding'} eq "connected") {
	$statusnote = qq(<B><FONT COLOR="#000000">Rebuilding Connected Files</FONT></B><P>);
} elsif ($IN{'rebuilding'} eq "connectedaftersave") {
	$statusnote = qq(<B><FONT COLOR="#000000">Rebuilding Connected Files</FONT></B><P>);
} else {
	$statusnote = qq(<B><FONT COLOR="#000000">Rebuilding Files</FONT></B><P>);
}

$gmrebuildheadtag = qq#<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<TITLE>Greymatter</TITLE>
$metarefreshtag

<STYLE TYPE="text/css">
<!--
.copynotice { text-decoration: none }
.copynotice:hover { color: \#FFFFFF }
.button { font-family: verdana, arial, helvetica; font-size: 13px; background: \#FFFFD0; border-color: \#000000 }
BODY { scrollbar-face-color: \#A0C0E0; scrollbar-shadow-color: \#000000; scrollbar-highlight-color: \#000000; scrollbar-3dlight-color: \#000000; scrollbar-darkshadow-color: \#000000; scrollbar-track-color: \#000000; scrollbar-arrow-color: \#000000 }
}
-->
</STYLE>

<STYLE TYPE="text/css" MEDIA="all">
<!--
.button { width: 240; height: 26 }
-->
</STYLE>

</HEAD>

<BODY BGCOLOR="\#8080B0" TEXT="\#000000" LINK="\#000000" VLINK="\#000000" ALINK="\#000000" MARGIN=10 TOPMARGIN=10 LEFTMARGIN=10 RIGHTMARGIN=10 BOTTOMMARGIN=10 MARGINHEIGHT=10 MARGINWIDTH=10>#;

print<<GMREBUILDUPDATE;

$gmrebuildheadtag
$gmframetop
$statusnote
$whatimdoing
$gmframebottom

</BODY>
</HTML>

GMREBUILDUPDATE

exit;

}
