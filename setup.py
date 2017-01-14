# This file is liscenced under the GNU GPL v3
import sys
import os
import webbrowser
import time
import shutil

pyver = sys.version_info[0]
if pyver == 3: # Checks and confirms python 3 is installed.
    break
else:
    print("Download Python 3!")
	try:
	    webbrowser.open(https://www.python.org/downloads/)
	time.sleep(5)
	quit()

try: #Retrieves OS information for filesystem.
    opsys = os.uname().sysname.lower()
except AttributeError: #except for windows and osx systems.
    opsys = sys.platform.lower()
	
if opsys == 'win32':
    os.chdir(..)
	shutil.copytree('LibreWorkout-master', 'C:\\Program Files\\LibreWorkout')