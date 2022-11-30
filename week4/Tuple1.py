# print(help(tuple))
# Declare and initialize
# from array import array
# tup1 = ()
# tup1 = tuple()
# tup1 = tuple([4,5,6,7,8]) # List to tuple
# tup1 = 3,4,5,6,7,8,9
# arr1 = array('i', [6,2,3,4,5])
# tup1 = tuple(arr1) # array to tuple

# count(self,value, /)
# index(self,value, start=0,stop=9223372036854775807
# tup1 = 5,4,3,6,7,8,9,2,3,4,6
# value = 5
# result = tup1.count(value)
# print(result)

# index(self,value, start=0,stop=9223372036854775807
# tup1 = 6,3,4,5,6,7,2,1,2,3,5,6
# value = 5
# result = tup1.index(value)
# print(result)

import random
# num = random.random()
# print(num)
# num1 = random.random(10,20)
# print(num1)

# print(random.random())
# print(random.randint(0,10))

# 1.) Create a blank list
list1 = []

# 2.) Append 100 random numbers in list(int)
import random
MAX = 100
for i in range(MAX):
    tmp = random.randint(16,24)
    list1.append(tmp)
print(list1)

# Export all values to data.txt file(save)
file1 = open("data.txt", "w")
for i in range(len(list1)):
    file1.writelines(str(list1[i]))
file1.close()

# Print Max Number of List
max = max(list1)
min = min(list1)
print(max)
print(min)

# Search user given number in list
tmp = int(input("Enter any number to search : "))
result = list1.count(tmp)
if(result == 0):
    print("Not Found")
else:
    print("Found {} times".format(result))