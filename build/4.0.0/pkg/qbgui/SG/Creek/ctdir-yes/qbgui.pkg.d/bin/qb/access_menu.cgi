#!/usr/bin/perl
print "Content-type:text/html\n\n";
use CGI;
require ("/usr/local/apache/qb/language/qblanguage.cgi");
require ("qbmod.cgi");
@qblang = QBlanguage();

#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate( action=>'RANDOMCHECK' );

#---------------- Just for form to show available items of subnets and services ------------------
my %action;
my $form = new CGI;

#--------------------------------------------------------------------------------------------------
#$action{viewpoint}=$form->param('viewpoint'); 

print qq (<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">);
print qq (<link rel="stylesheet" href="gui.css" type="text/css"></head>);
print qq (<body  style="margin:0" scroll="no" bgcolor="#336699">);
print qq (<script type="text/javascript" src="qb.js"></script>);
#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

print qq (<table cellspacing="0" cellpadding="0" width="100%" height="100%" border="0">);

#==================================================================================================
# 1. Display Title 
#==================================================================================================
print qq (<tr><td height="10">);
print qq (<br><font class="bigtitle" align="center" >$qblang[484]<font> );
print qq (<hr size=1>);
print qq (</td>);
print qq (</tr>);

#==================================================================================================
# 2. Interface to edit the list of all rules in iniroute.xml
#==================================================================================================
print qq (<tr><td valign="top" align="center">);
my $frameSource='show_access.cgi';
print qq (<iframe name="showaccess" scrolling="no" frameborder="0" frameSpacing="0" src="$frameSource" height="100%" width="100%" framespacing="NO"></iframe>);
print qq (</td></tr>);


#==================================================================================================
# 3. Interface to edit selected rule in iniroute.xml
#==================================================================================================
print qq (<tr><td height="160" align="bottom">);
print qq (<hr size=1>);
my $frameSource='edit_access.cgi';
print qq (<iframe name="editaccess" frameborder="0" src="$frameSource" height="100%" width="100%" framespacing="NO"></iframe>);

print qq (</td></tr>);
print qq (</table>);
print qq (</HTML>);

