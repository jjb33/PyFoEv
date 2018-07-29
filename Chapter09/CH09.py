#Chapter 9: Dictionaries

#person(key) to age(value) dictionary

age = dict() #defines the dictionary
age ['mark'] = 55 #adds to the dictionary
age ['lisa'] = 22
#age['mark', "lisa", 'pablo', 'jorge'] = {55, 22, 86, 56} #This doesn't work
print('age: ', age)
ages = {'mark': 55, 'lisa': 22, 'pable': 86, 'jorge': 56} #create and add simultaneously
print('ages: ', ages)

#Ex9.1
x = 0
wordpositions = dict() #each new position of a word is effectively a 'count' of the word
fhand = open('R:\\OneDrive\\PythonProjects\\InputOutput\\Input\\words.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        x += 1
        wordpositions [word] = (x) #Position x is overwritten if word occurs again. So get last position
print(wordpositions)
print('There are', len(wordpositions), 'unique words in this file.')
print('Is the word \"programs\" in the file? ', ('programs' in wordpositions))
print ('programs' in wordpositions)

#Simple counting of letters in words
word = 'fluxommedmegalomaniac'
d = dict()
for letter in word:
    if letter in d:
        d [letter] += 1
    else:
        d [letter] = 1
print(d)

#The GET method (takes a key, and a value to return if key is not there). rembmer object.method()
#example 1:
word = 'fluxommedmegalomaniac'
d = dict()
for letter in word:
    d [letter] = d.get(letter, 0) + 1 #cf. age ['lisa'] = 22
print('can I have an "m"? ', (d.get('m', 0))) #useful for iterations and other code computations
print('can I have a "z"? ', (d.get('z', 'not there'))) #usefule for user feedback


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