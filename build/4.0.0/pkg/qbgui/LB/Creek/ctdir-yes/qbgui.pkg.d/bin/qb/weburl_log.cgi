#!/usr/bin/perl
use Data::Dumper;
use CGI;

print "Content-type:text/html\n\n";

#---------------- Just for form to show available items of subnets and services ------------------
my  %action;
my  $form = new CGI;


print qq (<html><head><meta charset="UTF-8"><link rel="stylesheet" href="gui.css" type="text/css"></head><body bgcolor="#336699" text="#ffffff" link="#000040" >);

print qq(<div align="center">);
#------- start to draw every form object to interact with users --------------------------------

#print qq(<form name="show_layer7_log" method="post" action="layer7_log.cgi">);
print qq (<table cellspacing="0" border="0">);
print qq (<tr><td class="bigtitle">Keyword );
print qq (</td></tr>);
print qq (</table>);

print qq (<div class="divframe" style="width=950; " >);
print qq (<table class="sortable" width="80%" border="0"><tr bgcolor="#332211">);
print qq (<td align="center" width="100" style="white-space: nowrap;">Time</td>);
print qq (<td align="center" width="100" style="white-space: nowrap;">Keyword</td>);
print qq (<td align="center" width="100" style="white-space: nowrap;">Source</td>);
print qq (<td align="center" width="100" style="white-space: nowrap;">Destination</td>);

my $lineCount=0;

#my @all_layer7=("GoogleBooks","GoogleAnalytics","GoogleCalendar","GoogleChrome","GooglePicasa","GooglePLAY","RSS","Evernote","Niconico","NextTV","Youtube","HiChannel","JustinTV","PPStream","Qvod","BaiduVideo","TeamViewer","GoToMeeting");
my @all_layer7=("KEYFILTER");

foreach my $Target_layer7 ( @all_layer7 )
{
    my $all_layer7_log=`/usr/local/apache/qb/setuid/run grep -r $Target_layer7 /var/log/iptables_layer7.log | awk '{print \$1,\$2,\$3,\$6,\$9,\$10}'`;
`/usr/local/apache/qb/setuid/run echo weburl >> /tmp/garytest`;
    my @layer7_log_array=split(/\n/,$all_layer7_log);
    

    foreach my $layer7_log ( @layer7_log_array )
    {
    	my @log_array=split(/\ /,$layer7_log);
    	
    	
	my $originalColor=my $bgcolor=($lineCount%2) ? ( '#334455' ) : ( '#556677' );
	print qq (<tr bgcolor="$bgcolor" originalColor="$originalColor" onmouseover="focusedColor(this)" onmouseout="blurColor(this)">);
    
	print qq (<td align="center" width="100" height="25">$log_array[0] $log_array[1] $log_array[2]</td>);
	$log_array[3]=~s/KEYFILTER_//g;
	print qq (<td align="center" width="100" height="25">$log_array[3]</td>);
	$log_array[4]=~s/SRC=//g;
	print qq (<td align="center" width="100" height="25">$log_array[4]</td>);
	$log_array[5]=~s/DST=//g;
	print qq (<td align="center" width="100" height="25">$log_array[5]</td>);
    
	print qq (</tr>);
	$lineCount++;
    }

}
print qq (</table>);

print qq(</form></div>);
print qq(</body></html>);

