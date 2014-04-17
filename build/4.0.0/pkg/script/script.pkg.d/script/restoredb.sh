#!/bin/bash
#
#set -x
echo "Stopping Traffic Flow Momitor Daemon ..."
killall -9 nfcapd
echo "Cleaning current data ..."
cd /mnt/tclog/
rm -rf ./nfcapd ./total_*
echo "Unpacking backup file ..."
tar zxfC /tmp/tmp_import.tgz /mnt/tclog
echo "Starting Traffic Flow Momitor Daemon ..."
/usr/local/bin/nfcapd -w -D -t 60 -S 1 -l /mnt/tclog/nfcapd/ -p 54311

