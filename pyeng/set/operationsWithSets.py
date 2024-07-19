vlans1 = {10,20,30,40}
vlans2 = {100,101,102,103}

union = vlans1.union(vlans2)

print("Union: ")
print(union)

print('Union with operator "|" ')
union2 = vlans1 | vlans2
print(union2)

print("Intersection (common element of  set): ")
vlans1 = {10,20,30,40,200}
vlans2 = {100,101,102,103,200}
intersec = vlans1.intersection(vlans2)
print(intersec)


print("Intersection option 2 with & operator")
intersec_2 = vlans1 & vlans2
print(intersec_2)


print("Difference: ")
vlans1 = {10,20,30,40,200}
vlans2 = {100,101,102,103,200}
difference = vlans1.difference(vlans2)
print(difference)

