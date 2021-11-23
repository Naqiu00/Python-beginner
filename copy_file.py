# copyfile() = copy the contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copy metadata (file's creation and modification times)

import shutil

shutil.copy2('test.txt', 'copy.txt') #src, dst

