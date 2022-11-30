class Driver():
    def __init__(self, did=0, name='', licenseno=''):
        self.did = did
        self.name = name
        self.licenseno = licenseno
    # getters
    def getDID(self):
        return self.did
    def getName(self):
        return self.name
    def getLicenceNo(self):
        return self.licenseno

    # setters
    def setDID(self, did):
        self.did=did
    def setName(self, name):
        self.name=name
    def setLicenceNo(self, licenseno):
        self.licenseno=licenseno
    # __ str __
    def __str__(self):
        return ("{}, {}, {}".format(self.did, self.name, self.licenseno))
