'''
converts user input as Celsius to Fahrenheit
'''
def f2c (Celsius):
    try:
        float(Celsius)
    except:
        print('Please enter a number. Exiting.\n')
        exit()
    F = (9 / 5) * float(Celsius) + 32
    return F


C = float(input('What is the temperature in Celsius?\n'))
print(f2c(C))
