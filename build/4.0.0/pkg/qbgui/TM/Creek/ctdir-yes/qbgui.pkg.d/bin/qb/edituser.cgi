#!/usr/bin/perl
use CGI;
use Data::Dumper;
require ("qbmod.cgi");

#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate( action=>'RANDOMCHECK' );

print "Content-type:text/html\n\n";

my $form=new CGI;
my %action;
$action{action}=$form->param('action');

$action{user}=$form->param('user');
$action{newusername}=$form->param('newusername');
$action{newpassword}=$form->param('newpassword');
$action{privilege}=$form->param('privilege');
$action{key}=$form->param('key');
$action{value}=$form->param('value');

print qq(<html><head><link rel="stylesheet" href="gui.css" type="text/css"></head><body  bgcolor="#336699">);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

userScript();

editUsers( %action );

print qq (<div align="center">);
print qq (<form name="editUser" method="post" action="edituser.cgi">);
listUsers( %action );
print qq (<input type="hidden" name="action" value="$action{action}">);
print qq (<input type="hidden" name="user" value="">);
print qq (</form>);
print qq (</div>);

general_script();

print qq(</body></html> );  

