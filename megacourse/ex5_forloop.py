'''
Create a for loop blockthat iterates through the following list and prints out each item of the list in each iteration.
mylist = [1, 2, 3, 4, 5]
'''
mylist = [1, 2, 3, 4, 5]

for item in mylist:
    print(item)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')    
for item in mylist:
    if item > 2:
        print(item)