#!/bin/sh

cd /home/pablo/.juniper_networks/network_connect

#
# Use the "-r" option when logging in remotely
# In other words, uncomment the first invocation of juniperncprompt.py
# and comment out the second
#
# ./juniperncprompt.py -r "Active Directory Users" vpn.constantcontact.com
./juniperncprompt.py vpn.constantcontact.com
