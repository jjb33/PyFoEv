import os
print('listdir() of CWD is:\n', os.listdir())

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('CWD is: ', os.getcwd())

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('dir(os)) lists the functions of os module:', '\n', dir(os))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('Get path of module using os using os.__file__:\n', os.__file__)
print('You can get all the default libraries from there and use them by importing them')
print('There are 3rd party libraries out there dealing with astronomy, biology, web scraping, etc. These do not all come installed by default because it would make the installation of python very heavy!')
print('If you want help on a specific library, type help(library name)')