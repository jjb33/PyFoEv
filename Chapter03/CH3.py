#######################
#Boolean expressions
5 == 5
5 == 6

#A single "=" is an assignment operator, while a double "==" is a comparison operator

# x != y            # x is not equal to y
# x > y             # x is greater than y
# x < y             # x is less than y
# x >= y            # x is greater than or equal to y
# x <= y            # x is less than or equal to y
# x is y            # x is the same as y
# x is not y        # x is not the same as y

print(4 == 4)
print(3 != 4)
print(4 > 3)
print(3 < 4)
print(4.1 >= 4)
print(4 <= 4.001)
print(4 is 4)
print(4 is 4.0)
print(4 is not 4.0)
#########################

#The three logical operators: and, or , not

#Conditional execution
x = 3
y = 4
z = 5

if x < 10:
    pass #pass is useful as a placeholder

if x%2 == 0:
    print("even")
else:
    print('odd')

#A simple if/elif/else "Chained condition". If there are multiple elifs, . If one of them is true, the corresponding branch executes, and the statement
#ends. Even if more than one condition is true, only the first true branch executes.
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('the two are equal')

#operators can be used to replace nested conditional, which should be used sparingly
if 0 < x and x < 10:
    print('x is a positive single-digit integer')

#############################
#using try and except
#in the Celsius to F code, make it so entering text throws a message.

try:
    C = float(input("What Celsius temp do you want me to convert to F?\n"))
    F = (1.8*C) + 32
    print("The corresponding temperature in Fahrenheit is", F, "degrees.")
except:
    print('You have to enter a number here.') #This does not give a chance for user to reenter their number



##################################################################
#Exercise 3.1
#Get gross pay and give 1.5* pay for hours over 40

hours = float(input('How many hours did you work?\n'))
pay = float(input('How much do you make per hour?\n'))
try:
    hours >= 0 == True
    hours and pay == int
except:
    print('you can\'t have negative hours')
if hours > 40:
    gross = float((40*pay) + ((hours-40)*(1.5 * pay)))
else:
    gross = float(hours * pay)
print(gross)