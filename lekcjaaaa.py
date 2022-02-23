import sys
import math
print(sys.version)


# a = 'inzynieria\nsystemow\ninformatycznych'
# print(a)
# print(type(a))
#
# b = 5
# print(b)
# print(type(b))
#
# c = 5.4
# print(c)
# print(type(c))
#
# d = 2+3j
# print(d)
# print(type(d))
#
# #Ctrl + / komentuje zaznaczone wiersze
#
# # del a
# # print(a)
#
# f = 'isi'
# g = ' grupa 3'
# print(f+g)
#
# h = 7
# i = 2
# print(h//i) #dzielenie calkowite
# print(2/4**i) #potegowanie zwraca typ int, kolejnosc wykonywania dzialan przy ulamkach podaje zly wynik
#
# print(math.pow(2/4,i)) #potegowanie przy uzyciu math
#
# h += 1
# print(h)


a = 5
b = 3
c = a - b
print("wynik dzialania %(z1)d - %(z2)d = %(z3)d" %{'z1':a,'z2':b,'z3':c})
print("wynik dzialania {0:d} - {1:d} = {2:d}".format(a,b,c))

