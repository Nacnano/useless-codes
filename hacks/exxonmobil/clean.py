import pandas as pd
import numpy as np
import os

# Load CSV/XLSX files (adjust paths if running locally)
inventory_df = pd.read_csv("Inventory.csv", parse_dates=["BALANCE_AS_OF_DATE"])
inbound_df = pd.read_csv("Inbound.csv", parse_dates=["INBOUND_DATE"])
outbound_df = pd.read_csv("Outbound.csv", parse_dates=["OUTBOUND_DATE"])
material_df = pd.read_csv("MaterialMaster.csv")
operation_cost_df = pd.read_csv("OperationCost.csv")
forecast_df = pd.read_excel("Forecast.xlsx")  # Sheet parsing can be added if needed
calendar_df = pd.read_excel("WH Calendar.xlsx")  # if has multiple sheets, add sheet_name param

# 1. Standardize date formats
inventory_df["BALANCE_AS_OF_DATE"] = pd.to_datetime(inventory_df["BALANCE_AS_OF_DATE"])
inbound_df["INBOUND_DATE"] = pd.to_datetime(inbound_df["INBOUND_DATE"])
outbound_df["OUTBOUND_DATE"] = pd.to_datetime(outbound_df["OUTBOUND_DATE"])

# 2. Normalize units: Convert all inventory quantities from KG to MT (1 MT = 1000 KG)
inventory_df["UNRESRICTED_STOCK"] = np.where(
    inventory_df["STOCK_UNIT"] == "KG",
    inventory_df["UNRESRICTED_STOCK"] / 1000,
    inventory_df["UNRESRICTED_STOCK"]
)
inventory_df["STOCK_UNIT"] = "MT"  # Normalize unit

# 3. Aggregate Inventory: Total by Month + Plant + Material
inventory_df["YearMonth"] = inventory_df["BALANCE_AS_OF_DATE"].dt.to_period("M")
inventory_monthly = inventory_df.groupby(["YearMonth", "PLANT_NAME", "MATERIAL_NAME"], as_index=False)["UNRESRICTED_STOCK"].sum()

# 4. Aggregate Inbound/Outbound by Month + Plant + Material
inbound_df["YearMonth"] = inbound_df["INBOUND_DATE"].dt.to_period("M")
inbound_monthly = inbound_df.groupby(["YearMonth", "PLANT_NAME", "MATERIAL_NAME"], as_index=False)["NET_QUANTITY_MT"].sum()
outbound_df["YearMonth"] = outbound_df["OUTBOUND_DATE"].dt.to_period("M")
outbound_monthly = outbound_df.groupby(["YearMonth", "PLANT_NAME", "MATERIAL_NAME"], as_index=False)["NET_QUANTITY_MT"].sum()

# 5. Join with Material Master for enrichment
data_combined = inventory_monthly.merge(
    material_df,
    on="MATERIAL_NAME",
    how="left"
)

# 6. Combine Inbound and Outbound
final_df = data_combined.merge(
    inbound_monthly.rename(columns={"NET_QUANTITY_MT": "INBOUND_MT"}),
    on=["YearMonth", "PLANT_NAME", "MATERIAL_NAME"],
    how="left"
)
final_df = final_df.merge(
    outbound_monthly.rename(columns={"NET_QUANTITY_MT": "OUTBOUND_MT"}),
    on=["YearMonth", "PLANT_NAME", "MATERIAL_NAME"],
    how="left"
)

# Fill NaNs (no inbound/outbound) with 0
final_df["INBOUND_MT"] = final_df["INBOUND_MT"].fillna(0)
final_df["OUTBOUND_MT"] = final_df["OUTBOUND_MT"].fillna(0)

# 7. Sort and reset index
final_df = final_df.sort_values(by=["PLANT_NAME", "MATERIAL_NAME", "YearMonth"])
final_df.reset_index(drop=True, inplace=True)

# Save cleaned and aggregated data
final_df.to_csv("cleaned_inventory_data.csv", index=False)

print("✅ Data cleaned and saved to 'cleaned_inventory_data.csv'")
