fhand = open('R:\\OneDrive\\PythonProjects\\PyFoEv_Repo\\PyFoEv\\PyFoEv\\Chapter07\\logdoc.txt')
print(fhand)
count = 0
for line in fhand: #'line' can be replaced with anything you want and will still work.
    count = count +1
print('Count of For loop: ', count)

#Read will store the whole file in RAM. the variable mem stores the whole doc as one long string
fhand = open('R:\\OneDrive\\PythonProjects\\PyFoEv_Repo\\PyFoEv\\PyFoEv\\Chapter07\\logdoc.txt')
mem = fhand.read()
print('Count of len(mem): ', len(mem))
print('First 35 characters: ', mem[:35])
print('Count of Read: ', len(fhand.read())) #is 0 b/c each call to read() exhausts the resource (clears the fhand?). Store in a variable like mem above

count = 0
for line in fhand:
    count = count + 1
print(count) #will be 0 becuase you didn't store info in variable. Now you have to open file again like below.

# count = 0
# fhand = open('R:\\OneDrive\\PythonProjects\\PyFoEv_Repo\\PyFoEv\\PyFoEv\\Chapter07\\logdoc.txt')
# mem = fhand.read()
# for line in mem:
#     count = count + 1
# print('Count of read() stored in variable: ', count) #Took 8 seconds with read() vs the miliseconds with the For loop
# #print(line[43]) #How to print a specific line from a read file??

count_From = 0
fhand = open('R:\\OneDrive\\PythonProjects\\PyFoEv_Repo\\PyFoEv\\PyFoEv\\Chapter07\\logdoc.txt')
count = 0
for line in fhand:
    if line.startswith('From'):
        count_From = count_From + 1
        print(line)
        print(count_From)
    if count_From >= 25: #Tried to use a While loop for this, but couldn't get to work
        break

#Add an rstrip() method to get rid f the extra spaces in the output:
count_From = 0
fhand = open('R:\\OneDrive\\PythonProjects\\PyFoEv_Repo\\PyFoEv\\PyFoEv\\Chapter07\\logdoc.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        count_From = count_From + 1
        print(line)
        print(count_From)
    if count_From >= 25:
        break

#Use the find() method to search for from anywhere in the line:
count_From = 0
fhand = open('R:\\OneDrive\\PythonProjects\\PyFoEv_Repo\\PyFoEv\\PyFoEv\\Chapter07\\logdoc.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('From:') == 0: #find returns the index (location) of the string. IS NOT true/false. is -1 if nothing found
        count_From = count_From + 1
print(count_From)

#to get all lines that contains a string using .find, we have to continue over lines where "find(string) = -1"
count_From = 0
fhand = open('R:\\OneDrive\\PythonProjects\\PyFoEv_Repo\\PyFoEv\\PyFoEv\\Chapter07\\logdoc.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('from') == -1: #find returns the index (location) of the string. IS NOT true/false. is -1 if nothing found
        continue
    else:
        count_From = count_From + 1
print('line.find() = -1: ', count_From)

#Same program as above, but let's user define filename (within single directory). Also can define search string and user if they want to print matching lines.
count = 0
inpfilename = input('What is the name of the file?\n')
searchstring = input('And what are you looking for?\n')
printlines = input('And do you want to print matching lines?\n')
savefile = input('Do you want to save the output to a file?\n')
if savefile == 'yes':
    outfilename = input("Save file as:")
    ffoot = open('R:\\OneDrive\\PythonProjects\\InputOutput\\Output\\' + outfilename, 'w')
else:
    outfilename = None
fhand = open('R:\\OneDrive\\PythonProjects\\InputOutput\\Input\\' + inpfilename)
for line in fhand:
    line = line.rstrip()
    line = line.strip()
    if line.find(searchstring) == -1: #find returns the index (location) of the string. IS NOT true/false. is -1 if nothing found
        continue
    if len(line) > 500:
        continue
    else:
        count = count + 1
        if printlines == 'yes':
            print(line)
        if savefile == 'yes':
            ffoot.write(line.upper() + '\n') #added print to uppercase as part of exercise
if outfilename != None:
    ffoot.close()
print('There were', count, 'lines containing', '"' + searchstring + '"')


