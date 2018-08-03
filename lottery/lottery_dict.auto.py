'''
This program simulates a Powerball lottery drawing. It prompts the user to pick the 6 unique numbers required for the drawing. It will then draw a complete set of winning numbers until the draw matches the user's pick.
'''


import random
import time
from datetime import timedelta

def picknums(): #prompt the user to pick numbers
    picks = {33:33, 7:7, 21:21, 42:42, 27:27, 13:13}
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
        # if odds % 100000 == 0: #print every 1 in every 100K odds to show working
        #     print('{:,}'.format(odds))
    stoptime = time.time()
    print('Your odds of getting these winning numbers are about 1 in', ('{:,}'.format(odds)))
    print('This calculation took this much time (HH:MM:SS): ', str(timedelta(seconds = (round(stoptime, 0) - round(starttime, 0)))))
    print('Draw speed was', ('{:,}'.format(odds/((round(stoptime, 0) - round(starttime, 0))/60))), 'draws per minute')
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()
play()

