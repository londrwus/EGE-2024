from ipaddress import *

ip = ip_address('238.237.149.255')

for mask in range(33):
    net = ip_network(f'238.237.149.255/{mask}', 0)

    if net[0] < ip < net[-1]:
        print(mask, net) # 22