# from MyFunctions import f1
# for i in range(1):
#     f1()

# from MyFunctions import f3,f4,f5,f6
# str1 = "PCPS College"
# f3(str1)
# str2 = "Kishore Shrestha"
# f3(str2)
# f4(1, "Kishore Shrestha")
# f4(12, "Hari Sharma")
# print(f6(10,9))

from MyFunctions2 import readInt,calcsum,printresult
n1 = None
n2 = None
n3 = None
n1 = readInt()
n2 = readInt()
n3 = calcsum(n1 ,n2)
printresult("Sum",n3)
