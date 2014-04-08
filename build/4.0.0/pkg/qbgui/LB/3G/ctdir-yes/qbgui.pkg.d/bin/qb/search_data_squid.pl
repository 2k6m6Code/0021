#!/usr/bin/perl
require ("qbmod.cgi");

BEGIN { unshift (@INC,"/usr/local/apache/qb/perl_lib"); }

use CGI;
my $cgi = CGI-> new();
my $tm_title = $cgi->param("title");
my $tm_ip = $cgi->param("ip");
my $tm_symd = $cgi->param("symd");
my $tm_domain = $cgi->param("domain");
my $tm_search_domain = $cgi->param("search_domain");
my $search='';
my $service=XMLread('/usr/local/apache/qbconf/flow.xml');
my $flow=$service->{user};
my $auth=XMLread('/usr/local/apache/qbconf/auth.xml');
my $auser=$auth->{user};
my $ipaddr=XMLread('/usr/local/apache/qbconf/ipaddr.xml');
my $iplist=$ipaddr->{ipaddress};
my ($y,$m,$d) = split(/\//,$tm_symd);
if($d < 10){$d=~s/^0//g;}
if($m < 10){$m=~s/^0//g;}
my %abbr = (Jan=>'1',Feb=>'2',Mar=>'3',Apr=>'4',May=>'5',Jun=>'6',Jul=>'7',Aug=>'8',Sep=>'9',Oct=>'10',Nov=>'11',Dec=>'12');
system ("/usr/local/apache/qb/setuid/run chmod 777 /tmp/");
print "Content-type: text/html\n\n";
if($tm_domain eq 'y'){
if($tm_title eq 'webfilter')
{
	#/mnt/tclog/squid/log/filter.log
	system ("/usr/local/apache/qb/setuid/run /bin/cat /mnt/tclog/squid/log/$y-$m-$d | awk '/TCP_DENIED/ {print\$1 \" \" \$3 \" \" \$7}' > /tmp/$y-$m-$d.log");
	system ("/usr/local/apache/qb/setuid/run /usr/bin/perl -p -e 's/^\\d+\.\\d+/localtime \$&/e' < /tmp/$y-$m-$d.log > /tmp/tmp_squid.log");
        system ("/usr/local/apache/qb/setuid/run /bin/cat /tmp/tmp_squid.log | awk '{print \$7}' |sort|uniq -c|sort -nr > /tmp/tmp_squid2.log");
        system ("/usr/local/apache/qb/setuid/run /bin/cat /tmp/tmp_squid.log | awk '$7 ~ /^h/{print \$7}' |cut -s -f 1-3 -d /|sort|uniq -c|sort -nr > /tmp/tmp_squid_domain.log");
	system ("sync");
}
if($tm_title eq 'webcache')
{
	system ("/usr/local/apache/qb/setuid/run /bin/cat /mnt/tclog/squid/log/$y-$m-$d | awk '{print\$1 \" \" \$3 \" \" \$7}' > /tmp/$y-$m-$d.log");
	system ("/usr/local/apache/qb/setuid/run /usr/bin/perl -p -e 's/^\\d+\.\\d+/localtime \$&/e' < /tmp/$y-$m-$d.log > /tmp/tmp_squid.log");
	system ("/usr/local/apache/qb/setuid/run /bin/cat /tmp/tmp_squid.log | awk '{print \$7}' |sort|uniq -c|sort -nr > /tmp/tmp_squid2.log");
	system ("/usr/local/apache/qb/setuid/run /bin/cat /tmp/tmp_squid.log | awk '\$7 ~ /^h/{print \$7}' |cut -s -f 1-3 -d / |sort|uniq -c|sort -nr > /tmp/tmp_squid_domain.log");
	system ("sync");
	#/mnt/tclog/squid/log/access.log
}
}
else
{
	$tm_search_domain=~s/\//\\\//g;
	system ("/usr/local/apache/qb/setuid/run /bin/cat /tmp/tmp_squid.log | awk '\$7 ~ /^$tm_search_domain/{print \$7}' |sort|uniq -c|sort -nr > /tmp/tmp_squid2.log");
}
print qq (<table bgcolor="#332211" width="1000" border="0" id="tables">);
my $search_file = '/tmp/tmp_squid2.log';
if($tm_domain eq 'y'){$search_file = '/tmp/tmp_squid_domain.log';}
open(FILE,"$search_file");
my $lineCount = 0;
my $top = '1';
my $time = '0';
my $title='0';
my $originalColor=my $bgcolor=($lineCount%2) ? ( '#556677' ) : ( '#334455' );
print qq (<thead><tr>);
print qq(<th style="width: 100px;">No</th>);
#print qq(<th style="width: 100px;">Time</th>);
#print qq(<th style="width: 100px;">IP</th>);
print qq(<th style="width: 800px;">Request</th>);
print qq(<th style="width: 100px;">Count</th>);
print qq (</tr></thead>);


$top='1';
$total=0;
t1:foreach my $database (<FILE>)
{
	my @traffic = split(/\s+/,$database);
	print qq (<tr bgcolor="$bgcolor" originalColor="$originalColor" onmouseover="focusedColor(this)" onmouseout="blurColor(this)">);
	print qq (<td width="100" align="center">$top</td>);
	print qq (<td width="800" align="center" style="display:inline-block;overflow:hidden;text-overflow:ellipsis;white-space: nowrap;"><a href="$traffic[2]" target="_blank">$traffic[2]</a></td>);
	if($tm_domain eq 'y'){print qq (<td width="100" align="center" onclick="javascript:search_squid('$traffic[2]','$tm_title','$tm_ip','$tm_symd')">$traffic[1]</td>);}
	else{print qq (<td width="100" align="center" onclick="javascript:search_squid_detail('$tm_title','$tm_ip','$tm_symd','$traffic[2]')">$traffic[1]</td>);}
	$top++;
	$total+=$traffic[1];
}
close(FILE);
#print qq ($total<br>);
#system ("/usr/local/apache/qb/setuid/run rm -rf /tmp/$y-$m-$d.log /tmp/tmp_squid.log");
system ("sync");
=cut
print qq (<tfoot><tr><th>TOTAL:</th><th></th><th></th></tr></tfoot>);
	my $line;
=cut
