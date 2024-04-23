from ipaddress import *

ip = ip_address('192.168.32.128')

cnt = 0
net = ip_network(f'{ip}/255.255.255.192', 0)
for adr in net:
    if bin(int(adr))[2:].zfill(32).count('1') % 2 == 0:
        cnt += 1

print(cnt)