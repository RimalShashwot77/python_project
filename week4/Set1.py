# declare and initialize
from array import array
# set1 = {}
# set1 = set([1,2,3,4,5,6]) # List to set
# set1 = set((1,2,3,4,5,6)) # Tuple to set
# set1 = set(array('i', [3,4,5,6,7])) # array to set

# add(...)
# set1 = {1,2,3}
# set1.add(6)
# set1.add(1)
# print(set1)

# copy(...)
# set1 = {3,4,1,2,3,1,2}
# set2 = set1
# print(id(set1))
# print(id(set2))
# set3 = set1.copy()
# print(id(set3))

# difference(...)
# set1 = {3,4,5,6,7,8}
# set2 = {4,5,6,7}
# set3 = set1.difference(set2)
# print(set3)
# set3 = set2.difference(set1)
# print(set3)

# intersection(...)
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# set3 = set1.union(set2)
# print(set3)

# pop(...)
# remove(...)
set1 = {1,2,3,1,2,3,4,6,7}
print(set1)
set1.pop() # remove from -1 index
print(set1)
set1.remove(3) # remove value
print(set1)