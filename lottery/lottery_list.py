# import random
# import timeit

# starttime = timeit.default_timer()

# def windraw():
#     win = []
#     n = 1
#     while n <= 5:
#         ball = random.randrange(1, 70)
#         if ball not in win:
#             win.append(ball)
#             n += 1
#         else:
#             continue
#     ball = random.randrange(1, 27)
#     win.append(ball)
#     return win

# def picknums():
#     one = input('First number? (1-69)')
#     two = input('Second number? (1-69)')
#     three = input('Third number? (1-69)')
#     four = input('Fourth number? (1-69)')
#     five = input('Fifth number? (1-69)')
#     six = input('Power number? (1-26')
#     picks = [one, two, three, four, five, six]
#     return picks


# odds = 0
# w = 0
# x = windraw()
# y = [11, 12, 13, 14, 15, 22] #picknums()
# while w != 6:
#     if y[0] in x:
#         w += 1
#     if y[1] in x:
#         w += 1
#     if y[2] in x:
#         w += 1
#     if y[3] in x:
#         w += 1
#     if y[4] in x:
#         w += 1
#     if y[5] in x:
#         w += 1
#     if w < 6:
#         odds += 1
#         w = 0
#         x = windraw()
#     if odds % 10000 == 0:
#         print(odds)
# #return odds

# stoptime = timeit.default_timer()
# print('Your odds of getting these winning numbers are about 1 in', odds)
# print('This calculation took this much time: ', (stoptime - starttime))


#----------------------------------------------
'''
This program simulates a Powerball lottery drawing. It prompts the user to pick the 6 unique numbers required for the drawing. It will then draw a complete set of winning numbers until the draw matches the user's pick.
'''


import random
import time
from datetime import timedelta

def picknums(): #prompt the user to pick numbers
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
    win = []
    while (len(win)) <= 4: #draw the first 5 numbers
        ball = random.randrange(1, 70)
        if ball not in win: #can't pick number already picked
            win.append(ball)
        else:
            continue
    ball = random.randrange(1, 27) #draw the last number
    win.append(ball)
    return win

def play():
    odds = 1
    y = picknums()
    x = windraw()
    starttime = time.time() #for measuring time to get calculation
    while x != y:
        odds += 1
        x = windraw() #draw again if picks not a winner
        if odds % 100000 == 0: #print every 1 in every 100K odds to show working
            print('{:,}'.format(odds))

    stoptime = time.time()
    print('Your odds of getting these winning numbers are about 1 in', ('{:,}'.format(odds)))
    print('This calculation took this much time (HH:MM:SS): ', str(timedelta(seconds = (round(stoptime, 0) - round(starttime, 0)))))
    print('Draw speed was', ('{:,}'.format(odds/((round(stoptime, 0) - round(starttime, 0))/60))), 'draws per minute')
play()