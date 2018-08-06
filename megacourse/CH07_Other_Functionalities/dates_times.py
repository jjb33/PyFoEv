r'''
covering dates and times in Python.
'''

import datetime, random

#get the start time
t0 = datetime.datetime.now()
#Prints year, mo, day, hour, min, sec, microseconds as an array

#instert some code to run
nums = []
i = 0
while i < 36000:
    nums.append(random.randrange(1, 20000))
    i += 1
print(nums)

#get the new time
t1 = datetime.datetime.now()

#print time difference to see how long the code took
t = t1 - t0
print('Time taken: ', t)
print('Total seconds: ', t.total_seconds())
#can convert to string too (to maybe name files for example. Have to convert first so doesn't have illegal chars in file name. see below)
print('Total seconds as string: ', str(t.total_seconds()))

#formatting
print(t0.strftime(r'%Y-%m-%d-%H-%M-%S-%f')) #strftime.org has a comprehensive list

#add time to
print('t0 is: ', t0)
print('and adding time is now: ', (t0 + datetime.timedelta(days = 3, seconds = 3000)))

'''
The TIME module. Handy for delaying time in script
'''
import time
import datetime

lst = []
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1) #will wait one second before continuing
    print('1')
for i in lst:
    print(i)
