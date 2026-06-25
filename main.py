import pandas as pd

# Read all CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine them
df = pd.concat([df1, df2, df3])

# Keep only pink morsels
df = df[df["product"] == "pink morsel"]

# Remove $ sign and convert price to float
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Create sales column
df["sales"] = df["price"] * df["quantity"]

# Keep required columns
output = df[["sales", "date", "region"]]

# Save output
output.to_csv("formatted_sales_data.csv", index=False)

print("Done!")