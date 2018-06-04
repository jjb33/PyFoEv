d = 7 / 3
q = 7 // 3
r = 7 % 3
print(d, q, r)

t = 57 % 10
print("t =", t)

tt = 5703 % 100
print('tt =', tt)

############################

#adding numbers as variables
first = 10
second = 15
print(first + second)

#adding strings as variables
first = '100'
second = '150'
print(first + second)
print("the above \"number\" is actually a concatenation of the previous two string variables")

###########################
#Prompting for input
# inp = input('What is your name?\n') #The question here could be a variable too. Like below
# print(inp, ",eh?")

# promptQ = "What is your name?\n"
# inp = input(promptQ)
# print("Your name is", inp, 'eh?')

############################
word = "thisisarediculouslylongword withspace"
for p in word:
    print(p)

number = '98459483049583450924059823045'
for diggitydigit in number:
    print(diggitydigit)
#Note: 'int' object is not iterable

#############################################################################
#Excercise 2.3
#ask for hours and pay rate and retern the user's gross income.

# hours = int(input("How many hours did you work this week?\n"))
# rate = int(input("How much money do you make per hour?\n"))
# gross = str(hours*rate)
# print('If that is the case, your gross pay for the week is $' + gross + ".")

#Exercise 2.4
width = 17 #This is an int
height = 12.0 #This is a float

s = width//2   # Value is 8 and type is int
t = width/2.0  # Value is 8.5 and type is float
u = height/3   # Value is 4.0 and type is float
v = 1 + 2 * 5  # Value is 11 and type is int

#Excercise 2.5
#User inputs Celsius temp. Convert it to F and print it out.

C = float(input("What Celsius temp do you want me to convert to F?\n"))
F = (1.8*C) + 32
print("The corresponding temperature in Fahrenheit is", F, "degrees.")