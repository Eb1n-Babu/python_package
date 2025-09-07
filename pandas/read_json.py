import pandas as pd

json_read = pd.read_json("read_json.json")
print(json_read)
print(json_read.to_string())