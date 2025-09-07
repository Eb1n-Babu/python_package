import pandas as pd

a = [1,2,3]

adf = pd.DataFrame(a)
print(adf)
print(adf[0])

b = list(range(20))
print(b)

ddf = pd.DataFrame(b)
print(ddf)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df_data = pd.DataFrame(data)
print(df_data)

