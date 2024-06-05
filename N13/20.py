from ipaddress import *

net = ip_network('122.159.136.144/255.255.255.248', 0)

cnt = 0
for adr in net:
    new_adr = bin(int(adr))[2:].count('1')
    if new_adr % 4 != 0:
        cnt += 1
        
print(cnt)