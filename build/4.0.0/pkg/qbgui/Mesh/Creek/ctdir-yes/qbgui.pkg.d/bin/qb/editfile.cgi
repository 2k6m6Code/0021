#!/usr/bin/perl
use CGI;
require ("qbmod.cgi");
require ("./qblib/editfile.lib");

#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate(action=>'RANDOMCHECK');

print "Content-type:text/html\n\n";

#---------------- Just for form to show available items of subnets and services ------------------
my  %action;
my  $form = new CGI;
$action{action} = $form->param('action');
$action{filename} = $form->param('filename');
$action{oldfilename} = $form->param('oldfilename');
$action{description} = $form->param('description');
$action{block} = $form->param('block');

print qq (<html><head><link rel="stylesheet" href="gui.css" type="text/css"></head><body bgcolor="#336699" text="#ffffff" link="#000040" >);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} ) { maintainFile( %action ); }

print qq(<div align="center">);
#------- start to draw every form object to interact with users --------------------------------
print qq(<form name="editfileform" method="post" action="editfile.cgi">);
print qq (<table cellspacing="0" border="0">);
print qq (<tr><td>);
showEditFile(%action);
scriptEditFile();
print qq (</td></tr>);
print qq (</table>);
print qq (<input type="hidden" class="qbtext" name="action" value="$action{action}">);
print qq(</form></div>);
general_script();
print qq(</body></html>);

