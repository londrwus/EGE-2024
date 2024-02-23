from ipaddress import *

for mask in range(33):
    net = ip_network(f'173.103.25.118/{mask}', 0)
    print(net, 32 - mask) # max value of 0 in mask
    # output correct: 173.103.24.0/21 11 => 11