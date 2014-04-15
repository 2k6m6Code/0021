#!/usr/bin/perl

require("/usr/local/apache/qb/qbmod.cgi");
my $cgi = new CGI;
my $aa;
my $sel = $cgi->param("sel");

$action{action} = $cgi->param("action");
$action{file} = $cgi->param("filename");
$action{sel} = $cgi->param("sel");

$aa=XMLread("/usr/local/apache/qbconf/flow.xml");
if($sel eq 'tp'){$aa=XMLread("/usr/local/apache/qbconf/flow_sec.xml");}
my $flow=$aa->{user};

print "Content-type:text/html\n\n";
print qq (<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="../gui.css" type="text/css"></head>);
print qq (<body bgcolor="#336699" text="#ffffff" link="#000040" >);
print qq (<div align="center" style="width: 100%; margin: 12px auto 5px auto;">);

if ( $action{action} ) { maintainImport( %action ); }
#print qq(action:$action{action}  sel:$action{sel});

print qq (<form enctype="multipart/form-data" method="post" action="file_import.cgi" style="width:100%">);
print qq (<input type="hidden" name="sel" id="sel"  value="$sel">);
print qq (<input type="hidden" name="action" id="action"  value="">);
print qq (<fieldset class="fieldset">);
print qq (<legend class="subtitle">File Import</legend>);
print qq (<table class="body">);
print qq (<tr><td align="center">);
print qq (<input type="file" class="qbtext" id="filename" name="filename" style="width:50">);
print qq (</td></tr>);
print qq (<tr><td align="center"><input type="submit" value="Submit" onclick="goSubmit('SAVE')"></td></tr>);
print qq (</table>); 
print qq (</fieldset>);
print qq (</form>);
print qq (<script type="text/javascript" src="qb.js"></script>);
print qq (</div></body></html>);


sub maintainImport
{
    my (%action)=@_;
	if(!$action{file}){return;}
	my $aa;
	my $file = $action{file};
	my $sel = $action{sel};
	$aa="flow.xml";
	if($sel eq 'tp'){$aa="flow_sec.xml";}
	
    my $schref=XMLread($gPATH.$aa);
    my $schlist=$schref->{user};
    my $exist=0;
    my @subscharrary;
    my %newschedule;

    if ( !$action{action} ) { return; }
    
    if ( $action{action}=~m/^SAVE$/ )
    {
		$basedir = '/tmp';
		$fileName = 'tmp_import';		
		if ($file ne "") 
		{
			open (OUTFILE, ">$basedir/$fileName");
			binmode(OUTFILE);
			while (my $bytesread = read($file, my $buffer, 1024)) {
				print OUTFILE $buffer;
			}
			close (OUTFILE);
		}
		system("cat $basedir/$fileName | tr -d '\r' > $basedir/$fileName.test");
		system("rm -rf $basedir/$fileName");
		
}
