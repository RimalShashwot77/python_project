# from array import array
# list1 = [5,6,7,2,2] # style-1
# list1 = list(5,6,7,8,9) # style-2
# arr1 = array('i', [7,8,9,2,3]) # array declare and initialize
# list1 = list(arr1) # array to list # style-3

# from array import array
# # indexing and slicing
# list1 = list([5,6,7,8,1,2]) #0-4
# print(list1[0])
# print(list1[2])
# print(list1[3]) # IndexError: list index out of range
#
# print(list1[-1])
# print(list1[-5])
# print(list1[-10]) # IndexError: list index out of range

# Slicing
# Expression multiple values
# list1 = list([5,6,7,8,9,3,4,2,4,7]) # 0 to 9
# result = list1[5:100]
# print(result)

# Functions
# append(self,object, /)
# list1 = list([5,6,7,8,9,3,4,2,4,7]) # 0 to 9
# list1.append(True)
# list1.append(False)
# list1.append("Hello")
# print(list1)

# clear(self, /)
# list1.clear()
# print(list1)

# list1=[2,4,5] # declare and initialize
# list2 = list1 # list1 assign to list2
# list2.clear() # clear list2
# print(list1)  # print list1
# print(list2)  # print list2
# print(id(list1)) # memory address
# print(id(list2)) # memory address

# copy(self, /)
# list1 = [4,5,6]
# list2 = list1 # Copy by reference -> Address
# list3 = list1.copy() # Copy by Value
# print(id(list1))
# print(id(list2))
# print(id(list3))

# count(self,value, /)
# list1 = [6,7,8,9,0,2,3,4]
# num1 = 7
# result = list1.count(num1)
# print(result)

# extend(self,iterable, /)
# list1 = [6,7]
# list2 = [3,4,1]
# list1.extend(list2)
# print(list1)

# from array import array
# arr1 = array('i', [4,6,7,8,8])
# list1.extend(arr1)
# print(list1)

# index(self,value, start=0, stop=)
# try:
#     list1 = [4,6,7,8,8]
#     value = int(input("Enter any number: "))
#     result = list1.index(value)
#     print(result)
# except:
#     print("Not Found")

# Example-2
# list1 = [5,6,2,3,5]
# value = 5
# result = list1.index(value)
# print(result)

# Example-3
# list1 = [5,6,2,3,5]
# value = 5
# count = list1.count(value)
# start=-1
# for i in range(count):
#     start+=1
#     print(list1.index(value,start))

# Example-4
# insert(self,index,object, /)
# append(self,object, /)
# list1 = []
# list2 = [5,2]
# list1.append(5)
# list1.append(6)
# list2.insert(0,8)
# print(list1)
# print(list2)

# pop(self, index=-1, /) # Remove
# list1 = [6,4,2,8,9]
# print(list1)
# list1.pop()
# print(list1)

# remove(self,value, /) # Remove value
# list1 = [5,6,7,8,5]
# print(list1)
# list1.remove(5) # value 5 -> 0 to N-1
# print(list1)

# Example-5
# list1 = [5,6,7,8,5]
# print(list1)
# count = list1.count(5)
# for i in range(count):
#     list1.remove(5)
# print(list1)

# Example-6
# reverse(self, /)
# list1 = [4,5,1,2,9]
# print(list1)
# list1.reverse()
# print(list1)

# Example-7
# sort(self, /, *, key = None, reverse = False)
list1 = [9,1,5,2,7]
print(list1)
list1.sort() # Ascending order
print(list1)
list1.sort(reverse = True) # Descending order
print(list1)
list1.sort(reverse = False) # Ascending order
print(list1)