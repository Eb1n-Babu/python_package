import pandas as pd

df = pd.read_csv("demo_data.csv")
print(df.to_string())


df_clean = df.dropna()
print(df_clean.to_string())