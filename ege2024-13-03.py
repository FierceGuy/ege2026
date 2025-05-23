network = 79 * (256**3) + 128 * (256**2) + 96 * 256  # IP-адрес сети в числе
mask = 255 * (256**3) + 255 * (256**2) + 224 * 256    # Маска сети в числе

host_bits = 32 - bin(mask).count('1')  # Количество битов для хостов
total_hosts = 2 ** host_bits           # Всего IP-адресов в сети

count = 0
for i in range(total_hosts):
    ip = network + i
    bin_ip = bin(ip)[2:]  # Двоичная запись IP
    if bin_ip.count('1') % 7 != 0 and bin_ip.endswith('100'):
        count += 1

print(count)
