#!/usr/bin/perl
use CGI;
require ("qbmod.cgi");
require ("qblib/newsauth_user.lib");

#認證是否是經過正常且標準的程序登入進來的
authenticate(action=>'RANDOMCHECK');

print "Content-type:text/html\n\n";

#---------------- Just for form to show available items of subnets and services ------------------
my  %action;
my  $form = new CGI;
$action{action} = $form->param('action');
$action{focusedvip} = $form->param('focusedvip');

my @publiciptodel=$form->param('publiciptodel');
$action{publiciptodel}=\@publiciptodel;

$action{isp_of_vip}=$form->param('isp_of_vip');

$action{viptoappend}=$form->param('set'.$action{isp_of_vip});

$action{dmit}=$form->param('dmit');
$action{dbps}=$form->param('dbps');
$action{umit}=$form->param('umit');
$action{ubps}=$form->param('ubps');
$action{cycle}=$form->param('cycle');
$action{chose}=$form->param('chose');
$action{hr}=$form->param('hr');
$action{sec}=$form->param('sec');
$action{bs}=$form->param('bs');
$action{ql}=$form->param('ql');
$action{lmit}=$form->param('lmit');

$action{ip}=$form->param('ip');
$action{port}=$form->param('port');
$action{pwd}=$form->param('pwd');
$action{mail}=$form->param('mail');
$action{en}=$form->param('en');
$action{dis}=$form->param('dis');
$action{en_quota}=$form->param('en_quota');
$action{dis_quota}=$form->param('dis_quota');
$action{en_CL}=$form->param('en_CL');
$action{dis_CL}=$form->param('dis_CL');
$action{tcp}=$form->param('tcp');
$action{udp}=$form->param('udp');

my $dis='1';
my $dis_quota='1';
my $dis_CL='1';
my $ip,$port,$pwd,$mail='';
if($action{en} ne ''){$en=$action{en};}
if($action{dis} ne ''){$dis=$action{dis};}
if($action{en_quota} ne ''){$en_quota=$action{en_quota};}
if($action{dis_quota} ne ''){$dis_quota=$action{dis_quota};}
if($action{ip} ne ''){$ip=$action{ip};}
if($action{port} ne ''){$port=$action{port};}
if($action{pwd} ne ''){$pwd=$action{pwd};}
if($action{mail} ne ''){$mail=$action{mail};}

my $dmit,$dbps,$umit,$ubps,$cycle,$chose,$mhr,$msec,$bs,$ql,$lmit,$tmit,$tbps = '';
$lmit='10';
if($action{dmit} ne ''){$dmit=$action{dmit};}
if($action{dbps} ne ''){$dbps=$action{dbps};}#$dbps=$action{dbps};
if($action{umit} ne ''){$umit=$action{umit};}
if($action{ubps} ne ''){$ubps=$action{ubps};}
if($action{cycle} ne ''){$cycle=$action{cycle};}
if($action{chose} ne ''){$chose=$action{chose};}
if($action{hr} ne ''){$mhr=$action{hr};}
if($action{sec} ne ''){$msec=$action{sec};}
if($action{bs} ne ''){$bs=$action{bs};}
if($action{ql} ne ''){$ql=$action{ql};}
if($action{lmit} ne ''){$lmit=$action{lmit};}
if($action{lmit} eq 'undefined'){$lmit='10';}
if($bs eq '1'){$tmit=$dmit;$tbps=$dbps;}
if($en eq '1'){$en = 'checked';$dis='';}
if($dis eq '1'){$dis = 'checked';$en='';}
if($en_quota eq '1'){$en_quota = 'checked';$dis_quota='';}
if($dis_quota eq '1'){$dis_quota = 'checked';$en_quota='';}
if($action{tcp} ne ''){$tcp=$action{tcp};}
if($action{udp} ne ''){$udp=$action{udp};}
if($tcp ne ''&&$udp ne ''){$en_CL = 'checked';$dis_CL='';}
if($tcp eq ''&&$udp eq ''){$dis_CL = 'checked';$en_CL='';}


