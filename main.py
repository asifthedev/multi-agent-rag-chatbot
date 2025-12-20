import pandas as pd

df = pd.read_excel("./data/raw/faqs.xlsx")

df.drop(columns=["Actual Answer", "Category"], inplace=True)

print(df.columns)

df.to_csv("./data")