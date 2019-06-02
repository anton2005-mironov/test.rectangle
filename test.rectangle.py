# -*- coding: UTF-8 -*-

import sys

if len(sys.argv) < 3:
    print("нужно 2 переменных")
    exit()


param = sys.argv[1]
m = param.split('=')
if len(m) <2:
    print("в массиве нужно 2 части")
    exit()

if not m[1].isdigit():
    print("всё должно быть числом")
    exit()


a = int(m[1])

param = sys.argv[2]
m = param.split('=')

if len(m) <2:
    print("в массиве нужно 2 части")
    exit()

if not m[1].isdigit():
    print("всё должно быть числом")
    exit()

b = int(m[1])

P=(a+b)*2
S=a*b
print("первая сторона-"+ str(a)+ " см")
print("вторая сторона-"+ str(b)+ " см")
print("периметр-"+ str(P))
print("площадь-"+ str(S))
print('Ответ: P='+ str(P)+ ' ,S='+ str(S))

