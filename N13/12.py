from ipaddress import *

net = ip_network('112.154.132.0/255.255.252.0', 0)

cnt = 0
for adr in net:
    new_adr = bin(int(adr))[2:].zfill(32)

    if new_adr[16:].count('0') % 2 != 0:
        if new_adr[:16].count('1') <= new_adr[16:].count('0'):
            cnt += 1

print(cnt)