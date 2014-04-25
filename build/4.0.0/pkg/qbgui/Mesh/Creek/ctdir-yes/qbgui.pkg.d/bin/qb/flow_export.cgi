#!/usr/bin/perl

require("/usr/local/apache/qb/qbmod.cgi");
my $cgi = new CGI;
my $aa;
my $sel = $cgi->param("sel");

$action{action} = $cgi->param("action");
$action{total_result} = $cgi->param("total_result");

print "Content-type:text/html\n\n";
print qq (<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="../gui.css" type="text/css"></head>);
print qq (<body bgcolor="#336699" text="#ffffff" link="#000040" >);
print qq (<div align="center" style="width: 100%; margin: 12px auto 5px auto;">);

if ( $action{action} ) { maintainExport( %action ); }
print qq($action{total_result});

print qq (</div></body></html>);


sub maintainExport
{
    my (%action)=@_;
    if(!$action{action}||!$action{total_result}){return;}
    my $total_result=$action{total_result};
    if ( $action{action}=~m/^SAVE$/ )
    {
    	my @result = split(/_/,$total_result);
    	system("/usr/local/apache/qb/setuid/run /bin/chmod 777 /tmp");
    	$basedir = '/tmp';
    	$fileName = 'flow.csv';
  	foreach $my_result(@result)
   	{
    		system("echo -e '$my_result' >> $basedir/flowoutput");
    	}
    	#system("echo -e $total_result >> $basedir/flowoutput");
        system("/usr/local/apache/qb/setuid/run mv $basedir/flowoutput $basedir/$fileName");
        print qq (<script language="javascript"> location.replace("unitexport.cgi?file=$fileName")</script>);
    }
}
