import pandas as pd
from sklearn import linear_model

df = pd.read_csv("data.csv")

volume_weight = df[['Volume','Weight']]
co2 = df['CO2']

regressor = linear_model.LinearRegression()