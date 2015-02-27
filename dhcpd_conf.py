#!/usr/bin/env python

import dicosR1 as d
import deniedMAC as deny
import os
import dns as dn


output = open("out1.txt", "w")

output.write("ddns-update-style none;\n")
output.write("option domain-name "+d.domain+";\n")
output.write("option domain-name-servers "+ d.dns +";\n")
output.write("\n")
output.write("default-lease-time 3600;\n")
output.write("max-lease-time 7200;\n")
output.write("\n")

output.write("authoritative;\n")
output.write("log-facility local7;\n")
output.write("\n")

output.write("subnet 10.1.2.0 netmask 255.255.255.0 {\n")
output.write("  range 10.1.2."+ d.range_dyn_dhcp_min +" 10.1.2."+ d.range_dyn_dhcp_max +";\n")
output.write("  option broadcast-address 10.1.2.255;\n")
output.write("  option routers 10.1.2.1;\n")
output.write("\n")

for (i, x) in enumerate(d.dico_ip):
	output.write("  host "+ d.dico_host[i] +" {\n")
	output.write("    hardware ethernet "+ d.dico_mac[i] +";\n")
	output.write("    fixed-address "+ d.dico_ip[i] +";\n")
	output.write("  }\n")
	output.write("\n")

for (i, x) in enumerate(deny.dico_mac_block):
	output.write("  host "+deny.dico_host_block[i]+" {\n")
	output.write("    hardware ethernet "+deny.dico_mac_block[i]+";\n")
        output.write("    deny booting;\n")
	output.write("  }\n")
	output.write("\n")

output.write("}\n")
output.close()

os.system("mv /root/out1.txt /etc/dhcp/dhcpd.conf")
os.system("/etc/init.d/isc-dhcp-server restart")
