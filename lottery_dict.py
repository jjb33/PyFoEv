import random

def windraw():
    win = {}
    n = 1
    while len(win) <= 5:
        ball = random.randrange(1, 70)
        if ball not in win:
            win[ball] = ball
            n += 1
        else:
            continue
    ball = random.randrange(1, 27)
    win[ball] = ball
    return win

def picknums():
    one = input('First number? (1-69)')
    two = input('Second number? (1-69)')
    three = input('Third number? (1-69)')
    four = input('Fourth number? (1-69)')
    five = input('Fifth number? (1-69)')
    six = input('Power number? (1-26')
    picks = {one:one, two:two, three:three, four:four, five:five, six:six}
    return picks


odds = 0
x = windraw()
y = {11:11, 12:12, 13:13, 14:14, 15:15, 22:22} #picknums()
while x != y:
    odds += 1
    x = windraw()
    if odds % 10000 == 0:
        print(odds)

print('Your odds of getting these winning numbers are about 1 in', odds)