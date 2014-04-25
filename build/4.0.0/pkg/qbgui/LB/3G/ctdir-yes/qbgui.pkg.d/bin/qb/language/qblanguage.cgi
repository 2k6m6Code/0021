#!/usr/bin/perl
# require ("/usr/local/apache/qb/language/qblanguage.cgi");
# @qblang = QBlanguage();
# Find String command : find .| xargs grep "qblang\[123\]"
#<meta charset="UTF-8">
sub QBlanguage{
use CGI;
$cgi = new CGI;
$langcookie = $cgi->cookie('locale');

my @qblanguage;
if($langcookie eq "en_US")
{
$qblanguage[0]  ="Auto Refresh Per";   #dashboard.lib
$qblanguage[1]  ="seconds";
$qblanguage[2]  ="System Status";
$qblanguage[3]  ="System Time";
$qblanguage[4]  ="System Uptime";
$qblanguage[5]  ="Firmware Version";
$qblanguage[6]  ="System Usage";
$qblanguage[7]  ="CPU Usage";
$qblanguage[8]  ="Memory Usage";
$qblanguage[9]  ="Cache Usage";
$qblanguage[10] ="Ramdisk Usage";
$qblanguage[11] ="Active Sessions";
$qblanguage[12] ="Device Information";
$qblanguage[13] ="Host Name";
$qblanguage[14] ="Model Name";
$qblanguage[15] ="MAC Address Range";
$qblanguage[16] ="Register Information";
$qblanguage[17] ="Serial Number";
$qblanguage[18] ="Registered Date";
$qblanguage[19] ="Not registered";
$qblanguage[20] ="Register Within";
$qblanguage[21] ="License Expiry";
$qblanguage[22] ="Warranty Expiry";
$qblanguage[23] ="WAN Link";
$qblanguage[24] ="Status";

$qblanguage[25] ="Edit"; #showbasic.lib
$qblanguage[26] ="Enable";
$qblanguage[27] ="3G Information";
$qblanguage[28] ="Interface";
$qblanguage[29] ="Name";
$qblanguage[30] ="Gateway";
$qblanguage[31] ="System IP";
$qblanguage[32] ="Healthcheck IP";
$qblanguage[33] ="Subnet";
$qblanguage[34] ="Down/Up";
$qblanguage[35] ="Version";
$qblanguage[36] ="Additional Subnet";
$qblanguage[37] ="Additional Subnet2";
$qblanguage[38] ="Proxy IP";
$qblanguage[39] ="Proxy Name";
$qblanguage[40] ="Proxy Port";


$qblanguage[41] ="Link Health Check";   #hcconf.lib
$qblanguage[42] ="Link Check Method";
$qblanguage[43] ="Ping to Healthcheck IP";
$qblanguage[44] ="Ping and Trace Route to Healthcheck IP";
$qblanguage[45] ="Port Checking to Healthcheck IP";
$qblanguage[46] ="Port Checking and Trace Route to Healthcheck IP";
$qblanguage[47] ="Advanced Setting";
$qblanguage[48] ="Disable Passive Line Check";
$qblanguage[49] ="Port";
$qblanguage[50] ="Ping Time Out";
$qblanguage[51] ="Traceroute Time Out";
$qblanguage[52] ="Connection Time Out";
$qblanguage[53] ="Healthcheck Interval";
$qblanguage[54] ="Save";


$qblanguage[55] ="Public IP";     #vs.lib
$qblanguage[56] ="ISP ID";
$qblanguage[57] ="Add";
$qblanguage[58] ="Update";
$qblanguage[59] ="Multi-add";
$qblanguage[60] ="Link IP Binding";
$qblanguage[61] ="Public IP to bind";

$qblanguage[62] ="Link Configuration"; #showbasic.lib

$qblanguage[63] ="MPV Configuration"; #mpv.lib
$qblanguage[64] ="Enabled";
$qblanguage[65] ="ID";
$qblanguage[66] ="NIC";
$qblanguage[67] ="TVLI";
$qblanguage[68] ="TVRI";
$qblanguage[69] ="THLI";
$qblanguage[70] ="THRI";
$qblanguage[71] ="PORT";
$qblanguage[72] ="THRN";
$qblanguage[73] ="MTU";
$qblanguage[74] ="MSS";
$qblanguage[75] ="NAT";
$qblanguage[76] ="ENC";
$qblanguage[77] ="Algorithm";
$qblanguage[78] ="COMP";
$qblanguage[79] ="Add";

$qblanguage[80] ="Add";  #showbasic.lib
$qblanguage[81] ="TMV Configuration"; #tmv.lib

$qblanguage[82] ="Role"; #tmv.lib
$qblanguage[83] ="Add";

$qblanguage[84] ="THSI"; #ipsec.lib
$qblanguage[85] ="Isakmp_SA";  #ipsec.lib
$qblanguage[86] ="Ph1_Encryption";
$qblanguage[87] ="Hash";
$qblanguage[88] ="DH_Group";
$qblanguage[89] ="IPSec_SA";
$qblanguage[90] ="Ph2_Encryption";
$qblanguage[91] ="Authentition";
$qblanguage[92] ="PF_Group";
$qblanguage[93] ="IPSec Configuration";
$qblanguage[94] ="Add"; #ipsec.lib

$qblanguage[95] ="LAN IP binding, Static Routes and DHCP setting";   #zone.lib
$qblanguage[96] ="Related ISP";
$qblanguage[97] ="DHCP";
$qblanguage[98] ="Network";
$qblanguage[99] ="IPver";
$qblanguage[100]="On";
$qblanguage[101]="Off";
$qblanguage[102]="Auto";
$qblanguage[103]="Disabled";
$qblanguage[104]="None";
$qblanguage[105]="Internal Zone";
$qblanguage[106]="related to";
$qblanguage[107]="IP Version";
$qblanguage[108]="NIC Speed";
$qblanguage[109]="Interface IP";
$qblanguage[110]="Note";
$qblanguage[111]="Create";
$qblanguage[112]="Batch Create";
$qblanguage[113]="Set DHCP";   #zone.lib

$qblanguage[114]="Static MAC Binding"; #arp.lib
$qblanguage[115]="Multi-Add";
$qblanguage[116]="Restore"; #arp.lib dns.lib

$qblanguage[117]="Wireless LAN Configuration"; #wireless.lib
$qblanguage[118]="Basic Parameters";
$qblanguage[119]="Enable Wireless";
$qblanguage[120]="Wireless Name(SSID)";
$qblanguage[121]="Hide SSID";
$qblanguage[122]="Wireless Mode";
$qblanguage[123]="Channel Selection";
$qblanguage[124]="Operation Channel";
$qblanguage[125]="Security Parameters";
$qblanguage[126]="Encrypt Type";
$qblanguage[127]="Auth Mode";
$qblanguage[128]="The WEP keys are used to encrypt data.";
$qblanguage[129]="Clients must use the same key for data transmission.";
$qblanguage[130]="You can enter";
$qblanguage[131]="5 or 13 ASCII characters";
$qblanguage[132]='10 or 26 hexadecimal characters ("0-9","a-f","A-F").';
$qblanguage[133]="Key";
$qblanguage[134]="The key is used to encrypt data.";
$qblanguage[135]="Clients must use the same key for data transmission.";
$qblanguage[136]="8 to 63 ASCII characters";
$qblanguage[137]="64 hexadecimal characters";
$qblanguage[138]="Pre-Shared Key";
$qblanguage[139]="Apply";

$qblanguage[140]="ARP proxy"; #zone.lib

$qblanguage[141]="BRIDGE"; #zone.lib
$qblanguage[142]="ARP PROXY"; #zone.lib
$qblanguage[143]="Public IP reused as Pass Through IP for Bridge"; #zone.lib
$qblanguage[144]="Pass Through IP registration for ARP Proxy"; #zone.lib

$qblanguage[145]="VlanID"; #vlan.lib
$qblanguage[146]="MAC";
$qblanguage[147]="VLAN Setting";

$qblanguage[148]="Update"; #qoslan.lib
$qblanguage[149]="MPV Bandwidth Shaper"; #qosisp.lib

$qblanguage[150]="Source"; #qoslan.lib
$qblanguage[151]="Download";
$qblanguage[152]="Priority";
$qblanguage[153]="Type";
$qblanguage[154]="Download Bandwidth";
$qblanguage[155]="Upload Bandwidth";
$qblanguage[156]="Usage Type";
$qblanguage[157]="Share";
$qblanguage[158]="Individual";
$qblanguage[159]="IP Bandwidth Shaper";
$qblanguage[160]="Hosts"; #host.lib

$qblanguage[161]="Address Detail";
$qblanguage[162]="Add";

$qblanguage[163]="Service Configuration";
$qblanguage[164]="Service";
$qblanguage[165]="Delete";
$qblanguage[166]="Protocol";
$qblanguage[167]="Information";
$qblanguage[168]="Protocol defined";
$qblanguage[169]="Description";

$qblanguage[170]="Schedule";

$qblanguage[171]="Outbound Pool Configuration";
$qblanguage[172]="Pool ID";
$qblanguage[173]="Link Info";
$qblanguage[174]="Backup Pool";
$qblanguage[175]="By Packet";
$qblanguage[176]="By Connection";
$qblanguage[177]="Balance Mode";
$qblanguage[178]="Pool Name";
$qblanguage[179]="Balance Algorithm";
$qblanguage[180]="Weight";
$qblanguage[181]="DSIP";

$qblanguage[182]="QoS Class";

$qblanguage[183]="Server Mapping";
$qblanguage[184]="Virtual IP";
$qblanguage[185]="Real Servers";
$qblanguage[186]="Real Service";

$qblanguage[187]="Policy Routing";
$qblanguage[188]="Advanced Setting";

$qblanguage[189]="Application Filtering";

$qblanguage[190]="L2TP IPsec VPN Configuration";
$qblanguage[191]="Enable L2TP IPsec";
$qblanguage[192]="VPN Server IP";
$qblanguage[193]="IP release range";
$qblanguage[194]="Pre-share key";

$qblanguage[195]="L2TP IPsec Authentication";
$qblanguage[196]="Username";
$qblanguage[197]="Assigned IP";
$qblanguage[198]="Login IP";
$qblanguage[199]="Use device";
$qblanguage[200]="Kick Out";
$qblanguage[201]="Password";
$qblanguage[202]="Confirm Password";
$qblanguage[203]="Assign IP";

$qblanguage[204]="PPTP Server Configuration";
$qblanguage[205]="Enable QB PPTP Server";
$qblanguage[206]="PPTP Encryption";
$qblanguage[207]="PPTP Compression";
$qblanguage[208]="Authentication Method";
$qblanguage[209]="Max client connections";
$qblanguage[210]="Disconnect idle time";
$qblanguage[211]="DNS IP";
$qblanguage[212]="IP release range";

$qblanguage[213]="PPTP User Authentication";
$qblanguage[214]="SSL Configuration";
$qblanguage[215]="SSL Server State";
$qblanguage[216]="Enable QB SSL Server";
$qblanguage[217]="General Setting";
$qblanguage[218]="VPN Server IP";
$qblanguage[219]="VPN Net Range";
$qblanguage[220]="VPN Netmask";
$qblanguage[221]="Full Access Settings";
$qblanguage[222]="MAX Client";
$qblanguage[223]="Available Subnet";
$qblanguage[224]="Lease Subnet";
$qblanguage[225]="SSL User Authentication";
$qblanguage[226]="Real IP";
$qblanguage[227]="VPN IP";
$qblanguage[228]="Bytes Received";
$qblanguage[229]="Bytes Sent";
$qblanguage[230]="SSL Portal Setting";
$qblanguage[231]="General Setting";
$qblanguage[232]="Window title";
$qblanguage[233]="Login Page Message";
$qblanguage[234]="Login Logo";

$qblanguage[235]="Multi-DNS Configuration";
$qblanguage[236]="General Setting";
$qblanguage[237]="ISP Selection";
$qblanguage[238]="Domain Selection";
$qblanguage[239]="Domain";
$qblanguage[240]="Domain IP";
$qblanguage[241]="Domain Level Settings";
$qblanguage[242]="Host Properties";
$qblanguage[243]="Host";
$qblanguage[244]="Value";

$qblanguage[245]="DoS Prevention";
$qblanguage[246]="Privileged List to bypass checks below";
$qblanguage[247]="Connection Overflow Detection";
$qblanguage[248]="Privileged List to bypass COD";
$qblanguage[249]="Log Rate";
$qblanguage[250]="minute";
$qblanguage[251]="hour";
$qblanguage[252]="Log Prefix";
$qblanguage[253]="Drop Packet if matched";
$qblanguage[254]="Can not go over";
$qblanguage[255]="Connections per IP";
$qblanguage[256]="Fuzzy Ping Flooding Detection";
$qblanguage[257]="Privileged List to bypass FPFD";
$qblanguage[258]="Lower";
$qblanguage[259]="Upper";
$qblanguage[260]="Port Scan Detection";
$qblanguage[261]="Privileged List to bypass PSD";
$qblanguage[262]="Weight Threshold";
$qblanguage[263]="High Port Weight";
$qblanguage[264]="Low Port Weight";
$qblanguage[265]="Delay Thershold";
$qblanguage[266]="Quota Overflow Detection";
$qblanguage[267]="Privileged List to bypass QOD";
$qblanguage[268]="If quota";
$qblanguage[269]="Set TOS value as";
$qblanguage[270]="DROP Them";

$qblanguage[271]="HA Config";
$qblanguage[272]="High Availablility is not enabled.";
$qblanguage[273]="Enable HA";
$qblanguage[274]="High Availability";
$qblanguage[275]="HA Management Message";
$qblanguage[276]="Launch HA on Boot";
$qblanguage[277]="Primary";
$qblanguage[278]="Secondary";
$qblanguage[279]="Auto Fail Over";
$qblanguage[280]="Auto Switch Back";
$qblanguage[281]="Fail on LAN Interface";
$qblanguage[282]="Host FAILOVER Timeout";
$qblanguage[283]="Network FAILOVER Timeout";
$qblanguage[284]="Enable Virtual MAC";
$qblanguage[285]="Floating IP";
$qblanguage[286]="Standby IP of Primary";
$qblanguage[287]="Standby IP of Secondary";
$qblanguage[288]="HA LAN Check Targets";
$qblanguage[289]="Check Mode";
$qblanguage[290]="Show Status";
$qblanguage[291]="Force Change Mode";
$qblanguage[292]="Save Setting";
$qblanguage[293]="Apply Setting";

$qblanguage[294]="Admin Setting";
$qblanguage[295]="Maximum User";
$qblanguage[296]="Edit User Account";
$qblanguage[297]="Https Port Number";
$qblanguage[298]="Hostname";
$qblanguage[299]="Hostname on LCM";
$qblanguage[300]="E-mail Alert";

$qblanguage[301]="Appliance Registration";
$qblanguage[302]="Company Name";
$qblanguage[303]="Contact E-mail";
$qblanguage[304]="Serial Number";
$qblanguage[305]="Registered Date";
$qblanguage[306]="Register";
$qblanguage[307]="QB Serial Number";

$qblanguage[308]="Firmware";
$qblanguage[309]="Configuration";
$qblanguage[310]="UPG and CMS Key";
$qblanguage[311]="Upload Config";
$qblanguage[312]="Upload Firmware";
$qblanguage[313]="Menu for Firmware";
$qblanguage[314]="Menu for Config";
$qblanguage[315]="Menu for CMS";
$qblanguage[316]="Menu for Config";
$qblanguage[317]="Menu for Firmware";
$qblanguage[318]="Upload Upgrade Package";
$qblanguage[319]="Upload Fs/Lib Image Package";
$qblanguage[320]="Launch Upgrade Process";
$qblanguage[321]="Backup Config";
$qblanguage[322]="FTP Server";
$qblanguage[323]="Auto Save";
$qblanguage[324]="Upload Management Key";
$qblanguage[325]="Download Management Key";
$qblanguage[326]="Upload UPG";
$qblanguage[327]="Select Config. Set";
$qblanguage[328]="Config. Set";
$qblanguage[329]="Save As";
$qblanguage[330]="Config. File";
$qblanguage[331]="Upload to";
$qblanguage[332]="Please Choose!!";
$qblanguage[333]="Select Upgrade Package";
$qblanguage[334]="Upgrade File";
$qblanguage[335]="Select Upgrade Image";
$qblanguage[336]="Launching Upgrade Procedure";
$qblanguage[337]="Select Upload Key";
$qblanguage[338]="Export Config. to FTP Server";
$qblanguage[339]="FTP Mode";
$qblanguage[340]="Server address";
$qblanguage[341]="Login username";
$qblanguage[342]="Login password";
$qblanguage[343]="Upload directory";
$qblanguage[344]="Enable Auto-Save";
$qblanguage[345]="Configuration Via CMS";
$qblanguage[346]="Note:This Function is only for Bonding Client to Server with CMS!!";
$qblanguage[347]="Select Upload UPG";
$qblanguage[348]="Select Number";
$qblanguage[349]="Start";
$qblanguage[350]="Stop";
$qblanguage[351]="Back";

$qblanguage[352]="DNS resolver";
$qblanguage[353]="QB works as DNS Server";
$qblanguage[354]="with Authoritative DNS";
$qblanguage[355]="Dynamic Routing Configuration";
$qblanguage[356]="Dynamic Routing State";
$qblanguage[357]="Enable Dynamic Routing";
$qblanguage[358]="Method";
$qblanguage[359]="Route Metric";
$qblanguage[360]="Route Update Time";
$qblanguage[361]="Monitor";
$qblanguage[362]="Monitor Port";

$qblanguage[363]="External Storage";
$qblanguage[364]="Format Hard Disk";
$qblanguage[365]="Analyser Hard Disk";

$qblanguage[366]="Miscellaneous";
$qblanguage[367]="Modify MSS ...";
$qblanguage[368]="User define";
$qblanguage[369]="Default";
$qblanguage[370]="UDP cache timeout";

$qblanguage[371]="TCP Optimization";
$qblanguage[372]="Enable TCP Optimization";
$qblanguage[373]="Destination";
$qblanguage[374]="Destination Port";

$qblanguage[375]="Time Setting";
$qblanguage[376]="Local Time";
$qblanguage[377]="Firmware License Expiry";
$qblanguage[378]="Firmware Warranty Expired";
$qblanguage[379]="Time Zone";
$qblanguage[380]="NTP Time Server";
$qblanguage[381]="Sync";


$qblanguage[382]="SNMP Administration Console";
$qblanguage[383]="Enable SNMP";
$qblanguage[384]="Enable SNMP trap";
$qblanguage[385]="Snmp Manager IP 1";
$qblanguage[386]="Snmp Manager IP 2";
$qblanguage[387]="Snmp Community String";
$qblanguage[388]="System Information";
$qblanguage[389]="System Name";
$qblanguage[390]="System Contact";
$qblanguage[391]="System Location";

$qblanguage[392]="VOIP Setting";
$qblanguage[393]="H.323";
$qblanguage[394]="H.323 NAT Support";
$qblanguage[395]="SIP";
$qblanguage[396]="SIP NAT Support";

$qblanguage[397]="Web Cache Configuration";
$qblanguage[398]="Enable QB Proxy Server";
$qblanguage[399]="Maximum Object Size";
$qblanguage[400]="Minimum Object Size";
$qblanguage[401]="Object Replacement";
$qblanguage[402]="Proxy Cache Size";
$qblanguage[403]="Maxsize";

$qblanguage[404]="Reboot";
$qblanguage[405]="Reboot QB at";
$qblanguage[406]="the moment";
$qblanguage[407]="Go";

$qblanguage[408]="Real Time Traffic";
$qblanguage[409]="Query by Defined Time Frame";
$qblanguage[410]="Query by Custom Time Frame";
$qblanguage[411]="Total Volume Pie Chart";
$qblanguage[412]="Sessions Pie Chart by Src IP";
$qblanguage[413]="Sessions Pie Chart by Nat IP";

$qblanguage[414]="Real Time Traffic";
$qblanguage[415]="Real Time Traffic Pie Chart";
$qblanguage[416]="Real Time Traffic Bar Chart";
$qblanguage[417]="Historical traffic";
$qblanguage[418]="Volume Pie Chart by Subnet";
$qblanguage[419]="Volume Bar Chart by Subnet";

$qblanguage[420]="Diagnostic Tools";
$qblanguage[421]="Tool Selection";
$qblanguage[422]="Show & Set NIC";
$qblanguage[423]="Traceroute";
$qblanguage[424]="Ping by Arp Packet";
$qblanguage[425]="Packet Sniffer";
$qblanguage[426]="Show ARP Cache";
$qblanguage[427]="Open Port Check";
$qblanguage[428]="Measure Download Speed";
$qblanguage[429]="Measure Tunnel Speed by Link";
$qblanguage[430]="Measure Tunnel Speed by Pool";
$qblanguage[431]="Tunnel Bandwidth Autotuning";
$qblanguage[432]="Tunnel Packet Lost Detection";
$qblanguage[433]="Alter ARP Table";
$qblanguage[434]="Restart QB Engine";
$qblanguage[435]="Options of Ping";
$qblanguage[436]="Options";
$qblanguage[437]="Count";
$qblanguage[438]="Through";
$qblanguage[439]="Options of NIC";
$qblanguage[440]="Duplex";
$qblanguage[441]="Speed";
$qblanguage[442]="Auto Negotiation";
$qblanguage[443]="Target of traceroute";
$qblanguage[444]="Options of Arping";
$qblanguage[445]="Source IP";
$qblanguage[446]="Destination IP";
$qblanguage[447]="Options of Packet Captor";
$qblanguage[448]="Show ARP Cache";
$qblanguage[449]="Options of Check Info";
$qblanguage[450]="Port Number";
$qblanguage[451]="Options of Measure Info";
$qblanguage[452]="Local IP";
$qblanguage[453]="Remote File";
$qblanguage[454]="Login User";
$qblanguage[455]="Link ID";
$qblanguage[456]="Latency";
$qblanguage[457]="Options of Detection Info";
$qblanguage[458]="Options of Host Info";
$qblanguage[459]="Packets";
$qblanguage[460]="Target IP";
$qblanguage[461]="Target MAC";
$qblanguage[462]="Restart QB Engine";

$qblanguage[463]="Syslog Administration Console";
$qblanguage[464]="Enable QB Server log";
$qblanguage[465]="Enable QB Traffic log";
$qblanguage[466]="Enable QB Proxy log";
$qblanguage[467]="Enable Log on Local";
$qblanguage[468]="Enable Remote Syslog Server";
$qblanguage[469]="Enable Remote FTP Server";
$qblanguage[470]="Local syslog storage";
$qblanguage[471]="FTP Login Username";
$qblanguage[472]="FTP Login Password";
$qblanguage[473]="FTP Upload Directory";
$qblanguage[474]="Frequency of FTP Server";

$qblanguage[475]="Config. Management";
$qblanguage[476]="Load";
$qblanguage[477]="Save";
$qblanguage[478]="Delete";
$qblanguage[479]="Template";
$qblanguage[480]="Dashboard";
$qblanguage[481]="Update Config";
$qblanguage[482]="Logout";

$qblanguage[483]="ARP porxy On";
$qblanguage[484]="Rules";
$qblanguage[485]="DHCP";
$qblanguage[486]="ARP Table";
$qblanguage[487]="Authentication";
$qblanguage[488]="Real Time";
$qblanguage[489]="History";
$qblanguage[490]="Speed";
$qblanguage[491]="Latency";
$qblanguage[492]="Packet Loss";
$qblanguage[493]="User Flow";
$qblanguage[494]="Sessions";
$qblanguage[495]="Quota by Link";
$qblanguage[496]="Quota by Plicy";
$qblanguage[497]="Quota by Authenticated Uers";
$qblanguage[498]="Show";
$qblanguage[499]="Reset";
$qblanguage[500]="Links By Default";
$qblanguage[501]="Links Alphabetically";
$qblanguage[502]="Links Down";
$qblanguage[503]="Physical Links";
$qblanguage[504]="Log Configuration";
$qblanguage[505]="Unit";
$qblanguage[506]="Transparent Subnets";
$qblanguage[507]="Storage";
$qblanguage[508]="Backup Database";
$qblanguage[509]="DoS Log Configuration";
$qblanguage[510]="Select/Deselect all";
$qblanguage[511]="Application";
$qblanguage[512]="Select/Deselect all";
$qblanguage[513]="IM";
$qblanguage[514]="Game";
$qblanguage[515]="Voice";
$qblanguage[516]="Others";
$qblanguage[517]="Save";
$qblanguage[518]="Group";
$qblanguage[519]="Description";
$qblanguage[520]="Edit";
$qblanguage[521]="Import File";
$qblanguage[522]="Export File";
$qblanguage[523]="Storage Setting";
$qblanguage[524]="Available";
$qblanguage[525]="Used";
$qblanguage[526]="Maximum";
$qblanguage[527]="Clear All Data";
$qblanguage[528]="Apply";
$qblanguage[529]="External FTP Server";
$qblanguage[530]="Restore File";
$qblanguage[531]="System Logs";
$qblanguage[532]="Log Selection";
$qblanguage[533]="Go";
$qblanguage[534]="Show Engine Process Log";
$qblanguage[535]="Show Alert Log";
$qblanguage[536]="Show PPPoE Dial Log";
$qblanguage[537]="Show IPSEC Log";
$qblanguage[538]="Show PPTP Log";
$qblanguage[539]="Show IP Change Log";
$qblanguage[540]="PPPoE Status";
$qblanguage[541]="DHCP Log";
$qblanguage[542]="User's Action Log";
$qblanguage[543]="External Log Server";
$qblanguage[544]="User Account Management";
$qblanguage[545]="Username";
$qblanguage[546]="Privilege";
$qblanguage[547]="Status";
$qblanguage[548]="Session ID";
$qblanguage[549]="Last Login";
$qblanguage[550]="Last Logout";
$qblanguage[551]="Kick Out";
$qblanguage[552]="Username";
$qblanguage[553]="Password";
$qblanguage[554]="Confirm Password";
$qblanguage[555]="Privilege";
$qblanguage[556]="Multiple Login";
$qblanguage[557]="Add";
$qblanguage[558]="Update";
$qblanguage[559]="Back";
$qblanguage[560]="Auto Save";
$qblanguage[561]="Authentication Server";
$qblanguage[562]="Server";
$qblanguage[563]="Group";
$qblanguage[564]="Option";
$qblanguage[565]="Status";
$qblanguage[566]="Enabled";
$qblanguage[567]="Authentication Group";
$qblanguage[568]="Name";
$qblanguage[569]="Type";
$qblanguage[570]="Edit";
$qblanguage[571]="Authentication Setting";
$qblanguage[572]="Timer Setting";
$qblanguage[573]="Login Time Out";
$qblanguage[574]="Sec.";
$qblanguage[575]="Idle Interval";
$qblanguage[576]="Time to Reset";
$qblanguage[577]="Multi-Add User";
$qblanguage[578]="Export";
$qblanguage[579]="Import";
$qblanguage[580]="Login Page";
$qblanguage[581]="Logo Upload";
$qblanguage[582]="Message";
$qblanguage[583]="Network Scan";
$qblanguage[584]="Netbios Scan";

}
if($langcookie eq "zh_TW")
{
$qblanguage[0]="自動更新每";
$qblanguage[1]="秒";
$qblanguage[2]="系統狀態";
$qblanguage[3]="系統時間";
$qblanguage[4]="系統已開機時間";
$qblanguage[5]="韌體版本";
$qblanguage[6]="系統使用率";
$qblanguage[7]="CPU使用率";
$qblanguage[8]="記憶體使用率";
$qblanguage[9]="快取記憶體使用率";
$qblanguage[10]="Ramdisk使用率";
$qblanguage[11]="現行連線數目";
$qblanguage[12]="設備資訊";
$qblanguage[13]="主機名稱";
$qblanguage[14]="型號名稱";
$qblanguage[15]="硬體位址";
$qblanguage[16]="註冊資訊";
$qblanguage[17]="序號";
$qblanguage[18]="註冊日期";
$qblanguage[19]="未註冊";
$qblanguage[20]="註冊期間";
$qblanguage[21]="授權到期日";
$qblanguage[22]="保固到期日";
$qblanguage[23]="廣域網路";
$qblanguage[24]="狀態";
$qblanguage[25]="編輯";
$qblanguage[26]="啟用";
$qblanguage[27]="3G資訊";
$qblanguage[28]="界面";
$qblanguage[29]="名稱";
$qblanguage[30]="閘道";
$qblanguage[31]="系統網路位址";
$qblanguage[32]="線路檢查位址";
$qblanguage[33]="網段";
$qblanguage[34]="下載/上傳";
$qblanguage[35]="版本";
$qblanguage[36]="附加子網路";
$qblanguage[37]="附加子網路2";
$qblanguage[38]="代理伺服器IP";
$qblanguage[39]="代理伺服器名稱";
$qblanguage[40]="代理伺服器通訊埠";

$qblanguage[41]="連線檢查參數";
$qblanguage[42]="連線檢查方式";
$qblanguage[43]="根據 Ping";
$qblanguage[44]="根據 Ping 和 Traceroute";
$qblanguage[45]="根據連線到特定埠號";
$qblanguage[46]="根據連線到特定連接埠號和 Traceroute";
$qblanguage[47]="進階設定";
$qblanguage[48]="關閉被動式連線檢查";
$qblanguage[49]="連接埠號";
$qblanguage[50]="Ping 逾時";
$qblanguage[51]="Traceroute 逾時";
$qblanguage[52]="連線特定埠號逾時";
$qblanguage[53]="線路檢查間距";
$qblanguage[54]="儲存";


$qblanguage[55]="對外網路位址";
$qblanguage[56]="網路服務提供者";
$qblanguage[57]="新增";
$qblanguage[58]="更新";
$qblanguage[59]="新增多個";
$qblanguage[60]="線路位址綁定";
$qblanguage[61]="增加對外網路位址";

$qblanguage[62]="線路設定";

$qblanguage[63]="MPV 設定";
$qblanguage[64]="啟用";
$qblanguage[65]="識別";
$qblanguage[66]="網卡";
$qblanguage[67]="TVLI";
$qblanguage[68]="TVRI";
$qblanguage[69]="THLI";
$qblanguage[70]="THRI";
$qblanguage[71]="PORT";
$qblanguage[72]="THRN";
$qblanguage[73]="最大傳輸單位";
$qblanguage[74]="最大區段";
$qblanguage[75]="轉址";
$qblanguage[76]="加密法";
$qblanguage[77]="演算法";
$qblanguage[78]="壓縮";
$qblanguage[79]="新增 MPV";

$qblanguage[80]="新增線路";
$qblanguage[81]="TMV 設定";

$qblanguage[82]="角色";
$qblanguage[83]="新增 TMV";

$qblanguage[84]="THSI";
$qblanguage[85]="Isakmp_SA";
$qblanguage[86]="Ph1_Encryption";
$qblanguage[87]="Hash";
$qblanguage[88]="DH_Group";
$qblanguage[89]="IPSec_SA";
$qblanguage[90]="Ph2_Encryption";
$qblanguage[91]="認證";
$qblanguage[92]="PF_Group";
$qblanguage[93]="IPSec 設定";
$qblanguage[94]="新增 IPSec";

$qblanguage[95]="區網設定,靜態路由和DHCP設定";
$qblanguage[96]="相關的網路服務提供者";
$qblanguage[97]="DHCP";
$qblanguage[98]="網路區段";
$qblanguage[99]="網路位址版本";
$qblanguage[100]="開";
$qblanguage[101]="關";
$qblanguage[102]="自動";
$qblanguage[103]="不啟用";
$qblanguage[104]="無";
$qblanguage[105]="內部區域";
$qblanguage[106]="關連到";
$qblanguage[107]="位址版本";
$qblanguage[108]="網卡速度";
$qblanguage[109]="介面位址";
$qblanguage[110]="註記";
$qblanguage[111]="新增";
$qblanguage[112]="批量新增";
$qblanguage[113]="設定 DHCP";

$qblanguage[114]="靜態 ARP 設定";
$qblanguage[115]="新增多個";
$qblanguage[116]="恢復";

$qblanguage[117]="無線網路設定";
$qblanguage[118]="基本參數";
$qblanguage[119]="啟用無線網路";
$qblanguage[120]="無線網路名稱(SSID)";
$qblanguage[121]="隱藏 SSID";
$qblanguage[122]="無線網路模式";
$qblanguage[123]="頻道選擇";
$qblanguage[124]="運行頻道";
$qblanguage[125]="安全參數";
$qblanguage[126]="加密類型";
$qblanguage[127]="認證模式";
$qblanguage[128]="啟用金鑰加密資料";
$qblanguage[129]="用戶端也必須使用相同的金鑰傳輸資料";
$qblanguage[130]="您可以輸入";
$qblanguage[131]="5個或13個 ASCII 字";
$qblanguage[132]='10個或26個十六進位字 ("0-9","a-f","A-F")';
$qblanguage[133]="金鑰";
$qblanguage[134]="此金鑰用來加密資料.";
$qblanguage[135]="用戶端也必須使用相同的金鑰傳輸資料";
$qblanguage[136]="8個或63個 ASCII 字";
$qblanguage[137]="64個十六進位字";
$qblanguage[138]="預先共用金鑰";
$qblanguage[139]="套用";

$qblanguage[140]="透通設定";

$qblanguage[141]="橋接";
$qblanguage[142]="代理ARP";

$qblanguage[143]="將公共位址做為橋接模式的透通位址";
$qblanguage[144]="註冊透通位址";

$qblanguage[145]="虛擬區網識別";
$qblanguage[146]="MAC";
$qblanguage[147]="設定虛擬區網";

$qblanguage[148]="上傳";
$qblanguage[149]="MPV 頻寬優化";

$qblanguage[150]="來源";
$qblanguage[151]="下載";
$qblanguage[152]="優先順序";
$qblanguage[153]="類型";
$qblanguage[154]="下載頻寬";
$qblanguage[155]="上傳頻寬";
$qblanguage[156]="使用類型";
$qblanguage[157]="分享";
$qblanguage[158]="個人";
$qblanguage[159]="網路位址頻寬優化";
$qblanguage[160]="主機";

$qblanguage[161]="詳細位置";
$qblanguage[162]="新增";

$qblanguage[163]="服務配置";
$qblanguage[164]="服務";
$qblanguage[165]="刪除";
$qblanguage[166]="協議";
$qblanguage[167]="資訊";
$qblanguage[168]="協議定義";
$qblanguage[169]="描述";

$qblanguage[170]="排程物件";

$qblanguage[171]="對外群組設定";
$qblanguage[172]="群組識別";
$qblanguage[173]="線路資訊";
$qblanguage[174]="備援群組";
$qblanguage[175]="根據封包";
$qblanguage[176]="根據連線";
$qblanguage[177]="平衡模式";
$qblanguage[178]="群組名稱";
$qblanguage[179]="平衡演算法";
$qblanguage[180]="權重";
$qblanguage[181]="DSIP";

$qblanguage[182]="網路服務質量的類別";

$qblanguage[183]="伺服器對映";
$qblanguage[184]="虛擬網路位址";
$qblanguage[185]="實體伺服器";
$qblanguage[186]="實際服務";

$qblanguage[187]="政策性路由";
$qblanguage[188]="進階設定";

$qblanguage[189]="應用程式過濾";

$qblanguage[190]="L2TP IPsec虛擬私人網路設定";
$qblanguage[191]="啟用 L2TP IPsec";
$qblanguage[192]="虛擬私人網路伺服器位址";
$qblanguage[193]="網路位址分發範圍";
$qblanguage[194]="預先共用金鑰";

$qblanguage[195]="L2TP IPsec 認證";
$qblanguage[196]="使用者名稱";
$qblanguage[197]="分配位址";
$qblanguage[198]="登入位址";
$qblanguage[199]="使用設備";
$qblanguage[200]="登出";
$qblanguage[201]="密碼";
$qblanguage[202]="確認密碼";
$qblanguage[203]="指派位址";

$qblanguage[204]="PPTP 伺服器配置";
$qblanguage[205]="啟用 QB PPTP 伺服器";
$qblanguage[206]="PPTP 加密";
$qblanguage[207]="PPTP 壓縮";
$qblanguage[208]="驗證方法";
$qblanguage[209]="最大用戶連接";
$qblanguage[210]="閒置離線時間";
$qblanguage[211]="域名位址";
$qblanguage[212]="網路位址分發範圍";

$qblanguage[213]="PPTP 使用者配置";
$qblanguage[214]="SSL 設定";
$qblanguage[215]="SSL 伺服器狀態";
$qblanguage[216]="啟用 QB SSL 伺服器";
$qblanguage[217]="一般設定";
$qblanguage[218]="虛擬私人網路伺服器位址";
$qblanguage[219]="虛擬私人網路網路範圍";
$qblanguage[220]="虛擬私人網路網路遮罩";
$qblanguage[221]="完整存取設定";
$qblanguage[222]="客戶端極大值";
$qblanguage[223]="可使用的子網路";
$qblanguage[224]="租用子網路";
$qblanguage[225]="SSL 使用者認證";
$qblanguage[226]="實際網路位址";
$qblanguage[227]="虛擬私人網路位址";
$qblanguage[228]="已接收位元組";
$qblanguage[229]="已發送位元組";
$qblanguage[230]="SSL 傳送口設定";
$qblanguage[231]="一般設定";
$qblanguage[232]="視窗名稱";
$qblanguage[233]="登入頁面訊息";
$qblanguage[234]="登入圖案";

$qblanguage[235]="多域名配置";
$qblanguage[236]="一般設定";
$qblanguage[237]="選擇網路服務供應者";
$qblanguage[238]="域名選擇";
$qblanguage[239]="網域";
$qblanguage[240]="網域位址";
$qblanguage[241]="域名等級設定";
$qblanguage[242]="主機性質";
$qblanguage[243]="主機";
$qblanguage[244]="價值";

$qblanguage[245]="防止阻斷服務攻擊";
$qblanguage[246]="略過下列清單";
$qblanguage[247]="溢出連接偵測";
$qblanguage[248]="通過COD的特權名單";
$qblanguage[249]="紀錄率";
$qblanguage[250]="分鐘";
$qblanguage[251]="小時";
$qblanguage[252]="前綴紀錄";
$qblanguage[253]="過濾符合的封包";
$qblanguage[254]="無法通過";
$qblanguage[255]="每個網路位址的連線";
$qblanguage[256]="不明確的Ping的洪氾偵測";
$qblanguage[257]="通過FPFD的特權名單";
$qblanguage[258]="降低";
$qblanguage[259]="提高";
$qblanguage[260]="通訊埠掃描偵測";
$qblanguage[261]="通過PSD的特權名單";
$qblanguage[262]="權重門檻";
$qblanguage[263]="高通訊埠權重";
$qblanguage[264]="低通訊埠權重";
$qblanguage[265]="延遲門檻";
$qblanguage[266]="配額溢值偵測";
$qblanguage[267]="通過QOD的特權名單";
$qblanguage[268]="假設配額";
$qblanguage[269]="設TOS的價值為";
$qblanguage[270]="放棄他們";

$qblanguage[271]="備援機制配置";
$qblanguage[272]="高可用性功能未啟動";
$qblanguage[273]="使用備援機制";
$qblanguage[274]="高可用性";
$qblanguage[275]="備援機制管理訊息";
$qblanguage[276]="開機啟動備援機制";
$qblanguage[277]="主要的";
$qblanguage[278]="次要的";
$qblanguage[279]="自動故障復原";
$qblanguage[280]="自動切換機器";
$qblanguage[281]="區網介面失敗";
$qblanguage[282]="主機容錯移轉暫停";
$qblanguage[283]="網路容錯移轉暫停";
$qblanguage[284]="啟用虛擬MAC";
$qblanguage[285]="浮動位址";
$qblanguage[286]="主要預備位址";
$qblanguage[287]="次要預備位址";
$qblanguage[288]="備援機制區網檢測目標";
$qblanguage[289]="驗證模式";
$qblanguage[290]="狀態顯示";
$qblanguage[291]="強制改變模式";
$qblanguage[292]="儲存設定";
$qblanguage[293]="套用設定";

$qblanguage[294]="管理設定";
$qblanguage[295]="最多使用者";
$qblanguage[296]="編輯使用者帳戶";
$qblanguage[297]="Https通訊埠數量";
$qblanguage[298]="主機名稱";
$qblanguage[299]="LCM上的主機名稱";
$qblanguage[300]="電子郵件通知";

$qblanguage[301]="應用程式配置";
$qblanguage[302]="公司名稱";
$qblanguage[303]="聯絡用電子郵件";
$qblanguage[304]="序號";
$qblanguage[305]="註冊日期";
$qblanguage[306]="註冊";
$qblanguage[307]="QB序號";

$qblanguage[308]="韌體";
$qblanguage[309]="配置";
$qblanguage[310]="UPG和中控系統金鑰";
$qblanguage[311]="上傳設定";
$qblanguage[312]="上傳韌體";
$qblanguage[313]="韌體目錄";
$qblanguage[314]="設定檔目錄";
$qblanguage[315]="中控系統目錄";
$qblanguage[316]="設定檔目錄";
$qblanguage[317]="韌體目錄";
$qblanguage[318]="上傳更新包";
$qblanguage[319]="上傳檔案系統/函式映像檔更新包";
$qblanguage[320]="開始更新程序";
$qblanguage[321]="備份設定檔";
$qblanguage[322]="FTP伺服器";
$qblanguage[323]="自動存檔";
$qblanguage[324]="上傳管理金鑰";
$qblanguage[325]="下載管理金鑰";
$qblanguage[326]="上傳UPG";
$qblanguage[327]="選擇Config. Set";
$qblanguage[328]="Config. Set";
$qblanguage[329]="另存新檔";
$qblanguage[330]="Config. File";
$qblanguage[331]="上傳到";
$qblanguage[332]="請選擇";
$qblanguage[333]="選擇更新包";
$qblanguage[334]="升級檔案";
$qblanguage[335]="選擇更新映像檔";
$qblanguage[336]="開始更新程序";
$qblanguage[337]="選擇上傳金鑰";
$qblanguage[338]="匯出設定檔至FTP伺服器";
$qblanguage[339]="FTP模式";
$qblanguage[340]="伺服器網址";
$qblanguage[341]="登入名稱";
$qblanguage[342]="登入密碼";
$qblanguage[343]="上傳目錄";
$qblanguage[344]="啟用自動存檔";
$qblanguage[345]="透過中控系統設定";
$qblanguage[346]="注意:此功能只支援線路聚合客戶端至中控系統伺服器。";
$qblanguage[347]="選擇上傳 UPG";
$qblanguage[348]="選擇數值";
$qblanguage[349]="開始";
$qblanguage[350]="停止";
$qblanguage[351]="退回";

$qblanguage[352]="域名編碼";
$qblanguage[353]="QB 做為域名伺服器";
$qblanguage[354]="具備認證的域名";
$qblanguage[355]="動態路由設定";
$qblanguage[356]="動態路由狀態";
$qblanguage[357]="啟用動態路由";
$qblanguage[358]="方法";
$qblanguage[359]="路由演算法";
$qblanguage[360]="路由更新時間";
$qblanguage[361]="監控";
$qblanguage[362]="監控埠";

$qblanguage[363]="外部儲存";
$qblanguage[364]="硬碟格式化";
$qblanguage[365]="硬碟分析";

$qblanguage[366]="其他";
$qblanguage[367]="修改最大區段 ...";
$qblanguage[368]="使用者自定義";
$qblanguage[369]="預設";
$qblanguage[370]="UDP快取暫停";

$qblanguage[371]="TCP優化";
$qblanguage[372]="啟用TCP優化";
$qblanguage[373]="目的地";
$qblanguage[374]="目的地通訊埠";

$qblanguage[375]="時間設定";
$qblanguage[376]="本地時間";
$qblanguage[377]="韌體許可期限";
$qblanguage[378]="韌體保固過期";
$qblanguage[379]="時區";
$qblanguage[380]="NTP時間伺服器";
$qblanguage[381]="同步";


$qblanguage[382]="SNMP管理控制台";
$qblanguage[383]="啟用SNMP";
$qblanguage[384]="啟用SNMP陷阱";
$qblanguage[385]="Snmp管理者一號位址";
$qblanguage[386]="Snmp管理者二號位址";
$qblanguage[387]="Snmp共同字串";
$qblanguage[388]="系統資訊";
$qblanguage[389]="系統名稱";
$qblanguage[390]="系統內容";
$qblanguage[391]="系統位置";

$qblanguage[392]="網路電話設定";
$qblanguage[393]="H.323";
$qblanguage[394]="H.323轉址支援";
$qblanguage[395]="SIP";
$qblanguage[396]="SIP轉址支援";

$qblanguage[397]="網頁快取設定";
$qblanguage[398]="啟用QB代裡伺服器";
$qblanguage[399]="極大化物件尺寸";
$qblanguage[400]="極小化物件尺寸";
$qblanguage[401]="物件置換";
$qblanguage[402]="代理快取尺寸";
$qblanguage[403]="最大尺寸";

$qblanguage[404]="重新啟動";
$qblanguage[405]="在什麼時候重開機";
$qblanguage[406]="現在";
$qblanguage[407]="執行";

$qblanguage[408]="及時流量";
$qblanguage[409]="使用預設時間查詢";
$qblanguage[410]="使用自定義時間查詢";
$qblanguage[411]="總流量統計";
$qblanguage[412]="來源流量統計";
$qblanguage[413]="轉址流量統計";

$qblanguage[414]="即時流量";
$qblanguage[415]="即時流量圖";
$qblanguage[416]="即時流量長條圖";
$qblanguage[417]="歷史流量";
$qblanguage[418]="網段流量圖";
$qblanguage[419]="子網路容量長條圖t";

$qblanguage[420]="診斷工具";
$qblanguage[421]="工具選擇";
$qblanguage[422]="網卡顯示與設定";
$qblanguage[423]="Traceroute";
$qblanguage[424]="根據ARP封包執行Ping ";
$qblanguage[425]="封包監聽";
$qblanguage[426]="顯示ARP快取";
$qblanguage[427]="開啟通訊埠檢驗";
$qblanguage[428]="測量下載速度";
$qblanguage[429]="測量線路的隧道速度";
$qblanguage[430]="測量群組的隧道速度";
$qblanguage[431]="隧道頻寬自動調整";
$qblanguage[432]="隧道封包掉落偵測";
$qblanguage[433]="更改ARP Table";
$qblanguage[434]="重啟QB";
$qblanguage[435]="Ping的選項";
$qblanguage[436]="選項";
$qblanguage[437]="次數";
$qblanguage[438]="通過";
$qblanguage[439]="網卡選項";
$qblanguage[440]="雙工";
$qblanguage[441]="速度";
$qblanguage[442]="自調";
$qblanguage[443]="Traceroute的目標";
$qblanguage[444]="Arping的選項";
$qblanguage[445]="來源位址";
$qblanguage[446]="目的位址";
$qblanguage[447]="封包補手的選項";
$qblanguage[448]="顯示ARP快取";
$qblanguage[449]="檢驗資訊的選項";
$qblanguage[450]="通訊埠號碼";
$qblanguage[451]="量測資訊的選項";
$qblanguage[452]="本地檔案";
$qblanguage[453]="遠端檔案";
$qblanguage[454]="使用者登錄";
$qblanguage[455]="線路識別";
$qblanguage[456]="延遲";
$qblanguage[457]="偵測資訊的選項";
$qblanguage[458]="主機資訊的選項";
$qblanguage[459]="封包";
$qblanguage[460]="目標位址";
$qblanguage[461]="MAC目標";
$qblanguage[462]="重啟QB";

$qblanguage[463]="系統日誌控制台";
$qblanguage[464]="啟用QB伺服器紀錄";
$qblanguage[465]="啟用QB流量紀錄";
$qblanguage[466]="啟用QB代理紀錄";
$qblanguage[467]="啟用本機紀錄";
$qblanguage[468]="啟用遠端系統日誌伺服器";
$qblanguage[469]="啟用遠端FTP伺服器";
$qblanguage[470]="本機系統日誌儲存器";
$qblanguage[471]="FTP 登入名稱";
$qblanguage[472]="FTP 登入密碼";
$qblanguage[473]="FTP 上傳目錄";
$qblanguage[474]="FTP伺服器的頻率";

$qblanguage[475]="設定檔管理";
$qblanguage[476]="載入";
$qblanguage[477]="儲存";
$qblanguage[478]="刪除";
$qblanguage[479]="載入樣板";
$qblanguage[480]="儀表板";
$qblanguage[481]="更新配置";
$qblanguage[482]="登出";

$qblanguage[483]="ARP代理啟動";
$qblanguage[484]="規定";
$qblanguage[485]="DHCP表";
$qblanguage[486]="ARP表";
$qblanguage[487]="認證使用者";
$qblanguage[488]="即時";
$qblanguage[489]="歷史";
$qblanguage[490]="速率";
$qblanguage[491]="封包延遲";
$qblanguage[492]="封包損失";
$qblanguage[493]="使用流量分析";
$qblanguage[494]="封包連線分析";
$qblanguage[495]="查詢線路配額";
$qblanguage[496]="查詢政策路由配額";
$qblanguage[497]="查詢認證使用者配額";
$qblanguage[498]="顯示";
$qblanguage[499]="重置";
$qblanguage[500]="所有線路";
$qblanguage[501]="所有線路(排序)";
$qblanguage[502]="故障線路";
$qblanguage[503]="實體線路";
$qblanguage[504]="紀錄設定";
$qblanguage[505]="單元";
$qblanguage[506]="透通子網路";
$qblanguage[507]="儲存區";
$qblanguage[508]="資料庫備份";
$qblanguage[509]="阻斷服務紀錄設定";
$qblanguage[510]="全選/取消全選";
$qblanguage[511]="應用程式";
$qblanguage[512]="全選/取消全選";
$qblanguage[513]="網路通訊軟體";
$qblanguage[514]="遊戲";
$qblanguage[515]="聲音";
$qblanguage[516]="其他";
$qblanguage[517]="存檔";
$qblanguage[518]="群組";
$qblanguage[519]="描述";
$qblanguage[520]="編輯";
$qblanguage[521]="匯入檔案";
$qblanguage[522]="匯出檔案";
$qblanguage[523]="儲存設定";
$qblanguage[524]="可用";
$qblanguage[525]="已用";
$qblanguage[526]="最大值";
$qblanguage[527]="清除所有資料";
$qblanguage[528]="套用";
$qblanguage[529]="外部FTP伺服器";
$qblanguage[530]="檔案恢復";
$qblanguage[531]="系統記錄";
$qblanguage[532]="記錄選項";
$qblanguage[533]="前往";
$qblanguage[534]="顯示引擎處理記錄";
$qblanguage[535]="顯示警告記錄";
$qblanguage[536]="顯示PPPoE 撥號記錄";
$qblanguage[537]="顯示IPSEC記錄";
$qblanguage[538]="顯示PPTP記錄";
$qblanguage[539]="顯示位址改變記錄";
$qblanguage[540]="PPPoE 狀態";
$qblanguage[541]="DHCP 記錄";
$qblanguage[542]="使用者行為記錄";
$qblanguage[543]="外部伺服器紀錄";
$qblanguage[544]="使用者帳戶管理";
$qblanguage[545]="使用者名稱";
$qblanguage[546]="權限";
$qblanguage[547]="狀態";
$qblanguage[548]="連線身分";
$qblanguage[549]="最後登入";
$qblanguage[550]="最後登出";
$qblanguage[551]="剔除";
$qblanguage[552]="使用者名稱";
$qblanguage[553]="密碼";
$qblanguage[554]="確認密碼";
$qblanguage[555]="權限";
$qblanguage[556]="重複登入";
$qblanguage[557]="新增";
$qblanguage[558]="更新";
$qblanguage[559]="返回";
$qblanguage[560]="自動儲存";
$qblanguage[561]="認證伺服器";
$qblanguage[562]="伺服器";
$qblanguage[563]="群組";
$qblanguage[564]="選項";
$qblanguage[565]="狀態";
$qblanguage[566]="啟用";
$qblanguage[567]="認證群組";
$qblanguage[568]="名稱";
$qblanguage[569]="類型";
$qblanguage[570]="編輯";

$qblanguage[583]="網路掃描";
$qblanguage[584]="Netbios 掃描";
}

if($langcookie eq "fr_FR")
{
$qblanguage[0]  ="Auto Refresh Par";
$qblanguage[1]  ="deuxième";
$qblanguage[2]  ="l'état du système";
$qblanguage[3]  ="Système Time";
$qblanguage[4]  ="Système Uptime";
$qblanguage[5]  ="Firmware Version";
$qblanguage[6]  ="Système Usage";
$qblanguage[7]  ="CPU Usage";
$qblanguage[8]  ="Memory Usage";
$qblanguage[9]  ="Cache Usage";
$qblanguage[10] ="Ramdisk Usage";
$qblanguage[11] ="Actif Sessions";
$qblanguage[12] ="Appareil Information";
$qblanguage[13] ="Nom de l'hôte";
$qblanguage[14] ="Nom du modèle";
$qblanguage[15] ="MAC Plage d'adresses";
$qblanguage[16] ="Register Information";
$qblanguage[17] ="numéro de série";
$qblanguage[18] ="inscrit le";
$qblanguage[19] ="non enregistré";
$qblanguage[20] ="S'inscrire De Etats";
$qblanguage[21] ="Licence d'expiration";
$qblanguage[22] ="Garantie d'expiration";
$qblanguage[23] ="WAN Link";
$qblanguage[24] ="statut";

$qblanguage[25] ="éditer";
$qblanguage[26] ="permettre";
$qblanguage[27] ="3G Information";
$qblanguage[28] ="Interface";
$qblanguage[29] ="prénom";
$qblanguage[30] ="Gateway";
$qblanguage[31] ="System IP";
$qblanguage[32] ="Healthcheck IP";
$qblanguage[33] ="Subnet";
$qblanguage[34] ="Down/Up";
$qblanguage[35] ="Version";
$qblanguage[36] ="supplémentaire Subnet";
$qblanguage[37] ="supplémentaire Subnet2";
$qblanguage[38] ="Proxy IP";
$qblanguage[39] ="Proxy Name";
$qblanguage[40] ="Proxy Port";


$qblanguage[41] ="Lien Vérifiez Paramètres";
$qblanguage[42] ="Lien Vérifiez Méthode";
$qblanguage[43] ="By Ping";
$qblanguage[44] ="By Ping and Trace Route";
$qblanguage[45] ="By Connection to Specified Port";
$qblanguage[46] ="By Connection and Trace Route";
$qblanguage[47] ="Paramètres avancés";
$qblanguage[48] ="Disable Passive Line Check";
$qblanguage[49] ="Port";
$qblanguage[50] ="Ping Time Out";
$qblanguage[51] ="Traceroute Time Out";
$qblanguage[52] ="Connection Time Out";
$qblanguage[53] ="Check Time Interval";
$qblanguage[54] ="sauver";


$qblanguage[55] ="Public IP";
$qblanguage[56] ="ISP ID";
$qblanguage[57] ="ajouter";
$qblanguage[58] ="mettre à jour";
$qblanguage[59] ="Multi-add";
$qblanguage[60] ="Link IP Binding";
$qblanguage[61] ="Public IP to bind";

$qblanguage[62] ="Link Configuration";

$qblanguage[63] ="MPV Configuration";
$qblanguage[64] ="Activé";
$qblanguage[65] ="ID";
$qblanguage[66] ="NIC";
$qblanguage[67] ="TVLI";
$qblanguage[68] ="TVRI";
$qblanguage[69] ="THLI";
$qblanguage[70] ="THRI";
$qblanguage[71] ="PORT";
$qblanguage[72] ="THRN";
$qblanguage[73] ="MTU";
$qblanguage[74] ="MSS";
$qblanguage[75] ="NAT";
$qblanguage[76] ="ENC";
$qblanguage[77] ="Algorithm";
$qblanguage[78] ="COMP";
$qblanguage[79] ="Add";

$qblanguage[80] ="Ajouter un lien";
$qblanguage[81] ="TMV Configuration";

$qblanguage[82] ="rôle";
$qblanguage[83] ="ajouter TMV";

$qblanguage[84] ="THSI";
$qblanguage[85] ="Isakmp_SA";
$qblanguage[86] ="Ph1_Encryption";
$qblanguage[87] ="Hash";
$qblanguage[88] ="DH_Group";
$qblanguage[89] ="IPSec_SA";
$qblanguage[90] ="Ph2_Encryption";
$qblanguage[91] ="Authentition";
$qblanguage[92] ="PF_Group";
$qblanguage[93] ="IPSec Configuration";
$qblanguage[94] ="ajouter IPSec";

$qblanguage[95] ="LAN IP binding, Static Routes and DHCP setting";
$qblanguage[96] ="connexe ISP";
$qblanguage[97] ="DHCP";
$qblanguage[98] ="Network";
$qblanguage[99] ="IPver";
$qblanguage[100]="allumer";
$qblanguage[101]="éteindre";
$qblanguage[102]="Auto";
$qblanguage[103]="handicapé";
$qblanguage[104]="aucun";
$qblanguage[105]="Internal Zone";
$qblanguage[106]="lié à";
$qblanguage[107]="IP Version";
$qblanguage[108]="NIC Speed";
$qblanguage[109]="Interface IP";
$qblanguage[110]="Note";
$qblanguage[111]="créer";
$qblanguage[112]="Batch Create";
$qblanguage[113]="Set DHCP";

$qblanguage[114]="Static ARP Configuration";
$qblanguage[115]="Multi-Add";
$qblanguage[116]="Restore";

$qblanguage[117]="Wireless LAN Configuration";
$qblanguage[118]="Basic Parameters";
$qblanguage[119]="Enable Wireless";
$qblanguage[120]="Wireless Name(SSID)";
$qblanguage[121]="Hide SSID";
$qblanguage[122]="Wireless Mode";
$qblanguage[123]="canal sélection";
$qblanguage[124]="opération canal";
$qblanguage[125]="Security Parameters";
$qblanguage[126]="Encrypt Type";
$qblanguage[127]="Auth Mode";
$qblanguage[128]="The WEP keys are used to encrypt data.";
$qblanguage[129]="Clients must use the same key for data transmission.";
$qblanguage[130]="You can enter";
$qblanguage[131]="5 or 13 ASCII characters";
$qblanguage[132]='10 or 26 hexadecimal characters ("0-9","a-f","A-F").';
$qblanguage[133]="Key";
$qblanguage[134]="The key is used to encrypt data.";
$qblanguage[135]="Clients must use the same key for data transmission.";
$qblanguage[136]="8 to 63 ASCII characters";
$qblanguage[137]="64 hexadecimal characters";
$qblanguage[138]="Pre-Shared Key";
$qblanguage[139]="appliquer";

$qblanguage[140]="Réglage transparent";

$qblanguage[141]="BRIDGE";
$qblanguage[142]="ARPPROXY";

$qblanguage[143]="Public IP reused as Pass Through IP for Bridge";
$qblanguage[144]="Pass Through IP registration for ARP Proxy";

$qblanguage[145]="VlanID";
$qblanguage[146]="MAC";
$qblanguage[147]="VLAN Setting";

$qblanguage[148]="Upload";
$qblanguage[149]="MPV Bandwidth Shaper";

$qblanguage[150]="Source";
$qblanguage[151]="télécharger";
$qblanguage[152]="Priority";
$qblanguage[153]="Type";
$qblanguage[154]="Download Bandwidth";
$qblanguage[155]="Upload Bandwidth";
$qblanguage[156]="Usage Type";
$qblanguage[157]="partager";
$qblanguage[158]="Individual";
$qblanguage[159]="IP Bandwidth Shaper";
$qblanguage[160]="Objet hôtes";

$qblanguage[161]="Détail d'adresses";
$qblanguage[162]="nouvelle entrée";

$qblanguage[163]="Configuration des services";
$qblanguage[164]="Service";
$qblanguage[165]="effacer";
$qblanguage[166]="Protocol";
$qblanguage[167]="Information";
$qblanguage[168]="Protocol defined";
$qblanguage[169]="Description";

$qblanguage[170]="Horaire objet";

$qblanguage[171]="Outbound Pool Configuration";
$qblanguage[172]="Pool ID";
$qblanguage[173]="Link Info";
$qblanguage[174]="Backup Pool";
$qblanguage[175]="By Packet";
$qblanguage[176]="By Connection";
$qblanguage[177]="Balance Mode";
$qblanguage[178]="Pool nom";
$qblanguage[179]="Balance Algorithm";
$qblanguage[180]="poids";
$qblanguage[181]="DSIP";

$qblanguage[182]="QoS Class";

$qblanguage[183]="Server Mapping";
$qblanguage[184]="Virtual IP";
$qblanguage[185]="serveurs réels";
$qblanguage[186]="services réels";

$qblanguage[187]="Policy Routing";
$qblanguage[188]="Advanced Setting";

$qblanguage[189]="Application Filtering";

$qblanguage[190]="L2TP IPsec VPN Configuration";
$qblanguage[191]="Enable L2TP IPsec";
$qblanguage[192]="VPN Server IP";
$qblanguage[193]="IP release range";
$qblanguage[194]="Pre-share key";

$qblanguage[195]="L2TP IPsec Authentication";
$qblanguage[196]="Nom d'utilisateur";
$qblanguage[197]="Assigned IP";
$qblanguage[198]="Login IP";
$qblanguage[199]="Utilisez dispositif";
$qblanguage[200]="Kick Out";
$qblanguage[201]="mot de passe";
$qblanguage[202]="Confirm Password";
$qblanguage[203]="Assign IP";

$qblanguage[204]="PPTP Server Configuration";
$qblanguage[205]="Enable QB PPTP Server";
$qblanguage[206]="PPTP Chiffrement";
$qblanguage[207]="PPTP Compression";
$qblanguage[208]="Authentication méthode";
$qblanguage[209]="Max client connections";
$qblanguage[210]="Disconnect idle time";
$qblanguage[211]="DNS IP";
$qblanguage[212]="IP release range";

$qblanguage[213]="PPTP User Authentication";
$qblanguage[214]="SSL Configuration";
$qblanguage[215]="SSL Server State";
$qblanguage[216]="Enable QB SSL Server";
$qblanguage[217]="Configuration générale";
$qblanguage[218]="VPN Server IP";
$qblanguage[219]="VPN Net Range";
$qblanguage[220]="VPN Netmask";
$qblanguage[221]="Full Access Settings";
$qblanguage[222]="MAX Client";
$qblanguage[223]="disponible Subnet";
$qblanguage[224]="Lease Subnet";
$qblanguage[225]="SSL User Authentication";
$qblanguage[226]="Real IP";
$qblanguage[227]="VPN IP";
$qblanguage[228]="Bytes recevoir";
$qblanguage[229]="Bytes expédié";
$qblanguage[230]="SSL Portal Setting";
$qblanguage[231]="General Setting";
$qblanguage[232]="Window title";
$qblanguage[233]="Login Page Message";
$qblanguage[234]="Login Logo";

$qblanguage[235]="Multi-DNS Configuration";
$qblanguage[236]="Configuration générale";
$qblanguage[237]="ISP Selection";
$qblanguage[238]="Domain Selection";
$qblanguage[239]="Domain";
$qblanguage[240]="Domain IP";
$qblanguage[241]="Domain Level Settings";
$qblanguage[242]="Host Properties";
$qblanguage[243]="Host";
$qblanguage[244]="valeur";

$qblanguage[245]="DoS Prévention";
$qblanguage[246]="Privileged List to bypass checks below";
$qblanguage[247]="Connection Overflow Detection";
$qblanguage[248]="Privileged List to bypass COD";
$qblanguage[249]="Log Rate";
$qblanguage[250]="minute";
$qblanguage[251]="heure";
$qblanguage[252]="Log Prefix";
$qblanguage[253]="Drop Packet if matched";
$qblanguage[254]="Can not go over";
$qblanguage[255]="Connections per IP";
$qblanguage[256]="Fuzzy Ping Flooding Detection";
$qblanguage[257]="Privileged List to bypass FPFD";
$qblanguage[258]="Lower";
$qblanguage[259]="Upper";
$qblanguage[260]="Port Scan détection";
$qblanguage[261]="Privileged List to bypass PSD";
$qblanguage[262]="Weight Threshold";
$qblanguage[263]="High Port Weight";
$qblanguage[264]="Low Port Weight";
$qblanguage[265]="Retard Thershold";
$qblanguage[266]="Quota Overflow Detection";
$qblanguage[267]="Privileged List to bypass QOD";
$qblanguage[268]="If quota";
$qblanguage[269]="Set TOS value as";
$qblanguage[270]="DROP Them";

$qblanguage[271]="HA Config";
$qblanguage[272]="Availablility élevée n'est pas lancé.";
$qblanguage[273]="Enable HA";
$qblanguage[274]="Haute disponibilité";
$qblanguage[275]="HA Management Message";
$qblanguage[276]="Launch HA on Boot";
$qblanguage[277]="Primary";
$qblanguage[278]="secondaire";
$qblanguage[279]="Auto Fail Over";
$qblanguage[280]="Auto Switch Back";
$qblanguage[281]="Fail on LAN Interface";
$qblanguage[282]="Host FAILOVER Timeout";
$qblanguage[283]="Network FAILOVER Timeout";
$qblanguage[284]="Enable Virtual MAC";
$qblanguage[285]="Floating IP";
$qblanguage[286]="Standby IP of Primary";
$qblanguage[287]="Standby IP of Secondary";
$qblanguage[288]="HA LAN Check Targets";
$qblanguage[289]="Check Mode";
$qblanguage[290]="Afficher l'état";
$qblanguage[291]="Force Change Mode";
$qblanguage[292]="Enregistrer le réglage";
$qblanguage[293]="appliquer Réglage";

$qblanguage[294]="Admin Setting";
$qblanguage[295]="Maximum User";
$qblanguage[296]="Edit User Account";
$qblanguage[297]="Https Port Number";
$qblanguage[298]="Hostname";
$qblanguage[299]="Hostname on LCM";
$qblanguage[300]="E-mail Alert";

$qblanguage[301]="Appliance Registration";
$qblanguage[302]="Nom de la société";
$qblanguage[303]="Contact E-mail";
$qblanguage[304]="numéro de série";
$qblanguage[305]="inscrit le";
$qblanguage[306]="s'inscrire";
$qblanguage[307]="QB numéro de série";

$qblanguage[308]="Firmware";
$qblanguage[309]="Configuration";
$qblanguage[310]="UPG and CMS Key";
$qblanguage[311]="Upload Config";
$qblanguage[312]="Upload Firmware";
$qblanguage[313]="Menu for Firmware";
$qblanguage[314]="Menu for Config";
$qblanguage[315]="Menu for CMS";
$qblanguage[316]="Menu for Config";
$qblanguage[317]="Menu for Firmware";
$qblanguage[318]="Téléchargez Upgrade Package";
$qblanguage[319]="Forfait Image Upload Fs / Lib";
$qblanguage[320]="Lancement Mets Processus";
$qblanguage[321]="Sauvegarde config";
$qblanguage[322]="Serveur FTP";
$qblanguage[323]="Auto Save";
$qblanguage[324]="Téléchargez Key Management";
$qblanguage[325]="Télécharger Key Management";
$qblanguage[326]="Téléchargez UPG";
$qblanguage[327]="Sélectionnez Config. Set";
$qblanguage[328]="Config. Set";
$qblanguage[329]="Enregistrer en tant que";
$qblanguage[330]="Config. Dossier";
$qblanguage[331]="Upload to";
$qblanguage[332]="S'il vous plaît Choisir!!";
$qblanguage[333]="Sélectionnez Mise à niveau Forfait";
$qblanguage[334]="Mise à jour du fichier";
$qblanguage[335]="Sélectionnez Mise à niveau Image";
$qblanguage[336]="Lancement de la procédure de mise à niveau";
$qblanguage[337]="Sélectionnez Envoyer la clé";
$qblanguage[338]="Export Config. à un serveur FTP";
$qblanguage[339]="Mode FTP";
$qblanguage[340]="Adresse du serveur";
$qblanguage[341]="Connexion nom d'utilisateur";
$qblanguage[342]="Connexion Mot de passe";
$qblanguage[343]="Téléchargez répertoire";
$qblanguage[344]="Activer l'enregistrement automatique";
$qblanguage[345]="Configuration Via CMS";
$qblanguage[346]="Remarque:! Cette fonction est uniquement pour les clients de collage avec le serveur grâce CMS";
$qblanguage[347]="Sélectionnez Télécharger UPG";
$qblanguage[348]="Sélectionnez Numéro";
$qblanguage[349]="Start";
$qblanguage[350]="Stop";
$qblanguage[351]="Retour";

$qblanguage[352]="DNS résoudre";
$qblanguage[353]="QB travaille comme serveur DNS";
$qblanguage[354]="with Authoritative DNS";
$qblanguage[355]="Configuration du routage dynamique";
$qblanguage[356]="Routage dynamique État";
$qblanguage[357]="Activation du routage dynamique";
$qblanguage[358]="méthode";
$qblanguage[359]="Route métrique";
$qblanguage[360]="Route Mise à jour Temps";
$qblanguage[361]="Monitor";
$qblanguage[362]="Monitor Port";

$qblanguage[363]="de stockage externe";
$qblanguage[364]="Disque dur Format";
$qblanguage[365]="Disque dur Analyseur";

$qblanguage[366]="divers";
$qblanguage[367]="Modify MSS ...";
$qblanguage[368]="défini par l'utilisateur";
$qblanguage[369]="Default";
$qblanguage[370]="UDP cache temps mort";

$qblanguage[371]="TCP optimisation";
$qblanguage[372]="Enable TCP optimisation";
$qblanguage[373]="Destination";
$qblanguage[374]="Destination Port";

$qblanguage[375]="Réglage de l'heure";
$qblanguage[376]="Heure locale";
$qblanguage[377]="Firmware Licence d'expiration";
$qblanguage[378]="Firmware garantie Expiré";
$qblanguage[379]="fuseau horaire";
$qblanguage[380]="NTP Time Server";
$qblanguage[381]="Sync";


$qblanguage[382]="Snmp Administration Console";
$qblanguage[383]="Enable SNMP";
$qblanguage[384]="Enable SNMP trap";
$qblanguage[385]="Snmp Manager IP 1";
$qblanguage[386]="Snmp Manager IP 2";
$qblanguage[387]="Snmp Community String";
$qblanguage[388]="système d'information";
$qblanguage[389]="Nom du système";
$qblanguage[390]="contact système";
$qblanguage[391]="Emplacement du système";

$qblanguage[392]="VOIP mise";
$qblanguage[393]="H.323";
$qblanguage[394]="H.323 NAT soutenir";
$qblanguage[395]="SIP";
$qblanguage[396]="SIP NAT soutenir";

$qblanguage[397]="Web Cache Configuration";
$qblanguage[398]="Enable QB Proxy Server";
$qblanguage[399]="Maximum Object Size";
$qblanguage[400]="Minimum Object Size";
$qblanguage[401]="Object Replacement";
$qblanguage[402]="Proxy Cache Size";
$qblanguage[403]="Maxsize";

$qblanguage[404]="Reboot";
$qblanguage[405]="Reboot QB at";
$qblanguage[406]="the moment";
$qblanguage[407]="Go";

$qblanguage[408]="Trafic en temps réel";
$qblanguage[409]="Query by Defined Time Frame";
$qblanguage[410]="Query by Custom Time Frame";
$qblanguage[411]="Total Volume Pie Chart";
$qblanguage[412]="Sessions Pie Chart by Src IP";
$qblanguage[413]="Sessions Pie Chart by Nat IP";

$qblanguage[414]="Trafic en temps réel";
$qblanguage[415]="Trafic en temps réel Pie Chart";
$qblanguage[416]="Trafic en temps réel Bar Chart";
$qblanguage[417]="Historical traffic";
$qblanguage[418]="Volume Pie Chart by Subnet";
$qblanguage[419]="Volume Bar Chart by Subnet";

$qblanguage[420]="Diagnostic Tools";
$qblanguage[421]="sélection de l'outil";
$qblanguage[422]="Show & Set NIC";
$qblanguage[423]="Traceroute";
$qblanguage[424]="Ping by Arp Packet";
$qblanguage[425]="Packet Sniffer";
$qblanguage[426]="Show ARP Cache";
$qblanguage[427]="Open Port Check";
$qblanguage[428]="Measure Download Speed";
$qblanguage[429]="Measure Tunnel Speed by Link";
$qblanguage[430]="Measure Tunnel Speed by Pool";
$qblanguage[431]="Tunnel Bandwidth Autotuning";
$qblanguage[432]="Tunnel Packet Lost Detection";
$qblanguage[433]="Alter ARP Table";
$qblanguage[434]="Restart QB Engine";
$qblanguage[435]="Options de Ping";
$qblanguage[436]="Options";
$qblanguage[437]="compter";
$qblanguage[438]="Through";
$qblanguage[439]="Options de NIC";
$qblanguage[440]="Duplex";
$qblanguage[441]="Speed";
$qblanguage[442]="Auto Negotiation";
$qblanguage[443]="Target de traceroute";
$qblanguage[444]="Options de arping";
$qblanguage[445]="Source IP";
$qblanguage[446]="Destination IP";
$qblanguage[447]="Options of Packet Captor";
$qblanguage[448]="Show ARP Cache";
$qblanguage[449]="Options of Check Info";
$qblanguage[450]="Port Number";
$qblanguage[451]="Options of Measure Info";
$qblanguage[452]="Local IP";
$qblanguage[453]="Remote File";
$qblanguage[454]="Connexion utilisateur";
$qblanguage[455]="Link ID";
$qblanguage[456]="Latency";
$qblanguage[457]="Options of Detection Info";
$qblanguage[458]="Options of Host Info";
$qblanguage[459]="Packets";
$qblanguage[460]="Target IP";
$qblanguage[461]="Target MAC";
$qblanguage[462]="Restart QB Engine";

$qblanguage[463]="Syslog Administration Console";
$qblanguage[464]="permettre QB Server log";
$qblanguage[465]="permettre QB Traffic log";
$qblanguage[466]="permettre QB Proxy log";
$qblanguage[467]="permettre Log on Local";
$qblanguage[468]="permettre Remote Syslog Server";
$qblanguage[469]="permettre Remote FTP Server";
$qblanguage[470]="Local syslog storage";
$qblanguage[471]="FTP Login Username";
$qblanguage[472]="FTP Login Password";
$qblanguage[473]="FTP Upload Directory";
$qblanguage[474]="Frequency of FTP Server";

$qblanguage[475]="Config. Management";
$qblanguage[476]="charger";
$qblanguage[477]="sauver";
$qblanguage[478]="effacer";
$qblanguage[479]="Template";
$qblanguage[480]="tableau de bord";
$qblanguage[481]="Update Config";
$qblanguage[482]="Logout";

$qblanguage[483]="ARP porxy On";
$qblanguage[484]="Rules";
$qblanguage[485]="DHCP";
$qblanguage[486]="ARP Table";
$qblanguage[487]="Authentication";
$qblanguage[488]="Real Time";
$qblanguage[489]="History";
$qblanguage[490]="Speed";
$qblanguage[491]="Latency";
$qblanguage[492]="Packet Loss";
$qblanguage[493]="User Flow";
$qblanguage[494]="Sessions";
$qblanguage[495]="Quota by Link";
$qblanguage[496]="Quota by Plicy";
$qblanguage[497]="Quota by Authenticated Uers";
$qblanguage[498]="Show";
$qblanguage[499]="Reset";
}

return @qblanguage;

}




1
