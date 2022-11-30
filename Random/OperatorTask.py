# Result Processing
# declare
sid = None
fullname = None
sub1 = None # Obtained Mark
sub2 = None
sub3 = None
sub4 = None
Total  = None
average = None
result = None
# input
sid = input("Enter Student ID : ")
fullname = input("Enter your name : ")
sub1 = input("Enter SUB-1 : ")
sub2 = input("Enter SUB-2 : ")
sub3 = input("Enter SUB-3 : ")
sub4 = input("Enter SUB-4 : ")
Total = sub1+sub2+sub3+sub4
average = Total/4
result =  (sub1>=30 and sub2>=30 and sub3>=30 and sub4>=30) 
# process
# calculate total
# calculate average
# calculate result
# output
print("SID : {}" .format(sid))
print("Name : {}" .format(fullname))
print("SUB1 : {}" .format(sub1))
print("SUB2 : {}" .format(sub2))
print("SUB3 : {}" .format(sub3))
print("SUB4 : {}" .format(sub4))