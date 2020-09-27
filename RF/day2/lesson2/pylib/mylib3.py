import os,sys


def opencalc():
    os.system('calc')

def openmspaint():
    os.system('mspaint')

def printarg(*args,**kwargs):

    if len(args) == 0:
        print('** no args **')
    else:
        print('** args are **')
        print('-----------------')
        for one in args:
            print(repr(one))
        print('-----------------')

    if len(kwargs) == 0:
        print('** no kwargs **')
    else:
        print('** kwargs are **')
        print('-----------------')
        for k,v in kwargs.items():
            print(repr(k) + ':' + repr(v))
        print('-----------------')



def returnlist():
    return [1,2,3,4]

def returndict():
    return {
        'ele1' : 'male',
        'ele2' : 'female'
    }

def testloop():
    list1=[1,2,3]
    for i in range(9):
        print(i)

if __name__ == '__main__':
    printarg()