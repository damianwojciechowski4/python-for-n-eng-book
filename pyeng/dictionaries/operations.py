london = {
'id': 1,
'name': 'London',
'int_vlan': 320,
'user_vlan': 1010,
'mngmt_vlan': 99,
'to_name': None,
'to_id': None,
'port': 'G1/0/11'
}

#getting value of key 'name'
print(london['name'])

# adding new key-value pair
london['int_speed'] = '1Gbps'

print(london)

#rewrite key-value pair
london['int_speed'] = '10Gbps'
print(london)


# deleting key-value pair
del london['to_name']


print(london)