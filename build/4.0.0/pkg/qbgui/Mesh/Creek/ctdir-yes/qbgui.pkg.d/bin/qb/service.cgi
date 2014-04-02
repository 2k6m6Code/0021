#!/usr/bin/perl
use CGI;
use Data::Dumper;
require ("qbmod.cgi");

my $form=new CGI;
my %action;
$action{action}=$form->param('action'); 
$action{service}=$form->param('service');
my @service_del=$form->param('service_del');
$action{service_del}=\@service_del;
my @sergroupname=$form->param('sergroupname');
$action{sergroupname}=\@sergroupname;

#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate( action=>'RANDOMCHECK' );

print "Content-type:text/html\n\n";

if ( !$action{service} )
{
    @allServices=maintainService(action=>'GETUSERSERVICE');
    $action{service}=$allServices[0];
}

my $focusedPort=$action{focusedport}=$form->param('port');
$action{newservice}=$form->param('newservice');

#****************************************************
$action{protocol}=$form->param('protocol');
$action{porttype}=$form->param('porttype');
if ( $action{protocol} eq "defined" ) { $action{protocol}=$action{porttype}; }
$action{portvalue}=$form->param('portvalue');

#add types
$action{types}=$form->param('types');

#�Y�� new �F�@�ӷs�� service�A�ݷ|��N����  show �X��
if ( $action{action}=~m/^NEWSERVICE$/ ) { $action{service}=$action{newservice}; } 
if ( $action{action}=~m/^ADDPORT$/ ) { $focusedPort=$action{protocol}.':'.$action{portvalue}; }

#��z�� hash array �᩹���h�e
#-------------------------- send html header --------------------------------------
print qq (<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><link rel="stylesheet" href="gui.css" type="text/css"></head><body  bgcolor="#336699" text="#ffffff" link="#2030dd" vlink="#400040">);


#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

#------- pass form information to the procedure of updating  dns.xml -----------------------------------
if ( $action{action} ) { maintainService( %action ); }

print qq(<div align="center">);

#------- start to draw every form object to interact with users ------------------------------------
print qq(<form name="serviceform" method="post" action="service.cgi">);
print qq (<table cellspacing="0" border="0">);
print qq (<tr><td>);
service_script();
showService( %action );
print qq (</td></tr>);
print qq (</table>);
print qq(<input type="hidden" name="action" value="">);
print qq(</form></div>);


general_script();


#showResult();

print qq(</div></body></html>);


