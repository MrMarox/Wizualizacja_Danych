# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('1. Załaduj dane z pliku nieruchomosci2.csv,')
df=pd.read_csv('https://gist.githubusercontent.com/msobiecki/c2bd3bc0ef2deaf95abbb7956a789121/raw/6edb35713ecb6c01d3277048393da06e9a768446/nieruchomosci2.csv',header=None,sep=';')
print(df)


print('2. Uporządkuj dane tak, aby dane liczbowe były zgodne z koncepcją “czystych danych” (w kolumnach)')
df.loc[3,:] = df.loc[3,:].str.replace(" ", "").astype(int)

# df.index =['rodzaj rynku', 'metraż', 'rok powstania', 'ilość sztuk']

df = df.transpose()
df.columns =['rodzaj rynku', 'metraż', 'rok powstania', 'ilość sztuk']
print(df)

# df.loc[8] = ['rynek pierwotny', 'od 80,1 m2', '2018', 1000]


print('3. Stwórz wykres kołowy prezentujący dane zawarte w pliku (mogą być dwa wykresy kołowe). Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.')

grupaA=df.where(df['rodzaj rynku']=='rynek pierwotny')
grupaB=df.where(df['rodzaj rynku']=='rynek wtórny')
print(grupaA)
print(grupaB)

grupaA=grupaA.groupby('metraż').agg({'ilość sztuk': 'sum'})
grupaB=grupaB.groupby('metraż').agg({'ilość sztuk': 'sum'})
print(grupaA)
print(grupaB)


fig, axes = plt.subplots(1, 2)
plt.suptitle('ilości sprzedanych mieszkań z poszczególnych przedziałów metrażowych na poszczególnym rynku')

axes[0].pie(grupaA['ilość sztuk'], autopct='%1.1f%%', labels=grupaA.index)
axes[0].set_title('rynek pierwotny')
axes[0].legend(title='legenda', loc="upper left")

axes[1].pie(grupaB['ilość sztuk'], autopct='%1.1f%%', labels=grupaB.index)
axes[1].set_title('rynek wtórny')
axes[1].legend(title='legenda', loc="upper left")

plt.show()
