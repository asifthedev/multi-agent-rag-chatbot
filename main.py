import pandas as pd

df = pd.read_excel("./data/raw/faqs.xlsx")

pd.save_csv("faqs.csv")

print(df.head(5))