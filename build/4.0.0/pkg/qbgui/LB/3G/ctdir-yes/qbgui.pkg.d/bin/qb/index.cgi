#!/usr/bin/perl

require ("qbmod.cgi");

BEGIN { unshift (@INC,"/usr/local/apache/qb/perl_lib"); }

use CGI;
use JSON;
my $form=new CGI;
my $action1 = $form->param(action);
my $username=$form->param(username);
my $password=$form->param(password);
my $now_lang=$form->cookie('locale');
my $TYPE=runCommand(command=>'cat', params=>'/opt/qb/registry|awk \'$1 == "TYPE" { print $2 }\'');
authenticate( action=>'LOGIN', username=>$username, password=>$password );

#�o�@��@�w�n��b authenticate �᭱
print "Content-type:text/html\n\n";

#���p�{�ҥ��ѡA�N��������
if ( $gLOGINRESULT ) 
{
#print << "QB_HOME";
print qq(<html>);
print qq(<head>);
print qq(<title>Q-Balancer Configuration Center</title>);
print qq(<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">);
print qq(<script type="text/javascript" src="qb.js"></script>);
print qq(<script language="javascript">);
print qq(window.onunload =function(){);
print qq(var clearcookie=getcookie('clearcookie'););
#print qq ( alert (getcookie('locale') ); );
print qq(if ( clearcookie=='false' ) { return; });
print qq(qbLogout(); });
print qq(</script>);
print qq(</head>);
print qq(<frameset rows="*" cols="140,*" frameborder="AUTO" border="0" framespacing="0">);
print qq(<frame name="menuFrame" scrolling="YES" noresize src="menu.cgi" frameborder="NO">);
print qq(<frameset rows="50,*" frameborder="NO" border="0" framespacing="0" cols="*"> );
print qq(<frame name="configFrame" src="config.cgi" scrolling="NO">);
print qq(<frameset rows="*" cols="*" frameborder="NO">);

#if (grep(/Mesh/,$TYPE))
if ( grep(/Mesh/,$TYPE) || $now_lang eq "zh_TW" )
{
    print qq(<frame name="mainFrame" src="dashboard.cgi" frameborder="NO" noresize scrolling="AUTO">);
}
elsif (!grep(/Mesh/,$TYPE) && $action1 > 8)
{
    print qq(<frame name="mainFrame" src="dashboard.php" frameborder="NO" noresize scrolling="AUTO">);
}else
{
    print qq(<frame name="mainFrame" src="dashboard.cgi" frameborder="NO" noresize scrolling="AUTO">);
}
print qq(</frameset>);
print qq(</frameset>);
print qq(<frame src="right.htm" scrolling="NO">);
print qq(</frameset>);
print qq(</noframes>);
print qq(</html>);
}
else 
{
    print qq(<html><head><link rel="stylesheet" href="gui.css" type="text/css"></head>);
    print qq(<body bgcolor="#003366" text="#ffffff" link="#000040" vlink="#400040"></body></html>);
}

general_script();

