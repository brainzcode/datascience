import pandas as pd

sales = pd.read_csv("datasets/sales_1_1.csv")


# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])[
    "weekly_sales"].sum()
print(sales_by_type_is_holiday)
