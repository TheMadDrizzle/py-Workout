#
# Workout Testbed
# 11APR16
# Drew Davis
#

# IMPORT
from sys import argv
import os.path
import mastery
import exersize
import time

# GLOBAL
ufile = argv # prepping for workout save between uses
debug = 1

def login(name, day, date):
    if name != os.path.isfile(name):
        pass

def main():
    week = 1
    m = mastery
    e = exersize
    day = time.strftime('%a')
    date = time.strftime('%d%b%y')

    exer = e.Exersize("Bent Hollow Body Hold", 1, m.SIXTY[week])

    if debug != 0:
        uinput = raw_input("Please enter attribute to examine: ")
        print getattr(exer, uinput)
    
    user = raw_input("Please input your name: ")
    name = open(user, "w+")
    print "%s, today is %s the %s" % (name, day, date)

main()
