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

$action{portnum}=$form->param('portnum');
$action{newvlannic}=$form->param('newvlannic');
$action{mac_addr}=$form->param('mac_addr');
$action{vid}=$form->param('vid');
$action{enablevlan}=$form->param('enablevlan');
$action{key}=$form->param('key');
$action{value}=$form->param('value');

print qq(<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><link rel="stylesheet" href="gui.css" type="text/css"></head><body  bgcolor="#336699">);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

vlanScript();

editVlan( %action );

print qq (<div align="center">);
print qq (<form name="editVlan" method="post" action="vlan.cgi">);
listVlan( %action );
print qq (<input type="hidden" name="action" value="$action{action}">);
print qq (<input type="hidden" name="vlan" value="">);
print qq (</form>);
print qq (</div>);

general_script();

print qq(</body></html> );  

