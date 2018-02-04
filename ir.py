import csv
from enum import Enum

Dict = {"a":("b", "c", "d")}

class ir:
    def __init__(self, op, out, in1, in2):
        self.op = op
        self.out = out
        self.in1 = in1
        self.in2 = in2
    
    def Insert(self, rowList):
        for key, val in Dict.iteritems():

with open('3ac.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"', doublequote=True, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        for element in row:

