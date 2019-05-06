import pandas as pd

file = pd.read_excel(r"C:\Thameem\Book1.xlsx")

list2 = file["Filenames "].str.split(".")
for x in list2:
    print(x[0])
