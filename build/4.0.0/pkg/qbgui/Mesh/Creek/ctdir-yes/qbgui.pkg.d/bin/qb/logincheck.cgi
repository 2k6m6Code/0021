#!/usr/bin/perl
use CGI;
require ("qbmod.cgi");


#�{�ҬO�_�O�g�L���`�B�зǪ��{�ǵn�J�i�Ӫ�
authenticate(action=>'RANDOMCHECK');
print "Content-type:text/html\n\n";

#read-in form information ------------------------------
#a hash structure to  package form info and then pass it as parameter to  subnet_maintain()  --------------            
my $form = new CGI;

#=========================================================================================
#���p�{�ҥ��ѡA�N��������
if ( !$gLOGINRESULT ) {
print qq(0);
} else {
print qq(1);
}

#------- start to draw every form object to interact with users ------------------------------------






