#!/usr/bin/perl
use CGI;
require ("/usr/local/apache/qb/language/qblanguage.cgi");
@qblang = QBlanguage();
my  %action;
my  $form = new CGI;
$action{page} = $form->param('p');
my $page = 'auth_server.cgi';
if($action{page}){$page=$action{page};}

print "Content-type:text/html\n\n";
print '<html lang="en">';
print '<head>';
print '<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">';
#print '<title></title>';
print '<script type="text/javascript" src="../qbjs/jquery.js"></script>';

print '	<style type="text/css">';
print '	button.menu{';
print '	width:14%;';
print '	height:18;';
print '	font:10px Verdana;';
print '	color:white;';
print ' background:#336699;';	
print '	border:1px solid black;';
print '	cursor:hand;';
print '	margin-right: 4px;';
print '	}';
print '	</style>';
print '</head><body style="margin: 5px; background-color:#336699;" scroll="no">';
#print '<table style="width: 100%; height: 100%;">';
print '<tr style="height: 25px;"><td>';
print '<button class="menu"  onclick="mainframe.location=\'auth_server.cgi\'		"style="width: 170">'.$qblang[562].'</button>';
print '<button class="menu"  onclick="mainframe.location=\'auth_user.cgi\'		"style="width: 170">'.$qblang[563].'</button>';
print '<button class="menu"  onclick="mainframe.location=\'auth_option.cgi\'		"style="width: 170">'.$qblang[564].'</button>';
print '<button class="menu"  onclick="mainframe.location=\'auth_status.cgi\'		"style="width: 170">'.$qblang[565].'</button>';

print '<script type="text/javascript" src="../qb.js"></script>';
#print '<a href="javascript:qbShowHelp(\'traffic\')"><img src="/image/help.gif" title="Help" alt="help image" ></a>';
print '</td></tr><tr><td><iframe frameborder="0" style="height:92%;width:100%" src="'.$page.'" name="mainframe"></iframe></td></tr>';
#print '</table></body></html>';
print '</body></html>';
