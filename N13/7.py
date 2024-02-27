from ipaddress import *

net = ip_network("192.168.240.0/255.255.255.0", 0)

k = 0
for ip in net:
    ip_adr = bin(int(ip))[2:].zfill(32)
    if ip_adr.count("1") == ip_adr.count("0"):
        k += 1

print(k)  # 8
