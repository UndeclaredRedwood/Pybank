#implementation 1, pull inital accounts from  csv
import csv
import account

class Accounts:
    _totalInd = None

    def __init__(self):
        self._totalInd = 0
        with open('accounts.csv') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self._totalInd += 1

    def _addAcc(self, ind, accNum, accPass):

