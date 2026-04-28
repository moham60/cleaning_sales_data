import pandas as pd
import numpy as np

# ----------------------------
# Load dirty dataset
# ----------------------------
df = pd.read_csv("dirty_sales_orders.csv")

# ----------------------------
# 1. Remove duplicates
# ----------------------------
df = df.drop_duplicates()

# ----------------------------
# 2. Fix order_id duplicates logic (keep first occurrence)
# ----------------------------
df = df.drop_duplicates(subset="order_id", keep="first")

# ----------------------------
# 3. Handle missing customer names
# ----------------------------
df["customer"] = df["customer"].fillna("Unknown")

# ----------------------------
# 4. Standardize product names
# ----------------------------
df["product"] = df["product"].str.lower().str.strip()

df["product"] = df["product"].replace({
    "laptop": "Laptop",
    "phone": "Phone",
    "tablet": "Tablet",
    "headphones": "Headphones",
    "monitor": "Monitor"
})

# ----------------------------
# 5. Standardize city names
# ----------------------------
df["city"] = df["city"].str.lower().str.strip()

df["city"] = df["city"].replace({
    "cairo": "Cairo",
    "alex": "Alex",
    "giza": "Giza"
})

# ----------------------------
# 6. Handle missing prices
# ----------------------------
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# fill missing prices with median (best practice)
df["price"] = df["price"].fillna(df["price"].median())

# ----------------------------
# 7. Fix invalid dates
# ----------------------------
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# fill invalid dates with mode (most common date)
df["date"] = df["date"].fillna(df["date"].mode()[0])

# ----------------------------
# 8. Final sorting
# ----------------------------
df = df.sort_values(by="date")

# ----------------------------
# 9. Reset index
# ----------------------------
df = df.reset_index(drop=True)

# ----------------------------
# Save cleaned dataset
# ----------------------------
df.to_csv("clean_sales_orders.csv", index=False)

print("Cleaning completed successfully!")