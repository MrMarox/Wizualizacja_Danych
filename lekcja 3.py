import math
#lista = [1,2,3,4,5]
#print(lista[0])


# lista=[]
# for element in sekcja:
#     if warunek_na_element:
#         lista.append(akcja_na_element)
#
# lista = [akcja_na_element for element in sekwencja if warunek_na_element]

# a={x^2 :x∈<0,9>}
# b={1,3,9,27,...,3^5}
# c={x∈a i x nieparzyste}

# a = []
# for x in range(0,10): # musi byc 10 bo 10 jest pomijane
#     a.append(x**2)
# print(a)
# a1 = [x**2 for x in range(0,10)]
# print(a1)
#
# b = []
# for x in range(0,6):
#     b.append(3**x)
# print(b)
#
# b1 = [3**x for x in range(0,6)]
# print(b1)
#
# c = []
# for x in a:
#     if x % 2 != 0:
#         c.append(x)
# print(c)
#
# c1 = [x for x in a if x % 2 != 0]
# print(c1)

# lista = []
# for a in [1,2,3]:
#     for b in [4,5,6]:
#         lista.append((a,b))
# print(lista)
#
# lista2 = [(a,b) for a in [1,2,3] for b in [4,5,6]]
# print(lista2)

# slownik = {'PZU': 'Państwowy zakład ubezpieczeń',
#            'ZUS': 'Zakład ubezpieczeń społecznych',
#            'PKO': 'Państwowa kasa oszczędności'}
# slownik_odwrocony = {}
# print(slownik)
# for key, value in slownik.items():
#     slownik_odwrocony[value] = key
# print(slownik_odwrocony)
#
# slownik2 = {value: key for key, value in slownik.items()}
# print(slownik2)
#
#
#
# def nazwa_funkcji(arg.pozycyjne, domysśnie = wartość, *argument, **argument):
# instrukcje
# return

# def row_kwadratowe(a,b,c):
#     delta = b**2 - 4 * a * c
#     if delta < 0:
#         print('brak rozwiązań')
#         return -1
#     elif delta == 0:
#         print('jedno rozwiązanie')
#         x = (-b)/(2*a)
#         return x
#     else:
#         print('dwa rozwiazania')
#         x1 = ((-b) - math.sqrt(delta))/(2*a)
#         x2 = ((-b) + math.sqrt(delta))/(2*a)
#         return x1,x2
#
# print(row_kwadratowe(6, 1, 3))
# print(row_kwadratowe(1, -2, 1))
# print(row_kwadratowe(1, -4, 1))

# def czy_parzysta(a):
#     if a % 2 == 0:
#        return 'a jest parzyste'

#     else:
#         return 'a jest nie parzyste'


# print(czy_parzysta(2))

#
# def dlugosc_odcinka(x1=1, y1=2, x2=3, y2=4):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)


# #argumenty domyślne
# print(dlugosc_odcinka())
#
# #agumenty pozycyjne
# print(dlugosc_odcinka(4,5,6,9))
#
# #dwa pierwsze argumenty pozycyjne, kolejne dwa wpisane wartości
# print(dlugosc_odcinka(1,1,y2=8, x2=7))
#
# #wartość przypisana do danego argumentu
# print(dlugosc_odcinka(y2=3,x1=5,y1=6,x2=0))
#
# #dwa pierwsze domyślne, kolejne dwa nowe wartości wpisane
# print(dlugosc_odcinka(y2=1,x2=6))


# def ciag(* liczba):
#     if len(liczba) == 0:
#         return 0
#     else:
#         suma = 0
#         for i in liczba:
#             suma += i
#         return suma
#
# print(ciag())
# print(ciag(1,2,3,4,5,6,7,8))

# def co_lubie(** rzeczy):
#     for cos in rzeczy:
#         print('lubie')
#         print(cos)
#         print('co lubie')
#         print(rzeczy[cos])

# co_lubie(gry=['planszowe','komputerowe'])







