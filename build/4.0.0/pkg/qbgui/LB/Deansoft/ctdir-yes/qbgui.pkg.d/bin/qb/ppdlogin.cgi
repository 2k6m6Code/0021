#!/usr/bin/perl
use CGI;
use Data::Dumper;
require ("qbmod.cgi");
require "./qblib/ppdlogin.lib";

#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
#authenticate( action=>'RANDOMCHECK' );

print "Content-type:text/html\n\n";

my $form=new CGI;
my %action;
$action{action}=$form->param('action');

$action{user}=$form->param('user');
$action{newusername}=$form->param('newusername');
$action{newpassword}=$form->param('newpassword');
$action{newassignip}=$form->param('newassignip');
$action{key}=$form->param('key');
$action{value}=$form->param('value');

print qq(<html><head><link rel="stylesheet" href="gui.css" type="text/css"></head><body  bgcolor="#336699">);
print qq(<style type="text/css">button.menu{margin-right: 4px;height:18px;font:10px Verdana;color:white;background:#336699;border:1px solid black;cursor:hand;}</style>);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}
elsif ( !$gENABLEPPTPSERVER) { noneFunctionExit('PPTP Server is an Option');} #No PPTP server
userScript();
print qq (<button  onclick="parent.mainFrame.location='pptpinit.cgi'" hidefocus="true" class="menu">PPTP Server Configuration</button>);
print qq (<button  onclick="parent.mainFrame.location='ppdlogin.cgi'" hidefocus="true" class="menu">PPTP User Authentication</button>);
editUsers( %action );
print qq (<div align="center">);
print qq (<form name="editUser" method="post" action="ppdlogin.cgi">);
listUsers( %action );
print qq (<input type="hidden" name="action" value="$action{action}">);
print qq (<input type="hidden" name="user" value="">);
print qq (</form>);
print qq (</div>);

general_script();

print qq(</body></html> );  

