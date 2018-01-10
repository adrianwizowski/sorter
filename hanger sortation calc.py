import codecs
import tkinter as Tk
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog as sdg

root = Tk.Tk()
root.withdraw()
with codecs.open(askopenfilename(filetypes=[("Text files", "*.txt")])) as f:
    lines = [line.rstrip('\n') for line in f]

print(lines)

hangers_dict = {}

for i in lines:
    if i[0:2] not in hangers_dict.keys():
        hangers_dict[i[0:2]] = {i[2:]: 1}
    elif i[2:] not in hangers_dict[i[0:2]].keys():
        hangers_dict[i[0:2]][i[2:]] = 1
    else:
        hangers_dict[i[0:2]][i[2:]] += 1

print(hangers_dict)

for key in hangers_dict.keys():
    name = sdg.askstring(key, 'Podaj imie')
    surname = sdg.askstring(key, 'Podaj nazwisko')
    hangers_dict[key].update({'Imie': name, 'Nazwisko': surname})

print(hangers_dict)



#testing
from collections import Counter
x = Counter(lines)
for i in x.keys():
    if x[i] != hangers_dict[i[0:2]][i[2:]]:
        print('Error')


#excel time!
import pandas as pd
import sqlite3
import time
now = time.strftime('%Y-%m-%d')

df = pd.DataFrame.from_dict(hangers_dict, orient='Index')
df = df[['Nazwisko', 'Imie', 'ADULT', 'CLIP', 'JACKET', 'KIDS', 'KNIT', 'SCRAP']]
df.to_csv('final.csv')
conn = sqlite3.connect("hangers_sortation_database")
df.to_sql(now, conn, if_exists='append', index=False)

from pyexcel.cookbook import merge_all_to_a_book
import glob

merge_all_to_a_book(glob.glob("final.csv"), "output.xlsx")
