'''
1.Please download thethree text files attached in this lecture and put them in a folder. The first text file contains the textContent1.The second contains Content2and the third Content3.
2. You should create a Python script that generates a new text file which should contain the content of all three text files. So the generated file should have this content:

Content1
Content2
Content3

In other words, your Pythonscript should merge the three text files.
3. Also, the name of the output file should be the current timestamp. Example:2017-11-01-13-57-39-170965.txt
You have some tips in the next lecture and the solution in the lecture afterthat.
'''
'''
WARNING: DO NOT RUN THIS MULTIPLE TIMES WITHOUT DELETED SOME FILES IT HAS CREATED. MEMORY ISSUES WILL ENSUE SINCE IT WILL OPERATE ALSO ON THE NEWLY CREATED FILES WHICH BECOME SUBSEQUENTLY LARGER.
'''

import datetime

files = ['content1.txt', 'content2.txt', 'content3.txt']
contents = []

for f in files:
    with open(f, 'r') as r:
        for line in r:
            print(line)
            contents.append(line)
            print(contents)

with open(((datetime.datetime.now()).strftime(r'%Y-%m-%d-%H-%M-%S-%f')) + '.txt', 'w') as w:
    for content in contents:
        w.write(content + '\n')

'''
Yay! Got it on first try!!
'''