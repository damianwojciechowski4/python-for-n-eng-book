vlans = [10, 20,30,1,2,100,10,30,3,4,10]


vlans_set  = set(vlans)


new_vlansList = list(vlans_set)
stdout = sorted(new_vlansList)
print(stdout)