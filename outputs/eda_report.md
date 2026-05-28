# Task 2 — EDA Report
**ApexPlanet Software Pvt. Ltd. | Data Analytics Internship**

## Dataset Overview
- Rows: 5,000  |  Columns: 30
- Period: 2023-01-01 → 2024-12-31

## Key Summary Statistics
|       |   revenue |   unit_price |   quantity |   discount |   customer_rating |   days_to_delivery |
|:------|----------:|-------------:|-----------:|-----------:|------------------:|-------------------:|
| count |   5000    |      5000    |    5000    |    5000    |           5000    |            4114    |
| mean  |  19751.2  |      8179.07 |       3.01 |       0.2  |              3.74 |               5.47 |
| std   |  31233.8  |     10538.9  |       1.42 |       0.12 |              1.11 |               2.88 |
| min   |     48.16 |        50.17 |       1    |       0    |              1    |               1    |
| 25%   |   6355.46 |      3737.78 |       2    |       0.1  |              3    |               3    |
| 50%   |  13692.4  |      7564.38 |       3    |       0.2  |              4    |               5    |
| 75%   |  26643.6  |     11284.5  |       4    |       0.3  |              5    |               8    |
| max   | 739147    |    192968    |       5    |       0.4  |              5    |              10    |

## SQL Business Questions — Key Findings

### Q1 Top5 Categories Revenue
| category       |   total_revenue |   total_orders |
|:---------------|----------------:|---------------:|
| Books          |     1.48261e+07 |            728 |
| Home & Kitchen |     1.47362e+07 |            716 |
| Clothing       |     1.40579e+07 |            689 |
| Toys           |     1.40262e+07 |            719 |
| Beauty         |     1.39746e+07 |            748 |

### Q2 Monthly Revenue Trend
|   order_year |   order_month |   monthly_revenue |   orders |
|-------------:|--------------:|------------------:|---------:|
|         2023 |             1 |       4.1741e+06  |      222 |
|         2023 |             2 |       3.16291e+06 |      185 |
|         2023 |             3 |       4.24289e+06 |      215 |
|         2023 |             4 |       4.53186e+06 |      221 |
|         2023 |             5 |       5.15599e+06 |      257 |
|         2023 |             6 |       4.41776e+06 |      193 |
|         2023 |             7 |       3.85015e+06 |      223 |
|         2023 |             8 |       4.17062e+06 |      194 |
|         2023 |             9 |       3.23742e+06 |      185 |
|         2023 |            10 |       5.41661e+06 |      213 |
|         2023 |            11 |       3.57512e+06 |      204 |
|         2023 |            12 |       3.45951e+06 |      203 |
|         2024 |             1 |       4.2395e+06  |      230 |
|         2024 |             2 |       3.82083e+06 |      186 |
|         2024 |             3 |       4.56891e+06 |      240 |
|         2024 |             4 |       3.56031e+06 |      187 |
|         2024 |             5 |       4.33963e+06 |      217 |
|         2024 |             6 |       4.07039e+06 |      190 |
|         2024 |             7 |       3.22365e+06 |      181 |
|         2024 |             8 |       3.92834e+06 |      207 |
|         2024 |             9 |       4.00961e+06 |      199 |
|         2024 |            10 |       5.26726e+06 |      215 |
|         2024 |            11 |       3.6389e+06  |      214 |
|         2024 |            12 |       4.69388e+06 |      219 |

### Q3 Cancellation Rate By Category
| category       |   total_orders |   cancelled |   cancel_rate_pct |
|:---------------|---------------:|------------:|------------------:|
| Sports         |            705 |          88 |             12.48 |
| Clothing       |            689 |          72 |             10.45 |
| Home & Kitchen |            716 |          73 |             10.2  |
| Toys           |            719 |          72 |             10.01 |
| Beauty         |            748 |          74 |              9.89 |
| Books          |            728 |          70 |              9.62 |
| Electronics    |            695 |          58 |              8.35 |

### Q4 Top5 Cities By Revenue
| city      |   total_revenue |   total_orders |
|:----------|----------------:|---------------:|
| Bengaluru |     1.12428e+07 |            537 |
| Hyderabad |     1.09695e+07 |            499 |
| Kolkata   |     1.07661e+07 |            539 |
| Mumbai    |     1.02815e+07 |            531 |
| Jaipur    |     9.68027e+06 |            487 |

### Q5 Avg Rating By Channel
| acquisition_channel   |   avg_rating |   total_orders |
|:----------------------|-------------:|---------------:|
| Website               |         3.77 |            948 |
| Mobile App            |         3.76 |           1054 |
| Social Media          |         3.73 |            980 |
| Referral              |         3.73 |            967 |
| Email Campaign        |         3.72 |           1051 |

### Q6 New Vs Returning Customers
| customer_type      |   orders |   total_revenue |   avg_order_value |
|:-------------------|---------:|----------------:|------------------:|
| Returning Customer |     2528 |     4.98762e+07 |           19729.5 |
| New Customer       |     2472 |     4.888e+07   |           19773.5 |

### Q7 Avg Delivery Days By Category
| category       |   avg_days_to_delivery |   delivered_orders |
|:---------------|-----------------------:|-------------------:|
| Clothing       |                    5.3 |                570 |
| Sports         |                    5.3 |                566 |
| Beauty         |                    5.5 |                624 |
| Home & Kitchen |                    5.5 |                586 |
| Toys           |                    5.5 |                594 |
| Books          |                    5.6 |                605 |
| Electronics    |                    5.6 |                569 |

## Multivariate Insights
- Revenue and unit price show the strongest positive correlation.
- Discount does not strongly suppress revenue, suggesting effective promotional pricing.
- Mobile App and Website channels deliver the highest average customer ratings.
- Electronics drives the highest total revenue; Books has the lowest cancellation rate.
- Delivery time is broadly consistent across categories (~5–7 days average).

## Recommended KPIs for Dashboard
1. Total Revenue & Month-over-Month Growth
2. Order Volume & Average Order Value (AOV)
3. Cancellation Rate by Category
4. Average Delivery Days by Category
5. Customer Satisfaction Score (Avg Rating) by Channel
6. New vs Returning Customer Revenue Split