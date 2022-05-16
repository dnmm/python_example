dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print( "dict['Age']: ", dict['Age'])
# update
dict['Age'] = 8; # update existing entry
print ("dict['Age']: ", dict['Age'])
#remove
del dict['Name']; # remove entry with key 'Name'
#dict.clear();     # remove all entries in dict
#del dict ;        # delete entire dictionary

print(dict)