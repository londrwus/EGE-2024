from ipaddress import *

net = ip_network(f'192.168.32.48/255.255.255.240', 0)

cnt = 0
for adr in net:
    new_adr = bin(int(adr))[2:].zfill(32)
    if new_adr.count('1') % 2 != 0:
        cnt += 1

print(cnt)