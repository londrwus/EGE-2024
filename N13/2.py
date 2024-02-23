from ipaddress import *

for mask in range(33): # cuz 32 is max value
    net = ip_network(f'118.193.30.139/{mask}', 0)
    print(net, net.netmask) # 118.193.24.0/21 255.255.248.0