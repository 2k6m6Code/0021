#!/usr/bin/perl

BEGIN { unshift (@INC,"/usr/local/apache/qb/perl_lib"); }

use Time::Local;
use CGI;
my $cgi = CGI-> new();
my $start = $cgi->param("start");
my $end = $cgi->param("end");
my $tm_id = $cgi->param("id");
my $search='';

print "Content-type: text/html\n\n";
print qq (<table bgcolor="#332211" width="100%" border="0" id="tables">);
my $lineCount = 0;
my $top = '1';
my $ttime = '0.001s';
my $title='0';
my $originalColor=my $bgcolor=($lineCount%2) ? ( '#556677' ) : ( '#334455' );
my @file=`/usr/local/apache/qb/setuid/run /bin/cat /mnt/log/quota.log`;
my @title =('No','Time','ID','Infomation');
#my @start=split(/-/,$tm_time);
print qq (<thead><tr>);
foreach my $tt (@title){print qq (<th style="width: 200px;">$tt</th>);}
print qq (</tr></thead>);
#my $start = time_1($start);
#my $end = time_1($end);
#print qq($start,$end<br>);
#print qq($tm_option<br>);
my @my_year = split(/ /,$start);
foreach my $data (@file)
{
    my @data_splic=split(/\s+/,$data);
	if ($tm_id ne $data_splic[2]){next;}
    #if (time_2($start,$end,"$data_splic[0] $data_splic[1] $data_splic[2] $my_year[3]"))
    #{   
        print qq (<tr bgcolor="$bgcolor" originalColor="$originalColor" onmouseover="focusedColor(this)" onmouseout="blurColor(this)">);
        print qq(<td style="width: 200px;">$top</td>); 
        print qq(<td style="width: 200px;">$data_splic[0] $data_splic[1]</td>);
		print qq(<td style="width: 200px;">$data_splic[2]</td>);
		print qq(<td style="width: 200px;">$data_splic[3] $data_splic[4]</td>);
        print qq (</tr>);
        $top++;
    #}
}
$top--;
print qq (<FONT SIZE=4>Query Completed (Time used $ttime Seconds) Data transfer completed (Total $top Records)</FONT>);
#system("/usr/local/apache/qb/setuid/run /bin/rm -rf /tmp/test_nfdump");

#sub time_1
#{
#   ($time)=@_;
#   my @tmp=split(/,/,$time);
#   return "$tmp[1] $tmp[2] $tmp[4]";
#}

sub time_2
{
   ($a,$b,$c)=@_;
   my @tmp_a=split(/ /,$a);
   my @tmp_b=split(/ /,$b);
   my @tmp_c=split(/ /,$c);
   my ($hr_a,$min_a,$sec_a)=split(/:/,$tmp_a[2]);
   my ($hr_b,$min_b,$sec_b)=split(/:/,$tmp_b[2]);
   my ($hr_c,$min_c,$sec_c)=split(/:/,$tmp_c[2]);
   
	my %month;
	@month{ qw/Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec/ } = 0..11;
	my $atime = timelocal($sec_a,$min_a,$hr_a,$tmp_a[1],$tmp_a[0]{$month},$tmp_a[3]);
	my $btime = timelocal($sec_b,$min_b,$hr_b,$tmp_b[1],$tmp_b[0]{$month},$tmp_b[3]);
	my $ctime = timelocal($sec_c,$min_c,$hr_c,$tmp_c[1],$tmp_c[0]{$month},$tmp_c[3]);

	if ($atime <= $ctime && $ctime <= $btime){return 1;}
	return 0;
}
