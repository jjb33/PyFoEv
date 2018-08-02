'''
This program simulates a Powerball lottery drawing. It prompts the user to pick the 6 unique numbers required for the drawing. It will then draw a complete set of winning numbers until the draw matches the user's pick.
'''


import random
import time
from datetime import timedelta

def picknums(): #prompt the user to pick numbers
    picks = {}
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
        picks[p] = p #put the number in the dictionary
    while len(picks) < 6: #for the last number
        p = input('Pick a unique number between 1 and 26:\n')
        try:
            int(p) #make sure it is a whole number
        except:
            print(emsg6)
            continue
        p = int(p)
        if p in picks or (0 < p < 27) == False: #make sure number within range
            print(emsg6)
            continue
        picks[p] = p #put the number in the dictionary
    return picks

def windraw(): #draw the winning numbers
    win = {}
    while len(win) <= 4: #draw the first 5 numbers
        ball = random.randrange(1, 70)
        if ball not in win: #can't pick number already picked
            win[ball] = ball
        else:
            continue
    ball = random.randrange(1, 27) #draw the last number
    win[ball] = ball
    return win

def play():
    odds = 1
    x = windraw()
    y = picknums()
    starttime = time.time() #for measuring time to get calculation
    while x != y:
        odds += 1
        x = windraw() #draw again if picks not a winner
        if odds % 100000 == 0: #print every 1 in every 100K odds to show working
            print(odds)

    stoptime = time.time()
    print('Your odds of getting these winning numbers are about 1 in', odds)
    print('This calculation took this much time (HH:MM:SS): ', str(timedelta(seconds = (round(stoptime, 0) - round(starttime, 0)))))

play()