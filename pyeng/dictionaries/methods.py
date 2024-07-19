test = {
    'name':'Damian',
    'age': 18,
    'phone': '1234567890',
    'hobby': 'coding'
}

print(test)

#sorting dictionary keys
print(sorted(test))

#clearing dictionary
test.clear()
print(test)

test2 = {
    'name':'Damian',
    'age': 18,
    'phone': '1234567890',
    'hobby': 'coding'
}

#get
# when you query a key that does not exist, it will return None
print(test2.get('name'))
print(test2.get('name2'))

#setdefault
# searches for key and if there is no key it creates key with default None value
height = test2.setdefault('height')
print(test2)
#if key exists setdefault() returns its value
age = test2.setdefault('age')



#keys, values, items
print(f" Keys: {test2.keys()}")
print(f" Values: {test2.values()}")
print(f" Items: {test2.items()}")

#getting list of keys
keys = list(test2.keys())
print(keys)
#getting list of values
values = list(test2.values())
print(values)


#removing key and value
print('Removing key "name" and its value')
del test2['name']
print(test2)

#adding key and value
test2['name'] = 'Damian'

#update - add contents of one dictionary to another
test2.update({'height': 5.11, 'favourite_color': 'khaki'})
print(test2)

#updating values
test2.update({'height': 6.0, 'favourite_color': 'blue'})
print(test2)