"""
Advanced Parsing:
translate() is a find/replace/delete function with maketrans() as the argument
"""
import string
fyle = 'R:\\Onedrive\\PythonProjects\\InputOutput\\Input\\romeopunct.txt'
typetest = "string"
try:
    fhand = open(fyle)
    print("File is open")
    print("Excluding the following from file:\n" + (string.punctuation) + '\n' + (40 * '~'))
except:
    print('The file can not be opened.')
counts = dict()
x = 0
for line in fhand:
    line = line.rstrip() #string
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower() #can't lower a list. put before list
    words = line.split() # now a list
    for word in words:
        # if word not in counts:
        #     x = 1
        # else:
        #     x += 1
        # counts[word] = x
        if word not in counts: #better way?
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)






