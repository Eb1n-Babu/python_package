import pandas as pd

mydata = {
    "cars":['bmw','volvo','ford'],
    "passing's":[3,7,2]
}

mydf = pd.DataFrame(mydata)
print(mydf)