print qq (<html><head><meta charset="UTF-8"><script src="jquery-1.10.2.js"></script><link rel="stylesheet" href="gui.css" type="text/css"></head><body bgcolor="#336699" text="#ffffff" link="#000040">);

#假如認證失敗，就直接結束
if ( !$gLOGINRESULT ) { general_script(); exit;}

if ( $action{action} ) { maintainVS( %action ); }

print qq(<div align="center">);
#------- start to draw every form object to interact with users --------------------------------

print qq(<form name="quotaform" method="post">);
print qq (<table class="body" cellspacing="0" border="0">);

print qq (<tr><td class="bigtitle" colspan="5">User Setting</td></tr>);
print qq (<tr><td colspan="5"><hr size=1></td></tr>);

	print qq (<tr>);
#########BIND IP/ID#################################################################	
    print qq (<td class="body" valign="center" align="left" style="width:25%;">);
    print qq (IP/ID Bind :);
    print qq (</td>);
    print qq (<td class="body" valign="center" align="left" style="width:25%;">);
    print qq (<input type="radio" name="restriction" id="en" onclick="change('1')" $en>Enabled);
    print qq (<input type="radio" name="restriction" id="dis" onclick="change('0')" $dis>Disabled);
	print qq (</td>);
	print qq (<td valign="center" align="left" style="width:5px"></td>);
#########On/Off Quota###############################################################	
	print qq (<td class="body"  valign="center" align="left" style="width:25%;">);
    print qq (Quota :);
    print qq (</td>);
    print qq (<td class="body"  valign="center" align="left" style="width:25%;">);
    print qq (<input type="radio" name="restriction_quota" id="en_quota" onclick="change_quota('1')" $en_quota>Enabled);
    print qq (<input type="radio" name="restriction_quota" id="dis_quota" onclick="change_quota('0')" $dis_quota>Disabled);
    print qq (</td></tr>);
	
	print qq (<tr>);
#########IP Address#################################################################
	print qq (<td class="body"  valign="center" align="left">);
    print qq (IP address:);
    print qq (</td>);
    print qq (<td class="body"  valign="center" align="left">);
    print qq (<input type="text" id="ip" name="alldays" value="$ip" >);
    print qq (</td>);
	print qq (<td class="body" valign="center" align="left"></td>);
#########Quota Type#################################################################
	print qq (<td>Limit :&nbsp; </td>);
	print qq (<td>);
	print qq (<select class="qb" id="bs" style="WIDTH:110px" onchange="bs_change()">);
	if ($bs eq '0')
	{
		print qq (<option value="0" Selected>by Up/Down</option>);
		print qq (<option value="1">by Total</option>);
	}
	elsif ($bs eq '1')
	{
		print qq (<option value="0">by Up/Down</option>);
		print qq (<option value="1" Selected>by Total</option>);
	}
	elsif ($bs ne '0'||$bs ne '1')
	{
		print qq (<option value="0">by Up/Down</option>);
		print qq (<option value="1">by Total</option>);
	}
	print qq (</select></td></tr>);
	
	print qq (<tr>);
##########User Name################################################################
    print qq (<td class="body"  valign="center" align="left">);
    print qq (Name :</td>);
    print qq (<td class="body"  valign="center" align="left">);
    print qq (<input type="text" id="port" name="alldays" value="$port"></td>);
	print qq (<td class="body" valign="center" align="left"></td>);
