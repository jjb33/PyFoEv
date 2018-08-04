def lenth_of_string(a_string):
    return len(a_string)

s = input('Gimme a string:\n')

try:
    type(float(s)) is float
except: #don't always have to be an error msg :-)
    print('The length of the string is:', lenth_of_string(s))
    exit()
print('Ummm, that\'s not a string. Bye')
exit()
