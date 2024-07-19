nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat_replaced = nat.replace('Fast', 'Gigabit')
print(nat_replaced)

