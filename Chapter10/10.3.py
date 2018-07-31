m = ['have', 'fun'] # a list
x, y = m #left is tuple
print('x=' + x)
print('y=' + y)

t = 'a', 'b'
u = 'b', 'a'
print('t=', t)
print('u=', u)
#The old switcharoo:
t = u #left becomes a tuple of variables, right a tuple of expressions
print('t=', t)
print('u=', u)

#as long as number of things on left = number of things on right, can assign
addr = 'jason.banks@case.edu'
uname, domain = addr.split('@') #list w/ 2 elements
print(uname)
print(domain)

