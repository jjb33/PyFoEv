from random import *

d = {}
randlist = []
while len(randlist) < 50:
    r = randrange(1, 51)
    if r in randlist:
        continue
    else:
        randlist.append(r)
    d['value' + str(r)] = r

for x in d:
    if 20 <= d[x] < 26:
        print(x, d[x])

#put in order
dlist = list(d.keys())
dlist.sort(key=int)
for key in dlist:
    print(key, d[key]) #right Python order, but not my tempo. Will come back to it.