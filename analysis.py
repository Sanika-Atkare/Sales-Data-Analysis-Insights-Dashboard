import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('output', exist_ok=True)
print("Libraries imported successfully!")

df = pd.read_csv('data/sales_data.csv', encoding='latin1')
print("Shape:", df.shape)
print("First 5 rows:")
print(df.head())
print("Missing values:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
df.dropna(inplace=True)
print("Data cleaned! Final shape:", df.shape)

total_sales = df['Sales'].sum().round(2)
total_profit = df['Profit'].sum().round(2)
print(f"Total Sales: ${total_sales}")
print(f"Total Profit: ${total_profit}")

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)

print("Sales by Category:")
print(category_sales)
print("Sales by Region:")
print(region_sales)
print("Top 10 Customers:")
print(top_customers)

sns.set_style("whitegrid")

plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales.values, palette='Blues_d')
plt.title('Sales by Category', fontsize=14, fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('output/sales_by_category.png')
plt.show()
print("Chart 1 saved!")

plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette='Greens_d')
plt.title('Sales by Region', fontsize=14, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('output/sales_by_region.png')
plt.show()
print("Chart 2 saved!")

plt.figure(figsize=(12,5))
monthly_sales = df.groupby('Order Date')['Sales'].sum().resample('M').sum()
monthly_sales.plot(kind='line', color='steelblue', linewidth=2, marker='o')
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('output/monthly_trend.png')
plt.show()
print("Chart 3 saved!")

plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', hue='Category', data=df, alpha=0.6)
plt.title('Profit vs Sales by Category', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('output/profit_vs_sales.png')
plt.show()
print("Chart 4 saved!")

plt.figure(figsize=(10,6))
sns.barplot(x=top_customers.values, y=top_customers.index, palette='Oranges_d')
plt.title('Top 10 Customers by Sales', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales')
plt.tight_layout()
plt.savefig('output/top_customers.png')
plt.show()
print("Chart 5 saved!")

print("All done! Check your output folder for all charts!")