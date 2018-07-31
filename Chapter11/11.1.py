'''
REGEX:
.........................
Identifiers:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
.  any character, except for a new line
\b the whitespace around words
\. a period

Modifiers:
{1,3} we'ere expecting 1-3 characters
{x} expecting x amount
+ match one or more
? match 0 or 1
* match 0 or more
$ match the end of a string
^ matching the beginning of a string
| either or 
[] range or variance [A-Za-z] [1-5a-qA-Z]

Whitespace Characters
\n new line
\s space
\t tab
\f form feed (rare)
\r return (rare)

DONT FORGET HAVE TO ESCAPE THESE:
.  + *  ? [] $ ^ () {} | \
'''
import os
print(os.listdir())
print('CWD is: ', os.getcwd())
import re

# x = 0
# f = open('.\\Chapter11\\maillog.txt', 'r')
# while x < 15:
#     for line in f:
#         if re.search('From', line):
#             line = line.rstrip()
#             print(line)
#             x += 1
#OR
x = 0
f = open('.\\Chapter11\\maillog.txt', 'r')
while x < 15:
    for line in f:
        if re.search('F..m', line):
            line = line.rstrip()
            print(line)
            x += 1

f.close()

