#you cannot create an empty set using literal set - (it will be dictionary not the set!)
set1 = {}
print(type(set1))

set2 = set()
print(type(set2))



print("Set from string: ")
set3 = set('long string of text')
print(set3)

print("Set from list: ")
set4 = set([10,20,30,10,50])
print(set4)


