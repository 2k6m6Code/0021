#!/usr/bin/perl
use Data::Dumper;
use CGI;
require ("qbmod.cgi");
require ("./qblib/mime.lib");
require ("./qblib/editmime.lib");


#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate(action=>'RANDOMCHECK');

print "Content-type:text/html\n\n";

#---------------- Just for form to show available items of subnets and services ------------------
my  %action;
my  $form = new CGI;
$action{action} = $form->param('action');
my @mimetypes=$form->param('mimetypes');

$action{mimetypes}=\@mimetypes;

my @block_mimes=$form->param('block_mimes');
$action{block_mimes}=\@block_mimes;

print qq (<html><head><link rel="stylesheet" href="gui.css" type="text/css"></head><body bgcolor="#336699" text="#ffffff" link="#000040" >);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} ) { maintainMIME( %action ); }

print qq(<div align="center">);
#------- start to draw every form object to interact with users --------------------------------
print qq(<form name="mimeform" method="post" action="mime.cgi">);
print qq (<table cellspacing="0" border="0">);
print qq (<tr><td>);
showMIME(%action);
scriptMIME();
print qq (</td></tr>);
print qq (</table>);

print qq(<input type="hidden" name="action" value="">);
print qq(</form></div>);
general_script();
print qq(</body></html>);

