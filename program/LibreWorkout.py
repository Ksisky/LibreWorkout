# This file is liscenced under the GNU GPL v3
# This file is the main program file which uses the objects in functions.py.
# Python 3
import functions as f
import os

print('Welcome to LibreWorkout.')
newuser = not os.path.exists('savedinfo.dat')
if newuser == True:
    print('We see you are a new user!')
    f.newuser()
