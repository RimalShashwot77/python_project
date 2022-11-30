# Assignment Operator
# = Simple Assignment Operator
# shift value from right to left variable
var1 = 20
print(var1)

var1, var2 = 34,35
print(var1, var2)

var1, var2 = var2, var1 # swap
print(var1,var2)

# Multiple Assignment
var1 = var2 = var3 = 100
print(var1, var2, var3)
print(id(var1))
print(id(var2))
print(id(var3))

# Short-Hand Assignment Operator
num1 = 20
print(id(num1))
# num1 = num1 + 5
num1 +=5
print(id(num1))
print(num1)

# 2. Arithmetic Operators
n1 = {'sid':1}
n2 = {'name':'6''Your Name'}
n3 = n1 + n2
print(n3)

# + Addition
n1 = array('i', [3,4,5])
n2 = array('i', [6,7,8])
n3 = n1 + n2
print(n3)

# Assignment Operator
# +, -, *, /
var1 = 20
var2 = 7
var3 = var1//var2
var4 = var1%var2
var5 = var1 ** var2
print (var3,var4,var5)
var6 = math.pow(2, 4)
print(var6)
var7 = math.sqrt(49)
print(var7)

# Relational Operator
# compare two values and return boolean result
#  == Equals to 
# value 1 is equal to value2 ->  True
var1 = 89
var2 = 80
result = (var1 == var2)
print(result)

# Less than  <
# Left value is less than right value -> True
v1 = 12
v2 = 20
result = v1 < v2
print(result)

# Greater than or equals to
# Left value is greater than or equals to right value-> True
v1 = 10
v2 = 5*2
result = v1>=v2
print(result)

# Not Equal to !=
# Left value is not equals to right value
v1 = 20
v2 = 30
result1 = v1 == v2
result2 = v1 != v2

# 4. Logical Operator
# a. and
result = (10>5) and (10>6)
print(result)
result = (10>50) and (10>6)
print(result)

# b. or
# c. not
# True -> False
# False -> True
print(not True)
print(not False)
print(not True or False)
print(not False and False)

# 5. Other Operators
# [], {}, (), .