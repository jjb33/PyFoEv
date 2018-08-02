import random

def windraw():
    win = []
    n = 1
    while n <= 5:
        ball = random.randrange(1, 70)
        if ball not in win:
            win.append(ball)
            n += 1
        else:
            continue
    ball = random.randrange(1, 27)
    win.append(ball)
    return win

def picknums():
    one = input('First number? (1-69)')
    two = input('Second number? (1-69)')
    three = input('Third number? (1-69)')
    four = input('Fourth number? (1-69)')
    five = input('Fifth number? (1-69)')
    six = input('Power number? (1-26')
    picks = [one, two, three, four, five, six]
    return picks


odds = 0
w = 0
x = windraw()
y = [11, 12, 13, 14, 15, 22] #picknums()
while w != 6:
    if y[0] in x:
        w += 1
    if y[1] in x:
        w += 1
    if y[2] in x:
        w += 1
    if y[3] in x:
        w += 1
    if y[4] in x:
        w += 1
    if y[5] in x:
        w += 1
    if w < 6:
        odds += 1
        w = 0
        x = windraw()
    if odds % 10000 == 0:
        print(odds)
#return odds
print('Your odds of getting these winning numbers are about 1 in', odds)



