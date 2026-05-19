# 📊 Sales Data Analysis & Insights Dashboard

**Tools Used:** Python | Pandas | NumPy | Matplotlib | Seaborn | OpenPyXL  
**Dataset:** Sample Superstore Sales Dataset (9,994 records)  
**GitHub:** [Sales-Data-Analysis-Insights-Dashboard](https://github.com/Sanika-Atkare/Sales-Data-Analysis-Insights-Dashboard)

---

## 📌 About This Project

This is an end-to-end data analytics project that analyzes real-world sales data from a superstore.  
The goal is to find useful business insights from raw data — such as which products sell the most,  
which regions generate the highest revenue, and who the top customers are.

The project covers the full data analytics workflow:
- Data Loading
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Automated Excel Report Generation

---

## 📁 Project Structure

```
Sales-Data-Analysis-Insights-Dashboard/
│
├── data/
│   └── sales_data.csv              ← Raw dataset from Kaggle
│
├── output/
│   ├── sales_by_category.png       ← Bar chart: Sales by Category
│   ├── sales_by_region.png         ← Bar chart: Sales by Region
│   ├── monthly_trend.png           ← Line chart: Monthly Sales Trend
│   ├── profit_vs_sales.png         ← Scatter plot: Profit vs Sales
│   ├── top_customers.png           ← Bar chart: Top 10 Customers
│   └── sales_report.xlsx           ← Automated Excel Report
│
├── notebooks/
│   └── sales_analysis.ipynb        ← Jupyter Notebook (exploration)
│
├── analysis.py                     ← Main Python file: EDA + Visualizations
├── report.py                       ← Excel report generation
└── README.md                       ← Project documentation
```

---

## 🔍 Key Business Questions Answered

1. Which product category generates the highest revenue?
2. Which region performs best in terms of sales?
3. What is the monthly sales trend over the years?
4. Who are the top 10 customers by revenue?
5. What is the relationship between Sales and Profit?

---

## 📊 Key Insights Found

- **Technology** category generates the highest total sales
- **West** region leads all regions in total revenue
- Sales show a consistent **upward trend** with peaks in Q4 every year
- **Phones and Chairs** are the top-selling sub-categories
- Some products have **high sales but negative profit** — indicating discount issues

---

## 🛠️ How to Run This Project

**Step 1 — Clone the repository:**
```
git clone https://github.com/Sanika-Atkare/Sales-Data-Analysis-Insights-Dashboard.git
```

**Step 2 — Install required libraries:**
```
pip install pandas numpy matplotlib seaborn openpyxl
```

**Step 3 — Run the analysis:**
```
py analysis.py
```

**Step 4 — Generate Excel report:**
```
py report.py
```

**Step 5 — Check the output folder** for all charts and the Excel report.

---

## 📦 Libraries Used

| Library | Purpose |
|---|---|
| Pandas | Data loading, cleaning, analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Advanced styled charts |
| OpenPyXL | Excel report generation |
| OS | File and folder management |

---

## 👤 Author

**Sanika Atkare**  
Aspiring Data Analyst | Python | SQL | Power BI | Excel  
GitHub: [Sanika-Atkare](https://github.com/Sanika-Atkare)
