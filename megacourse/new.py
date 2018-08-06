from multiprocessing import Pool, Process
import random, os

def createlist():
    numlist = []
    while len(numlist) < 60000:
        w = random.randrange(1, 600000)
        numlist.append(w)
        if len(numlist) % 100000 == 0:
            print(len(numlist))
    return numlist
        # if w < 200:
        #     print('Yay! getting close: ', w)
        # if w > 200:
        #     print('Far!!')

nl = createlist()
print(nl)


# def play(y):
#     dic = {'No':0, 'Yes':0}
#     x = 6
#     while x != y:
#         print(os.getpid())
#         print(os.getppid())
#         dic['No'] += 1
#         if dic['No'] % 1000 == 0:
#             print(y, dic)
#     dic['Yes'] += 1
#     print(dic)
#     return dic


# if __name__ == '__main__':
#     for n in nl:
#         p = Process(target=play, args=(n))
#         p.start()
#         p.join()

# p = play()
# print(p)
