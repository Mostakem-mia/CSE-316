import pandas as pd;

df = pd.DataFrame({
    "A": [10, 20, None, 40],
    "B": [50, None, 15, 10]});

df.fillna(df.mean(), inplace=True);
print(df);
