import pandas as pd;

csvfileread = pd.read_csv("manual 2/sales_data.csv");
total_revenue = csvfileread.groupby("Product")["Revenue"].sum();

print(total_revenue);
