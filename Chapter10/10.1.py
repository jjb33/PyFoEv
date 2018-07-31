t = 'a', 'b', 'c', 'd', 'e'
u = ('a', 'b', 'c', 'd', 'e')
v = tuple(('a', 'b', 'c', 'd', 'e'))
print('T or F? t = u.')
print(t == u == v)

w = tuple('fuxxomed')
print(w)
print(w[2:4])

#can't modify tuple, but can create another
x = t[0:3] + w[4:]
print(x)
