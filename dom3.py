import sys
import math
import random

print('Zad 1\n')

# A = {1-x: x∈<1,10> }

a = []
for x in range(1,11):
    a.append(1-x)
print(a)

# B = {1,4,16,...,4^7}

b = []
for x in range(0,8):
    b.append(4**x)
print(b)

# C = {x: x∈B i x jest liczba podzielna przez 2}

c = []
for x in b:
    if x % 2 == 0:
        c.append(x)
print(c)

print('\nZad 2\n')

d = []
for x in range(0,11):
    d.append(random.randint(0, 100))
print(d)
e = []
for x in d:
    if x % 2 == 0:
        e.append(x)
print(e)

print('\n Zad 3 \n')

slownik = {'Ciastka': 'kg',
           'Banany': 'kg',
           'Bułki': 'szt',
           'Batony': 'szt'}

lista = []
print(slownik)
for key, value in slownik.items():
    if slownik[key] == 'szt':
        lista.append(key)

print(lista)

print('\n Zad 4 \n')

def czyProstokatny(a, b, c):
    if pow(a, 2)+pow(b, 2)==pow(c, 2):
        print("Jest prostokątny")
    else:
        print("Nie jest prostokątny")
czyProstokatny(6,8,10)

print('\n Zad 5 \n')

def poleTrapezu(a=3, b=5, h=7):
    pole=((a+b)*h)/2
    return pole
print(poleTrapezu())

print('\n Zad 6 \n')

def ciag(a1=1,b=6,ile=8):
    for x in range(ile):
        a1=a1*b
    return a1
print(ciag())


print('\n Zad 7 \n')

def ciag2(*liczba):
    if len(liczba)==0:
        return 0
    else:
        iloczyn = 1
        for x in liczba:
            iloczyn=iloczyn*x
    return iloczyn
print(ciag2(1,2,3,4,5))

print('\n Zad 8 \n')

def zakupy(**a):
    ile=len(a.items())
    wartosc = 0
    for key, value in a.items():
        wartosc+=value
    return ile,wartosc

print(zakupy(pomidor=8,salata=9))
