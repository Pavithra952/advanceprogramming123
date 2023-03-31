import pandas as pd
df = pd.read_csv("C://mydatasets//tips.csv")
json = df.to_json(path_or_buf="C://mydatasets//df.json")