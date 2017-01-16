# This file is liscenced under the GNU GPL v3
# This file contains the objects used in LibreWorkout.py.
# Python 3
import shelve
import time

def newuser():
    libredb = shelve.open('savedinfo')
    actcreation = time.strftime("%B %d, %Y", time.gmtime())
    print('What is your name')
    name = input('>>> ')
    
