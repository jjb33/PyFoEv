'''
Tyring to get multiprocessing to work
'''

import random
import time
from datetime import timedelta
import multiprocessing
from multiprocessing import Pool, Process, Queue
import threading
import os
    
def picknums(): #prompt the user to pick numbers
    global picks
    picks = []
    emsg1_5 = 'ERROR! Pick a UNIQUE WHOLE NUMBER between 1 and 69:\n'
    emsg6 = 'ERROR! Pick a UNIQUE WHOLE NUMBER between 1 and 26:\n'
    while len(picks) < 5: #for the first 5 numbers
        p = input('Pick a unique number between 1 and 69:\n')
        try:
            int(p) #make sure it is a whole number
        except:
            print(emsg1_5)
            continue
        p = int(p)
        if p in picks or (0 < p < 70) == False: #make sure hasn't already been picked and number within range
            print(emsg1_5)
            continue
        picks.append(p) #put the number in the list
        picks.sort()
    while len(picks) < 6: #for the last number
        p = input('Pick a unique number between 1 and 26:\n')
        try:
            int(p) #make sure it is a whole number
        except:
            print(emsg6)
            continue
        p = int(p)
        if (0 < p < 27) == False: #make sure number within range
            print(emsg6)
            continue
        picks.append(p) #put the number in the list
    return picks

def windraw(): #draw the winning numbers
    win = random.sample(range(1,70), 5)
    win.sort()
    pball = random.randrange(1, 27) #draw the last number
    win.append(pball)
    return win

def play(num):
    num = -1 + num
    odds = 1
#    y = picknums() #multiproc stops b/c runs into user input for each process
    y = [22,66,41,24,13,6]
    x = windraw()
    starttime = time.time() #for measuring time to get calculation
    while x != y:
        print(os.getpid())
        print(os.getppid())
        odds += 1
        if num >= odds:
            print('Done picking. No winner.')
            break
        else:
            x = windraw() #draw again if picks not a winner
            if odds % 1000000 == 0: #print every 1 in every 100K odds to show working
                print('{:,}'.format(odds))
        

    stoptime = time.time()
    print('Your odds of getting these winning numbers were 1 in', ('{:,}'.format(odds)))
    print('This calculation took this much time (HH:MM:SS): ', str(timedelta(seconds = (round(stoptime, 0) - round(starttime, 0)))))
    print('Draw speed was', ('{:,}'.format(odds/((round(stoptime, 0) - round(starttime, 0))/60))), 'draws per minute')

for l in range(6 ):
    play(l)

if __name__ == '__main__':
    for l in range(6):
        q = Process(target=play, args=(l))
        q.start()
        q.join()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    # q = Pool(6)
    # q.play()

# def get_id():   
#     pp = os.getppid()   # parent process
#     p = os.getpid()     # current process
#     print("parent process:", pp)
#     print("current process:", p)

# if __name__ == '__main__':
#     p = Process(target=get_id)
#     p.start()
#     p.join()

