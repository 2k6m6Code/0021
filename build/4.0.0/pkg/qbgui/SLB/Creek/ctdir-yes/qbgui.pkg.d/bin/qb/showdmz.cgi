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
$action{focuseddmz}=$form->param('focuseddmz');
$action{sortingkey}=$form->param('sortingkey');

my @dmznets=$form->param('dmznets');
$action{dmznets}=\@dmznets;

#-------------------------- send html header --------------------------------------
print qq (<html><head><link rel="stylesheet" href="gui.css" type="text/css"></head><body  style="margin:0" bgcolor="#336699" text="#ffffff" link="#2030dd" vlink="#400040">);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} ) { maintainDMZ( %action ); }

#------- pass form information to the procedure of updating  subnet.xml -----------------------------------
print qq(<div class="myframe"><form action="showdmz.cgi" method="post">);
showDMZScript();
showDMZ( %action );
print qq(<input type="hidden" name="action" value="">);
print qq(<input type="hidden" name="focuseddmz" value="">);
print qq(<input type="hidden" name="sortingkey" value="">);
print qq(</form></div>);

general_script();

print qq(</body></html>);
