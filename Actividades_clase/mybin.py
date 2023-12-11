#!/usr/bin/env python3
def mybin(x):
    print('__name__ = {}'.format(__name__))
    return bin(x)[2:].rjust(8, "0")
if __name__=='__main__':
    n=input('Escriba un entero;\n')
    b=mybin(int(n))
    print('Su representación binaria es: {}'.format(b))
