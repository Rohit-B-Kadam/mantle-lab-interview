import pandas as pd

data = pd.read_csv("Pokemon.csv", encoding = "ISO-8859-1")

print(data.head(5))