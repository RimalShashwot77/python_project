# def readInt():
#
#     # read input from keyboard
#     tmp = input("Enter any number : ")
#
#     # convert tmp to int
#     tmp = int(tmp)
#
#     # return value of tmp
#     return tmp
#
# def calcSum(n1, n2):
#     return n1+n2
#
# def printMessage(label,value):
#     print(label,value)

def f1():
    print("Hello from f1")
def f2():
    print("Hello from f2")
def f3(message):
    print(message)
def f4(n1, n2):
    return n1+n2,
def f5():   # Nested Loop
    tmp = f4(7,8)
    f3(tmp)
def f6(n1=0 ,n2=0):   #Default Parameterized
    return n1+n2
def f7():   #Recursive Function
    f7()