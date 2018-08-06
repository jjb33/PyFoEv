import json
from difflib import SequenceMatcher, get_close_matches #for fuzzy comparison of misspelled words

#load the json data into Python. If data is huge, you should use database
data = json.load(open('.\\megacourse\\ch08_BuildingDictionary\\data.json', 'r'))

inp = ''

while inp != '--exit': #-- so you can search for word 'exit' successfully
    inp = input('What word do you want to search for? (type \'--exit\' to quit)\n')
    if inp == '--exit':
        break
    inp = inp.lower()
    if inp not in data:
        c = get_close_matches(inp, data.keys(), n = 3, cutoff = .8)
        if len(c) == 0:
           print('Sorry, I don\'t have any close matches.')
           continue
        else:
            print('Sorry, I don\'t know that one. Did you mean:')
            for closematch in c: #get top 3 suggestions
                print(closematch + '? ')
            continue
    else:
        definitions = data[inp]
        for definition in definitions:
            print(str(definitions.index(definition) + 1) + '. ', definition)


#Get some close matches if inp doesn't exist
#get_close_matches(inp, data.keys(), n = 5) #top 5 matches

#SequenceMatcher(None, 'rainn', 'rain').ratio()
