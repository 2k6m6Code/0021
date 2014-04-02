#!/usr/bin/perl
require ("qbmod.cgi");
require "./qblib/snmp.lib";


#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate( action=>'RANDOMCHECK' );

print "Content-type:text/html\n\n";

use CGI;
use Data::Dumper;

#---------------- read-in form information ------------------------------
my $form=new CGI;
my %action;

###############################################
#GENERAL
$action{action}=$form->param('action');
$action{enablesnmp}=($form->param('enablesnmp')) ? (1) : (0);
$action{enabletrap}=($form->param('enabletrap')) ? (1) : (0);
$action{snmpmgrip}=$form->param('snmpmgrip');
$action{snmpmgrip2}=$form->param('snmpmgrip2');

if ( !$action{snmpmgrip} ) { $action{enabletrap}=0; }

$action{syscontact}=$form->param('syscontact');
$action{syslocation}=$form->param('syslocation');
$action{sysname}=$form->param('sysname');
$action{community}=$form->param('community');if ( !$action{community} ) { $action{community}=public; }

#=========================================================================================
print qq(<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><link rel="stylesheet" href="gui.css" type="text/css"></head>);
print qq(<body bgcolor="#336699" text="#ffffff" link="#000040" vlink="#400040">);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} ) { maintainSnmp( %action ); }

#------- start to draw every form object to interact with users ------------------------------------
print qq (<div align="center">);
print qq (<form name="syslogform" method="post" action="snmp.cgi">);

snmpScript();

showSnmp( %action ); 

print qq (<input type="hidden" name="action" value="">);
print qq (</form>);
print qq (</div>);

general_script();

print qq(</body></html>);





