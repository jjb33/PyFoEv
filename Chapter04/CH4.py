import random
listi = []
for i in range(0,22,3): #upper limit is not inclusive
    listi.append(i)
    # print(listi)
    
listj = []
for i in range(2): #2 is the number of random numbers to be generated
    x = random.random()
    listj.append(x)
    # print(listj)

listk = []
for i in range(2):
    x = int(random.random()*10) #Don't need to do this since there is a randomint function. Radom() should be called random percentage
    listk.append(x)
    # print(listk)

listl = []
x = random.randint(2,1000)
listl.append(x)
# print(listl)

#Picking random # from a list
t = [1, 6, 144, 5959]
p = random.choice(t)
# print(p)

####################################################
#Defining own functions rather than using built-in functions

def print_above_crap():
    print('--------HERE IS A PRINTOUT OF THE ABOVE CRAP-------')
    print('list I:\n', listi)
    print('list J:\n', listj)
    print('list K:\n', listk)
    print('list L:\n', listl)
    print('P:\n', p)

print(print_above_crap) #defining a function creates a variable with the same name. However, it is just the function object
print(type (print_above_crap))
print_above_crap()

def crapX3(): #new function calls above function 3 times
    print_above_crap()
    print_above_crap()
    print_above_crap()

crapX3()

##################################
#Parameters
def print_twice(xxx): #xxx is just a placeholder for definition purposes. When actually using the function, it will perform the steps in the body on whatever you put in there
    print(xxx)
    print(xxx)

print_twice(33333333)
print_twice(print_above_crap()) #Could simplify crapX3() function. Insted of print(xxx), just use xxx
print_twice('panda')

def execute_twice(xxx):
    return xxx
    # xxx #This does not execute a 2nd time. Has to do with recursive calling of a function? Yes the value of the function does not get stored unless you assign it to a variable!
ssss = execute_twice(print_above_crap())
print(ssss)

#Fruitful vs void functions
#Fruitful functions spit out a result, but the result does not get stored unless you assign it to a variable
#Void functions will return "None" if you try to assign it to a variable. Void functions are doing something...not giving something

#Example
def addtwo(a, b):
    added = a + b
    return added #"return" can be thought of as "produce this as output". You can then store what the function "produced" as a variable (see below)
x = addtwo(3, 5)
print(x)

##########################################
#Exercises
#Ex4.5
def fred():
    print("Zap")
def jane():
    print("ABC")
jane()
fred()
jane()

#Ex4.6
def computepay(hours, rate):
    # hours = int(hours)
    # rate = int(rate)
    if hours <= 40:
        pay = (hours * rate)
        print(pay)
    if hours > 40:
        pay = ((40 * rate) + ((hours - 40)*(rate * 1.5)))
        print(pay)

computepay(45, 10)

#Ex4.7
def computegrade(score):
    try:
        float(score)
    except:
        print('Bad Score')
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
testscore = input('What was your score?\n')
computegrade(testscore)
uu = 6    
#break line