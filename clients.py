#implementation 1, pull inital accounts from  csv
#accounts are in form xxxx-xx, where the first 4 digits are the acc num and the 2nd two numbers are the "branch number"
#this will be called on initalization of the client manager and will setup some base clients to test with
#this will setup up a hash data structure to store client account num and password pairs

#change implementation to safely store passwords
#change implementation to work with a database rather than a csv
import csv
from .account import AccountStruc as accSt

class Clients:

    def __init__(self):
        self._buckets = None
        self._totalInd = None
        self._tempLs = []


        with open('path\\file.csv') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self._tempLs.append([int(row[0][0:4]+row[0][5:]), row[1]])

        self._totalInd = len(self._tempLs)

        self._initBuckets_(self._totalInd)

        for val in self._tempLs:
            self._assignToBucket_(self._totalInd, val[0], val[1])

        print(self._buckets)

    #def addClient(self, accNum, accPass):
        #accSt()

    #init bucket size based on total length
    def _initBuckets_(self, tind):
        self._buckets = [[None]] * (tind)

    def _assignToBucket_(self, tind, key, obj):


        index = key % tind
        print(index, " ", key, " ", obj)
        #temp setup for this, using a list to store key obj pair in a list
        #this wont work, needs to be  re done to properly add on a key val pair to a specific bucket
        #or just hurry up and make aa linked list and get it done

        if self._buckets[index] == [None]:
            self._buckets[index] = [[key, obj]]
        else:
            self._buckets[index].append([key, obj])



