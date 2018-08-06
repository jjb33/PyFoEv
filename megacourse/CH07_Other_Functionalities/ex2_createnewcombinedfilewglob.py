'''
same as prev exercise but using glob
'''

import datetime, glob

#files = ['content1.txt', 'content2.txt', 'content3.txt']
files = glob.glob('*.txt')
contents = []
print(files)

for f in files:
    with open(f, 'r') as r:
        for line in r:
            #print(line)
            line = line.rstrip()
            contents.append(line)
            #print(contents)

with open(((datetime.datetime.now()).strftime(r'%Y-%m-%d-%H-%M-%S-%f')) + '.txt', 'w') as w:
    for content in contents:
        w.write(content + '\n')

'''
Yay! Got it on first try!!
'''