int = "interface FastEthernet0/{}".format('1')
print(int)


print('{}'.format(100))


print('{}'.format(1,2,3,4))


print("Test {}, Test{}".format(1,2))

vlan, mac , intf = ['100', 'aabb.cc80.7000', 'Gi0/1']

print("{:>15} {:>15} {:>15}".format(vlan, mac, intf))


#Converting to binary
print("{:b} {:b} {:b} {:b}".format(192, 100, 1, 1))


print("{:08b} {:08b} {:08b} {:08b}".format(192, 100, 1, 1))


#Passing variables in curly braces
print("{ip}/{mask}".format(mask='24',ip='192.168.1.1'))


ip_template = """
    IP address:
    {:<8} {:<8} {:<8} {:<8}
    {:08b} {:08b} {:<08b} {:08b}
"""

print(ip_template.format(192, 168, 1, 1, 192, 168, 1, 1))

print("With value indexes")
ip_template = """
    IP address:
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
"""

print(ip_template.format(192, 168, 1, 1))


#f-String - available since Python 3.6
print("f-String")
ip='10.1.1.1'
mask = 24

print(f"IP: {ip}, mask: {mask}")


oct1, oct2, oct3, oct4 = [192, 168, 1, 1]

print(f"""
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}
""")

