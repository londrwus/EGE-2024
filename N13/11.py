from ipaddress import *

for a in range(256):
    net = ip_network(f'183.192.{a}.0/255.255.252.0', 0)
    
    cnt = 0
    cnt_lay = 0
    for adr in net:
        cnt += 1
        new = bin(int(adr))[2:].zfill(32)
        if new[16:].count('1') > 3:
            cnt_lay += 1

    if cnt == cnt_lay:
        print(a)
        break