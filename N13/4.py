from ipaddress import *

net = ip_network('192.168.0.0/255.255.240.0', 0)

k = 0
for ip in net:
    k += 1

print(k - 2) # how many different computer addresses it can contain