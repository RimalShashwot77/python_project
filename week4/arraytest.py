# # from array import array
# # arr1 = array('i',[])
# # print(arr1)
# # arr1.append(6)
# # print(arr1)
# # arr1.append(1)
# # arr1.append(55)
# # arr1.append(69)
# # arr1.append(3)
# # print(arr1)
# #
# # # reading 25 ages
# # ages = array('i', [])
# # MAX = 500
# # for i in range(MAX):
# #     tmp = int(input("Enter age: "))
# #     ages.append(tmp)
# # print(ages)
#
# from array import array
# arr1 = array('i', [6,4,3,2,1,1,2,3,4,5,5,5,5,4,5])
# result = arr1.count(5)
# print(result)
# tmp = int(input("Enter no to search"))
# result = arr1.count(tmp)
# print(("found {} times".format(result)))
#
# # # index
# # arr1 = array('i', [4,5,6,7,8,5,3,4,56,67,8,9,5,43,2,2,34])
# # tmp = 5
# # count_result = arr1.count(tmp)
#
# #indexing
# arr1 = array('i', [4,5,6,7,8,9,10,11,12,13,14,5])
# result_count = arr1.count(15)
# if(result_count>=1):
#     result = arr1.index(15)
#     print(result)
# else:
#     print("Not Found")
#
#print(help(array))

# from array import array
# arr2 = array('i',[3,9,5,7,8,9])
# result1 = arr2.count(7)
# print(result1)

# try:
#     result2 = arr2.index(7) # value
#     print(result2)
# except:
#     print("Not Found")
# arr2 = array('i',[3,9,5,7,8,9])
# arr2.insert(2,8)
# print(arr2)
#
# arr2.pop()
# print(arr2)
# arr2.pop(i=2) # Error
# print(arr2)

# try:
#     arr2.remove(50)
#     print(arr2)
# except:
#     print("Not Found")
#
# try:
#     arr2.reverse()
#     print(arr2)
# except:
#     print("Error")
#
# # Assignment-1
# """
# -------- Main Menu --------
# 1. Add Value
# 2. Display All
# 0. Exit
# ---------------------------
# Enter your choice : _1
# ---------------------------
# Enter value to add : _7
# 7 Add successfully
# -------- Main Menu --------
# 1. Add Value
# 2. Display All
# 0. Exit
# ---------------------------
# Enter your choice : _2
# Elements of an array
# 7
# -------- Main Menu --------
# 1. Add Value
# 2. Display All
# 0. Exit
# ---------------------------
# Enter your choice : _0
# ---------------------------
# Bye!
# """

# print(help(list))