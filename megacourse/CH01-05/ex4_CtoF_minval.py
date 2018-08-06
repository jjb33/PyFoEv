'''
converts user input as Celsius to Fahrenheit
'''
def f2c (Celsius):
    F = (9 / 5) * float(Celsius) + 32
    return F

def getc():
    C = (input('What is the temperature in Celsius?\n'))
    try:
        float(C)
    except:
        print('That\'s not a number!\n')
        exit()
    C = float(C)
    if C < -273.15:
        print('Can\'t be lower than -273.15.')
        exit()

    else:
        return C

print(f2c(getc()))
