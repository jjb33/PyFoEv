def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars

r = input('Enter rate: ')
e = input('Enter Euros: ')
print(currency_converter(float(r), float(e)))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

password = ''
while password != 'python123':
    password = input('Enter password: ')
    if password == 'python123':
        print('You are logged in!')
    else:
        print('Sorry, try again.')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

names = ['earl', 'jason', 'jan', 'merl', 'perry', 'ron']
email_doms = ['gmail.com', 'yahoo.com', 'hotmail.com', 'pearl', 'amy', 'rick',]

for i, j in zip(names, email_doms):
    print(i, j)