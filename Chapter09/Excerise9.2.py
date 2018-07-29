"""
Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
"""

daycounts = {} 
f=0
l = 0
while f == 0:
    try:
        fname = input('What\'s the name of the txt file? (No extention. Press Ctrl+c to quit)')
        fhand = open('R:\\OneDrive\\PythonProjects\\InputOutput\\Input\\' + fname + '.txt')
        print('File available. Working...')
        f = 1
    except:
        print('Could not find file. Please try again')
for line in fhand:
    l += 1
    #print('Trying line', l)
    if line.startswith('From '):
        print('Found on line', l)
        line = line.strip()
        words = line.split()
        day = words[2]
        if day not in daycounts:
            daycounts[day] = 1
        else:
            daycounts[day] += 1
print(daycounts)
    

# define a dictionary
# find the lines starting with From
# strip lin
# split line
# get 3rd word
# if its not in dict its count is one, otherwise count is +=1
# print dict
