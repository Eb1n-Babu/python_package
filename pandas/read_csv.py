import pandas as pd

csv_read = pd.read_csv('user_profiles.csv')
print(csv_read)
print(csv_read.to_string())
print(csv_read.to_excel)