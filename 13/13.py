"""1 номер"""
# import ipaddress
# net = ipaddress.ip_network('172.16.160.0/255.255.240.0', 0)
# c = 0
# for i in net:
#     b = bin(int(i))[2:].zfill(32)
#     if b.count('1') % 2 == 0:
#         c += 1
# print(c)

"""2 номер"""
# import ipaddress
# net = ipaddress.ip_network('111.222.0.124/255.255.224.0', 0)
# for i in net:
#     b = bin(int(i))[2:].zfill(32)
#     if b.count('1') * b.count('0') % 2 != 0:
#         print(i, sum(int(i) for i in str(i).split('.')))

"""3 номер"""
# import ipaddress
# for m in range(32):
#     net = ipaddress.ip_network(f'84.23.84.23/{m}', 0)
#     if str(net.network_address) == '84.23.84.0':
#         mask = '1'*m+'0'*(32-m)
#         ok3 = mask[16:24]
#         ok4 = mask[24:32]
#         print(int(ok3, 2) + int(ok4, 2))










