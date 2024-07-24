# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

network = str(input("Input Network in the format 10.1.1.0/24: "))
delimiters = [".","/"]
for delimiter in delimiters:
    networkList = network.split(delimiter)

ipList = networkList[0].split(".")
mask = networkList[1]
ones  = int(mask)
zeros = 32 - ones
binary_mask = str("1" * ones + "0" * zeros)



octet_length = 8
ip_oct1 = int(ipList[0])
ip_oct2 = int(ipList[1])
ip_oct3 = int(ipList[2])
ip_oct4 = int(ipList[3])




print(f"""
{ipList[0]:<8} {ipList[1]:<8} {ipList[2]:<8} {ipList[3]:<8} 
{ip_oct1:08b} {ip_oct2:08b} {ip_oct3:08b} {ip_oct4:08b} 
""")




#mask in decimal form
m_oct1 = str(binary_mask[0:octet_length])
m_oct2 = str(binary_mask[octet_length:2*octet_length])
m_oct3 = str(binary_mask[2*octet_length:3*octet_length])
m_oct4 = str(binary_mask[3*octet_length:4*octet_length])

#mask in binary form
m_digit_oct1 = int(binary_mask[0:octet_length],2)
m_digit_oct2 = int(binary_mask[octet_length:2*octet_length],2)
m_digit_oct3 = int(binary_mask[2*octet_length:3*octet_length],2)
m_digit_oct4 = int(binary_mask[3*octet_length:4*octet_length],2)

print(f"""
Mask: 
/{mask}
{m_digit_oct1:<8} {m_digit_oct2:<8} {m_digit_oct3:<8} {m_digit_oct4:<8}    
{m_oct1} {m_oct2} {m_oct3} {m_oct4}
""")
