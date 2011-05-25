$guestbook_file = "cgi-bin\\guestbook\\guestbook.html";
$guestbook_url = "guestbook.html";

###################################################################
#  GuestBook Version 0.9(BETA) Last Modified: 8-30-97             #
#  Written by: David Tsai                                         #
#  Copyright © 1997 Web-Consultant All rights reserved.           #
#  http://www.web-consult.com                                     #
#  Permission to use this script for any purposes granted and     #
#  persmission to distribute this script granted as long as this  #
#  copyright notice stays attached.                               #
###################################################################
$mailprog = '/usr/sbin/sendmail';
#--> Title of your website
$site_name = "Website";
#--> Your email address
$your_email = "mikes\@9netave.com";

##############################

#      O P T I O N S
$top = 1;          #--> 1 = new entries are added to top of the page
                   #--> 0 = new entries are added to the bottom of page

$allow_html = 2;   #--> 1 = allows html; 2 = does not allow html

$email = 1;        #--> 1 = email the user a confirmation message
                   #--> 0 = no

$email_you = 0;    #--> 1 = emails you a confirmation message

$redirect = 1;     #--> 1 = redirects user to your guestbook
                   #--> 0 = prints a return page

#---------------------------------------#
#   S T O P   E D I T I N G   H E R E   #
#---------------------------------------#


@day = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");

# Get the input data
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

# Parse the data
@pairs = split(/&/, $buffer);

foreach $pair (@pairs) {
      	($name, $value) = split(/=/, $pair);

	# get rid of the % encoding
      	$value =~ tr/+/ /;
      	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
      	$name =~ tr/+/ /;
      	$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
      	$value =~ s/<!--(.|\n)*-->//g;
	
	if(! $allow_html) {
      		$value =~ s/<([^>]|\n)*>//g;
	}

      	$FORM{$name} = $value;
}


&incomplete unless $FORM{'name'};
&incomplete unless $FORM{'location'};
&incomplete unless $FORM{'comments'};

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime(time);
$mon += 1;
$date = "$day[$wday], $mon-$mday-$year<BR>\n";

open(GUESTBOOK, "$guestbook_file") || die "Can't open GUESTBOOK: $guestbook_file\n";
@guestbook =<GUESTBOOK>;
close(GUESTBOOK);

open(GUESTBOOK, ">$guestbook_file") || die "Can't open GUESTBOOK: $guestbook_file\n";
foreach $line (@guestbook) {
	if($line =~ /<!--Begin GuestBook-->/i) {
		if($top) {
			print GUESTBOOK "<!--Begin GuestBook-->\n";
		}
		
		if($FORM{'email'}) {
			print GUESTBOOK "<B>From:</B><A HREF=\"mailto:$FORM{'email'}\">
					$FORM{'name'}</A><BR>\n";
		}
		else {
			print GUESTBOOK "<B>From:</B> $FORM{'name'}<BR>\n";
		}

		if($FORM{'url'}) {
			print GUESTBOOK "<B>URL:</B> <A HREF=\"$FORM{'url'}\">$FORM{'url'}</A><BR>\n";
		}

		print GUESTBOOK "<B>Location:</B> $FORM{'location'}<BR>\n";
		print GUESTBOOK "<B>Comments:</B><BR>\n";
		print GUESTBOOK "$FORM{'comments'}\n";
		print GUESTBOOK "<P>$date<HR><P>\n";

		if(! $top) {
			print GUESTBOOK "<!--Begin GuestBook-->\n";
		}
	}
	else {
		print GUESTBOOK "$line";
	}
}
close(GUESTBOOK);



if($email && $FORM{'email'} =~ /.*\@.*\..*/) {

	open(MAIL, "|$mailprog -t") || die "Can't open mailprog: $mailprog\n";

	print MAIL "To: $FORM{'email'}\n";
	print MAIL "From: Guestbook.Admin\n";
	print MAIL "Subject: Guestbook Entry\n";
	print MAIL "Reply-To: $your_email\n\n";

	print MAIL "Your guestbook entry submission has been completed!\n";
	print MAIL "Below is what you submited to $site_name\'s guestbook\n\n";

	print MAIL "Name: $FORM{'name'}\n";
	print MAIL "Email: $FORM{'email'}\n";
	print MAIL "URL: $FORM{'url'}\n";
	print MAIL "Location: $FORM{'location'}\n";
	print MAIL "Comments:\n";
	print MAIL "$FORM{'comments'}\n\n";

	close(MAIL);
}

if($email_you && $your_email) {

	open(MAIL, "|$mailprog -t") || die "Can't open mailprog: $mailprog\n";

	print MAIL "To: $your_email\n";
	print MAIL "From: GuestBook.Admin\n";
	print MAIL "Subject: GuestBook Entry\n\n";

	print MAIL "A new person has submited a entry in your guestbook\n";
	print MAIL "Below is what $FORM{'name'} submited\n\n";

	print MAIL "Name: $FORM{'name'}\n";
	print MAIL "Email: $FORM{'email'}\n";
	print MAIL "URL: $FORM{'url'}\n";
	print MAIL "Location: $FORM{'location'}\n";
	print MAIL "Comments:\n";
	print MAIL "$FORM{'comments'}\n\n";

	close(MAIL);

}

if($redirect) {

	print "Location: $guestbook_url\n\n";

}

else {

	print "Content-Type: text/html\n\n";

	print qq!
	<H1>Your GuestBook Entry has been Submited\!</H1>
	Your guestbook entry has been successfully added to the
	<A HREF="$guestbook_url">guestbook</A>.
	You may need to press reload to see your guestbook entry.<P>!;

}
	



sub incomplete {

	print "Content-Type: text/html\n\n";

	print qq!
	<H1>Form Incomplete\!</H1>
	You did not fill in all the required fields on the form.  
Please press the back button on your browser or go to <a href = "index.htm">start page</a> and try again.<P>

	The following fields are required name, location and comments<P>!;

	die;

}