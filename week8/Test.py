from driver import Driver
from ManageDriver import saveDriver
# Test-1
d1 = Driver()
d1.setDID(1)
d1.setName("Driver1")
d1.setLicenceNo("6775555")
saveDriver(d1)
