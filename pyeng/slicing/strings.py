string1 = "interface FastEthernet1/0"


#slicing --> "interface"
print(string1[0:9])

#reversed string
string1[-1::-1]



a='0123456789'


#odd numbers
print(a[1::2])

#even numbers
print(a[::2])

#reverse the string
print(a[::-1])



string2 = 'FastEthernet'

print(string2.upper())

print(string2.lower())

print(string2.swapcase())

print(string2.capitalize())

string3 = "Hello, hello, hello, hello"
print(string3.count('Hello'))
print(string3.count('hello'))

string4 = 'interface FastEthernet0/1'
print(len(string4))
print(string4.find('Fast'))
print(string4[string4.find('Fast')::])

#if no match find returns -1
print(string4.find('noMatch'))


#Startswith and endswith
print(string4.startswith('interface'))
print(string4.endswith('0/1'))
print(string4.endswith('0/2'))

#Replace
string5=string4[string4.find('Fast')::]
string5=string5.replace('Fast','Gigabit')
print(string5)

#String  - removing special characters from thr string (eg \t\n\r\f\v)
print("""
        Strip
""")

string6='\n\tinterface FastEthernet0/1\n'
print(string6)
string6=string6.strip()
print(string6)


#removal of characters from the string

ad_metric='[110/1045]'
print(ad_metric)
print(ad_metric.strip('[]'))
#Removing characters from left side of string
print(ad_metric.lstrip('['))
#Removing characters from right side of string
print(ad_metric.rstrip(']'))


#Split method
print('Split method')
print("*" * 40 )


#Split method
string1 = "switchport trunk allowed vlan 10,20,30,100-200"
commands = string1.split()

vlans = commands[-1].split(',')
print(vlans)

for vlan in vlans:
    print(vlan)