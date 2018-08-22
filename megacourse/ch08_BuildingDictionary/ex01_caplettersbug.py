'''
There's currently a bugin the program. When the user inputs a proper noun (e.g. Delhi, Paris, etc.) the program will convert it to lowercase and then tries to find the lowercase version (e.g. delhi)in the dataset and it cannot find it since the dataset has Delhi, but not delhi.

Please add another conditional block to the program so that the program returns the definition of names that start with acapital letter. You can find thecode we have so farattached here in this lecture for your convenience.

Also fixed the next problem where dictionary was not returning acronyms.
'''

import json
from difflib import SequenceMatcher, get_close_matches #for fuzzy comparison of misspelled words

#load the json data into Python. If data is huge, you should use database
#VSCode and Idle have different current working directories
try:
    data = json.load(open('.\\megacourse\\ch08_BuildingDictionary\\data.json', 'r'))
except:
    data = json.load(open('data.json', 'r'))

while inp != '--exit': #-- so you can search for word 'exit' successfully
    inp = input('What word do you want to search for? (type \'--exit\' to quit)\n')
    possibilities = []
    if inp == '--exit':
        break
    if len(inp) < 1:
        print('I need a word.')
        continue
#    if (inp.capitalize() in data) and (inp.lower() in data): #frend would not return French
    if inp.capitalize() in data:
        possibilities.append(inp.capitalize())
    if inp.lower() in data:
        possibilities.append(inp.lower())
    if inp.upper() in data:
        possibilities.append(inp.upper())
    else:
        if len(possibilities) < 1:
            possibilities.append(inp.lower())
    for p in possibilities:
        if p not in data:
            c = get_close_matches(inp, data.keys(), n = 3, cutoff = .8)
            if len(c) == 0:
                print('Sorry, I don\'t have any close matches.')
                continue
            else:
                print('\n' + 'Sorry, I don\'t know that one. Did you mean:')
                for closematch in c: #get top 3 suggestions
                    print(closematch + '? ')
                continue
        else:
            print('\n' + p + ':')
            definitions = data[p]
            for definition in definitions:
                print(str(definitions.index(definition) + 1) + '. ', definition)
