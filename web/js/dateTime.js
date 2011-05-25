function dateTime() {
	var months=new Array(13);
	months[1]="1";
	months[2]="2";
	months[3]="3";
	months[4]="4";
	months[5]="5";
	months[6]="6";
	months[7]="7";
	months[8]="8";
	months[9]="9";
	months[10]="10";
	months[11]="11";
	months[12]="12";
	
	var time=new Date();
	var lmonth=months[time.getMonth() + 1];
	var date=time.getDate();
	var year=time.getYear();

	var hours=time.getHours();
	var minutes=time.getMinutes();

	if ((navigator.appName == "Microsoft Internet Explorer") && (year < 2000))		
		year="19" + year;
	if (navigator.appName == "Netscape")
		year=1900 + year;

	document.write(lmonth + ".");
	document.write(date + ".");
	document.write(year);
	document.write("  ");
	document.write((hours > 12) ? hours-12 : hours);
	document.write(((minutes < 10) ? ":0" : ":") + minutes);
   	document.write((hours >= 12) ? " pm" : " am");
	}
