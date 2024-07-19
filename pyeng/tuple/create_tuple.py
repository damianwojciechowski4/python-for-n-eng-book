list_keys = ['hostname','location','vendor','model','ios','ip']
tuple_keys = tuple(list_keys)

print (f"Tuple from keys {tuple_keys}")

print(f"Printing first key: {tuple_keys[0]}")

#you cannot assign new value
#tuple_keys[0] = 'new value'

#output error
"""
----> 9 tuple_keys[0] = 'new value'
TypeError: 'tuple' object does not support item assignment"
}
"""

#function sorted sorts tuple elements and returns list
sorted_tuple = sorted(tuple_keys)
print(f"Sorted tuple: {sorted_tuple}")





