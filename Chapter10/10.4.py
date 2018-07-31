#Dicitonaries and tuples

#items() method of dictionaries
d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
u = d.items()
print(d.items())
print(t)
print(t == u)

for key, val in list(d.items()):
    print(val, key)

#create a list sorted by values, not keys
l = list()
for key, val in d.items():
    l.append((val, key))
    print(l)
l.sort() #sort modifies the list and stores as the same variable. 
print(l)
l.sort(reverse=True)
print(l)