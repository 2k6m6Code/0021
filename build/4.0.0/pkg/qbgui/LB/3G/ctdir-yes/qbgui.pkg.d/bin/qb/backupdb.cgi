#!/usr/bin/perl
require ("qbmod.cgi");
require "./qblib/backupdb.lib";


#認證是否是經過正常且標準的程序登入進來的
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

$action{ftpserver}=($form->param('ftpserver') && $form->param('ftpserverip')) ? (1) : (0);
$action{ftpserverip}=$form->param('ftpserverip');
$action{ftpusername}=$form->param('ftpusername');
$action{ftppassword}=$form->param('ftppassword');
$action{ftpfrequency}=$form->param('ftpfrequency');
$action{ftpdir}=$form->param('ftpdir');
$action{syslogdev}=$form->param('syslogdev');

#=========================================================================================
print qq(<html><head><link rel="stylesheet" href="gui.css" type="text/css">);
print qq(<style type="text/css">table.sortable thead{background-color:#eee;color:#666666;font-weight: bold;cursor: default;});
print qq(button.menu{margin-right: 4px;height:18px;width:14%;font:10px Verdana;color:white;background:#336699;border:1px solid black;cursor:hand;});
print qq(</style></head>);
print qq(<body bgcolor="#336699" text="#ffffff" link="#000040" vlink="#400040">);
print qq (<button  onclick="parent.mainFrame.location='l7log.cgi'" style="width:170" hidefocus="true" class="menu">Log Configuration</button>);
print qq (<button  onclick="parent.mainFrame.location='flow_user.cgi'" style="width:170" hidefocus="true" class="menu">Unit</button>);
print qq (<button  onclick="parent.mainFrame.location='flow_user_sec.cgi'" style="width:170" hidefocus="true" class="menu">Transparent Subnets</button>);
print qq (<button  onclick="parent.mainFrame.location='storage_set.cgi'" style="width:170" hidefocus="true" class="menu">Storage</button>);
print qq (<button  onclick="parent.mainFrame.location='backupdb.cgi'" style="width:170" hidefocus="true" class="menu">Backup</button>);
#假如認證失敗，就直接結束
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} ) { maintainSyslog( %action ); }

#------- start to draw every form object to interact with users ------------------------------------
print qq (<div align="center">);
print qq (<form name="l7logform" method="post" action="backupdb.cgi">);

backupdbScript();

showSyslog( %action ); 

print qq (<input type="hidden" name="action" id="action" value="">);
print qq (<input type="hidden" name="path" id="path" value="">);
print qq (</form>);
print qq (</div>);

general_script();

print qq(</body></html>);
