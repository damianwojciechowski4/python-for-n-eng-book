#intialize set
vlans = [10,20,30,40,50,100,10]

#Removal of repetitve elements
vlans_set = set(vlans)  
print(f"Unordered set: {vlans_set}")

sorted_vlans_set=sorted(vlans_set)
print(f"Ordered set: {sorted_vlans_set}")


#Methods
set1 = {10,20,30,40}

print(f"set1 {set1}")
print("Add method: ")

#add method
set1.add(50)

print(set1)

#discard method
print("Discard method: ")
set1.discard(10)
print(set1)

#clear method - empties set
print("Clear method: ")
set1.clear()
print(set1)

