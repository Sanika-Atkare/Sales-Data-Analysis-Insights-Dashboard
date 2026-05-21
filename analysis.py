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
monthly_sales = df.groupby('Order Date')['Sales'].sum().resample('ME').sum()
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


# ══════════════════════════════════════════
# DEEP ANALYSIS — LEVEL 2
# ══════════════════════════════════════════

print("\n========== DEEP ANALYSIS ==========")

# 1. Profit Margin % by Category
df['Profit Margin %'] = (df['Profit'] / df['Sales'] * 100).round(2)
category_margin = df.groupby('Category')['Profit Margin %'].mean().round(2)
print("\nProfit Margin % by Category:")
print(category_margin)

# 2. Loss Making Products (Negative Profit)
loss_products = df[df['Profit'] < 0].groupby('Product Name')['Profit'].sum().sort_values().head(10)
print("\nTop 10 Loss Making Products:")
print(loss_products)

# 3. Discount Impact on Profit
discount_impact = df.groupby('Discount')[['Sales', 'Profit']].mean().round(2)
print("\nAverage Sales & Profit by Discount Level:")
print(discount_impact)

# 4. Year over Year Sales Growth
yearly_sales = df.groupby('Year')['Sales'].sum().round(2)
print("\nYearly Sales:")
print(yearly_sales)
yearly_growth = yearly_sales.pct_change() * 100
print("\nYear over Year Growth %:")
print(yearly_growth.round(2))

# 5. Best and Worst States
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
print("\nTop 5 States by Sales:")
print(state_sales.head())
print("\nBottom 5 States by Sales:")
print(state_sales.tail())

# 6. Best and Worst Sub-Categories by Profit
subcategory_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)
print("\nMost Profitable Sub-Categories:")
print(subcategory_profit.head(5))
print("\nLeast Profitable Sub-Categories:")
print(subcategory_profit.tail(5))

# 7. Customer Segment Analysis
segment_analysis = df.groupby('Segment')[['Sales', 'Profit']].sum().round(2)
print("\nSales & Profit by Customer Segment:")
print(segment_analysis)

# 8. Average Order Value
df['Order Value'] = df.groupby('Order ID')['Sales'].transform('sum')
avg_order_value = df.groupby('Segment')['Order Value'].mean().round(2)
print("\nAverage Order Value by Segment:")
print(avg_order_value)

# 9. Shipping Mode Analysis
shipping_analysis = df.groupby('Ship Mode')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Shipping Mode:")
print(shipping_analysis)

# 10. Q4 vs Rest of Year
df['Quarter'] = df['Order Date'].dt.quarter
quarterly_sales = df.groupby('Quarter')['Sales'].sum().round(2)
q4_percentage = (quarterly_sales[4] / quarterly_sales.sum() * 100).round(2)
print("\nSales by Quarter:")
print(quarterly_sales)
print(f"\nQ4 contributes {q4_percentage}% of annual sales")


# ══════════════════════════════════════════
# ADVANCED VISUALIZATIONS
# ══════════════════════════════════════════

# 1. Profit Margin by Category
plt.figure(figsize=(8,5))
sns.barplot(x=category_margin.index, y=category_margin.values, palette='RdYlGn')
plt.title('Profit Margin % by Category', fontsize=14, fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Profit Margin %')
plt.tight_layout()
plt.savefig('output/profit_margin_category.png')
plt.show()
print("Advanced Chart 1 saved!")

# 2. Top 10 Loss Making Products
plt.figure(figsize=(12,6))
loss_products.plot(kind='barh', color='red', alpha=0.7)
plt.title('Top 10 Loss Making Products', fontsize=14, fontweight='bold')
plt.xlabel('Total Loss ($)')
plt.tight_layout()
plt.savefig('output/loss_making_products.png')
plt.show()
print("Advanced Chart 2 saved!")

# 3. Yearly Sales Growth
plt.figure(figsize=(8,5))
yearly_sales.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Year over Year Sales Growth', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('output/yearly_growth.png')
plt.show()
print("Advanced Chart 3 saved!")

# 4. Customer Segment Analysis
fig, axes = plt.subplots(1, 2, figsize=(14,5))
segment_analysis['Sales'].plot(kind='bar', ax=axes[0], color='steelblue', title='Sales by Segment')
segment_analysis['Profit'].plot(kind='bar', ax=axes[1], color='green', title='Profit by Segment')
plt.tight_layout()
plt.savefig('output/segment_analysis.png')
plt.show()
print("Advanced Chart 4 saved!")

# 5. Quarterly Sales Breakdown
plt.figure(figsize=(8,5))
colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']
plt.pie(quarterly_sales.values, labels=['Q1','Q2','Q3','Q4'],
        autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Sales Distribution by Quarter', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('output/quarterly_breakdown.png')
plt.show()
print("Advanced Chart 5 saved!")

# 6. Discount vs Profit Scatter
plt.figure(figsize=(8,5))
sns.scatterplot(x='Discount', y='Profit', hue='Category', data=df, alpha=0.5)
plt.title('Impact of Discount on Profit', fontsize=14, fontweight='bold')
plt.axhline(y=0, color='red', linestyle='--', label='Zero Profit Line')
plt.legend()
plt.tight_layout()
plt.savefig('output/discount_vs_profit.png')
plt.show()
print("Advanced Chart 6 saved!")

# 7. Top 10 States by Sales
top_states = state_sales.head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_states.values, y=top_states.index, palette='Blues_d')
plt.title('Top 10 States by Sales', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('output/top_states.png')
plt.show()
print("Advanced Chart 7 saved!")

# 8. Sub-Category Profit Heatmap
pivot = df.pivot_table(values='Profit', index='Sub-Category', columns='Year', aggfunc='sum')
plt.figure(figsize=(10,8))
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='RdYlGn', linewidths=0.5)
plt.title('Sub-Category Profit Heatmap by Year', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('output/subcategory_heatmap.png')
plt.show()
print("Advanced Chart 8 saved!")

print("\n✅ All advanced charts saved!")