##########Quota Limit##############################################################	
	print qq (<td class="body"  valign="center" align="left">);
    print qq (Limit :</td>);
	print qq (<td class="body" valign="center" align="left" colspan="2">);
	print qq (<span id="dview" style="display:'none';">);
    print qq (Downlink at :<input type="text" class="qbtext" id="dmit" style="WIDTH:45px" maxlength="4" value="$dmit" onchange="U_change()"/>);
    print qq (<select class="qb" id="dbps" style="WIDTH:60px" value="$dbps">);
	if ($dbps eq 'K')
	{
		print qq (<option value="K" Selected>KB</option>);
		print qq (<option value="M">MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T">TB</option>);
	}
	if ($dbps eq 'M')
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M" Selected>MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T">TB</option>);
	}
	if ($dbps eq 'G')
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M">MB</option>);
		print qq (<option value="G" Selected>GB</option>);
		print qq (<option value="T">TB</option>);
	}
	if ($dbps eq 'T')
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M">MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T" Selected>TB</option>);
	}
	if (!$dbps)
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M" Selected>MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T">TB</option>);
	}
    print qq (</select></span>);
    print qq (<span id="uview" style="display:'none';">);
	print qq (&nbsp;Uplink at :);
    print qq (<input type="text" class="qbtext" id="umit" style="WIDTH:45px" maxlength="4" value="$umit"/>);
    print qq (<select class="qb" id="ubps" style="WIDTH:60px" value="$ubps"><br>);
	if ($ubps eq 'K')
	{
		print qq (<option value="K" Selected>KB</option>);
		print qq (<option value="M">MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T">TB</option>);
	}
	if ($ubps eq 'M')
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M" Selected>MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T">TB</option>);
	}
	if ($ubps eq 'G')
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M">MB</option>);
		print qq (<option value="G" Selected>GB</option>);
		print qq (<option value="T">TB</option>);
	}
	if ($ubps eq 'T')
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M">MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T" Selected>TB</option>);
	}
	if (!$ubps)
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M" Selected>MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T">TB</option>);
	}
    print qq (</select></span>);
	print qq (<span id="tview" style="display:'none';">);
	print qq (Total at :);
    print qq (<input type="text" class="qbtext" id="tmit" style="WIDTH:45px" maxlength="4" value="$tmit"/>);
    print qq (<select class="qb" id="tbps" style="WIDTH:60px" value="$tbps">);
	if ($tbps eq 'K')
	{
		print qq (<option value="K" Selected>KB</option>);
		print qq (<option value="M">MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T">TB</option>);
	}
	if ($tbps eq 'M')
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M" Selected>MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T">TB</option>);
	}
	if ($tbps eq 'G')
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M">MB</option>);
		print qq (<option value="G" Selected>GB</option>);
		print qq (<option value="T">TB</option>);
	}
	if ($tbps eq 'T')
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M">MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T" Selected>TB</option>);
	}
	if (!$tbps)
	{
		print qq (<option value="K">KB</option>);
		print qq (<option value="M" Selected>MB</option>);
		print qq (<option value="G">GB</option>);
		print qq (<option value="T">TB</option>);
	}
    print qq (</select></span>);
	print qq (</td></tr>);
	
	print qq (<tr>);
##########User Password##############################################################
    print qq (<td class="body"  valign="center" align="left" style="width:25%">);
    print qq (Password :);
    print qq (<td class="body"  valign="center" align="left" style="width:25%">);
    print qq (<input type="text" id="pwd" name="alldays" value="$pwd" >);
	print qq (</td>);
	print qq (<td class="body" valign="center" align="left"></td>);
