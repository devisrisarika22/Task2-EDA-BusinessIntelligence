-- ============================================================
-- Task 2 — SQL Business Questions
-- ApexPlanet Software Pvt. Ltd. | Data Analytics Internship
-- Dataset: cleaned_ecommerce_orders (loaded into SQLite)
-- ============================================================

-- Q1. Top 5 categories by total revenue
SELECT
    category,
    ROUND(SUM(revenue), 2)  AS total_revenue,
    COUNT(*)                AS total_orders
FROM orders
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 5;

-- ─────────────────────────────────────────────────────────────

-- Q2. Monthly revenue trend — 2023 vs 2024
SELECT
    order_year,
    order_month,
    ROUND(SUM(revenue), 2)  AS monthly_revenue,
    COUNT(*)                AS orders
FROM orders
GROUP BY order_year, order_month
ORDER BY order_year, order_month;

-- ─────────────────────────────────────────────────────────────

-- Q3. Cancellation rate by category
SELECT
    category,
    COUNT(*)                                            AS total_orders,
    SUM(is_cancelled)                                   AS cancelled,
    ROUND(100.0 * SUM(is_cancelled) / COUNT(*), 2)    AS cancel_rate_pct
FROM orders
GROUP BY category
ORDER BY cancel_rate_pct DESC;

-- ─────────────────────────────────────────────────────────────

-- Q4. Top 5 cities by total revenue
SELECT
    city,
    ROUND(SUM(revenue), 2)  AS total_revenue,
    COUNT(*)                AS total_orders
FROM orders
GROUP BY city
ORDER BY total_revenue DESC
LIMIT 5;

-- ─────────────────────────────────────────────────────────────

-- Q5. Average customer rating by acquisition channel
SELECT
    acquisition_channel,
    ROUND(AVG(customer_rating), 2)  AS avg_rating,
    COUNT(*)                         AS total_orders
FROM orders
GROUP BY acquisition_channel
ORDER BY avg_rating DESC;

-- ─────────────────────────────────────────────────────────────

-- Q6. Revenue split — new vs returning customers
SELECT
    CASE WHEN is_first_order = 1
         THEN 'New Customer'
         ELSE 'Returning Customer'
    END                         AS customer_type,
    COUNT(*)                    AS orders,
    ROUND(SUM(revenue), 2)      AS total_revenue,
    ROUND(AVG(revenue), 2)      AS avg_order_value
FROM orders
GROUP BY is_first_order;

-- ─────────────────────────────────────────────────────────────

-- Q7. Average delivery days by category
SELECT
    category,
    ROUND(AVG(days_to_delivery), 1)  AS avg_days_to_delivery,
    COUNT(*)                          AS delivered_orders
FROM orders
WHERE days_to_delivery IS NOT NULL
GROUP BY category
ORDER BY avg_days_to_delivery;

-- ─────────────────────────────────────────────────────────────

-- BONUS Q8. Top payment methods by order volume
SELECT
    payment_method,
    COUNT(*)                    AS total_orders,
    ROUND(SUM(revenue), 2)      AS total_revenue,
    ROUND(AVG(revenue), 2)      AS avg_order_value
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;

-- BONUS Q9. Revenue by age group
SELECT
    age_group,
    COUNT(*)                    AS total_orders,
    ROUND(SUM(revenue), 2)      AS total_revenue,
    ROUND(AVG(revenue), 2)      AS avg_order_value
FROM orders
GROUP BY age_group
ORDER BY total_revenue DESC;

-- BONUS Q10. Return rate by category
SELECT
    category,
    COUNT(*)                                                        AS total_orders,
    SUM(CASE WHEN order_status = 'Returned' THEN 1 ELSE 0 END)    AS returned,
    ROUND(
        100.0 * SUM(CASE WHEN order_status = 'Returned' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    )                                                               AS return_rate_pct
FROM orders
GROUP BY category
ORDER BY return_rate_pct DESC;
