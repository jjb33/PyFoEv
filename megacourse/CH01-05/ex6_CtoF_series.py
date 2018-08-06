'''
converts user input as Celsius to Fahrenheit
'''
temperatures = [10,-20,-289,100]

def f2c (Celsius):
    C = Celsius
    try:
        float(C)
    except:
        print('That\'s not a number!\n')
    C = float(C)
    if C < -273.15:
        print('Can\'t be lower than -273.15.')
    F = (9 / 5) * float(Celsius) + 32
    return F
    
for temp in temperatures:
    print(f2c(temp))