##########Quota Cycle################################################################
    print qq (<td> Cycle : </td><td valign="center" align="left"><select class="qb" id="cycle" style="WIDTH:105px" onChange="cycleChange();">);
	if ($cycle eq '0')
	{
		print qq (<option value="0" Selected>non-cyclic</option>);
		print qq (<option value="1">Daily</option>);
		print qq (<option value="7">Weekly</option>);
		print qq (<option value="30">Monthly</option>);
	}
	elsif ($cycle eq '1')
	{
		print qq (<option value="0">non-cyclic</option>);
		print qq (<option value="1" Selected>Daily</option>);
		print qq (<option value="7">Weekly</option>);
		print qq (<option value="30">Monthly</option>);
	}
	elsif ($cycle eq '7')
	{
		print qq (<option value="0">non-cyclic</option>);
		print qq (<option value="1">Daily</option>);
		print qq (<option value="7" Selected>Weekly</option>);
		print qq (<option value="30">Monthly</option>);
	}
	elsif ($cycle eq '30')
	{
		print qq (<option value="0">non-cyclic</option>);
		print qq (<option value="1">Daily</option>);
		print qq (<option value="7">Weekly</option>);
		print qq (<option value="30" Selected>Monthly</option>);
	}
	elsif (!$cycle)
	{
		print qq (<option value="0">non-cyclic</option>);
		print qq (<option value="1">Daily</option>);
		print qq (<option value="7">Weekly</option>);
		print qq (<option value="30">Monthly</option>);
	}
    print qq (</select>);
	
	my @week=("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat");
	my $weeknum=0;
	print qq (<span id="week" style="display:none;">);
    foreach my $day ( @week )
    {
         if ($cycle eq '7' && $weeknum eq $chose)
		{
			print qq (<INPUT type="radio" name="week" id="selectDay" value="$day" checked/> $day&#32&#32);
		}
		else
		{
			print qq (<INPUT type="radio" name="week" id="selectDay" value="$day" /> $day&#32&#32);
		}
		#print qq (<INPUT type="radio" name="week" id="selectDay" value="$day"/> $day&#32&#32);
		#if($weeknum eq 3){print qq(<br>);}
		#if($weeknum eq 5){print qq(<br>);}
		$weeknum++;
    }
    print qq (</span>);
	print qq (<span id="monthly" style="visibility:hidden;">Day :);
    print qq (<select class="qb" id="number" style="WIDTH:50px">);
    foreach my $month (1..30)
    {
        if ($month < 10)
        {
            if ($cycle eq '30' && $month eq $chose)
			{
				print qq (<option value="$month" Selected>0$month</option>);
			}
			else
			{
				print qq (<option value="$month">0$month</option>);
			}
        }else
        {
            if ($cycle eq '30' && $month eq $chose)
			{
				print qq (<option value="$month" Selected>$month</option>);
			}
			else
			{
				print qq (<option value="$month">$month</option>);
			}
        }
    }
    print qq (</select></span>);
	
	print qq (</td></tr>);
	
	print qq (<tr>);	
    print qq (<td class="body"  valign="center" align="left">);
	print qq (E-mail :);
	print qq (</td>);
    print qq (<td class="body"  valign="center" align="left">);
	print qq (<input type="text" id="mail" name="alldays" value="$mail" >);
	print qq (</td>);
	print qq (<td class="body" valign="center" align="left"></td>);
##########Quota Reset Time#########################################################
    print qq (<td> Reset at :</td>);
    print qq (<td valign="center" align="left"><select class="qb" id="hr" style="WIDTH:50px;">);
    foreach my $hr (0..23)
	{
		if($hr < 10)
		{
			$myhr = "0$hr";
			$myhr2 = "$mhr";
			if ($myhr eq $myhr2)
			{
				print qq(<option value="0$hr" Selected>0$hr</option>);
			}
			else
			{
				print qq(<option value="0$hr">0$hr</option>);
			}
		}
		if($hr > 9)
		{
			$myhr = "$hr";
			$myhr2 = "$mhr";
			if ($myhr eq $myhr2)
			{
				print qq(<option value="$hr" Selected>$hr</option>);
			}
			else
			{
				print qq(<option value="$hr">$hr</option>);
			}
		}
	}
    print qq (</select>:<select class="qb" id="sec" style="WIDTH:50px">);
    foreach my $sec (0..59)
	{
		if($sec > 9)
		{
			$mysec = "$sec";
			$mysec2 = "$msec";
			if ($mysec eq $mysec2)
			{
				print qq(<option value="$sec" Selected>$sec</option>);
			}
			else{print qq(<option value="$sec">$sec</option>);}
		}
	
		if($sec < 10)
		{
			$mysec = "0$sec";
			$mysec2 = "$msec";
			if ($mysec eq $mysec2)
			{
				print qq(<option value="0$sec" Selected>0$sec</option>);
			}
			else{print qq(<option value="0$sec">0$sec</option>);}
		}
	}
    print qq (</select></td></tr>);
	
	print qq (<tr>);
    print qq (<td class="body"  valign="center" align="left"></td>);
    print qq (<td class="body"  valign="center" align="left"></td>);
	print qq (<td class="body" valign="center" align="left"></td>);
##########Quota Reset Time#########################################################	
	print qq (<td>When Quota full :&nbsp; </td>);
	print qq (<td>);
	print qq (<select class="qb" id="ql" style="WIDTH:110px" onchange="WQFChange()">);
	if ($ql eq '0')
	{
		print qq (<option value="0" Selected>Block</option>);
		print qq (<option value="1">Limit speed</option>);
	}
	elsif ($ql eq '1')
	{
		print qq (<option value="0">Block</option>);
		print qq (<option value="1" Selected>Limit speed</option>);
	}
	elsif ($ql ne '0'||$ql ne '1')
	{
		print qq (<option value="0">Block</option>);
		print qq (<option value="1">Limit speed</option>);
	}
	print qq (</select>);
	print qq (<span id="show_limit" style="visibility:hidden;"> at :);
    print qq (<input type="text" class="qbtext" id="lmit" style="WIDTH:45px" maxlength="4" value="$lmit"/> Packet/s);
    print qq (</span></td></tr>);
#################Connection Limit###############################################
	print qq (<tr>);	
    print qq (<td class="body" valign="center" align="left" style="width:25%;">);
    print qq (Connection Limit :);
    print qq (</td>);
    print qq (<td class="body" valign="center" align="left" style="width:25%;">);
    print qq (<input type="radio" name="restriction_CL" id="en_CL" onclick="change_CL('1')" $en_CL>Enabled);
    print qq (<input type="radio" name="restriction_CL" id="dis_CL" onclick="change_CL('0')" $dis_CL>Disabled);
	print qq (</td>);
	print qq (<td valign="center" align="left" style="width:5px"></td>);
##################################################################################	
	print qq (<td class="body"  valign="center" align="left" style="width:25%;">);
#    print qq (Quota :);
    print qq (</td>);
    print qq (<td class="body"  valign="center" align="left" style="width:25%;">);
#    print qq (<input type="radio" name="restriction_quota" id="en_quota" onclick="change_quota('1')" $en_quota>Enabled);
#    print qq (<input type="radio" name="restriction_quota" id="dis_quota" onclick="change_quota('0')" $dis_quota>Disabled);
    print qq (</td></tr>);
#################TCP Connection Limit###############################################
	print qq (<tr>);	
    print qq (<td class="body"  valign="center" align="left">);
    print qq (TCP Limit :</td>);
    print qq (<td class="body"  valign="center" align="left">);
    print qq (<input class="qbtext" type="text" id="tcp" name="alldays" value="$tcp" style="width:45">Connections</td>);
	print qq (<td class="body" valign="center" align="left"></td>);
##################################################################################	
	print qq (<td class="body"  valign="center" align="left" style="width:25%;">);
#    print qq (Quota :);
    print qq (</td>);
    print qq (<td class="body"  valign="center" align="left" style="width:25%;">);
#    print qq (<input type="radio" name="restriction_quota" id="en_quota" onclick="change_quota('1')" $en_quota>Enabled);
#    print qq (<input type="radio" name="restriction_quota" id="dis_quota" onclick="change_quota('0')" $dis_quota>Disabled);
    print qq (</td></tr>);
#################UDP Connection Limit###############################################
	print qq (<tr>);	
    print qq (<td class="body"  valign="center" align="left">);
    print qq (UDP Limit :</td>);
    print qq (<td class="body"  valign="center" align="left">);
    print qq (<input class="qbtext" type="text" id="udp" name="alldays" value="$udp" style="width:45">Connections</td>);
	print qq (<td class="body" valign="center" align="left"></td>);
##################################################################################	
	print qq (<td class="body"  valign="center" align="left" style="width:25%;">);
#    print qq (Quota :);
    print qq (</td>);
    print qq (<td class="body"  valign="center" align="left" style="width:25%;">);
#    print qq (<input type="radio" name="restriction_quota" id="en_quota" onclick="change_quota('1')" $en_quota>Enabled);
#    print qq (<input type="radio" name="restriction_quota" id="dis_quota" onclick="change_quota('0')" $dis_quota>Disabled);
    print qq (</td></tr>);
###################################################################################

print qq (<tr><td colspan="5"><hr size=1></td></tr>);
print qq (<tr><td colspan="5">);
print qq (<div class="body" align="center">);
print qq (<input type="button" class="qb" align="center" value="Save" style="width:60" onClick="myalert()">);
print qq (<input type="button" class="qb" align="center" value="Cancel" style="width:60" onClick="window.close()">);
print qq (<div>);
print qq (</td></tr>);

print qq (</td></tr>);
print qq (</table>);

print qq(<input type="hidden" name="action" value="">);
print qq(</form></div>);

print << "QB_AUTH";
<script language="javascript">
	function change(oo)
    {
        if (oo == '0')
        {
            document.getElementById("ip").disabled = true;
            document.getElementById("ip").value = '';
        }else
        {
            document.getElementById("ip").disabled = false;
            document.getElementById("ip").value = '';
        }
    }
	
	function change_CL(oo)
    {
        if (oo == '0')
        {
            document.getElementById("tcp").disabled = true;
            document.getElementById("tcp").value = '';
			document.getElementById("udp").disabled = true;
            document.getElementById("udp").value = '';
        }else
        {
            document.getElementById("tcp").disabled = false;
			document.getElementById("udp").disabled = false;
        }
    }
	
	function change_quota(oo)
    {
        if (oo == '0')
        {
			\$("\#dmit").prop('readOnly',true);
			\$("\#umit").prop('readOnly',true);
			\$("\#tmit").prop('readOnly',true);
            document.getElementById("bs").disabled = true;
            //document.getElementById("dmit").value = '';
			//document.getElementById("umit").value = '';
			//document.getElementById("tmit").value = '';
			document.getElementById("dbps").disabled = true;
			document.getElementById("ubps").disabled = true;
			document.getElementById("tbps").disabled = true;
			
			document.getElementById("cycle").disabled = true;
			document.getElementById("hr").disabled = true;
			document.getElementById("sec").disabled = true;
			document.getElementById("number").disabled = true;
			
			document.getElementById("ql").disabled = true;
			//document.getElementById("lmit").value = '';
			document.getElementById("lmit").disabled = true;			
        }else
        {
			\$("\#dmit").prop('readOnly',false);
			\$("\#umit").prop('readOnly',false);
			\$("\#tmit").prop('readOnly',false);
            document.getElementById("bs").disabled = false;
            //document.getElementById("dmit").value = '';
			//document.getElementById("umit").value = '';
			//document.getElementById("tmit").value = '';
			document.getElementById("dbps").disabled = false;
			document.getElementById("ubps").disabled = false;
			document.getElementById("tbps").disabled = false;			
			document.getElementById("cycle").disabled = false;
			document.getElementById("hr").disabled = false;
			document.getElementById("sec").disabled = false;
			document.getElementById("number").disabled = false;			
			document.getElementById("ql").disabled = false;
			//document.getElementById("lmit").value = '';
			document.getElementById("lmit").disabled = false;
			
			if (document.getElementById("cycle").value == '0' )
			{
				document.getElementById("hr").disabled = true;
				document.getElementById("sec").disabled = true;
				document.getElementById("week").style.display = 'none';
				document.getElementById("monthly").style.visibility = 'hidden';
			}else
			{
				document.getElementById("hr").disabled = false;
				document.getElementById("sec").disabled = false;
			}			
        }
    }

	function U_change()
    {
        var choose = document.getElementById('bs').value;
		var dmit = document.getElementById('dmit');
		var umit = document.getElementById('umit');
		var dbps = document.getElementById('dbps');
		var ubps = document.getElementById('ubps');
		if(choose == '1')
		{			
			umit.value=dmit.value;
			ubps.value=dbps.value;
		}
    }
	
	function bs_change()
	{
		var choose = document.getElementById('bs').value;
		var dmit = document.getElementById('dmit');
		var umit = document.getElementById('umit');
		var dbps = document.getElementById('dbps');
		var ubps = document.getElementById('ubps');
		var tmit = document.getElementById('tmit');
		var tbps = document.getElementById('tbps');
		
		var tview = document.getElementById('tview');
		var dview = document.getElementById('dview');
		var uview = document.getElementById('uview');
		if(choose == '1')
		{
			//tmit.style.display='';
			tview.style.display='';
			//umit.readOnly=true;
			//umit.value=dmit.value;
			//ubps.value=dbps.value;
			//dmit.style.display='none';
			dview.style.display='none';
			//umit.style.display='none';
			uview.style.display='none';
		}
		else
		{
			//umit.readOnly=false;
			//tmit.style.display='none';
			tview.style.display='none';
			//umit.readOnly=true;
			//umit.value=dmit.value;
			//ubps.value=dbps.value;
			//dmit.style.display='';
			dview.style.display='';
			//umit.style.display='';
			uview.style.display='';
		}
	}

	function WQFChange()
	{
		var choose = document.getElementById('ql').value;
		var show = document.getElementById('show_limit');
		if(choose == '1')
		{
			show.style.visibility='';
		}
		else{show.style.visibility='hidden';}
	}
	
	function myalert()
	{
		var ip = document.getElementById('ip');
		var name = document.getElementById('port');
		var pwd = document.getElementById('pwd');
		var mail = document.getElementById('mail');
		var en = document.getElementById('en');
		var dis = document.getElementById('dis');
		var en_quota = document.getElementById('en_quota');
		var dis_quota = document.getElementById('dis_quota');
		
		var en_CL = document.getElementById('en_CL');
		var dis_CL = document.getElementById('dis_CL');
		var tcp = document.getElementById('tcp');
		var udp = document.getElementById('udp');
		
		var dmit = document.getElementById('dmit');
		var dbps = document.getElementById('dbps');
		var umit = document.getElementById('umit');
		var ubps = document.getElementById('ubps');
		var tmit = document.getElementById('tmit');
		var tbps = document.getElementById('tbps');
		
		var cycle = document.getElementById('cycle');
		var hr = document.getElementById('hr');
		var sec = document.getElementById('sec');
		var number = document.getElementById('number');
		
		var radio = document.getElementsByName("week");
        var radio_data='';
        for (var i = 0; i < radio.length; i++)
        {
            if (radio[i].checked == true)
            radio_data=radio[i].value;
        }
		var bs = document.getElementById('bs');
		var ql = document.getElementById('ql');
		var lmit = document.getElementById('lmit');
		
		if(bs.value == '1')
		{
			dmit.value=tmit.value;
			umit.value=tmit.value;
			dbps.value=tbps.value;
			ubps.value=tbps.value;
		}else{tmit.value=dmit.value;tbps.value=dbps.value;}
		
		if(dmit.value > 909 && dbps.value == 'T')
		{
			alert('Limit Downlink must <= 909 TB');
			return;
		}
        if(umit.value > 909 && ubps.value == 'T')
		{
			alert('Limit Uplink must <= 909 TB');
			return;
		}
		if(en_quota.checked==true && (dmit.value == '' || umit.value == '' || tmit.value ==''))
		{
			alert('Must to type limit value');
			return;
		}
		if(cycle.value == '7' && radio_data==''){alert('Must to select days'); return;}
		
		oip = window.opener.document.getElementById('ip');
		oname = window.opener.document.getElementById('port');
		opwd = window.opener.document.getElementById('pwd');
		omail = window.opener.document.getElementById('mail');
		oen = window.opener.document.getElementById('en');
		odis = window.opener.document.getElementById('dis');
		
		otcp = window.opener.document.getElementById('tcp');
		oudp = window.opener.document.getElementById('udp');
		
		odmit = window.opener.document.getElementById('dmit1');
		odbps = window.opener.document.getElementById('dbps1');
		oumit = window.opener.document.getElementById('umit1');
		oubps = window.opener.document.getElementById('ubps1');
		
		ocycle = window.opener.document.getElementById('cycle1');
		ohr = window.opener.document.getElementById('hr1');
		osec = window.opener.document.getElementById('sec1');
		onumber = window.opener.document.getElementById('number1');
		oradio = window.opener.document.getElementsByName("week1");
		obs = window.opener.document.getElementById("bs");
		oql = window.opener.document.getElementById("ql");
		olmit = window.opener.document.getElementById("lmit1");
		//alert('proute windows'+obs.value);
		
		oip.value = ip.value;
		oname.value = name.value;
		opwd.value = pwd.value;
		omail.value = mail.value;
		if(en.checkd == true){oen.checked = true;}else{oen.checked = false;}
		if(dis.checked == true){odis.checked = true;}else{odis.checked = false;}
		if(en_CL.checked == true){otcp.value = tcp.value; oudp.value=udp.value;}
		if(dis_CL.checked == true){otcp.value = ''; oudp.value='';}
		
		if(en_quota.checked == true){
		odmit.value = dmit.value;
		odbps.value = dbps.value;
		oumit.value = umit.value;
		oubps.value = ubps.value;
		ocycle.value = cycle.value;
		ohr.value = hr.value;
		osec.value = sec.value;
		onumber.value = number.value;
		for (var i = 0; i < oradio.length; i++)
        {
            if (oradio[i].value == radio_data)
			{
				oradio[i].checked = true;
			}
        }
		obs.value = bs.value;
		oql.value = ql.value;
		olmit.value = lmit.value;
		}else{
		odmit.value = '0';
		odbps.value = '0';
		oumit.value = '0';
		oubps.value = '0';
		}
		window.opener.AddSchedule();
		window.close();
	}

function cycleChange()
{
    if (document.getElementById("cycle").value == '0' )
    {
        document.getElementById("hr").disabled = true;
        document.getElementById("sec").disabled = true;
        document.getElementById("week").style.display = 'none';
        document.getElementById("monthly").style.visibility = 'hidden';
    }else
    {
        document.getElementById("hr").disabled = false;
        document.getElementById("sec").disabled = false;
    }
    
    if (document.getElementById("cycle").value == '7' )
    {
        document.getElementById("week").style.display = 'block';
        document.getElementById("monthly").style.visibility  = 'hidden';
    }else if (document.getElementById("cycle").value == '30' )
    {
        document.getElementById("week").style.display = 'none';
        document.getElementById("monthly").style.visibility  = '';
    }else
    {
        document.getElementById("week").style.display = 'none';
        document.getElementById("monthly").style.visibility  = 'hidden';
    }
}
</script>
QB_AUTH
if($dis eq 'checked'){print qq(<SCRIPT LANGUAGE="JavaScript">change('0');</SCRIPT>);}else{print qq(<SCRIPT LANGUAGE="JavaScript">change('1');</SCRIPT>);}
if($dis_quota eq 'checked'){print qq(<SCRIPT LANGUAGE="JavaScript">change_quota('0');</SCRIPT>);}else{print qq(<SCRIPT LANGUAGE="JavaScript">change_quota('1');</SCRIPT>);}
if($dis_CL eq 'checked'){print qq(<SCRIPT LANGUAGE="JavaScript">change_CL('0');</SCRIPT>);}else{print qq(<SCRIPT LANGUAGE="JavaScript">change_CL('1');</SCRIPT>);}
print qq(<SCRIPT LANGUAGE="JavaScript">cycleChange(); U_change(); bs_change(); WQFChange();</SCRIPT>);
print qq(</body></html>);
