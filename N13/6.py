from ipaddress import *

for mask in range(33):
    net = ip_network(f"10.96.180.231/{mask}", 0)
    net2 = ip_network(f"10.96.140.118/{mask}", 0)

    if net != net2:
        print(bin(int(net.netmask))[2:].zfill(32).count("0"))  # 13

    # different networks and find max count '0' in bin
