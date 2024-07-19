#!/usr/bin/env python3
from sys import argv



"""
• argv is a list
• all arguments are in list and represented as strings
• argv contains not only arguments that passed to script but also name of script itself
In this case, argv list contains the following elements:
['access_template_argv.py', 'Gi0/7', '4']
"""


interface = argv[1]
vlan = argv[2]

access_template = [ 'switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print(f'interface {interface}')
print('\n'.join(access_template).format(vlan))

