#Chapter 9: Dictionaries

#person(key) to age(value) dictionary

age = dict()
age ['mark'] = 55
age ['lisa'] = 22
#age['mark', "lisa", 'pablo', 'jorge'] = {55, 22, 86, 56} #This doesn't work
ages = {'mark': 55, 'lisa': 22, 'pable': 86, 'jorge': 56}
print('age: ', age)
print('ages: ', ages)

#Ex9.1
x = 0
wordpositions = dict()
fhand = open('R:\\OneDrive\\PythonProjects\\InputOutput\\Input\\words.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        x += 1
        wordpositions [word] = (x) #Position x is overwritten if word occurs again. So get last position
print(wordpositions)
print('There are', len(wordpositions), 'unique words in this file.')

x = 0
wordcount = dict()
fhand = open('R:\\OneDrive\\PythonProjects\\InputOutput\\Input\\words.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] = wordcount[word] + 1
print (wordcount)

x = 0
lettercount = dict()
fhand = open('R:\\OneDrive\\PythonProjects\\InputOutput\\Input\\words.txt')
for line in fhand:
    line = line.rstrip()
    line = line.replace(' ', '')
    letters = list(line)
    for letter in letters:
        # print(line)
        # print(lettercount)
        # print(letters)
        # print('letter is: ', letter)
        if letter not in lettercount:
            lettercount[letter] = 1
        else:
            lettercount[letter] = lettercount[letter] + 1
print ('Letter count: ', lettercount)