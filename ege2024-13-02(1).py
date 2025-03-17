from ipaddress import ip_network

net = ip_network("94.253.128.0/255.255.128.0", strict=False)

number = 0
for addr in net:
    addr = int(addr)
    addr = bin(addr)[2:]
    if addr.count("1") % 6 != 0 and addr[-3:] == "101":
        number += 1

print(number)
