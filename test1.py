if(True == False ):
    print('there is something wrong here');
else:
    print('this is working fine!');
def hi(name):
    print('hello there, ' + name);
    print('any problem?');

hi('Maria');

girls = ['Maria', 'Pilar', 'Sara', 'Ana'];

for name in girls:
    hi(name)
    print('Next girl:')
