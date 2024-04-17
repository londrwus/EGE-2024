from ipaddress import *

net = ip_network('136.36.240.16/255.255.255.248', 0)

for adr in net:
    print(bin(int(adr))[2:].zfill(32))