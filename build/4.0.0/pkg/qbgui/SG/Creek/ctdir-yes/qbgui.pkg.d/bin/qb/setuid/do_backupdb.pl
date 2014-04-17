#!/usr/bin/perl

require ('/usr/local/apache/qb/qbmod.cgi');

# --------------------------
# main program start routine
# --------------------------

my $QB_BACKUPDB_FILE="/usr/local/apache/qbconf/backupdb.xml";
my $QB_CRONTAB="/etc/crontab";
#=======================================================
# parsing backupdb.xml into $backupdb

my $backupdb=XMLread($QB_BACKUPDB_FILE);

#=========================================================

#------------------------------------------------------------------

if ( $backupdb->{ftpserverip} && $backupdb->{ftpserver})
{
    if ( $backupdb->{ftpfrequency}=~m/day/)
    {
      $backupdb->{ftpfrequency}=~s/\.day//g;
      modifyfile($QB_CRONTAB,"backupdbftp.*","backupdbftp ".$backupdb->{ftpserverip}." ".$backupdb->{ftpusername}." ". $backupdb->{ftppassword}." ".$backupdb->{ftpdir}); # refresh https proxy port No.
      modifyfile($QB_CRONTAB,"^#.*backupdbftp","0 0 */$backupdb->{ftpfrequency} * *  root       /opt/qb/bin/script/backupdbftp"); # remove # character in the stateament
      modifyfile($QB_CRONTAB,"^*.*backupdbftp","0 0 */$backupdb->{ftpfrequency} * *  root       /opt/qb/bin/script/backupdbftp"); # remove # character in the stateament
    }
    if ( $backupdb->{ftpfrequency}=~m/hour/)
    {
      $backupdb->{ftpfrequency}=~s/\.hour//g;
      modifyfile($QB_CRONTAB,"backupdbftp.*","backupdbftp ".$backupdb->{ftpserverip}." ".$backupdb->{ftpusername}." ". $backupdb->{ftppassword}." ".$backupdb->{ftpdir}); # refresh https proxy port No.
      modifyfile($QB_CRONTAB,"^#.*backupdbftp","0 */$backupdb->{ftpfrequency} * * *  root       /opt/qb/bin/script/backupdbftp"); # remove # character in the stateament
      modifyfile($QB_CRONTAB,"^*.*backupdbftp","0 */$backupdb->{ftpfrequency} * * *  root       /opt/qb/bin/script/backupdbftp"); # remove # character in the stateament
    }
    if ( $backupdb->{ftpfrequency}=~m/everyd/)
    {
      $backupdb->{ftpfrequency}=~s/\.everyd//g;
      modifyfile($QB_CRONTAB,"backupdbftp.*","backupdbftp ".$backupdb->{ftpserverip}." ".$backupdb->{ftpusername}." ". $backupdb->{ftppassword}." ".$backupdb->{ftpdir}); # refresh https proxy port No.
      modifyfile($QB_CRONTAB,"^#.*backupdbftp","0 $backupdb->{ftpfrequency} * * *  root       /opt/qb/bin/script/backupdbftp"); # remove # character in the stateament
      modifyfile($QB_CRONTAB,"^*.*backupdbftp","0 $backupdb->{ftpfrequency} * * *  root       /opt/qb/bin/script/backupdbftp"); # remove # character in the stateament
    }
}
else
{
    modifyfile($QB_CRONTAB,"^#*"."backupdbftp","#"."backupdbftp"); # Disable https proxy function
}
                    
