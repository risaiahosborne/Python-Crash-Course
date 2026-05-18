Places = ['Japan', 'Mexico', 'Hawaii', 'Congo', 'Antarctica']

print(Places)

print(sorted(Places)) # Temporary sort

print(Places) # Original list remains unchanged

print(sorted(Places, reverse = True)) # Temporary reverse sort

print(Places) # Original list remains unchanged

Places.reverse() # Permanent reverse
print(Places)

Places.reverse() # Reversing back to original
print(Places)

Places.sort() 
print(Places) # Permanent sort in alphabetical order

Places.sort()
print(Places) # Permanent sort in reverse alphabetical order

#Every_Function = ['append()', 'insert()', 'remove()', 'pop()', 'sort()', 'reverse()', 'len()'
Things = ['Everest', 'Nile', 'Chile', 'Paris', 'English']
print(len(Things)) # Length of the list 
print(Things)  # Original list
print(Things.append('London')) # Appending an item to the list
print(Things) # List after appending
print(Things.remove('Chile')) # Removing an item from the list
print(Things.insert(1, 'Atlanta')) # Inserting an item at a specific index
print(Things) # List after insertion
print(Things.pop()) # Popping the last item from the list
print(Things) # List after popping
print(sorted(Things)) # Temporary sort
print(Things) # Original list remains unchanged
print(Things.reverse()) # Reversing the list prints None because reverse() modifies the list []
print(len(Things)) # Length of the list after modifications