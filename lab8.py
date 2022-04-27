import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# ts.plot()
# plt.show()

# dane = {'Kraj': ['Belgia','Indie','Brazylia','Polska'],
#         'Stolica': ['Bruksela','New Delhi','Brasilia','Warszawa'],
#         'Populacja': [11190846,1303171035,207847528,38675467],
#         'Kontynent': ['Europa','Azja','Ameryka Południowa','Europa']}
#
# df = pd.DataFrame(dane)
#
# grupa = df.groupby('Kontynent').agg({'Populacja': [sum]})
# print(grupa)
# # grupa.plot(kind='bar', xlabel='kontynent', ylabel='Populacja w mld',
# #            rot=0, title='Populacja dla kontynetów')
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend(loc="upper left")
# wykres.set_title('Populacja dla kontynentów')
# plt.savefig('wykres.png')
# plt.show()


# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
#
# grupa = df.groupby('Imię i nazwisko').agg(
#     {'Wartość zamówienia': ['sum']})
#
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, figsize=(8, 8), colors=['darkred', 'darkblue'] )
# plt.legend(loc='upper left')
# plt.show()

# df = pd.DataFrame(ts)
# print(df)
#
# df["Średnia krocząca"] = df.rolling(window=100).mean()
# df.plot()
# plt.legend(['Wartości', 'Średnia z n-elementów'])
# plt.show()

#Zadanie 1

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
#
# grupa = df.groupby('Rok').agg({'Liczba': ['sum']})
# grupa.plot(xlabel='Lata', ylabel='Liczba urodzeń',
#                     rot=0, title='Liczba urodzonych dzieci', figsize=(9, 9))
# plt.legend(['Liczba dzieci na przestrzeni lat'])
# plt.show()
#
# print(df)

#Zadanie 2

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# grupa = df.groupby('Plec').agg({'Liczba': ['sum']})
# grupa.plot(kind = 'bar', xlabel='Plec', ylabel='Liczba urodzeń',
#                    rot=0, title='Porównanie urodzen dzieci', figsize=(9, 9))
#
# plt.legend(['Liczba urodzen dzieci'])
# plt.show()
#
# print(df)

#Zadanie 3

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# sort = df[df['Rok'] >= 2012]
#
# grupa = sort.groupby('Plec').agg({'Liczba': ['sum']})
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, figsize=(8, 8), colors=['darkred', 'darkblue'], title='liczba urodzen dzieci na przestrzeni 5 lat' )
#
# plt.legend(['Liczba urodzen dzieci'])
# plt.show()

# print(sort)

#Zadanie 4

df = pd.read_csv('dane.csv',header=0, sep=';', decimal='.')
print(df)

grupa = df.groupby('Imię i nazwisko').size()

grupa.plot(kind='bar', xlabel='Klient', ylabel='Liczba zamowień', figsize=(8, 8), rot='0',title='Ilosc zamowien')
plt.legend(['ilosc zamowien'])
plt.show()
