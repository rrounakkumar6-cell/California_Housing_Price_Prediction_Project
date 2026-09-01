# Python-Data-Analysis
This repository contains an end-to-end sales data analysis project using Python (Pandas, Matplotlib, Seaborn) and Power BI. The dataset used is “Sample Sales Data: Denormalize Sales Data (Segmentation, Clustering, Shipping, etc.) by Gus Segura”, which contains retail sales transactions with order, product, customer, and geographical details.
# 📊 Sales Data Analysis Project

This project demonstrates end-to-end **data analysis and visualization** using Python and Power BI on a sample sales dataset.
## 📊 Dataset
The dataset used is:
- **Sample Sales Data – Denormalize Sales Data (Segmentation, Clustering, Shipping, etc.)**
- Contains **~2,800 rows** and **25 columns**
- Key columns:
  - `ORDERNUMBER`, `ORDERDATE`, `PRODUCTLINE`, `SALES`, `QUANTITYORDERED`, `PRICEEACH`
  - `CUSTOMERNAME`, `COUNTRY`, `STATE`, `CITY`
  - `DEALSIZE`, `TERRITORY`

---

## 🛠️ Tools & Libraries
- **Python**: `pandas`, `matplotlib`, `seaborn`
  ## 📈 Analysis & Visualizations
1. **Data Cleaning**
   - Handled missing values (`STATE`, `POSTALCODE`, `TERRITORY`)
   - Converted `ORDERDATE` to datetime
   - Extracted year and month for time-based analysis

2. **Exploratory Analysis**
   - Sales by product line
   - Deal size distribution
   - Sales trends over time
   - Pivot table summaries by country/product line

3. **Visualizations**
   - 📊 Bar chart: Sales by product line
   - 🥧 Pie chart: Deal size distribution
   - 📈 Line chart: Sales trend by month/year
   - 📋 Pivot tables: Country vs Product line sales
