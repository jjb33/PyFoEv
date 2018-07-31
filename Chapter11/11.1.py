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

