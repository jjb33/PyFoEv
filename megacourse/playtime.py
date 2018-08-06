def mintohrs (seconds, min = 70):
    hours = min / 60 + seconds / 3600
    return hours
#    print(hours)

from pathlib import Path
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print(os.path.realpath(__file__))
print(os.getcwd())
fpath = os.getcwd()
print(fpath)
fhand = open(fpath + '\\..\\..\\InputOutput\\Input\\romeo.txt', 'r')
print('Type is', type(fhand), fhand)
content = fhand.read()
print(content)
print(content)
print(fhand.readlines())
fhand.seek(0)
print(fhand.readlines())
fhand.seek(0)
print(fhand.readlines())