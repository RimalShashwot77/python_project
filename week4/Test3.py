# import library
from MyFunctions3 import readInt,calcSum

# call function
# n1 = readInt()
# n2 = readInt()
# n3 = readInt()
# n4 = calcSum(n1, n2, n3)
# print("n1:",n1)
# print("n2:",n2)
# print("n3:",n3)
# print("SUM:",n4)

n1 = 7
n2 = 8
n3 = 9
# add and run
n4 = calcSum(calcSum(n1, n2),n3)
print(n4)4
printMessage("Num1:", n1)
printMessage("Num2:", n2)
printMessage("Num3:", n3)
printMessage("Num4:", n4)

from array import array
arr1 = array('i',[])
print(arr1)
arr1.append(6)
