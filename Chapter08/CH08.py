cities = ['Chicago', 'Cleveland', 'Los Angeles']
numbers = [14, 3, 4]
archers = ['rick', 'steve', 'april']

print(archers)
for spot in archers:
    print (spot)

print(cities + archers)
print('april' in archers)

#range returns a list of indices from 0 to n − 1, where n is the length of the list
print(range(len(archers)))
print(len(archers))

for person in range(len(archers)):
    # print(person, 'is cool!') # Nope! this prints the index number is cool.
    print(archers[person], 'is cool!')

archers[0:2] = ['tony', 'bert'] #index 2 is not included
print(archers)

archers.append('simone')
print(archers)

archers.extend(['bill', 'butch', 'trey'])
print(archers)
newpeeps = ['anna', 'parker', 'Brom']
archers.extend(newpeeps)
print(archers)

#Sort is a void method so will not return the ordered list to be stored as a variable
archers.sort()
print(archers) #Capital letters are printed first
t = archers.sort()
print(t)

a = archers.pop(3) #remove bert and returns the name bert, in case you want to save it to a variable
print(archers)
print(a)

del archers[1] #removes anna. same as pop but doesn't return the removed value
print(archers)
del archers[2:4] #deletes a range not incluing last
print(archers)

archers.remove('tony') #deletes the element in case you don't know index
print(archers)

print(sum(numbers)/len(numbers)) #quick way to average a list of numbers

userlist = []
# while True:
#     num = input('Gimme a number (type \'done\' to exit):\n')
#     if num == 'done':
#         break
#     userlist.append(float(num))
# print('Your list is:\n', userlist)
# print('And your average is:\n', (sum(userlist) / len(userlist)))

s = 'thisisalongword'
t = list(s) ##############LIST IS A FUNCTION. FUNCTIONS TAKE ARGUMENTS
print(t)

s = 'this is a very long sentence I would-like to split each word into a list element'
t = s.split() #################SPLIT IS A METHOD
print(t)

s = 'HYPHEN-SEPARATED-sentence-here'
t = s.split('-') #You can specifiy a delimiter
print(t)

delimiter = '^^^^' #Can rejoin a list into string, but have to define the delimter to put between newly joined elements
s = delimiter.join(t)
print(s)

def tail(t):
    return t[1:]

print(tail(t))
print(t)

def bad_delete_head(t):
    t = t[1:]
    return t
print('BEH= ', bad_delete_head(t))
print('t= ', t)
