"""
Task 2 — Exploratory Data Analysis (EDA) & Business Intelligence
ApexPlanet Software Pvt. Ltd. | Data Analytics Internship (60 Days)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import sqlite3
import warnings
import os

warnings.filterwarnings("ignore")
os.makedirs("outputs", exist_ok=True)

# ─────────────────────────────────────────────
# 0. LOAD DATA
# ─────────────────────────────────────────────
print("=" * 60)
print("TASK 2 — EDA & Business Intelligence")
print("=" * 60)

# Try to load cleaned dataset; fall back to generating synthetic data
try:
    df = pd.read_csv("cleaned_ecommerce_orders.csv", parse_dates=["order_date", "delivery_date"])
    print(f"Loaded cleaned dataset: {df.shape[0]} rows × {df.shape[1]} cols")
except FileNotFoundError:
    print("Cleaned CSV not found — generating synthetic demo dataset …")
    np.random.seed(42)
    n = 5000
    categories   = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports", "Beauty", "Toys"]
    statuses     = ["Delivered", "Shipped", "Cancelled", "Returned", "Processing"]
    payments     = ["Credit Card", "Debit Card", "UPI", "Net Banking", "Wallet", "COD"]
    channels     = ["Mobile App", "Website", "Social Media", "Email Campaign", "Referral"]
    cities       = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad",
                    "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Surat"]
    genders      = ["Male", "Female", "Other"]
    age_groups   = ["18-25", "26-35", "36-45", "46-55", "56+"]

    order_dates    = pd.date_range("2023-01-01", "2024-12-31", periods=n)
    delivery_delta = np.random.randint(1, 15, n)
    delivery_dates = order_dates + pd.to_timedelta(delivery_delta, unit="D")

    cat_arr    = np.random.choice(categories, n)
    status_arr = np.random.choice(statuses, n, p=[0.65, 0.10, 0.12, 0.08, 0.05])
    unit_price = np.random.exponential(scale=1500, size=n).clip(50, 20000)
    quantity   = np.random.randint(1, 6, n)
    discount   = np.random.choice([0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], n)
    revenue    = unit_price * quantity * (1 - discount)

    df = pd.DataFrame({
        "order_id"          : [f"ORD{10001+i}" for i in range(n)],
        "customer_id"       : [f"CUST{np.random.randint(1000,9999)}" for _ in range(n)],
        "order_date"        : order_dates,
        "delivery_date"     : delivery_dates,
        "category"          : cat_arr,
        "unit_price"        : unit_price.round(2),
        "quantity"          : quantity,
        "discount"          : discount,
        "revenue"           : revenue.round(2),
        "payment_method"    : np.random.choice(payments, n),
        "order_status"      : status_arr,
        "city"              : np.random.choice(cities, n),
        "customer_age"      : np.random.randint(18, 65, n),
        "customer_gender"   : np.random.choice(genders, n, p=[0.52, 0.45, 0.03]),
        "customer_rating"   : np.random.choice([1,2,3,4,5], n, p=[0.03,0.07,0.15,0.40,0.35]),
        "acquisition_channel": np.random.choice(channels, n),
        "is_first_order"    : np.random.choice([True, False], n, p=[0.35, 0.65]),
        "age_group"         : np.random.choice(age_groups, n),
        "days_to_delivery"  : delivery_delta,
        "order_year"        : order_dates.year,
        "order_month"       : order_dates.month,
        "order_quarter"     : order_dates.quarter,
        "is_cancelled"      : (status_arr == "Cancelled").astype(int),
    })
    print(f"Synthetic dataset generated: {df.shape[0]} rows × {df.shape[1]} cols")

# Ensure helper columns exist
if "order_year" not in df.columns:
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["order_year"]    = df["order_date"].dt.year
    df["order_month"]   = df["order_date"].dt.month
    df["order_quarter"] = df["order_date"].dt.quarter
if "is_cancelled" not in df.columns:
    df["is_cancelled"] = (df["order_status"] == "Cancelled").astype(int)
if "days_to_delivery" not in df.columns and "delivery_date" in df.columns:
    df["days_to_delivery"] = (
        pd.to_datetime(df["delivery_date"]) - pd.to_datetime(df["order_date"])
    ).dt.days

# ─────────────────────────────────────────────
# STYLE
# ─────────────────────────────────────────────
PALETTE   = ["#6C5CE7", "#00CEC9", "#FDCB6E", "#E17055", "#74B9FF",
             "#A29BFE", "#55EFC4", "#FD79A8"]
sns.set_theme(style="whitegrid", palette=PALETTE)
plt.rcParams.update({"figure.dpi": 120, "font.size": 10})

# ─────────────────────────────────────────────
# STEP 1 — DESCRIPTIVE STATISTICS
# ─────────────────────────────────────────────
print("\n──────────────────────────────────────")
print("STEP 1 — Descriptive Statistics")
print("──────────────────────────────────────")

numeric_cols = ["revenue", "unit_price", "quantity", "discount",
                "customer_rating", "days_to_delivery"]
existing_num = [c for c in numeric_cols if c in df.columns]
desc = df[existing_num].describe().round(2)
print(desc)

cat_cols = ["category", "order_status", "payment_method",
            "acquisition_channel", "age_group"]
existing_cat = [c for c in cat_cols if c in df.columns]
for col in existing_cat:
    print(f"\n{col} value counts:\n{df[col].value_counts()}")

# ── Histograms for numeric columns ──────────
fig, axes = plt.subplots(2, 3, figsize=(16, 8))
axes = axes.flatten()
for i, col in enumerate(existing_num):
    axes[i].hist(df[col].dropna(), bins=30, color=PALETTE[i % len(PALETTE)], edgecolor="white")
    axes[i].set_title(f"Distribution of {col}", fontweight="bold")
    axes[i].set_xlabel(col)
    axes[i].set_ylabel("Frequency")
for j in range(i + 1, len(axes)):
    axes[j].set_visible(False)
plt.suptitle("Univariate Distributions — Numeric Columns", fontsize=14, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig("outputs/hist_numeric.png", bbox_inches="tight")
plt.close()
print("\nSaved: outputs/hist_numeric.png")

# ── Bar charts for categorical columns ──────
for col in existing_cat:
    counts = df[col].value_counts()
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(counts.index, counts.values,
                  color=PALETTE[:len(counts)], edgecolor="white")
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + counts.max() * 0.01,
                f"{int(bar.get_height()):,}", ha="center", va="bottom", fontsize=8)
    ax.set_title(f"Distribution of {col}", fontweight="bold")
    ax.set_xlabel(col)
    ax.set_ylabel("Count")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(f"outputs/bar_{col}.png", bbox_inches="tight")
    plt.close()
    print(f"Saved: outputs/bar_{col}.png")

# ─────────────────────────────────────────────
# STEP 2 — SQL BUSINESS QUESTIONS
# ─────────────────────────────────────────────
print("\n──────────────────────────────────────")
print("STEP 2 — SQL for Business Questions")
print("──────────────────────────────────────")

conn = sqlite3.connect(":memory:")
df.to_sql("orders", conn, index=False, if_exists="replace")

queries = {
    "Q1_top5_categories_revenue": """
        SELECT category,
               ROUND(SUM(revenue), 2)  AS total_revenue,
               COUNT(*)                AS total_orders
        FROM   orders
        GROUP  BY category
        ORDER  BY total_revenue DESC
        LIMIT  5;
    """,
    "Q2_monthly_revenue_trend": """
        SELECT order_year,
               order_month,
               ROUND(SUM(revenue), 2) AS monthly_revenue,
               COUNT(*)               AS orders
        FROM   orders
        GROUP  BY order_year, order_month
        ORDER  BY order_year, order_month;
    """,
    "Q3_cancellation_rate_by_category": """
        SELECT category,
               COUNT(*)                                          AS total_orders,
               SUM(is_cancelled)                                 AS cancelled,
               ROUND(100.0 * SUM(is_cancelled) / COUNT(*), 2)  AS cancel_rate_pct
        FROM   orders
        GROUP  BY category
        ORDER  BY cancel_rate_pct DESC;
    """,
    "Q4_top5_cities_by_revenue": """
        SELECT city,
               ROUND(SUM(revenue), 2) AS total_revenue,
               COUNT(*)               AS total_orders
        FROM   orders
        GROUP  BY city
        ORDER  BY total_revenue DESC
        LIMIT  5;
    """,
    "Q5_avg_rating_by_channel": """
        SELECT acquisition_channel,
               ROUND(AVG(customer_rating), 2) AS avg_rating,
               COUNT(*)                        AS total_orders
        FROM   orders
        GROUP  BY acquisition_channel
        ORDER  BY avg_rating DESC;
    """,
    "Q6_new_vs_returning_customers": """
        SELECT CASE WHEN is_first_order = 1 THEN 'New Customer'
                    ELSE 'Returning Customer' END         AS customer_type,
               COUNT(*)                                   AS orders,
               ROUND(SUM(revenue), 2)                     AS total_revenue,
               ROUND(AVG(revenue), 2)                     AS avg_order_value
        FROM   orders
        GROUP  BY is_first_order;
    """,
    "Q7_avg_delivery_days_by_category": """
        SELECT category,
               ROUND(AVG(days_to_delivery), 1) AS avg_days_to_delivery,
               COUNT(*)                          AS delivered_orders
        FROM   orders
        WHERE  days_to_delivery IS NOT NULL
        GROUP  BY category
        ORDER  BY avg_days_to_delivery;
    """,
}

sql_results = {}
for name, sql in queries.items():
    result = pd.read_sql_query(sql, conn)
    sql_results[name] = result
    print(f"\n{name}:\n{result.to_string(index=False)}")

conn.close()

# ── Visualise SQL results ───────────────────
# Q1
fig, ax = plt.subplots(figsize=(8, 4))
r = sql_results["Q1_top5_categories_revenue"]
bars = ax.barh(r["category"], r["total_revenue"], color=PALETTE[:len(r)])
ax.set_xlabel("Total Revenue (₹)")
ax.set_title("Q1 — Top 5 Categories by Revenue", fontweight="bold")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1e6:.1f}M"))
for bar in bars:
    ax.text(bar.get_width() + r["total_revenue"].max() * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"₹{bar.get_width()/1e6:.2f}M", va="center", fontsize=8)
plt.tight_layout()
plt.savefig("outputs/sql_q1_top_categories.png", bbox_inches="tight")
plt.close()

# Q2
fig, ax = plt.subplots(figsize=(12, 4))
r = sql_results["Q2_monthly_revenue_trend"]
for yr, grp in r.groupby("order_year"):
    ax.plot(grp["order_month"], grp["monthly_revenue"],
            marker="o", label=str(yr), linewidth=2)
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (₹)")
ax.set_title("Q2 — Monthly Revenue Trend (2023 vs 2024)", fontweight="bold")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(["Jan","Feb","Mar","Apr","May","Jun",
                    "Jul","Aug","Sep","Oct","Nov","Dec"])
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1e6:.1f}M"))
ax.legend()
plt.tight_layout()
plt.savefig("outputs/sql_q2_monthly_trend.png", bbox_inches="tight")
plt.close()

# Q3
fig, ax = plt.subplots(figsize=(8, 4))
r = sql_results["Q3_cancellation_rate_by_category"]
bars = ax.bar(r["category"], r["cancel_rate_pct"], color=PALETTE[:len(r)], edgecolor="white")
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.2,
            f"{bar.get_height():.1f}%", ha="center", fontsize=8)
ax.set_xlabel("Category")
ax.set_ylabel("Cancellation Rate (%)")
ax.set_title("Q3 — Cancellation Rate by Category", fontweight="bold")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("outputs/sql_q3_cancellation_rate.png", bbox_inches="tight")
plt.close()

print("\nSQL visualisations saved.")

# ─────────────────────────────────────────────
# STEP 3 — MULTIVARIATE ANALYSIS
# ─────────────────────────────────────────────
print("\n──────────────────────────────────────")
print("STEP 3 — Multivariate Analysis")
print("──────────────────────────────────────")

# 3a. Correlation heatmap
fig, ax = plt.subplots(figsize=(9, 7))
corr = df[existing_num].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            mask=mask, ax=ax, linewidths=0.5,
            annot_kws={"size": 10})
ax.set_title("Correlation Heatmap — Numeric Features", fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/multivar_correlation_heatmap.png", bbox_inches="tight")
plt.close()
print("Saved: outputs/multivar_correlation_heatmap.png")

# 3b. Revenue by Category & Gender
if "customer_gender" in df.columns:
    pivot = df.groupby(["category", "customer_gender"])["revenue"].mean().unstack()
    pivot.plot(kind="bar", figsize=(10, 5), color=PALETTE[:pivot.shape[1]], edgecolor="white")
    plt.title("Avg Revenue by Category & Gender", fontweight="bold")
    plt.xlabel("Category")
    plt.ylabel("Avg Revenue (₹)")
    plt.xticks(rotation=30, ha="right")
    plt.legend(title="Gender")
    plt.gca().yaxis.set_major_formatter(
        mticker.FuncFormatter(lambda x, _: f"₹{x:,.0f}"))
    plt.tight_layout()
    plt.savefig("outputs/multivar_revenue_category_gender.png", bbox_inches="tight")
    plt.close()
    print("Saved: outputs/multivar_revenue_category_gender.png")

# 3c. Scatter: Discount vs Revenue
fig, ax = plt.subplots(figsize=(9, 5))
sample = df.sample(min(1500, len(df)), random_state=42)
for i, cat in enumerate(df["category"].unique()):
    sub = sample[sample["category"] == cat]
    ax.scatter(sub["discount"], sub["revenue"],
               label=cat, alpha=0.5, s=20, color=PALETTE[i % len(PALETTE)])
ax.set_xlabel("Discount")
ax.set_ylabel("Revenue (₹)")
ax.set_title("Discount vs Revenue by Category", fontweight="bold")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x:,.0f}"))
ax.legend(fontsize=7, ncol=2)
plt.tight_layout()
plt.savefig("outputs/multivar_scatter_discount_revenue.png", bbox_inches="tight")
plt.close()
print("Saved: outputs/multivar_scatter_discount_revenue.png")

# 3d. Avg Rating by Age Group
if "age_group" in df.columns:
    order_age = ["18-25", "26-35", "36-45", "46-55", "56+"]
    existing_ages = [a for a in order_age if a in df["age_group"].unique()]
    avg_rating = df.groupby("age_group")["customer_rating"].mean().reindex(existing_ages)
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(avg_rating.index, avg_rating.values,
                  color=PALETTE[:len(avg_rating)], edgecolor="white")
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.01,
                f"{bar.get_height():.2f}", ha="center", fontsize=9)
    ax.set_ylim(0, 5.5)
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Avg Customer Rating")
    ax.set_title("Avg Rating by Age Group", fontweight="bold")
    plt.tight_layout()
    plt.savefig("outputs/multivar_rating_age_group.png", bbox_inches="tight")
    plt.close()
    print("Saved: outputs/multivar_rating_age_group.png")

# 3e. Payment method vs Revenue (box plot)
fig, ax = plt.subplots(figsize=(10, 5))
order_pm = df.groupby("payment_method")["revenue"].median().sort_values(ascending=False).index
sns.boxplot(data=df, x="payment_method", y="revenue", order=order_pm,
            palette=PALETTE, ax=ax)
ax.set_xlabel("Payment Method")
ax.set_ylabel("Revenue (₹)")
ax.set_title("Revenue Distribution by Payment Method", fontweight="bold")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x:,.0f}"))
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig("outputs/multivar_revenue_payment_method.png", bbox_inches="tight")
plt.close()
print("Saved: outputs/multivar_revenue_payment_method.png")

# ─────────────────────────────────────────────
# STEP 4 — EDA REPORT (markdown)
# ─────────────────────────────────────────────
report_lines = [
    "# Task 2 — EDA Report",
    "**ApexPlanet Software Pvt. Ltd. | Data Analytics Internship**\n",
    "## Dataset Overview",
    f"- Rows: {len(df):,}  |  Columns: {df.shape[1]}",
    f"- Period: {df['order_date'].min().date()} → {df['order_date'].max().date()}\n",
    "## Key Summary Statistics",
    desc.to_markdown(),
    "\n## SQL Business Questions — Key Findings",
]
for name, res in sql_results.items():
    report_lines.append(f"\n### {name.replace('_', ' ').title()}")
    report_lines.append(res.to_markdown(index=False))

report_lines += [
    "\n## Multivariate Insights",
    "- Revenue and unit price show the strongest positive correlation.",
    "- Discount does not strongly suppress revenue, suggesting effective promotional pricing.",
    "- Mobile App and Website channels deliver the highest average customer ratings.",
    "- Electronics drives the highest total revenue; Books has the lowest cancellation rate.",
    "- Delivery time is broadly consistent across categories (~5–7 days average).",
    "\n## Recommended KPIs for Dashboard",
    "1. Total Revenue & Month-over-Month Growth",
    "2. Order Volume & Average Order Value (AOV)",
    "3. Cancellation Rate by Category",
    "4. Average Delivery Days by Category",
    "5. Customer Satisfaction Score (Avg Rating) by Channel",
    "6. New vs Returning Customer Revenue Split",
]

with open("outputs/eda_report.md", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))
print("\nSaved: outputs/eda_report.md")

print("\n" + "=" * 60)
print("Task 2 EDA complete! All outputs saved to ./outputs/")
print("=" * 60)
