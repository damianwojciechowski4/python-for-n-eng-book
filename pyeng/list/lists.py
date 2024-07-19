#list initialization
list3 = [1, 20, 30, 50]
print(list3)


#reversed list
rev_list3 = list3[::-1]
print(rev_list3)

#replacing list element
list3[1]=200
print(list3)

#returning number of items in list
print(len(list3))   

#sorted function
names = ['John', 'Michael', 'Antony']
print(sorted(names))    


interfaces = [['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]
i=0
for i in interfaces:
    interface_id = i[0]
    ip_address = i[1]

    print(f"Interface ID: {interface_id}, IP Address: {ip_address}")



#joining the list into one variable
vlans = ['10','20','30']

joined = ','.join(vlans)
print(joined)


#appending new list element
vlans  = ['10','20','30']

vlans.append('400')

print(vlans)

#extending the list with another list

vlans1  = ['10','20','30']
vlans2 = ['300', '400', '500']

vlans1.extend(vlans2)
print(vlans1)

#removal of last element from the list
vlans1.pop(-1)
print(vlans1)

#removal of specific element from the list
#in remove() you must specify item to be deleted no the index!
vlans1.remove('400')
print(vlans1)



#getting index of the element
print(vlans1.index('300'))


#inserting element at specific index
vlans1.insert(2, '1000')
print(vlans1)


#sorting elements in the list
vlans1.sort()
print(vlans1)


#zip method