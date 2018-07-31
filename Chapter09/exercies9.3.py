"""
Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from
each email address, and print the dictionary.
"""

'''
Outline:
define dict
choose file (skip the user request for speed this time)
open file
find From or From:
if there, 
    count w dictionary
print key:val pairs (key, value)
'''
d = {}
#fout = open('R:\\OneDrive\\PythonProjects\\InputOutput\\Output\\e9.3fromcounts.txt', 'w')
with open('R:\\OneDrive\\PythonProjects\\InputOutput\\Input\\maillog.txt') as f:
    for line in f:
        if line.startswith('From'):
            line = line.rstrip()
            line = line.split()
            e = line[1]
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
# for key in d:
#     fout.write(key, d[key])
# fout.close()

for key in d:
    print(key, d[key])


            