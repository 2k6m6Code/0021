#!/usr/bin/perl

BEGIN { unshift (@INC,"/usr/local/apache/qb/perl_lib"); }

require ("/usr/local/apache/qb/qbmod.cgi");

require ("/usr/local/apache/qb/auth/quotalogin.lib");
use CGI;
use JSON;
use QB_LOG;
use QB_Action;

my $form=new CGI;
my $json = new JSON;
my $log = QB_LOG->new();
my $action = QB_Action->new();
my $reflist = XMLread($gPATH.'auth.xml');
my $quota = XMLread($gPATH.'quota.xml');
my $quotalist = $quota->{quota};
my $ip = '';
my $success = '0';
my $username=$form->param('username') ;
my $password=$form->param('password') ;
#$username='TOM';
#$password='123';
my $check='0';
my $conlimit='0';
my $enable_quota='';
my $tcp='';
my $udp='';
my $mac='';
authenticate(action=>'RANDOMCHECK');

print "Content-type:text/html\n\n";

if ($ENV{'HTTP_VIA'} && $ENV{'HTTP_X_FORWARDED_FOR'})
{
   ($fromip,$USE_DNS)=split(/\,/,$ENV{'HTTP_X_FORWARDED_FOR'});
   $ip=$ENV{'REMOTE_ADDR'};
}else 
{
   $ip = $ENV{'REMOTE_ADDR'};
}
   $mac = `/sbin/arp -a|grep $ip | awk '{print \$4}'`;
   $mac =~ s/://g;
   $username =~s/\s+//g;
   $password =~s/\s+//g;
   my $list = $reflist->{user};
   my $type;
   my $name_check = 0;
   my $badname ='';
   foreach my $server (@$list)
   {
       if ($server->{description} eq 'None'){next;}
       my $userlist = $server->{member};
       foreach my $user (@$userlist)
       {
           if ($user->{idd} eq $username && ($ip eq $user->{ip} || $user->{ip} eq ''))
           {
               $type = $user->{type};
               $name_check = 1;
               if ($user->{tcp} ne '' && $user->{udp} ne '')
               {
                        $conlimit='1';
                        $tcp=$user->{tcp};
               		$udp=$user->{udp};
               }
           }
       }
   }
   if($username eq ''&&$password eq ''){$type = 'Radius'}
   my $ser=$reflist->{server};
   foreach my $name (@$ser)
   {
       if ($name->{enabled} eq '0' && $name->{schname} eq $type ){$type ='';}
   }
   if ($type eq 'LDAP')
   {
       #LDAP
	   my $list_r = $reflist->{server};
       my $sip,$group,$port,$domain;
       foreach my $ss  (@$list_r)
       {
           if ($ss->{schname} eq 'system' || $ss->{schname} eq 'LD' || $ss->{schname} eq 'AD' || $ss->{schname} eq 'Radius'){next;}
           $sip=$ss->{ip};
           $group=$ss->{group};
           $port=$ss->{port};
           $domain=$ss->{domain};
       }
       my @dc = split(/\./,$domain);
       my $info='';
       $info=$info.'cn='.$username;
	   if($group ne ''){
       $info=$info.",cn=".$group;}
       foreach my $result (@dc)
       {
           $info=$info.',dc='.$result;
       }
       my @status = `/usr/local/apache/qb/setuid/run /usr/sbin/ldapwhoami -H ldap://$sip:$port -x -D \"$info\" -w $password`;
       foreach my $aa (@status)
       {
           if (!grep(/Success/,$aa)){next;}
           if (grep(/Success/,$aa))
			{
				$success = '1';
				foreach my $server (@$list)
			   {
				   if ($server->{description} eq 'None' || $server->{description} ne 'LDAP'){next;}
				   my $userlist = $server->{member};
				   my $ttime=time()+(8*60*60);
				   foreach my $user (@$userlist)
				   {
					   if (($user->{idd} eq $username && ($ip eq $user->{ip} || $user->{ip} eq '') && ($user->{time} eq '' || ($ttime - $user->{time}) > 0)))
					   {
						   $user->{time} = $ttime;
						   if ($user->{iip} ne '')
						   {
								system("/usr/local/apache/qb/setuid/run /sbin/iptables -t nat -D AUTH -s $user->{iip} -j RETURN");
						   }
						   $user->{iip} = $ip;
							foreach my $myquota (@$quotalist)
							{
								if($myquota->{name} eq $user->{idd})
								{
									system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -D PREROUTING -d $myquota->{ip} -j $myquota->{name}.down");
									system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -D POSTROUTING -s $myquota->{ip} -j $myquota->{name}.up");
									$myquota->{ip}=$user->{iip};
									$enable_quota=$myquota->{bs};
								}
							}
					   }
				   }
			   }
			}
			if ($success)
			{
				XMLwrite($quota,$gPATH.'quota.xml');
				XMLwrite($reflist,$gPATH.'auth.xml');
				foreach $new_ip (@$quotalist)
				{
					#print "$new_ip->{name}";
					if($new_ip->{name} eq $username){quotawork(quotaaction=>'CREAT', LINK=>$new_ip->{name});}
				}
			}
       }
   }elsif ($type eq 'Radius')
   {
       #RADIUS
	   my @status='';
       my $list_r = $reflist->{server};
       my $ip,$group,$port;
       foreach my $ss  (@$list_r)
       {
           if ($ss->{schname} eq 'system' || $ss->{schname} eq 'LD' || $ss->{schname} eq 'AD'){next;}   
           $ip=$ss->{ip};
           $group=$ss->{group};
           $port=$ss->{port};
       }
       #my $status = system("/usr/local/apache/qb/setuid/run /usr/local/bin/radtest $username $password 123.51.217.239 0 testing123 ");
	   if($username eq '' && $password eq '')
       {
           @status = `/usr/local/apache/qb/setuid/run /usr/local/bin/radtest $mac $mac $ip $port $group`;
           $success = '5';
       }else
       {
           @status = `/usr/local/apache/qb/setuid/run /usr/local/bin/radtest $username $password $ip $port $group`;
       }
       #my @status = `/usr/local/apache/qb/setuid/run /tmp/radtest $username $password $ip $port $group`;
       foreach my $aa (@status)
       {
           if (!grep(/rad_recv:/,$aa)){next;}
           if (grep(/Accept/,$aa))
		   {
				$success = '1';
				foreach my $server (@$list)
			   {
				   if ($server->{description} eq 'None' || $server->{description} ne 'Radius'){next;}
				   my $userlist = $server->{member};
				   my $ttime=time()+(8*60*60);
				   foreach my $user (@$userlist)
				   {
					   if (($user->{idd} eq $username && ($ip eq $user->{ip} || $user->{ip} eq '') && ($user->{time} eq '' || ($ttime - $user->{time}) > 0)))
					   {
						   $user->{time} = $ttime;
						   if ($user->{iip} ne '')
						   {
								system("/usr/local/apache/qb/setuid/run /sbin/iptables -t nat -D AUTH -s $user->{iip} -j RETURN");
						   }
						   $user->{iip} = $ip;
							foreach my $myquota (@$quotalist)
							{
								if($myquota->{name} eq $user->{idd})
								{
									system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -D PREROUTING -d $myquota->{ip} -j $myquota->{name}.down");
									system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -D POSTROUTING -s $myquota->{ip} -j $myquota->{name}.up");
									$myquota->{ip}=$user->{iip};
									$enable_quota=$myquota->{bs};
								}
							}
					   }
				   }
			   }
			}
			if ($success)
			{
				XMLwrite($quota,$gPATH.'quota.xml');
				XMLwrite($reflist,$gPATH.'auth.xml');
				foreach $new_ip (@$quotalist)
				{
					#print "$new_ip->{name}";
					if($new_ip->{name} eq $username){quotawork(quotaaction=>'CREAT', LINK=>$new_ip->{name});}
				}
			}
       }
   }elsif ($type eq 'AD')
   {
       #AD
       my $list_r = $reflist->{server};
       my $sip,$group,$port,$domain;
       foreach my $ss  (@$list_r)
       {
           if ($ss->{schname} eq 'system' || $ss->{schname} eq 'LD' || $ss->{schname} eq 'LDAP' || $ss->{schname} eq 'Radius'){next;}
           $sip=$ss->{ip};
           $group=$ss->{group};
           $port=$ss->{port};
           $domain=$ss->{domain};
       }
       my @dc = split(/\./,$domain);
       my $info='';
       $info=$info.'cn='.$username;
       $info=$info.",cn=".$group;
       foreach my $result (@dc)
       {
           $info=$info.',dc='.$result;
       }
       my @status = `/usr/local/apache/qb/setuid/run /usr/sbin/ldapwhoami -H ldap://$sip:$port -x -D \"$info\" -w $password`;
       foreach my $aa (@status)
       {
           if (!grep(/Success/,$aa)){next;}
           if (grep(/Success/,$aa))
			{
				$success = '1';
				foreach my $server (@$list)
			   {
				   if ($server->{description} eq 'None' || $server->{description} ne 'AD'){next;}
				   my $userlist = $server->{member};
				   my $ttime=time()+(8*60*60);
				   foreach my $user (@$userlist)
				   {
					   if (($user->{idd} eq $username && ($ip eq $user->{ip} || $user->{ip} eq '') && ($user->{time} eq '' || ($ttime - $user->{time}) > 0)))
					   {
						   $user->{time} = $ttime;
						   if ($user->{iip} ne '')
						   {
								system("/usr/local/apache/qb/setuid/run /sbin/iptables -t nat -D AUTH -s $user->{iip} -j RETURN");
						   }
						   $user->{iip} = $ip;
							foreach my $myquota (@$quotalist)
							{
								if($myquota->{name} eq $user->{idd})
								{
									system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -D PREROUTING -d $myquota->{ip} -j $myquota->{name}.down");
									system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -D POSTROUTING -s $myquota->{ip} -j $myquota->{name}.up");
									$myquota->{ip}=$user->{iip};
									$enable_quota=$myquota->{bs};
								}
							}
					   }
				   }
			   }
			}
			if ($success)
			{
				XMLwrite($quota,$gPATH.'quota.xml');
				XMLwrite($reflist,$gPATH.'auth.xml');
				foreach $new_ip (@$quotalist)
				{
					#print "$new_ip->{name}";
					if($new_ip->{name} eq $username){quotawork(quotaaction=>'CREAT', LINK=>$new_ip->{name});}
				}
			}
       }
   }elsif ($type eq 'LD')
   {
       foreach my $server (@$list)
       {
           if ($server->{description} eq 'None' || $server->{description} ne 'LD'){next;}
           my $userlist = $server->{member};
           my $ttime=time()+(8*60*60);
           foreach my $user (@$userlist)
           {
               if (($user->{idd} eq $username && $user->{pwd} eq $password && ($ip eq $user->{ip} || $user->{ip} eq '') && ($user->{time} eq '' || ($ttime - $user->{time}) > 0)))
               {
                   $user->{time} = $ttime;
                   if ($user->{iip} ne '')
                   {
        		system("/usr/local/apache/qb/setuid/run /sbin/iptables -t nat -D AUTH -s $user->{iip} -j RETURN");
                   }
                   $user->{iip} = $ip;
                   $success = '1';
					foreach my $myquota (@$quotalist)
					{
						if($myquota->{name} eq $user->{idd})
						{
							system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -D PREROUTING -d $myquota->{ip} -j $myquota->{name}.down");
							system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -D POSTROUTING -s $myquota->{ip} -j $myquota->{name}.up");
							$myquota->{ip}=$user->{iip};
							$enable_quota=$myquota->{bs};
						}
					}
               }
           }
           if ($success)
           {
				XMLwrite($quota,$gPATH.'quota.xml');
               XMLwrite($reflist,$gPATH.'auth.xml');
			   foreach $new_ip (@$quotalist)
			   {
					#print "$new_ip->{name}";
					if($new_ip->{name} eq $username){quotawork(quotaaction=>'CREAT', LINK=>$new_ip->{name});}
			   }
           }
       }
    }
    if ($name_check eq 0)
    {
        $badname = $username;
        $username='suspicious';
    }
	my $login_quota='1';
	if($enable_quota ne '')
	{
		system("/usr/local/apache/qb/setuid/run /bin/cat /dev/null >/tmp/login_quota");
		if($enable_quota eq "0")
        {
            system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -L $username.down --line-numbers -vn|awk '/quota/' >/tmp/login_quota");
            system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -L $username.up --line-numbers -vn|awk '/quota/' >>/tmp/login_quota");
        }
		elsif($enable_quota eq "1")
        {
            system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -L $username.total --line-numbers -vn|awk '/quota/' >/tmp/login_quota");
        }
		open(FILE,'</tmp/login_quota');
		foreach my $line (<FILE>)
        {
			if (grep(/IMQ/,$line) || grep(/PREROUTING/,$line) || grep(/source/,$line) || grep(/CTDIRMARK/,$line) || grep(/MARK/,$line)){next;}
            my @quotaref=split(/\s+/,$line);
			if($quotaref[11] eq '0')
			{
				$login_quota=$quotaref[11];
				$success = '2';
			}
		}
	}
    my @dd = split(/\//,$action->getdate());
    my $log_string = '';
	if ($success eq '0'){$log_string = "Failed"}
	if ($success eq '1'){$log_string = "Succeeded"}
	if ($success eq '2'){$log_string = "Quota_exceeded"}
    $log->Save_Log("/mnt/tclog/auth/$username/$dd[0]/$dd[1]/",$dd[2],"$ip $log_string $badname $type");
    #system("/usr/local/apache/qb/setuid/run /bin/cp -a /tmp/tclog/auth/$username /mnt/tclog/auth/");
    system(sync);
    system(sync);
    system(sync);
    if ($success eq '1')
    {
    	if($conlimit eq '1')
    	{
    		system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -A PREROUTING -p tcp -s $ip --syn -m connlimit --connlimit-above $tcp -j DROP");
    		system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -A PREROUTING -p udp -s $ip -m connlimit --connlimit-above $udp -j DROP");
    	}
        #system("/usr/local/apache/qb/setuid/run /sbin/iptables -t nat -I PREROUTING -s $ip -j ACCEPT");
        system("/usr/local/apache/qb/setuid/run /sbin/iptables -t nat -I AUTH -s $ip -j RETURN");
        #system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -I AUTH -d $ip -j ACCEPT");
        #system("/usr/local/apache/qb/setuid/run /sbin/iptables -t mangle -I AUTH -s $ip -j ACCEPT");
        print  "$ip,$success"
    }elsif ($success eq '2')
    {
        print  "$ip,$success"
    }elsif($success eq '5')
    {
        print "$mac,$success"

    }else
    {
        print  "$ip,$success"
    }
