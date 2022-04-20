import random
import math
a = [x * 2 for x in range(0, 31)]

print(a)

d = []
for x in range(0,11):
    d.append(random.randint(0, 100))
print(d)
e = []
for x in d:
    if x % 2 == 0:
        d.remove(x)
print(d)



def iloczyn(a=1, b=2, ile=3):
    licznik = 0
    while licznik != ile:
        a *= b
        licznik += 1
    return a
print(iloczyn())


# a = [1-x for x in range(1, 11)]
# b = [4**x for x in range(0, 8)]
# c = [x for x in b if x % 2 == 0]


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

import math
a=math.e
a=pow(a,10)
print(a)
b=math.pow(math.log(5+math.pow(math.sin(8),2)),1/6)
print(b)
c=math.floor(3.55)
print(c)
d=math.ceil(4.8)
print(d)

imie  = "Marceli"
nazwisko= "Sobiecki"
a = imie.upper()
b = nazwisko.lower()
print(a,b)

# plik = open('zad1.txt', 'w')
# for b in a:
#     plik.write(str(b))
#     plik.write('\n')
# plik.close()
# print(a)

a = input('podaj liczbę: ')
try:
    a = int(a)
    pierwiastek = math.sqrt(a)
    print(pierwiastek)
except ValueError:
    if type(a) != int:
        print('nie wczytano liczby')
    elif a < 0:
        print('liczba a nie może być mniejsza od 0')
        
        a = 1
b = 0
try:
   result = a / b
   print(result)
except:
   print("Error!")






LAB 9

import sys
import numpy as np
import math
#Zadanie 1
# macierz = np.array([1,6,5])
# print(macierz)
# macierz2 = np.array([6,4,3])
# print(macierz2)
#
# print(macierz*macierz2)

#Zadanie 2

# macierz = np.array([[1,5,4],[4,6,4],[6,4,2]])
# print(macierz)
# print("----------------")
# macierz2 = np.array([[1,2,5,4],[4,6,4,3],[6,4,7,3],[7,4,2,1]])
# print(macierz2)
# print("----------------")
#
# def minw(macierz):
#     for i in range(len(macierz)):
#         n = 60
#         for x in macierz[i]:
#             if n > x:
#                 n = x
#         print("Rząd " ,i+1,": ",n)
#
# minw(macierz)
# print("----------------")
# minw(macierz2)
#
# def mink(macierz):
#     for w in range(len(macierz)):
#         n = 60
#         for k in range(len(macierz)):
#              if macierz[k, w] < n:
#                  n = macierz[k, w]
#         print("Kolumna ", w + 1, ": ", n)
#
# print("----------------")
# mink(macierz)
# print("----------------")
# mink(macierz2)

#Zadanie 3

# macierz = np.array([1,6,5])
# print(macierz)
# macierz2 = np.array([6,4,3])
# print(macierz2)
#
# wynik = macierz.dot(macierz2)
# print(wynik)

#Zadanie 4

# macierz = np.array([6,8,9])
# macierz2 = np.array([7.6,4.2,7.5],dtype=float)
#
# c = macierz * macierz2
# print(c)

# #Zadanie 5

# m = np.array([[2,4,5],[5,2,3]])
# a = []
# for x in range(len(m)):
#     for n in m[x]:
#         a.append(math.sin(n))
# print(a)
#
# # #Zadanie 6
#
# m = np.array([[9,4,8],[5,3,6]])
# b = []
# for x in range(len(m)):
#     for n in m[x]:
#         b.append(math.cos(n))
# print(b)

# # Zadanie 7
#
# def dod(a, b):
#     c = []
#     for x in range(len(a)):
#         c.append(a[x]+b[x])
#     print(c)
#
# dod(a,b)

#Zadanie 8



a = np.arange(9).reshape(3,3)
for x in a:
    print(x)


