#!/usr/bin/perl
require ("qbmod.cgi");
require "./qblib/extroute.lib";
require ("/usr/local/apache/qb/language/qblanguage.cgi");
@qblang = QBlanguage();

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
$action{extrouteinfo}=$form->param('extrouteinfo');
#=========================================================================================
print qq(<html><head><link rel="stylesheet" href="gui.css" type="text/css"></head>);
print qq(<body bgcolor="#336699" text="#ffffff" link="#000040" vlink="#400040">);
print qq(<style type="text/css">button.menu{margin-right: 4px;height:18px;font:10px Verdana;color:white;background:#336699;border:1px solid black;cursor:hand;}</style>);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} ) { maintainEXTROUTE(%action); }

#------- start to draw every form object to interact with users ------------------------------------
showEXTROUTEScript();
print qq (<button  onclick="parent.mainFrame.location='zone10.cgi'" hidefocus="true" class="menu">$qblang[805]</button>);
print qq (<button  onclick="parent.mainFrame.location='extroute.cgi'" hidefocus="true" class="menu">$qblang[806]</button>);
  
print qq (<div align="center">);
print qq (<form name="extrouteform" method="post" action="extroute.cgi">);

showEXTROUTE();

print qq (<input type="hidden" name="action" value="">);
print qq (</form>);
print qq (</div>);

general_script();

print qq(</body></html>);
