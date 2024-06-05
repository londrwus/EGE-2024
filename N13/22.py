from ipaddress import *

net = ip_network('192.168.32.48/255.255.255.192', 0)

cnt = 0
for adr in net:
    new_adr = bin(int(adr))[2:].zfill(32).count('1')
    if net[0] < ip_address('192.168.32.48') < net[-1]:
        if new_adr % 5 != 0:
            cnt += 1
            
print(cnt)