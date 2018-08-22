import random

fry1001 = ['the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'I', 'at', 'be', 'this', 'have', 'from']
fry1002 = ['or', 'one', 'had', 'by', 'words', 'but', 'not', 'what', 'all', 'were', 'we', 'when', 'your', 'can', 'said', 'there', 'use', 'an', 'each', 'which', 'she', 'do', 'how', 'their', 'if']
fry1003 = ['will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look', 'two', 'more', 'write', 'go', 'see']
fry1004 = ['number', 'no', 'way', 'could', 'people', 'my', 'than', 'first', 'water', 'been', 'called', 'who', 'oil', 'sit', 'now', 'find', 'long', 'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part']
fry100all = fry1001 + fry1002 + fry1003 + fry1004

indrange = range(100)
randindex = random.sample(indrange, 100)

#Create 20 lists of 5
n = 1
workinglist = []
for i in randindex:
    if len(workinglist) % 5 == 0:
        listname = str('fry5' + str(n))
        listname = workinglist
        n += 1
        worklist = []
    else:
        workingist.append(fryall[i])

print(fry54)
    
    
    

