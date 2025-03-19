#Account  refers to

class AccountStruc:
    accountNum = None
    accountPass = None
    subAccLs = []

    def __init__(self, accNum, accPass):
        self.accountNum = accNum
        self.accountPass = accPass

    def addSubAcc(self, subAcc, baseAmt):
        #stores a
        self.subAccLs.append((subAcc, baseAmt))
