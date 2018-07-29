#dictionary = key:value pairs
d = {}
x = 0
while x < 50:
    x += 1
    d['key' + str(x)] = x
print(d)

#print key:val pairs
for pair in d: #thought this looked for key:Val pair, but look for key. so should be key not pair. d[pair] gets value.
    print(pair, "has a value of", d.get(pair, 'nothing'))

# for y in d:
#     print(d[y])

print((20 * '.'), (2 * '\n') + (20 * '.'))
for key in d:
    if 20 < d[key] < 41:
        print (key, d[key])





