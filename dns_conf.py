#!/usr/bin/env python

import os
import dns as dn
import dicosR1 as d
import dicosR2 as dR2


# FILE /etc/bind/named.conf.options

output = open("named.conf.options", "w")

output.write("acl \"trusted\" {\n")
output.write("	10.1.0.0/16;\n")
output.write("        localhost;\n")
output.write("        localnets;\n")
output.write("};\n")
output.write("\n")

output.write("options {\n")
output.write("        directory \"/var/cache/bind\";\n")
output.write("\n")

output.write("        recursion yes;\n")
output.write("        allow-query { trusted; };\n")
output.write("        allow-recursion { trusted; };\n")
output.write("\n")

output.write("        forwarders {\n")
output.write("               "+ dn.dns1+";\n")
output.write("               "+ dn.dns2+";\n")
output.write("        };\n")
output.write("\n")

	
output.write("	dnssec-enable yes;\n")
output.write("	dnssec-validation yes;\n")
output.write("\n")

output.write("        auth-nxdomain no;    # conform to RFC1035")
output.write("        listen-on-v6 { any; };\n")
output.write("};\n")

output.close()
os.system("mv /root/named.conf.options /etc/bind/named.conf.options")



# FILE /etc/bind/named.conf.local

output = open("named.conf.local", "w")

output.write("zone "+d.domain+" {\n")
output.write("    type master;\n")
output.write("    file \"/etc/bind/zones/db.resolve\"; # zone file path\n")
output.write("};\n")
output.write("\n")

output.write("zone \"1.10.in-addr.arpa\" {\n")
output.write("    type master;\n")
output.write("    file \"/etc/bind/zones/db.reverse\";  # 10.1.0.0/16 subnet\n")
output.write("};\n")

output.close()
os.system("mv /root/named.conf.local /etc/bind/named.conf.local")


# FILE /etc/bind/zones/db.resolve

output = open("db.resolve", "w")

output.write(";\n")
output.write("; BIND data file for local loopback interface\n")
output.write(";\n")
output.write("$TTL	604800\n")
output.write("@       IN      SOA     r1."+d.domain+". admin."+d.domain+". (\n")
output.write("                  3       ; Serial\n")
output.write("             604800     ; Refresh\n")
output.write("              86400     ; Retry\n")
output.write("            2419200     ; Expire\n")
output.write("             604800 )   ; Negative Cache TTL\n")
output.write(";\n")
output.write("; name servers - NS records\n")
output.write("     IN      NS      r1."+d.domain+".\n")
output.write("\n")

output.write("; name servers - A records\n")
output.write("r1."+d.domain+".          IN      A       10.1.2.1\n")
output.write("\n")

output.write("; 10.1.0.0/16 - A records\n")
output.write("r2."+d.domain+".          IN      A       10.1.3.1\n")

for (i, x) in enumerate(d.dico_ip):
  output.write(d.dico_host[i]+"."+d.domain+".        IN      A      "+d.dico_ip[i]+"\n")
for (i, x) in enumerate(dR2.dico_ip):
  output.write(dR2.dico_host[i]+"."+d.domain+".        IN      A      "+dR2.dico_ip[i]+"\n")

output.close()
os.system("mv /root/db.resolve /etc/bind/zones/db.resolve")

# FILE /etc/bind/zones/db.reverse

output = open("db.reverse", "w")

output.write(";\n")
output.write("; BIND reverse data file for local loopback interface\n")
output.write(";\n")
output.write("$TTL	604800\n")
output.write("@       IN      SOA     "+d.domain+". admin."+d.domain+". (\n")
output.write("                              3         ; Serial\n")
output.write("                         604800         ; Refresh\n")
output.write("                          86400         ; Retry\n")
output.write("                        2419200         ; Expire\n")
output.write("                         604800 )       ; Negative Cache TTL\n")
output.write("; name servers\n")
output.write("      IN      NS      r1."+d.domain+".\n")
output.write("\n")

output.write("; PTR Records\n")
for (i, x) in enumerate(d.dico_ip):
  ip = d.dico_ip[i].split(".")
  output.write(ip[3]+"."+ip[2]+"        IN      PTR      "+d.dico_host[i]+"."+d.domain+".	;\n")
for (i, x) in enumerate(dR2.dico_ip):
  ip = dR2.dico_ip[i].split(".")
  output.write(ip[3]+"."+ip[2]+"        IN      PTR      "+dR2.dico_host[i]+"."+d.domain+".	;\n")

output.close()
os.system("mv /root/db.reverse /etc/bind/zones/db.reverse")


# RESTART bind

os.system("service bind9 restart")
