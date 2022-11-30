import sys
# None
var1 = {1,2,3,4,5,6,7,8,9}
print(var1) # accessing value
print(type(var1))
print(id(var1))
# how to print memory size
print(sys.getsizeof(var1)) 
# None - None45
# bool - True /  False
# int - 123
# float - 123.456
# complex - 1234+567j
from array import array
var1 = {'sid':1, 'Shashwot': 'Baluwatar'}
print(var1) # accessing value
print(type(var1))
print(id(var1))
print(sys.getsizeof(var1))
print(len(var1))
var1 = [1,2,3,1,2,5,6] # list
var2 = set(var1) # set
del var1
del var2
print(var1)
print(var2)
