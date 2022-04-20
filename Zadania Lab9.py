
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

