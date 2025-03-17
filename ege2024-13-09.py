from ipaddress import ip_network

net = ip_network("172.16.128.0/255.255.192.0")
number = 0
for addr in net:
    addr = int(addr)
    if str(bin(addr)[2:]).count("1") % 2 != 0:
        number += 1
print(number)
