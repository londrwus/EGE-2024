from ipaddress import *

net = ip_network("135.12.171.214/255.255.248.0", 0)
print(net)  # 135.12.168.0/21
