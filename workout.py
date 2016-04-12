#
# Workout Testbed
# 11APR16
# Drew Davis
#

# IMPORT
from sys import argv

# GLOBAL
saveFile, openFile = argv


# WORKOUT
class Exersize(object):
    # Add index for auto advance upon completion of week 12?
    def __init__(self, name, week, mastery):
        self.name = name
        self.mastery = mastery
        self.week = week
    def printAll(self):
        print "Todays workout is:  %s, %s" % (self.name, self.mastery)

# MASTERY
SIXTY = { 1: '3X12', 2: '5X12', 3: '3X24', 4: '3X12', 5: '4X24', 6: '4X36', 7: '5X36', 8: '5X18' }
THIRTY = { 1: '3x6', 2: '5x6', 3: '3x12', 4: '3x6', 5: '4x12', 6: '4x18', 7: '5x18', 8: '5x9' } 
FIFTEEN = { 1: '3x3', 2: '5x3', 3: '3x6', 4: '3x3', 5: '4x6', 6: '4x9', 7: '5x9', 8: '4x5' }
TEN = { 1: '3x2', 2: '5x2', 3: '3x4', 4: '3x2', 5: '4x4', 6: '4x6', 7: '5x6', 8: '5x3' }
FIVE = { 1: '3x1', 2: '5x1', 3: '3x2', 4: '3x1', 5: '4x2', 6: '4x3', 7: '5x3', 8: '5x2' }

# List builder proto?
#class List(object):
#    def __init__(self)
#

def main():
    week = 1
    exersize = Exersize("Bent Hollow Body Hold", 1,  SIXTY[week])
    exersize.printAll()

main()
