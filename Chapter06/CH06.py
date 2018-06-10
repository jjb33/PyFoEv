fruit = 'bananas'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

for anything in "bananas":
    print(anything*30)

print(fruit[2:4])
newword = 'Z' + fruit[1:len(fruit)]
print(newword)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print('Count of \'a\' in banana: ',count)

def lettercount (string, alpha):
    cnt = 0
    for x in str(string):
        if x == str(alpha):
            cnt = cnt +1
    return cnt
a = 'l;kasjdfkas;flaKKJKJKJKssdl;kfaslfasdl;fkassdl;fjasd;lfassdl;fdsal;k'
b = 's'
c = lettercount(a, b)
print('Number of \'s\' in string: ', c)

#the .count method does the above

# for x in y, 'in' just returns True or False
q = 'banana' in 'ALl the bananas you can use!'
r = 's' in 'bananas'
s = q = 'pears' in 'ALl the bananas you can use!'
print(q, 'and', r, 'and', s)

#for ordering, all uppercase letters come before all lowercase letters

print(type(a))
print(dir(a))
#print(dir(str))
d = a.capitalize()
print(d)

newver = ''
for letter in a:
    n = letter.capitalize()
    newver = newver + n
print('Iterating with capitalize:\n', newver)

#the function .upper() does the same as above
newver = a.upper()
print('Using the .upper() function:\n', newver)

#'find' is a string method ('search' is regex?)
print(a.find('s'))

###################
#Excercises
#6.5
strng = 'X-DSPAM-Confidence:0.8475'
pos1 = strng.find(':')
numb = strng[pos1+1:len(strng)]
numb = float(numb)
print('Type is: ', type(numb), 'and number is: ', numb)

