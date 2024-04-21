from ipaddress import *

cnt_glob = 0
for a in range(256):
    ip = ip_address(f'207.0.{a}.167')
    net = ip_network(f'{ip}/255.255.255.192', 0)

    if all(str(bin(int(adr))[2:].zfill(32))[:16].count('0') > str(bin(int(adr))[2:].zfill(32))[16:].count('0') for adr in net):
        cnt_glob += 1

print(cnt_glob)
