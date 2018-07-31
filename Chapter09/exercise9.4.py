'''
Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary
has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
'''
#from exercise9.3 import d (didn't work)

d = {'stephen.marquard@uct.ac.za': 58, 'louis@media.berkeley.edu': 38, 'zqian@umich.edu': 90, 'rjlowe@iupui.edu': 32, 'cwen@iupui.edu': 253, 'gsilver@umich.edu': 36, 'wagnermr@iupui.edu': 36, 'antranig@caret.cam.ac.uk': 2, 'gopal.ramasammycook@gmail.com': 12, 'david.horwitz@uct.ac.za': 86, 'ray@media.berkeley.edu': 16, 'mmmay@indiana.edu': 46, 'stuart.freeman@et.gatech.edu': 20, 'tnguyen@iupui.edu': 12, 'chmaurer@iupui.edu': 16, 'aaronz@vt.edu': 2, 'ian@caret.cam.ac.uk': 68, 'csev@umich.edu': 32, 'jimeng@umich.edu': 36, 'josrodri@iupui.edu': 22, 'knoop@umich.edu': 10, 'bkirschn@umich.edu': 20, 'dlhaines@umich.edu': 36, 'hu2@iupui.edu': 4, 'sgithens@caret.cam.ac.uk': 40, 'arwhyte@umich.edu': 26, 'gbhatnag@umich.edu': 2, 'gjthomas@iupui.edu': 42, 'a.fish@lancaster.ac.uk': 4, 'ajpoland@iupui.edu': 4, 'lance@indiana.edu': 12, 'ssmail@indiana.edu': 2, 'jlrenfro@ucdavis.edu': 2, 'nuno@ufp.pt': 48, 'zach.thomas@txstate.edu': 16, 'ktsao@stanford.edu': 2, 'ostermmg@whitman.edu': 2}
dd = {}
with open('R:\\OneDrive\\PythonProjects\\InputOutput\\Input\\maillog.txt') as f:
    for line in f:
        if line.startswith('From'):
            line = line.rstrip()
            line = line.split()
            e = line[1]
            pos1 = e.find('@')
            pos2 = e.find(' ')
            e = e[pos1:pos2]
            if e not in dd:
                dd[e] = 1
            else:
                dd[e] += 1
# for key in d:
#     fout.write(key, d[key])
# fout.close()

for key in dd:
    print(key, dd[key])
