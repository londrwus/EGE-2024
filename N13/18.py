from ipaddress import *

ip1 = ip_address('216.54.187.235')
ip2 = ip_address('216.54.174.128')

for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)

    if net1 != net2 and net1[0] < ip1 < net1[-1] and net2[0] < ip2 < net2[-1]:
        print(mask)