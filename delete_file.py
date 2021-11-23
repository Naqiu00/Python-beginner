# delete file

import os
import shutil

path = 'copy.txt'
folder = 'empty_folder'

try:
    # os.remove(folder)     # delete a file  
    # os.rmdir(folder)      # delete an empty directory
    shutil.rmtree(folder)   # delete a directory along with it's files
except FileNotFoundError:
    print("There is no such file in this folder")
except PermissionError:
    print("You do not have the permission!!")
except OSError:
    print("You cannot delete using this function.")
else:
    print(folder + " was deleted")