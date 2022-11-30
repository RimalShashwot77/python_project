from driver import Driver
from ManageDriver import saveDriver,searchDriver,updateDriver,deleteDriver,allDriver

# Test-1
# d1 = Driver() # declare and initialize object
# d1.setDID(4) # set values
# d1.setName("Swoyam")
# d1.setLicenseNo("2300")
# saveDriver(d1) # save drive info

# Test-2
# driver = searchDriver('2200')
# # print(driver)
# # Check whether record found or not?
# if len(driver) == 0:
#     print("Record not found")
# else:
#     print(driver)

# Test-3
#'4'
#'Eclipse'
#'2300'
# driver2 = Driver(4,'Swoyam','2300')
# result = updateDriver(driver2)
# print(result)

# Test-4(Delete) 
# result = deleteDriver(4)
# print(result)

# Test-6(allDrivers)
driver = allDriver()
print(driver)

# Test-5
# did = name=lno =None
# did = int(input("Enter ID : "))
# name = input("NAME : ")
# lno = input("LICENSE NO : ")
# d2 = Driver(did, name, lno)
# saveDriver(d2)
# searchDriver(12345)
# ques = input("Enter the Driver's ID of the record you want to update:")
# name = input("Enter Name:")
# licen = input("Enter the License No:")
# updateDriver(name,licen,ques)
# deleteDriver(2)
# allDriver()

