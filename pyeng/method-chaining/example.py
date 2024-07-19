line = "switchport trunk allowed vlan 10,20,30"
words = line.split()
vlans_str = words[-1]
vlans = vlans_str.split(",")
print(vlans)


#shorter version of code
vlans = line.split()[-1].split(",")
print(vlans)