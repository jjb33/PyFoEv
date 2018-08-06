with open('fruits.txt', 'r') as fi:
    for line in fi:
        line = line.rstrip()
        print(len(line))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

wfile = open('fruit_w.txt', 'w')
list = ['Line 1\n', 'Line 2\n', 'Line 3\n']
for line in list:
    wfile.write(line)
wfile.close() #content will not save until this is done. (Use while instead?)

ofile = open('fruit_w.txt', 'r')
for line in ofile:
    line = line.rstrip()
    print(line)
ofile.close()


'''
below lines were printing each character as a "line")
'''
# ofile = open('fruit_w.txt', 'r')
# print('ofile:\n', ofile)
# content = ofile.read()
# print('content:\n ',content)
# for line in content:
#     line = line.rstrip()
#     line = line.split()
#     print('for line in: ', line)
# ofile.close()
# print('Why the hell is this printing each letter on a new line?????')
