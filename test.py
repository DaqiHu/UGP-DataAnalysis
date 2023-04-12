import pandas as pd

file = pd.read_csv("data.csv")

file.to_excel("output.xlsx")