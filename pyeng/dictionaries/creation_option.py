#Literal
r1 = {'model' : 2960, 'ios': 15.4}
print(f"Literal {r1}")

#dict key=value
r1 = dict(model=2960, ios=15.4)
print(f"Dict 1st method {r1}")


#dict 2nd method
r1 = dict ([('model', 2960), ('ios',15.4)])
print(f"Dict 2nd method {r1}")

#dictionary from keys
#use case: when the keys are only known
d_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
r1 = dict.fromkeys(d_keys, None)
print(f"Dict from keys {r1}")


# dictionary from keys with own value
router_models = ['ISR2811','ISR2911', 'ISR2921', 'ASR9002']
r1 = dict.fromkeys(router_models, 'unknown')

print(f"Dict from keys with own value {r1}")

# dictionary from keys with value []
#each key reffers to the same list object, be careful!

router_models = ['ISR2811','ISR2911', 'ISR2921', 'ASR9002']
routers = dict.fromkeys(router_models, [])
routers['ASR9002'].append('test_location')
print(f"Dict from keys with own value as [] {routers}")
#output:Dict from keys with own value as [] {'ISR2811': ['test_location'], 'ISR2911': ['test_location'], 'ISR2921': ['test_location'], 'ASR9002': ['test_location']}
