#!/usr/bin/perl
use Data::Dumper;
use CGI;
require ("qbmod.cgi");
require ("./qblib/mpv.lib");
require ("./qblib/newmpv.lib");


#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate(action=>'RANDOMCHECK');

print "Content-type:text/html\n\n";

#---------------- Just for form to show available items of subnets and services ------------------
my  %action;
my  $form = new CGI;
$action{action} = $form->param('action');
$action{iid} = $form->param('isp');
my @mpv=$form->param('mpv');
$action{mpv}=\@mpv;

print qq (<html><head><meta charset="UTF-8"><link rel="stylesheet" href="gui.css" type="text/css"></head><body bgcolor="#336699" text="#ffffff" link="#000040" >);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} eq 'ON' || $action {action} eq 'OFF' ) { forMPVenabled( %action ); }
else { if ( $action{action} ) { maintainMPV( %action ); }}

print qq(<div align="center">);
#------- start to draw every form object to interact with users --------------------------------
print qq(<form name="mpvform" method="post" action="mpv.cgi">);
print qq (<table cellspacing="0" border="0">);
print qq (<tr><td>);
showMPV(%action);
scriptMPV();
print qq (</td></tr>);
print qq (</table>);

print qq(<input type="hidden" name="action" value="$action{action}">);
print qq(<input type="hidden" name="isp" value="$action{isp}">);
print qq(</form></div>);
general_script();
print qq(</body></html>);

