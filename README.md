# Task 2 — Exploratory Data Analysis (EDA) & Business Intelligence
### ApexPlanet Software Pvt. Ltd. | Data Analytics Internship (60 Days)

---

## Overview

This repository contains all deliverables for **Task 2** of the ApexPlanet Data Analytics Internship.  
Building on the cleaned dataset from Task 1, the objective is to uncover patterns, trends, and relationships through EDA and SQL-based business intelligence.

**Timeline:** 14 Days  
**Dataset:** Cleaned Indian E-Commerce Orders — 2023 to 2024 (5,000 rows × 30 cols)

---

## Repository Structure

```
task2-eda/
│
├── eda_analysis.py          ← Main Python EDA script (Steps 1–3 + report generation)
├── sql_queries.sql          ← All 7 business SQL queries (+ 3 bonus queries)
├── README.md                ← This file
│
└── outputs/
    ├── eda_report.md                          ← Written EDA findings & insights
    │
    ├── hist_numeric.png                       ← Histograms for numeric columns
    ├── bar_category.png                       ← Category distribution
    ├── bar_order_status.png                   ← Order status distribution
    ├── bar_payment_method.png                 ← Payment method distribution
    ├── bar_acquisition_channel.png            ← Acquisition channel distribution
    ├── bar_age_group.png                      ← Age group distribution
    │
    ├── sql_q1_top_categories.png              ← Top 5 categories by revenue
    ├── sql_q2_monthly_trend.png               ← Monthly revenue trend 2023 vs 2024
    ├── sql_q3_cancellation_rate.png           ← Cancellation rate by category
    │
    ├── multivar_correlation_heatmap.png       ← Correlation heatmap
    ├── multivar_revenue_category_gender.png   ← Revenue by category & gender
    ├── multivar_scatter_discount_revenue.png  ← Discount vs revenue scatter
    ├── multivar_rating_age_group.png          ← Avg rating by age group
    └── multivar_revenue_payment_method.png    ← Revenue by payment method (boxplot)
```

---

## Steps & Methods

### Step 1 — Descriptive Statistics & Univariate Analysis
- Summary statistics (mean, median, std, min, max, quartiles) for all numeric columns
- Value counts and frequency distributions for all categorical columns
- Histograms and bar charts saved to `outputs/`

### Step 2 — SQL for Business Questions

| # | Question | Key Finding |
|---|----------|-------------|
| Q1 | Top 5 categories by revenue | Electronics leads, followed by Clothing |
| Q2 | Monthly revenue trend 2023 vs 2024 | Festive months (Oct–Dec) peak |
| Q3 | Cancellation rate by category | Toys has highest cancellation rate |
| Q4 | Top 5 cities by revenue | Mumbai, Delhi, Bangalore dominate |
| Q5 | Avg rating by acquisition channel | Mobile App users rate highest |
| Q6 | New vs returning customer revenue | Returning customers have 23% higher AOV |
| Q7 | Avg delivery days by category | Books deliver fastest (~4.5 days) |

### Step 3 — Multivariate Analysis & Correlation
- **Correlation heatmap** — Revenue and unit price are most positively correlated
- **Revenue by category & gender** — Electronics skews male; Beauty skews female
- **Discount vs revenue scatter** — Discount does not strongly suppress revenue
- **Rating by age group** — 36–45 age group gives highest ratings consistently
- **Revenue by payment method** — Credit Card and UPI show highest median order values

### Step 4 — Static Dashboard Mock-up
Key KPI panels proposed:
1. Total Revenue & MoM Growth
2. Orders by Category (bar chart)
3. Monthly Revenue Trend (line chart, 2023 vs 2024)
4. Top 5 Cities by Revenue (horizontal bar)
5. Cancellation Rate by Category
6. Avg Delivery Days by Category
7. New vs Returning Customer Revenue Split (pie/stacked bar)

---

## How to Run

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn
```

### Execute EDA Script
```bash
cd task2-eda/
python3 eda_analysis.py
```

All charts and the EDA report are written to `outputs/`.

---

## Key Insights

- **Electronics** is the highest revenue-generating category; **Books** has the lowest cancellation rate.
- **Mobile App** acquisition channel delivers the highest customer satisfaction ratings.
- **Returning customers** contribute significantly more revenue per order than first-time buyers.
- **Q4 (Oct–Dec)** shows a consistent seasonal revenue spike across both years.
- **UPI and Credit Card** are the dominant payment methods by order volume.
- **Discount levels** do not appear to negatively impact customer ratings.

---

## Skills Demonstrated

- Python EDA with Pandas, Matplotlib, and Seaborn
- SQL aggregation, filtering, and grouping with SQLite
- Univariate and multivariate statistical analysis
- Data visualization (histograms, bar charts, scatter plots, box plots, heatmaps)
- Business intelligence reporting and KPI definition

---

## Next Steps (Task 3 Preview)

- Define 3–5 formal KPIs with business rationale
- Deep-dive cohort or segmentation analysis
- Build interactive dashboard in Tableau / Power BI / Looker Studio

---

*ApexPlanet Software Pvt. Ltd. | www.apexplanet.in*
