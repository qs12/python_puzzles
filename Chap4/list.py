spam = ['apples', 'bananas','tofu','cats','trytre', 'tfgfdfcdxd']


def listo(lister):
    for i in lister[0:-1]:
        print i+',',
    print "and " + lister[-1] + '.'
    
           
listo(spam)