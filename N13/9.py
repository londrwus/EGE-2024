from ipaddress import *

net = ip_network("192.168.32.128/255.255.255.192", 0)

cnt = 0
for adr in net:
    bin_adr = bin(int(adr))[2:].zfill(32)
    if bin_adr.count('1') % 2 == 0:
        cnt += 1

print(cnt)