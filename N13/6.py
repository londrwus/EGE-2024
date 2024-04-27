from ipaddress import *

ip1 = ip_address('10.96.180.231')
ip2 = ip_address('10.96.140.118')

for mask in range(33):
    net = ip_network(f"10.96.180.231/{mask}", 0)
    net2 = ip_network(f"10.96.140.118/{mask}", 0)

    if net != net2 and net[0] < ip1 < net[-1] and net2[0] < ip2 < net2[-1]:
        print(bin(int(net.netmask))[2:].zfill(32).count("0"))  # 13

    # different networks and find max count '0' in bin
