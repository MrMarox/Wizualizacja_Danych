# import math
# a = 0x1f
# print('{0:x}'.format(a))
#
# b = math.pow(math.log(5 + math.pow(math.sin(8), 2)), 1/6)
# print(b)


# x = int(input("Podaj x: "))
# y = int(input("Podaj y: "))
# if x == y:
#     print("x jest rowny y")
# elif x > y:
#     print("x jest wiekszy od y")
# elif x < y:
#     print("x jest mniejszy od y")t
# else:
#     print("x nie jest rowny y")


# a = input("wpisz licze: ")
# print(a)
# print(type(a))
# a = int(a)
# print(type(a))


# a = int(input("Podaj x1: "))
# b = int(input("Podaj x2: "))
# c = int(input("Podaj x3: "))
# d = int(input("Podaj x4: "))
#
# if (a > b) & (c > d):
#     print('liczba x1 jest wieksza od liczby x2 i liczba x3 jest wieksza od liczby x4')
# else:
#     print('liczba x1 jest mniejsza od liczby x2 i liczba x3 jest mniejsza od liczby x4')
#
#
#
# a = int(input("Podaj ilosc: "))
#
# for x in range(1, a+1, 1):
#     print(x)
#
#
# lista = ['a', 5 , 6 , 7.6]
# for a in lista:
#     print(a)
# else:
#     print('wyswietlone zostaly wszystkie elementy z listy')

# a = 0
# while a <= 100:
#     print(a)
#     a += 1

# lista = [4,6,9,3,2,4]
# liczba = input('podaj liczbe: ')
# licznik = 0
# while licznik < len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print('liczba ' + str(liczba) + " - " + str(lista[licznik]) + '= 0\n')
#         break
#     else:
#         licznik += 1
# else:
#     print("zadna z wartosni nie dala odpowiednie wyniku")
#
#

# lista1 = [5, 4, 5, 6, 7, 2]
# lista2 = [6, 5, 3, 1, 2, 5]
#
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)
#
#
# try:
#     instrukcje ktore moga zawierac blad
# except nazwa bledu1:
#     instrukcje po wykryciu bledu1
# except nazwa bledu2:
#     instrukcje po wykryciu bledu2
# .
# .
# else:
#     wyniki gdy nie ma bledu
#
#
# a = input("wczytaj pierwsza liczbe: ")
# b = input("wczytaj druga liczbe: ")
# try:
#     a=int(a)
#     b=int(b)
#     wynik = a/b
#     print(wynik)
# except ZeroDivisionError:
#     print("nie mozna dzielic przez 0")
# except ValueError:
#     print("nie wczytano liczby calkowitej")
#
#
# lista = ['a',5.3,[1,2,3]]
# slownik = {klucz:wartosc}   #1 element slownika
# a - lista[nr_indeksu]
# print(slownik[klucz])

lista = ['a',5.3,[1,2,3]]
slownik = {'klucz':'a',"klucz2":'5'}   #1 element slownika
a = lista[2]
print(slownik['klucz2'])

#https://technikinformatyk.pl/kursy/kurs/python/lekcja/python-slowniki/
