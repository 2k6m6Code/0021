#!/usr/bin/perl
use CGI;
require ("qbmod.cgi");

#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate( action=>'RANDOMCHECK' );

print "Content-type:text/html\n\n";

my $form=new CGI;
my %action;
$action{action}=$form->param('action'); 
my @selectedVSes=$form->param('vses');
$action{vses}=\@selectedVSes;
$action{focusedvs}=$form->param('focusedvs');
$action{sortingkey}=$form->param('sortingkey');
    
#-------------------------- send html header --------------------------------------
print qq (<html><head><link rel="stylesheet" href="gui.css" type="text/css"></head><body  style="overflow:hidden" bgcolor="#336699" text="#ffffff" link="#ffffff" vlink="#400040">);

#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} ) { maintainVS( %action ); }

#------- pass form information to the procedure of updating  subnet.xml -----------------------------------
print qq(<div class="myframe"><form action="showvs.cgi" method="post">);
showVSScript();
showVS( %action );
print qq(<input type="hidden" name="action" value="">);
print qq(<input type="hidden" name="focusedvs" value="">);
print qq(<input type="hidden" name="sortingkey" value="">);
print qq(</form></div>);

general_script();

print qq(</body></html>);
