import pandas as pd
l1 = [1, 2, 7, 8, 10]
l2 = [2, 3, 5, 11, 12]
data = l1 + l2
data.sort()
series = pd.Series(data)
med = series.median()
print(med)