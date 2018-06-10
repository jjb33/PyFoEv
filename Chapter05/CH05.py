#Chapter 5: ITERATIONS

#While
n = float(5)
while n > 0:
    print(n)
    n = n - 0.1
print ('Blastoff')

#While True would have been the thing to use in my computegrade program to keep getting new input without having to restart the program
def computegrade(score):
    try:
        float(score)
    except ValueError:
        print('Bad Score Format')
    if float(score) >= 0.90:
        print('A')
    if 0.80 <= float(score) < 0.90:
        print('B')
    if 0.70 <= float(score) < 0.80:
        print('C')
    if 0.60 <= float(score) < 0.70:
        print('D')
    if float(score) < 0.60:
        print('F')
# 

#For loops
#For is for a definite set of things
#While is for an indefinite period until a condition is flase.

count = 0
sumnums = 0
list1 = [4, 12, 77, 94, 3, 55, 99, 700, 454, 5, 6, 99, 2, 55, 66, 33]
for anything in list1: #'anything" is the iteration variable and can be anythin.  It also doesn't have to be used in the loop body
    count = count + 1
    sumnums = sumnums + anything
print('Count: ', count)
print('Sum: ', sumnums)

#len() and sum() are built-in functions that accomplish the same as above

largest = None
for num in list1:
    if largest is None or num > largest:
        largest = num
    print(num, '   ', largest)
    
print('Largest: ', largest)

smallest = None
for num in list1:
    if smallest is None or num < smallest:
        smallest = num
    print(num, '   ', smallest)
    
print('Smallest: ', smallest)

#The above can be accomplised with max() and min(). These are built-in functions.

#Excercises
#Ex5.1

count = 0
numsum = 0
values = []
print(type(values))
while True:
    num = input('Gimme a number: ')
    if num == 'done':
        break
    try:
        int(num)
    except:
        print('That\'s not a number, dum dum. Try again.')
        continue
    num = int(num)
    values.append(num)
    count = count +1
    numsum = numsum + num
    avg = numsum / count
print('Count: ', count)
print('Running Total: ', numsum)
print('Average: ', avg)
print('Smallest: ', min(values))
print('Largest: ', max(values))
exit()