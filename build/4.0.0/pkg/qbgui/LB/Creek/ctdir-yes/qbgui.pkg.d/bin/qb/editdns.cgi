#!/usr/bin/perl
use CGI;
require ("qbmod.cgi");
require ("./qblib/editdns.lib");
require ("./qblib/inidns.lib");

#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate( action=>'RANDOMCHECK' );

print "Content-type:text/html\n\n";

my $form=new CGI;
my %action;
$action{action}=$form->param('action');

my @rule=$form->param('rule'); 
$action{rule}=\@rule;

print qq (<html><head><link rel="stylesheet" href="gui.css" type="text/css"></head>);
print qq(<body style="margin:0" bgcolor="#336699" text="#ffffff" link="#ffffff" vlink="#ffffff">);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} ) { maintianInidns( %action ); }

list_ini_rule_script();

print qq(<div style="myframe">);
print qq (<form name="editednsform" method="post" action="editdns.cgi">);

showDnsPolicyTitle( %action );

print qq (<input type="hidden" name="action" value="$action{action}">);
print qq (</form></div>);

general_script();

print qq(</body></html> );  

