#
# Workout Testbed
# 11APR16
# Drew Davis
#

# IMPORT
import os.path # file checking for login purposes
import shelve # persistant dict for saving user profiles
import mastery
import exersize
import time

# GLOBAL
debug = 0

def login(day, date):

    user = raw_input("Login: ")
    print "%s, today is %s the %s" % (user, day, date)

    # quick create a file!
    if user != os.path.isfile(user):
        f = open(user, "a")
        f.close()

    # WE USE SHELVE FROM HERE ON OUT!
        

def main():
    week = 1
    m = mastery
    e = exersize
    day = time.strftime('%a')
    date = time.strftime('%d%b%y')

    exer = e.Exersize("Bent Hollow Body Hold", 1, m.SIXTY[week])

    login(day, date)

    if debug != 0:
        uinput = raw_input("Please enter attribute to examine: ")
        print getattr(exer, uinput)

main()
