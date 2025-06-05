# `Analytics_Examples.md` 


```markdown
---
title: "Analytics Examples: SQL Queries for Metrics Extraction"
id: "analytics_examples_001"
doc_type: "analytics"
doc_version: "1.0"
date_created: "2025-04-23"
date_updated: "2025-04-23"
author: "João Castanheira"
db_name: "joaocastanheira_bancodedados"
db_version: "1.0"
doc_status: "Approved"
environment: "Production"
language: "en"
response_languages: ["pt-BR", "en"]
technical_terms_preservation: "strict"
original_language: "pt-BR"
related_docs: ["core_db_arch_001", "process_flow_purchase_lifecycle_001", "process_flow_subscription_lifecycle_001", "process_flow_commission_system_001", "process_flow_refund_chargeback_001", "ref_db_schema_details_001"]
tables_in_focus: ["transactions", "subscriptions", "customers", "plans", "products", "platform_commission", "transaction_status_history", "subscription_status_history", "transaction_items", "transaction_statuses", "commission_participants"]
primary_key_entities: ["transactions.id", "subscriptions.id", "customers.id", "products.id", "plans.id"]
technical_terms: {
  "table_names": [
    "transactions", "subscriptions", "customers", "plans", "products", 
    "platform_commission", "transaction_status_history", "subscription_status_history", 
    "transaction_items", "transaction_statuses", "commission_participants", 
    "platform_transaction_payment_history"
  ],
  "column_names": [
    "id", "transaction_id", "order_date", "customer_id", "offer_price", "platform_fee_amount",
    "partner_commission_amount", "producer_net_amount", "status_id", "subscription_id", 
    "is_subscription", "recurrence_number", "tracking_source", "email", "name", "start_date", 
    "end_date", "cancel_date", "next_billing_date", "price", "currency_code", "recurrence_period", 
    "max_cycles", "change_date", "reason", "amount", "source", "participant_id", "created_at", 
    "updated_at", "payment_method", "payment_date", "metadata", "product_id", "platform_origin"
  ],
  "data_types": [
    "DATE", "TIMESTAMP", "INTERVAL", "NUMERIC", "INTEGER", "VARCHAR", "BOOLEAN", "JSONB", 
    "TEXT", "SERIAL", "REFERENCES", "DATE_TRUNC", "GENERATE_SERIES", "EXTRACT", "TO_CHAR"
  ],
  "sql_keywords": [
    "SELECT", "FROM", "WHERE", "JOIN", "LEFT JOIN", "CROSS JOIN", "INNER JOIN", 
    "GROUP BY", "ORDER BY", "HAVING", "LIMIT", "WITH", "AS", "UNION", "UNION ALL", 
    "CASE", "WHEN", "THEN", "ELSE", "END", "AND", "OR", "IN", "NOT", "LIKE", "ILIKE", 
    "IS NULL", "IS NOT NULL", "BETWEEN", "COUNT", "SUM", "AVG", "MIN", "MAX", "COALESCE", 
    "NULLIF", "ROUND", "DENSE_RANK", "RANK", "ROW_NUMBER", "LAG", "LEAD", "OVER", 
    "PARTITION BY", "RECURSIVE", "ON", "DISTINCT", "EXISTS", "NOT EXISTS", "CURRENT_DATE", 
    "CURRENT_TIMESTAMP", "TRUE", "FALSE", "INTERVAL", "DATE_TRUNC", "EXTRACT", "TO_CHAR", 
    "GENERATE_SERIES", "CREATE", "UPDATE", "DELETE", "INSERT INTO", "VALUES", "ABS"
  ],
  "transaction_statuses": [
    "Aprovada", "Approved", "Reembolsada", "Refunded", "Ativa", "Active", 
    "Cancelada pelo Cliente", "Canceled by Customer", "Cancelada por Inadimplência", 
    "Canceled due to Default", "Inadimplente", "Defaulting", "Concluída", "Completed"
  ],
  "plan_recurrence_periods": [
    "YEAR", "QUARTER", "MONTH", "SEMIANNUAL", "WEEK"
  ],
  "payment_methods": [
    "credit_card", "boleto", "pix", "paypal", "refund", "REFUND", "PARTIAL_REFUND"
  ],
  "commission_sources": [
    "AFFILIATE", "PRODUCER", "COPRODUCER", "AFFILIATE_REFUND", "PRODUCER_REFUND"
  ],
  "tracking_sources": [
    "aff_", "fb_", "ig_", "gg_", "yt_", "em_"
  ],
  "programming_concepts": [
    "CTE", "Common Table Expression", "materialized view", "index", "subquery", 
    "recursive query", "pivot", "window function", "aggregate function"
  ]
}
embedding_guide_concepts: [
  "analytical queries", 
  "sales metrics", 
  "performance indicators", 
  "MRR", 
  "GMV", 
  "gross revenue", 
  "net revenue", 
  "churn rate", 
  "retention rate", 
  "LTV", 
  "CAC", 
  "conversion rate", 
  "refund rate", 
  "average order value", 
  "dashboard", 
  "financial reports", 
  "cohort analysis", 
  "customer segmentation", 
  "affiliate performance", 
  "product performance", 
  "query optimization", 
  "indexes", 
  "monitoring", 
  "trend analysis", 
  "revenue forecasting", 
  "analytical SQL"
]
---


# Analytics Examples: SQL Queries for Metrics Extraction


## Overview


This document presents practical examples of SQL queries for extracting key metrics and performance indicators from the `joaocastanheira_bancodedados` database. These queries are designed to provide valuable insights into business performance, customer behavior, product effectiveness, and affiliate commissions.


Each query includes:
- A description of its purpose
- The complete and commented SQL query
- Explanation of expected results
- Performance optimization considerations
- Tips for interpreting the results


While these queries can be used directly in SQL tools, they also serve as a foundation for dashboards, automated reports, and more specific ad-hoc analyses.


(Ref: Analytics Examples, ID analytics_examples_001)


## Sales and Revenue Metrics


### Total Revenue by Period


**Purpose**: Analyze gross revenue, net revenue, and platform fees by month, allowing visualization of growth trends and seasonality.


```sql
-- Gross revenue, net revenue and fees by month (approved transactions only)
SELECT 
    DATE_TRUNC('month', t.order_date) AS month,
    COUNT(*) AS total_transactions,
    SUM(t.offer_price) AS gross_revenue,
    SUM(t.platform_fee_amount) AS platform_fees,
    SUM(t.partner_commission_amount) AS partner_commissions,
    SUM(t.producer_net_amount) AS net_revenue,
    ROUND(AVG(t.offer_price), 2) AS average_order_value,
    ROUND(SUM(t.producer_net_amount) * 100.0 / NULLIF(SUM(t.offer_price), 0), 2) AS profit_margin_pct
FROM 
    transactions t
JOIN 
    transaction_statuses ts ON t.status_id = ts.id
WHERE 
    ts.status = 'Approved'
    AND t.order_date BETWEEN '2023-01-01' AND '2023-11-30'
GROUP BY 
    DATE_TRUNC('month', t.order_date)
ORDER BY 
    month;
```


**Interpreting the Results**:
- `gross_revenue`: Total amount charged to customers
- `platform_fees`: Fees charged by platforms
- `partner_commissions`: Commissions paid to affiliates and partners
- `net_revenue`: Producer's final revenue after all deductions
- `profit_margin_pct`: Percentage of gross revenue that converts to net revenue


**Optimization**:
- This query benefits from indexes on `transactions.order_date` and `transactions.status_id`
- For large data volumes, consider materializing this view in a daily or weekly aggregation table


(Ref: Analytics Examples, ID analytics_examples_001)


### GMV (Gross Merchandise Value) by Product


**Purpose**: Identify products that generate the highest sales volume, helping to direct marketing and development efforts.


```sql
-- GMV and number of sales by product, including refund rate
WITH product_sales AS (
    SELECT 
        p.id AS product_id,
        p.name AS product_name,
        p.platform_origin,
        COUNT(*) AS total_transactions,
        SUM(t.offer_price) AS gross_revenue,
        COUNT(CASE WHEN ts.status = 'Refunded' THEN 1 END) AS refunded_count,
        SUM(CASE WHEN ts.status = 'Refunded' THEN t.offer_price ELSE 0 END) AS refunded_amount
    FROM 
        transactions t
    JOIN 
        transaction_items ti ON t.id = ti.transaction_id
    JOIN 
        products p ON ti.product_id = p.id
    JOIN 
        transaction_statuses ts ON t.status_id = ts.id
    WHERE 
        t.order_date BETWEEN '2023-01-01' AND '2023-11-30'
        AND ts.status IN ('Approved', 'Refunded') -- Include only finalized transactions
    GROUP BY 
        p.id, p.name, p.platform_origin
)
SELECT 
    product_name,
    platform_origin,
    total_transactions,
    gross_revenue,
    ROUND(gross_revenue / total_transactions, 2) AS average_price,
    refunded_count,
    refunded_amount,
    ROUND((refunded_count * 100.0) / NULLIF(total_transactions, 0), 2) AS refund_rate_pct,
    ROUND((refunded_amount * 100.0) / NULLIF(gross_revenue, 0), 2) AS refunded_amount_pct,
    RANK() OVER (ORDER BY gross_revenue DESC) AS revenue_rank
FROM 
    product_sales
ORDER BY 
    gross_revenue DESC;
```


**Interpreting the Results**:
- Identifies best-selling products both in volume and value
- Calculates refund rate by product, an important satisfaction indicator
- Ranking allows quick identification of highest revenue products


**Optimization**:
- Use indexes on join tables, especially `transaction_items.transaction_id` and `transaction_items.product_id`
- The Common Table Expression (CTE) improves readability without significantly impacting performance


(Ref: Analytics Examples, ID analytics_examples_001)


### Recurring Revenue (MRR) from Subscriptions


**Purpose**: Calculate Monthly Recurring Revenue (MRR) for the subscription model, a critical metric for subscription-based businesses.


```sql
-- MRR (Monthly Recurring Revenue) and active subscriber count by month
WITH monthly_dates AS (
    -- Generate sequence of monthly dates for analysis
    SELECT generate_series(
        DATE_TRUNC('month', '2023-01-01'::date),
        DATE_TRUNC('month', '2023-11-01'::date),
        '1 month'::interval
    ) AS month_date
),
subscription_mrr AS (
    -- Calculate MRR per subscription, normalizing different periodicities
    SELECT 
        s.id AS subscription_id,
        p.price AS base_price,
        p.currency_code,
        CASE 
            WHEN p.recurrence_period = 'YEAR' THEN p.price / 12
            WHEN p.recurrence_period = 'QUARTER' THEN p.price / 3
            WHEN p.recurrence_period = 'SEMIANNUAL' THEN p.price / 6
            WHEN p.recurrence_period = 'WEEK' THEN p.price * 4.33 -- Approximation of weeks per month
            ELSE p.price -- Assume monthly periodicity as default
        END AS monthly_recurring_revenue
    FROM 
        subscriptions s
    JOIN 
        plans p ON s.plan_id = p.id
    WHERE 
        p.currency_code = 'BRL' -- Filter by currency for consistency
)
SELECT 
    d.month_date,
    COUNT(DISTINCT s.id) AS active_subscriptions,
    ROUND(SUM(sm.monthly_recurring_revenue), 2) AS total_mrr,
    ROUND(AVG(sm.monthly_recurring_revenue), 2) AS average_mrr_per_subscriber
FROM 
    monthly_dates d
LEFT JOIN 
    subscriptions s ON 
        DATE_TRUNC('month', s.start_date) <= d.month_date
        AND (
            s.end_date IS NULL OR 
            DATE_TRUNC('month', s.end_date) >= d.month_date
        )
LEFT JOIN 
    subscription_mrr sm ON s.id = sm.subscription_id
LEFT JOIN 
    transaction_statuses ts ON s.status_id = ts.id
WHERE 
    ts.status = 'Active' OR 
    (
        s.start_date <= (d.month_date + INTERVAL '1 month - 1 day')
        AND (s.end_date IS NULL OR s.end_date >= d.month_date)
        AND ts.status NOT IN ('Canceled by Customer', 'Canceled due to Default', 'Completed')
    )
GROUP BY 
    d.month_date
ORDER BY 
    d.month_date;
```


**Interpreting the Results**:
- `active_subscriptions`: Number of active subscriptions on the last day of the month
- `total_mrr`: Total monthly recurring revenue
- `average_mrr_per_subscriber`: Average amount paid per subscriber monthly


**Optimization**:
- This query is complex and can be heavy; consider materializing it in a metrics table
- Indexes on `subscriptions.start_date`, `subscriptions.end_date`, and `subscriptions.status_id` are essential
- The time series generation ensures that months without subscriptions also appear in the result


**Additional Notes**:
- Normalizing different periodicities (annual, semiannual, etc.) to a monthly basis is essential for correct MRR calculation
- For companies with multiple currencies, consider implementing conversion to a standard currency


(Ref: Analytics Examples, ID analytics_examples_001)


### New Sales Growth vs. Recurring Revenue


**Purpose**: Analyze revenue composition between new sales (one-time transactions) and recurring subscription revenue to understand the growth of each business model.


```sql
-- Revenue comparison: One-time sales vs. Recurring revenue
WITH monthly_revenue AS (
    SELECT 
        DATE_TRUNC('month', t.order_date) AS month,
        SUM(CASE WHEN t.is_subscription = false THEN t.offer_price ELSE 0 END) AS one_time_revenue,
        SUM(CASE 
                WHEN t.is_subscription = true AND t.recurrence_number = 1 THEN t.offer_price
                ELSE 0
            END) AS new_subscription_revenue,
        SUM(CASE 
                WHEN t.is_subscription = true AND t.recurrence_number > 1 THEN t.offer_price
                ELSE 0
            END) AS recurring_revenue
    FROM 
        transactions t
    JOIN 
        transaction_statuses ts ON t.status_id = ts.id
    WHERE 
        ts.status = 'Approved'
        AND t.order_date BETWEEN '2023-01-01' AND '2023-11-30'
    GROUP BY 
        DATE_TRUNC('month', t.order_date)
)
SELECT 
    month,
    one_time_revenue,
    new_subscription_revenue,
    recurring_revenue,
    (one_time_revenue + new_subscription_revenue + recurring_revenue) AS total_revenue,
    ROUND((one_time_revenue * 100.0) / 
        NULLIF((one_time_revenue + new_subscription_revenue + recurring_revenue), 0), 1) AS one_time_pct,
    ROUND((new_subscription_revenue * 100.0) / 
        NULLIF((one_time_revenue + new_subscription_revenue + recurring_revenue), 0), 1) AS new_subs_pct,
    ROUND((recurring_revenue * 100.0) / 
        NULLIF((one_time_revenue + new_subscription_revenue + recurring_revenue), 0), 1) AS recurring_pct,
    -- Month-over-Month (MoM) growth calculation
    ROUND(
        ((one_time_revenue + new_subscription_revenue + recurring_revenue) - 
        LAG(one_time_revenue + new_subscription_revenue + recurring_revenue) OVER (ORDER BY month)) * 100.0 / 
        NULLIF(LAG(one_time_revenue + new_subscription_revenue + recurring_revenue) OVER (ORDER BY month), 0),
        1
    ) AS total_revenue_growth_pct
FROM 
    monthly_revenue
ORDER BY 
    month;
```


**Interpreting the Results**:
- `one_time_revenue`: Revenue from one-time sales (non-subscription)
- `new_subscription_revenue`: Revenue from first subscription charges
- `recurring_revenue`: Revenue from recurring charges (second and beyond)
- `total_revenue_growth_pct`: Percentage growth compared to the previous month


**Optimization**:
- This query requires analyzing large volumes of data; consider optimizing with appropriate indexes
- Percentage calculations can be moved to the application if performance is critical


**Expected Insights**:
- As the business matures, the proportion of recurring revenue typically increases
- Reductions in new sales revenue can be offset by recurring revenue growth
- Seasonal variations typically affect new sales more than recurring revenue


(Ref: Analytics Examples, ID analytics_examples_001)


## Subscription and Engagement Metrics


### Churn and Retention Rate of Subscribers


**Purpose**: Calculate monthly subscriber churn (cancellation) and retention rates, critical metrics for subscription-based businesses.


```sql
-- Subscriber churn and retention rate by month
WITH monthly_dates AS (
    -- Generate sequence of monthly dates for analysis
    SELECT generate_series(
        DATE_TRUNC('month', '2023-01-01'::date),
        DATE_TRUNC('month', '2023-10-01'::date),
        '1 month'::interval
    ) AS month_start,
    generate_series(
        DATE_TRUNC('month', '2023-01-01'::date) + INTERVAL '1 month - 1 day',
        DATE_TRUNC('month', '2023-10-01'::date) + INTERVAL '1 month - 1 day',
        '1 month'::interval
    ) AS month_end
),
monthly_metrics AS (
    -- Calculate monthly subscriber metrics
    SELECT 
        d.month_start,
        d.month_end,
        COUNT(DISTINCT CASE 
            WHEN s.start_date < d.month_start 
                AND (s.end_date IS NULL OR s.end_date > d.month_end) 
            THEN s.id 
        END) AS active_start,
        COUNT(DISTINCT CASE 
            WHEN s.start_date BETWEEN d.month_start AND d.month_end 
            THEN s.id 
        END) AS new_subscribers,
        COUNT(DISTINCT CASE 
            WHEN s.end_date BETWEEN d.month_start AND d.month_end
                AND ts.status IN ('Canceled by Customer', 'Canceled due to Default')
            THEN s.id 
        END) AS churned_subscribers,
        COUNT(DISTINCT CASE 
            WHEN s.start_date < d.month_start 
                AND (s.end_date IS NULL OR s.end_date > d.month_end) 
            THEN s.id 
        END) + 
        COUNT(DISTINCT CASE 
            WHEN s.start_date BETWEEN d.month_start AND d.month_end 
            THEN s.id 
        END) -
        COUNT(DISTINCT CASE 
            WHEN s.end_date BETWEEN d.month_start AND d.month_end
                AND ts.status IN ('Canceled by Customer', 'Canceled due to Default')
            THEN s.id 
        END) AS active_end
    FROM 
        monthly_dates d
    LEFT JOIN 
        subscriptions s ON 
            s.start_date <= d.month_end AND
            (s.end_date IS NULL OR s.end_date >= d.month_start)
    LEFT JOIN 
        transaction_statuses ts ON s.status_id = ts.id
    GROUP BY 
        d.month_start, d.month_end
)
SELECT 
    TO_CHAR(month_start, 'YYYY-MM') AS month,
    active_start,
    new_subscribers,
    churned_subscribers,
    active_end,
    ROUND((churned_subscribers * 100.0) / NULLIF(active_start, 0), 2) AS churn_rate_pct,
    ROUND(((active_start - churned_subscribers) * 100.0) / NULLIF(active_start, 0), 2) AS retention_rate_pct,
    ROUND(((active_end - active_start) * 100.0) / NULLIF(active_start, 0), 2) AS net_growth_pct
FROM 
    monthly_metrics
ORDER BY 
    month_start;
```


**Interpreting the Results**:
- `active_start`: Subscribers active at the beginning of the month
- `new_subscribers`: New subscribers during the month
- `churned_subscribers`: Subscribers who canceled during the month
- `active_end`: Subscribers active at the end of the month
- `churn_rate_pct`: Percentage of subscribers who canceled relative to those active at the beginning
- `retention_rate_pct`: Percentage of subscribers who remained active
- `net_growth_pct`: Net growth of the subscriber base


**Optimization**:
- This query is computationally intensive; consider creating indexes on `subscriptions.start_date` and `subscriptions.end_date`
- For very large bases, a materialized implementation may be necessary


**Expected Insights**:
- A healthy churn rate is typically below 5% monthly for B2C and 2% for B2B
- Churn rate spikes may signal product issues or market changes
- Net growth should be positive to sustain the business long-term


(Ref: Analytics Examples, ID analytics_examples_001)


### Cohort Analysis for Subscribers


**Purpose**: Evaluate customer retention over time by grouping them by "cohort" (starting month), allowing analysis of retention patterns for different customer groups.


```sql
-- Cohort analysis for subscriber retention
WITH cohort_base AS (
    -- Identify the cohort (starting month) for each subscription
    SELECT 
        s.id AS subscription_id,
        DATE_TRUNC('month', s.start_date) AS cohort_month,
        s.start_date,
        s.end_date,
        s.status_id
    FROM 
        subscriptions s
    WHERE 
        s.start_date >= '2023-01-01'
        AND s.start_date < '2023-11-01'
),
cohort_sizes AS (
    -- Calculate the size of each cohort
    SELECT 
        cohort_month,
        COUNT(*) AS cohort_size
    FROM 
        cohort_base
    GROUP BY 
        cohort_month
),
retention_data AS (
    -- For each cohort and month, calculate how many subscriptions were still active
    SELECT 
        cb.cohort_month,
        DATE_TRUNC('month', GENERATE_SERIES(
            cb.cohort_month, 
            '2023-11-01'::date - INTERVAL '1 day', 
            '1 month'::interval
        )) AS activity_month,
        COUNT(DISTINCT CASE 
            WHEN cb.end_date IS NULL OR 
                 cb.end_date >= (DATE_TRUNC('month', GENERATE_SERIES) + INTERVAL '1 month - 1 day')
            THEN cb.subscription_id
        END) AS active_subscribers
    FROM 
        cohort_base cb
    CROSS JOIN 
        GENERATE_SERIES(
            cb.cohort_month, 
            '2023-11-01'::date - INTERVAL '1 day', 
            '1 month'::interval
        )
    GROUP BY 
        cb.cohort_month, activity_month
),
cohort_retention AS (
    -- Calculate retention percentages for each cohort and month
    SELECT 
        rd.cohort_month,
        TO_CHAR(rd.cohort_month, 'YYYY-MM') AS cohort_name,
        rd.activity_month,
        (rd.activity_month - rd.cohort_month) / '1 month'::interval AS months_since_start,
        rd.active_subscribers,
        cs.cohort_size,
        ROUND((rd.active_subscribers * 100.0) / NULLIF(cs.cohort_size, 0), 1) AS retention_rate_pct
    FROM 
        retention_data rd
    JOIN 
        cohort_sizes cs ON rd.cohort_month = cs.cohort_month
)
-- Format as a retention matrix (pivoted for better visualization)
SELECT 
    cohort_name,
    cohort_size,
    MAX(CASE WHEN months_since_start = 0 THEN retention_rate_pct END) AS "M0",
    MAX(CASE WHEN months_since_start = 1 THEN retention_rate_pct END) AS "M1",
    MAX(CASE WHEN months_since_start = 2 THEN retention_rate_pct END) AS "M2",
    MAX(CASE WHEN months_since_start = 3 THEN retention_rate_pct END) AS "M3",
    MAX(CASE WHEN months_since_start = 4 THEN retention_rate_pct END) AS "M4",
    MAX(CASE WHEN months_since_start = 5 THEN retention_rate_pct END) AS "M5",
    MAX(CASE WHEN months_since_start = 6 THEN retention_rate_pct END) AS "M6",
    MAX(CASE WHEN months_since_start = 7 THEN retention_rate_pct END) AS "M7",
    MAX(CASE WHEN months_since_start = 8 THEN retention_rate_pct END) AS "M8",
    MAX(CASE WHEN months_since_start = 9 THEN retention_rate_pct END) AS "M9",
    MAX(CASE WHEN months_since_start = 10 THEN retention_rate_pct END) AS "M10",
    MAX(CASE WHEN months_since_start = 11 THEN retention_rate_pct END) AS "M11"
FROM 
    cohort_retention
GROUP BY 
    cohort_name, cohort_size, cohort_month
ORDER BY 
    cohort_month;
```


**Interpreting the Results**:
- Each row represents a cohort (group of subscribers who started in the same month)
- Columns M0, M1, M2, etc. represent the months since subscription start
- Values are the percentage of subscribers who remained active in that month
- M0 is typically 100% (all subscribers active in the starting month)


**Optimization**:
- This query requires intensive time series generation; consider caching mechanisms
- The pivoted format is ideal for visualization, but it may be more efficient to store data without pivoting


**Expected Insights**:
- Consistent drop patterns (e.g., large drop after the first month) may indicate onboarding problems
- Retention improvements over time (comparing cohorts) indicate product improvements
- Retention curves that stabilize after a few months indicate a core of loyal users


(Ref: Analytics Examples, ID analytics_examples_001)


### Customer Lifetime Value (LTV) by Product


**Purpose**: Calculate the total value a customer generates during their lifecycle with the company, helping to guide marketing and customer acquisition decisions.


```sql
-- LTV (Lifetime Value) per customer, segmented by product
WITH customer_product_transactions AS (
    -- Aggregate transactions by customer and product
    SELECT 
        c.id AS customer_id,
        c.email,
        p.id AS product_id,
        p.name AS product_name,
        MIN(t.order_date) AS first_purchase_date,
        MAX(t.order_date) AS last_purchase_date,
        COUNT(*) AS purchase_count,
        SUM(CASE WHEN ts.status = 'Approved' THEN t.offer_price ELSE 0 END) AS total_spent,
        SUM(CASE WHEN ts.status = 'Refunded' THEN t.offer_price ELSE 0 END) AS total_refunded,
        EXTRACT(EPOCH FROM (MAX(t.order_date) - MIN(t.order_date))) / 86400 AS days_as_customer
    FROM 
        customers c
    JOIN 
        transactions t ON c.id = t.customer_id
    JOIN 
        transaction_items ti ON t.id = ti.transaction_id
    JOIN 
        products p ON ti.product_id = p.id
    JOIN 
        transaction_statuses ts ON t.status_id = ts.id
    WHERE 
        ts.status IN ('Approved', 'Refunded')
        AND t.order_date >= '2022-01-01'
    GROUP BY 
        c.id, c.email, p.id, p.name
),
product_customer_metrics AS (
    -- Calculate metrics by product
    SELECT 
        product_id,
        product_name,
        COUNT(DISTINCT customer_id) AS total_customers,
        AVG(total_spent - total_refunded) AS average_customer_value,
        AVG(purchase_count) AS average_purchases_per_customer,
        AVG(CASE WHEN days_as_customer > 0 THEN (total_spent - total_refunded) / days_as_customer * 365 ELSE 0 END) AS annual_ltv
    FROM 
        customer_product_transactions
    GROUP BY 
        product_id, product_name
),
customer_ltv_bands AS (
    -- Classify customers into value bands
    SELECT 
        cpt.product_id,
        cpt.product_name,
        SUM(CASE WHEN (cpt.total_spent - cpt.total_refunded) < 100 THEN 1 ELSE 0 END) AS customers_under_100,
        SUM(CASE WHEN (cpt.total_spent - cpt.total_refunded) BETWEEN 100 AND 499.99 THEN 1 ELSE 0 END) AS customers_100_499,
        SUM(CASE WHEN (cpt.total_spent - cpt.total_refunded) BETWEEN 500 AND 999.99 THEN 1 ELSE 0 END) AS customers_500_999,
        SUM(CASE WHEN (cpt.total_spent - cpt.total_refunded) >= 1000 THEN 1 ELSE 0 END) AS customers_1000_plus
    FROM 
        customer_product_transactions cpt
    GROUP BY 
        cpt.product_id, cpt.product_name
)
SELECT 
    m.product_name,
    m.total_customers,
    ROUND(m.average_customer_value, 2) AS avg_customer_value,
    ROUND(m.average_purchases_per_customer, 1) AS avg_purchases,
    ROUND(m.annual_ltv, 2) AS annual_ltv,
    b.customers_under_100,
    b.customers_100_499,
    b.customers_500_999,
    b.customers_1000_plus,
    ROUND((b.customers_under_100 * 100.0) / NULLIF(m.total_customers, 0), 1) AS pct_under_100,
    ROUND((b.customers_100_499 * 100.0) / NULLIF(m.total_customers, 0), 1) AS pct_100_499,
    ROUND((b.customers_500_999 * 100.0) / NULLIF(m.total_customers, 0), 1) AS pct_500_999,
    ROUND((b.customers_1000_plus * 100.0) / NULLIF(m.total_customers, 0), 1) AS pct_1000_plus
FROM 
    product_customer_metrics m
JOIN 
    customer_ltv_bands b ON m.product_id = b.product_id
ORDER BY 
    m.annual_ltv DESC;
```


**Interpreting the Results**:
- `avg_customer_value`: Average amount spent by customers throughout their lifecycle
- `avg_purchases`: Average number of purchases per customer
- `annual_ltv`: Annualized customer value projection (useful for comparison)
- Distribution in value bands (under_100, 100_499, etc.): Indicates customer concentration by value range


**Optimization**:
- This query is computation-intensive; consider materializing intermediate results
- Use CTEs (Common Table Expressions) to improve readability and maintenance


**Expected Insights**:
- Products with high LTV can justify higher customer acquisition investments
- Value band distribution helps identify segments for specific strategies
- When comparing LTV with Customer Acquisition Cost (CAC), you can assess the financial health of the business model


(Ref: Analytics Examples, ID analytics_examples_001)


## Commission and Partnership Metrics


### Affiliate Performance and Commissions


**Purpose**: Analyze affiliate performance, identifying the most productive affiliates and calculating key metrics such as conversion rate and average commission.


```sql
-- Affiliate performance in terms of sales and commissions
WITH affiliate_performance AS (
    SELECT 
        cp.id AS participant_id,
        cp.name AS affiliate_name,
        cp.email AS affiliate_email,
        COUNT(DISTINCT t.id) AS total_transactions,
        COUNT(DISTINCT t.customer_id) AS unique_customers,
        SUM(t.offer_price) AS total_sales_amount,
        SUM(pc.amount) AS total_commission,
        AVG(pc.amount) AS average_commission,
        MIN(t.order_date) AS first_sale_date,
        MAX(t.order_date) AS last_sale_date
    FROM 
        commission_participants cp
    JOIN 
        platform_commission pc ON cp.id = pc.participant_id
    JOIN 
        transactions t ON pc.transaction_id = t.id
    JOIN 
        transaction_statuses ts ON t.status_id = ts.id
    WHERE 
        pc.source = 'AFFILIATE'
        AND ts.status = 'Approved'
        AND t.order_date BETWEEN '2023-01-01' AND '2023-11-30'
    GROUP BY 
        cp.id, cp.name, cp.email
),
refund_data AS (
    -- Calculate refunds by affiliate
    SELECT 
        cp.id AS participant_id,
        COUNT(DISTINCT t.id) AS refunded_transactions,
        ABS(SUM(pc.amount)) AS refunded_commission_amount -- Considering refunds are recorded as negative values
    FROM 
        commission_participants cp
    JOIN 
        platform_commission pc ON cp.id = pc.participant_id
    JOIN 
        transactions t ON pc.transaction_id = t.id
    JOIN 
        transaction_statuses ts ON t.status_id = ts.id
    WHERE 
        pc.source LIKE '%REFUND%'
        AND t.order_date BETWEEN '2023-01-01' AND '2023-11-30'
    GROUP BY 
        cp.id
)
SELECT 
    ap.affiliate_name,
    ap.affiliate_email,
    ap.total_transactions,
    ap.unique_customers,
    ROUND(ap.total_sales_amount, 2) AS total_sales,
    ROUND(ap.total_commission, 2) AS total_commission,
    ROUND(ap.average_commission, 2) AS avg_commission,
    ROUND((ap.total_commission * 100.0) / NULLIF(ap.total_sales_amount, 0), 1) AS commission_rate_pct,
    COALESCE(rd.refunded_transactions, 0) AS refunded_transactions,
    ROUND(COALESCE((rd.refunded_transactions * 100.0) / NULLIF(ap.total_transactions, 0), 0), 1) AS refund_rate_pct,
    COALESCE(ROUND(rd.refunded_commission_amount, 2), 0) AS refunded_commission,
    TO_CHAR(CURRENT_DATE - ap.last_sale_date, 'DD "days"') AS days_since_last_sale,
    DENSE_RANK() OVER (ORDER BY ap.total_commission DESC) AS commission_rank
FROM 
    affiliate_performance ap
LEFT JOIN 
    refund_data rd ON ap.participant_id = rd.participant_id
ORDER BY 
    ap.total_commission DESC;
```


**Interpreting the Results**:
- `total_transactions`: Total number of sales made by the affiliate
- `unique_customers`: Number of unique customers brought by the affiliate
- `commission_rate_pct`: Average commission percentage on total sales value
- `refund_rate_pct`: Refund rate of affiliate sales (quality indicator)
- `days_since_last_sale`: Time since last sale (inactivity)


**Optimization**:
- Use indexes on `platform_commission.participant_id` and `platform_commission.source`
- Consider creating composite indexes to improve join performance


**Expected Insights**:
- Identification of high-performing affiliates for special programs
- Detection of affiliates with high refund rates (possible low-quality traffic)
- Inactive affiliates (high value in `days_since_last_sale`) who may need reactivation


(Ref: Analytics Examples, ID analytics_examples_001)


### Acquisition Channel Comparison


**Purpose**: Compare the effectiveness of different marketing and affiliate channels in generating sales, customer retention, and profitability.


```sql
-- Comparative performance of acquisition channels
WITH acquisition_channels AS (
    SELECT 
        CASE 
            WHEN t.tracking_source IS NULL OR t.tracking_source = '' THEN 'Direct/Unknown'
            WHEN t.tracking_source LIKE 'aff_%' THEN 'Affiliate'
            WHEN t.tracking_source LIKE 'fb_%' THEN 'Facebook'
            WHEN t.tracking_source LIKE 'ig_%' THEN 'Instagram'
            WHEN t.tracking_source LIKE 'gg_%' THEN 'Google'
            WHEN t.tracking_source LIKE 'yt_%' THEN 'YouTube'
            WHEN t.tracking_source LIKE 'em_%' THEN 'Email'
            ELSE 'Others'
        END AS channel,
        t.id AS transaction_id,
        t.customer_id,
        t.offer_price,
        t.platform_fee_amount,
        t.partner_commission_amount,
        t.producer_net_amount,
        t.is_subscription,
        t.order_date,
        ts.status
    FROM 
        transactions t
    JOIN 
        transaction_statuses ts ON t.status_id = ts.id
    WHERE 
        t.order_date BETWEEN '2023-01-01' AND '2023-11-30'
),
channel_metrics AS (
    SELECT 
        channel,
        COUNT(DISTINCT transaction_id) AS total_transactions,
        COUNT(DISTINCT customer_id) AS unique_customers,
        SUM(CASE WHEN status = 'Approved' THEN offer_price ELSE 0 END) AS total_revenue,
        SUM(CASE WHEN status = 'Refunded' THEN offer_price ELSE 0 END) AS refunded_amount,
        COUNT(CASE WHEN status = 'Refunded' THEN transaction_id END) AS refunded_count,
        SUM(CASE WHEN status = 'Approved' THEN producer_net_amount ELSE 0 END) AS net_revenue,
        COUNT(CASE WHEN is_subscription = true THEN transaction_id END) AS subscription_count,
        COUNT(CASE WHEN is_subscription = true THEN customer_id END) AS subscription_customers
    FROM 
        acquisition_channels
    GROUP BY 
        channel
),
channel_value_metrics AS (
    -- Calculate complementary metrics by channel
    SELECT 
        channel,
        total_transactions,
        unique_customers,
        ROUND(total_revenue, 2) AS total_revenue,
        ROUND(refunded_amount, 2) AS refunded_amount,
        refunded_count,
        ROUND((refunded_count * 100.0) / NULLIF(total_transactions, 0), 1) AS refund_rate_pct,
        ROUND(net_revenue, 2) AS net_revenue,
        ROUND((net_revenue * 100.0) / NULLIF(total_revenue, 0), 1) AS margin_pct,
        ROUND(total_revenue / NULLIF(unique_customers, 0), 2) AS revenue_per_customer,
        ROUND(total_revenue / NULLIF(total_transactions, 0), 2) AS average_order_value,
        subscription_count,
        subscription_customers,
        ROUND((subscription_customers * 100.0) / NULLIF(unique_customers, 0), 1) AS subscription_conversion_pct
    FROM 
        channel_metrics
)
SELECT *
FROM 
    channel_value_metrics
ORDER BY 
    total_revenue DESC;
```


**Interpreting the Results**:
- `refund_rate_pct`: Refund rate by channel (indicator of traffic quality)
- `margin_pct`: Percentage margin after deducting fees and commissions
- `revenue_per_customer`: Average value generated by customers from each channel
- `subscription_conversion_pct`: Percentage of customers converted to subscribers


**Optimization**:
- This analysis depends on good channel segmentation via `tracking_source`
- Consider expanding the CASE logic to capture specific channels relevant to your business


**Expected Insights**:
- Channels with higher customer value are candidates for more investment
- Channels with high refund rates may need better qualification
- Channels with high subscription conversion are ideal for recurring products


(Ref: Analytics Examples, ID analytics_examples_001)


## Optimization and Monitoring


### Index and Query Performance Monitoring


**Purpose**: Identify tables and queries that can benefit from optimization by analyzing index usage statistics and execution times.


```sql
-- Analysis of index usage and query times (requires appropriate permissions)
-- This query requires access to PostgreSQL system tables


-- 1. Least used indexes (candidates for removal)
SELECT 
    schemaname||'.'||relname AS table_name,
    indexrelname AS index_name,
    idx_scan AS index_scans,
    pg_size_pretty(pg_relation_size(idxoid)) AS index_size,
    indexdef AS index_definition
FROM 
    pg_stat_user_indexes
JOIN 
    pg_indexes ON pg_stat_user_indexes.indexrelname = pg_indexes.indexname
    AND pg_stat_user_indexes.schemaname = pg_indexes.schemaname
WHERE 
    schemaname NOT LIKE 'pg_%'
    AND idx_scan < 50  -- Few scans (adjust as needed)
    AND pg_relation_size(idxoid) > 1000000  -- Relatively large indexes (>1MB)
ORDER BY 
    idx_scan ASC, pg_relation_size(idxoid) DESC;


-- 2. Most accessed tables (candidates for optimization)
SELECT 
    schemaname||'.'||relname AS table_name,
    seq_scan,
    seq_tup_read,
    idx_scan,
    idx_tup_fetch,
    n_tup_ins AS inserts,
    n_tup_upd AS updates,
    n_tup_del AS deletes,
    n_live_tup AS live_rows,
    n_dead_tup AS dead_rows,
    ROUND((n_dead_tup * 100.0) / NULLIF(n_live_tup + n_dead_tup, 0), 2) AS dead_row_pct
FROM 
    pg_stat_user_tables
WHERE 
    schemaname NOT LIKE 'pg_%'
ORDER BY 
    coalesce(seq_scan, 0) + coalesce(idx_scan, 0) DESC
LIMIT 
    20;


-- 3. Slowest queries (candidates for optimization)
SELECT 
    substring(query, 1, 100) AS short_query,
    round(total_exec_time::numeric, 2) AS total_time_ms,
    calls,
    round(mean_exec_time::numeric, 2) AS mean_time_ms,
    round((100 * total_exec_time / sum(total_exec_time) OVER ()), 2) AS percentage_overall
FROM 
    pg_stat_statements
WHERE 
    query NOT LIKE '%pg_stat_statements%'
ORDER BY 
    total_exec_time DESC
LIMIT 
    20;
```


**Interpreting the Results**:


**1. Unused Indexes**:
- Indexes with few queries (`index_scans`) are candidates for removal
- Removing unused indexes can improve write performance and reduce disk space


**2. Highly Accessed Tables**:
- Tables with many `seq_scan` and few `idx_scan` may need additional indexes
- High percentage of `dead_rows` indicates need for more frequent VACUUM


**3. Slow Queries**:
- Queries with high `mean_time_ms` are candidates for optimization
- Frequent queries (`calls`) with moderate time are also priorities


**Optimization**:
- This query requires extensions like `pg_stat_statements` to be active
- Ideal for periodic execution and continuous monitoring


**Additional Notes**:
- After identifying slow queries, use `EXPLAIN ANALYZE` to deepen the analysis
- Optimization should balance reading and writing needs


(Ref: Analytics Examples, ID analytics_examples_001)


### Data Integrity Audit


**Purpose**: Check data integrity and consistency, identifying orphaned records, anomalous values, or inconsistencies between related tables.


```sql
-- Check data integrity and consistency


-- 1. Transactions without associated items
SELECT 
    t.id AS transaction_id,
    t.transaction_id AS external_id,
    t.order_date,
    ts.status
FROM 
    transactions t
LEFT JOIN 
    transaction_items ti ON t.id = ti.transaction_id
JOIN 
    transaction_statuses ts ON t.status_id = ts.id
WHERE 
    ti.id IS NULL
    AND ts.status = 'Approved'
ORDER BY 
    t.order_date DESC;


-- 2. Transactions marked as subscription but without subscription link
SELECT 
    t.id AS transaction_id,
    t.transaction_id AS external_id,
    t.order_date,
    ts.status
FROM 
    transactions t
JOIN 
    transaction_statuses ts ON t.status_id = ts.id
WHERE 
    t.is_subscription = true
    AND t.subscription_id IS NULL
    AND ts.status = 'Approved'
ORDER BY 
    t.order_date DESC;


-- 3. Commissions without valid participant
SELECT 
    pc.id AS commission_id,
    pc.transaction_id,
    pc.participant_id,
    pc.amount,
    pc.source,
    pc.created_at
FROM 
    platform_commission pc
LEFT JOIN 
    commission_participants cp ON pc.participant_id = cp.id
WHERE 
    cp.id IS NULL
ORDER BY 
    pc.created_at DESC;


-- 4. Subscriptions with date inconsistencies
SELECT 
    s.id AS subscription_id,
    s.subscription_id AS external_id,
    s.start_date,
    s.end_date,
    s.cancel_date,
    ts.status
FROM 
    subscriptions s
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
WHERE 
    (s.end_date IS NOT NULL AND s.end_date < s.start_date)
    OR (s.cancel_date IS NOT NULL AND s.end_date IS NULL)
    OR (ts.status IN ('Canceled by Customer', 'Canceled due to Default') AND s.cancel_date IS NULL)
    OR (ts.status = 'Active' AND s.end_date IS NOT NULL AND s.end_date < CURRENT_DATE)
ORDER BY 
    s.start_date DESC;


-- 5. Anomalous financial values (significant outliers)
WITH transaction_stats AS (
    SELECT 
        AVG(offer_price) AS avg_price,
        STDDEV(offer_price) AS stddev_price,
        AVG(platform_fee_amount) AS avg_fee,
        STDDEV(platform_fee_amount) AS stddev_fee
    FROM 
        transactions
    WHERE
        offer_price > 0
)
SELECT 
    t.id AS transaction_id,
    t.transaction_id AS external_id,
    t.offer_price,
    t.platform_fee_amount,
    t.partner_commission_amount,
    t.producer_net_amount,
    t.order_date,
    p.name AS product_name
FROM 
    transactions t
JOIN 
    transaction_items ti ON t.id = ti.transaction_id
JOIN 
    products p ON ti.product_id = p.id
CROSS JOIN 
    transaction_stats ts
WHERE 
    (t.offer_price > ts.avg_price + 3 * ts.stddev_price OR t.offer_price < ts.avg_price - 3 * ts.stddev_price)
    OR (t.platform_fee_amount > ts.avg_fee + 3 * ts.stddev_fee)
    OR (t.producer_net_amount < 0 AND t.offer_price > 0)
    OR (t.offer_price < t.platform_fee_amount + t.partner_commission_amount)
ORDER BY 
    t.order_date DESC;
```


**Interpreting the Results**:


**1. Transactions without Items**:
- May indicate issues in data synchronization or failures in the sales process
- Affect product analyses and can create inconsistencies in reports


**2. Subscription Transactions without Link**:
- Failure in the association between transaction and corresponding subscription
- Can affect MRR metrics and subscription lifecycle analyses


**3. Orphaned Commissions**:
- Commissions associated with non-existent participants, possibly due to improper deletions
- Risk of incorrect payments or lack of traceability


**4. Date Inconsistencies in Subscriptions**:
- Start dates later than end dates
- Canceled subscriptions without recorded cancellation date
- Active subscriptions with end date in the past


**5. Anomalous Financial Values**:
- Transactions with values much higher or lower than average (possible errors)
- Inconsistencies in financial math (negative net_amount, fees higher than total value)


**Optimization**:
- Run periodically as part of maintenance routines
- Consider creating triggers to prevent some inconsistencies


**Recommended Actions**:
- Correct identified inconsistent records
- Implement additional validations at application level
- Create automated verification routines


(Ref: Analytics Examples, ID analytics_examples_001)


## Queries for Specific Use Cases


### Customer Recovery Identification


**Purpose**: Identify subscribers who recently canceled or are at risk of cancellation, for retention or recovery actions.


```sql
-- Identification of customers for reactivation/recovery campaigns


-- 1. Subscribers who canceled in the last 30 days
SELECT 
    c.id AS customer_id,
    c.email,
    c.name,
    s.subscription_id AS external_subscription_id,
    p.name AS plan_name,
    pr.name AS product_name,
    s.cancel_date,
    s.start_date,
    EXTRACT(DAY FROM (s.cancel_date - s.start_date)) AS subscription_lifetime_days,
    ts.status AS current_status,
    ssh.reason AS cancellation_reason
FROM 
    customers c
JOIN 
    subscriptions s ON c.id = s.customer_id
JOIN 
    plans p ON s.plan_id = p.id
JOIN 
    products pr ON p.product_id = pr.id
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
LEFT JOIN 
    subscription_status_history ssh ON s.id = ssh.subscription_id
    AND ssh.status_id = s.status_id -- Get history entry corresponding to current status
WHERE 
    ts.status IN ('Canceled by Customer')
    AND s.cancel_date >= CURRENT_DATE - INTERVAL '30 days'
    -- Optional: filter by specific products/plans
    -- AND pr.name = 'Product XYZ'
ORDER BY 
    s.cancel_date DESC;


-- 2. Inactive subscribers (no login or no usage) but still paying
-- (Conceptual - would require integration with authentication/usage system)
/*
SELECT
    c.id AS customer_id,
    c.email,
    c.name,
    s.subscription_id AS external_subscription_id,
    p.name AS plan_name,
    pr.name AS product_name,
    s.start_date,
    -- Conceptual usage data
    last_login_date,
    EXTRACT(DAY FROM (CURRENT_DATE - last_login_date)) AS days_since_last_login,
    usage_count_last_30_days
FROM
    customers c
JOIN
    subscriptions s ON c.id = s.customer_id
JOIN
    plans p ON s.plan_id = p.id
JOIN
    products pr ON p.product_id = pr.id
JOIN
    transaction_statuses ts ON s.status_id = ts.id
LEFT JOIN
    customer_usage cu ON c.id = cu.customer_id -- Conceptual table
WHERE
    ts.status = 'Active'
    AND (
        last_login_date < CURRENT_DATE - INTERVAL '60 days'
        OR usage_count_last_30_days < 2
    )
ORDER BY
    last_login_date ASC;
*/


-- 3. Subscribers with failed last billing (defaulting)
SELECT 
    c.id AS customer_id,
    c.email,
    c.name,
    s.subscription_id AS external_subscription_id,
    p.name AS plan_name,
    s.next_billing_date,
    ts.status AS current_status,
    (SELECT MAX(ssh.change_date)
     FROM subscription_status_history ssh
     WHERE ssh.subscription_id = s.id
     AND ssh.status_id = (SELECT id FROM transaction_statuses WHERE status = 'Defaulting')) AS last_default_date,
    COUNT(DISTINCT t.id) AS total_payments_history,
    (SELECT COUNT(*)
     FROM transactions t2
     WHERE t2.subscription_id = s.id
     AND t2.status_id = (SELECT id FROM transaction_statuses WHERE status = 'Approved')) AS successful_payments
FROM 
    customers c
JOIN 
    subscriptions s ON c.id = s.customer_id
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
JOIN 
    plans p ON s.plan_id = p.id
LEFT JOIN 
    transactions t ON s.id = t.subscription_id
WHERE 
    ts.status = 'Defaulting'
    AND s.next_billing_date < CURRENT_DATE
GROUP BY 
    c.id, c.email, c.name, s.subscription_id, p.name, s.next_billing_date, ts.status, s.id
ORDER BY 
    s.next_billing_date;
```


**Interpreting the Results**:


**1. Recently Canceled Subscribers**:
- Ideal candidates for reactivation campaigns
- The cancellation reason (`cancellation_reason`) is crucial for personalizing the approach
- Subscription lifetime (`subscription_lifetime_days`) can indicate whether there was perceived value


**2. Inactive Subscribers** (conceptual query):
- Customers who pay but don't use the product are at high risk of cancellation
- Can be targeted for educational or re-engagement campaigns


**3. Defaulting Subscribers**:
- Payment failures that may be due to technical issues or expired cards
- The ratio between `successful_payments` and `total_payments_history` indicates payment history quality
- Customers with good history deserve more recovery attempts


**Optimization**:
- Queries can be computationally intensive due to multiple joins
- Consider adjusting time periods according to company retention policy


**Recommended Actions**:
- Segment communication based on cancellation/default reason
- Prioritize customers with longer lifetime or higher historical spending
- Offer personalized incentives for reactivation (discounts, extra benefits)


(Ref: Analytics Examples, ID analytics_examples_001)


### Future Revenue Forecast


**Purpose**: Project future revenue based on active subscriptions and historical patterns, helping with financial planning and growth projections.


```sql
-- Future revenue projection based on existing subscriptions


-- 1. MRR projection for the next 6 months based on active subscriptions
WITH RECURSIVE future_months AS (
    SELECT
        CURRENT_DATE AS month_date
    UNION ALL
    SELECT
        (month_date + INTERVAL '1 month')::date
    FROM
        future_months
    WHERE
        month_date < CURRENT_DATE + INTERVAL '6 months'
),
normalized_mrr AS (
    -- Normalize recurring value per subscription
    SELECT
        s.id AS subscription_id,
        p.price AS base_price,
        CASE
            WHEN p.recurrence_period = 'YEAR' THEN p.price / 12
            WHEN p.recurrence_period = 'QUARTER' THEN p.price / 3
            WHEN p.recurrence_period = 'SEMIANNUAL' THEN p.price / 6
            WHEN p.recurrence_period = 'WEEK' THEN p.price * 4.33
            ELSE p.price
        END AS monthly_recurring_revenue,
        s.start_date,
        s.end_date,
        -- If max_cycles is NULL or 0, we consider it infinite
        CASE
            WHEN s.max_cycles IS NULL OR s.max_cycles = 0 THEN NULL
            ELSE s.start_date + (s.max_cycles * 
                CASE
                    WHEN p.recurrence_period = 'YEAR' THEN INTERVAL '1 year'
                    WHEN p.recurrence_period = 'QUARTER' THEN INTERVAL '3 months'
                    WHEN p.recurrence_period = 'SEMIANNUAL' THEN INTERVAL '6 months'
                    WHEN p.recurrence_period = 'WEEK' THEN INTERVAL '7 days'
                    ELSE INTERVAL '1 month'
                END)
        END AS max_end_date
    FROM
        subscriptions s
    JOIN
        plans p ON s.plan_id = p.id
    JOIN
        transaction_statuses ts ON s.status_id = ts.id
    WHERE
        ts.status = 'Active'
        AND p.currency_code = 'BRL' -- Filter by currency for consistency
)
SELECT
    DATE_TRUNC('month', fm.month_date)::date AS projection_month,
    COUNT(DISTINCT nm.subscription_id) AS projected_active_subscriptions,
    ROUND(SUM(nm.monthly_recurring_revenue), 2) AS projected_mrr,
    ROUND(SUM(nm.monthly_recurring_revenue) * 12, 2) AS projected_arr
FROM
    future_months fm
LEFT JOIN
    normalized_mrr nm ON
        DATE_TRUNC('month', fm.month_date) >= DATE_TRUNC('month', nm.start_date)
        AND (
            nm.end_date IS NULL
            OR DATE_TRUNC('month', fm.month_date) <= DATE_TRUNC('month', nm.end_date)
        )
        AND (
            nm.max_end_date IS NULL
            OR DATE_TRUNC('month', fm.month_date) <= DATE_TRUNC('month', nm.max_end_date)
        )
GROUP BY
    DATE_TRUNC('month', fm.month_date)
ORDER BY
    projection_month;


-- 2. More sophisticated projection considering historical churn and growth
WITH historical_churn AS (
    -- Calculate average churn rate for the last 3 months
    WITH monthly_metrics AS (
        SELECT 
            DATE_TRUNC('month', date_series)::date AS month_start,
            (DATE_TRUNC('month', date_series) + INTERVAL '1 month - 1 day')::date AS month_end,
            COUNT(DISTINCT CASE 
                WHEN s.start_date < DATE_TRUNC('month', date_series)
                    AND (s.end_date IS NULL OR s.end_date > (DATE_TRUNC('month', date_series) + INTERVAL '1 month - 1 day'))
                THEN s.id 
            END) AS active_start,
            COUNT(DISTINCT CASE 
                WHEN s.end_date BETWEEN DATE_TRUNC('month', date_series) AND (DATE_TRUNC('month', date_series) + INTERVAL '1 month - 1 day')
                    AND ts.status IN ('Canceled by Customer', 'Canceled due to Default')
                THEN s.id 
            END) AS churned_subscribers
        FROM 
            GENERATE_SERIES(
                (CURRENT_DATE - INTERVAL '3 months')::date,
                CURRENT_DATE,
                '1 month'::interval
            ) AS date_series
        LEFT JOIN 
            subscriptions s ON true
        LEFT JOIN 
            transaction_statuses ts ON s.status_id = ts.id
        GROUP BY 
            DATE_TRUNC('month', date_series)
    )
    SELECT 
        AVG(CASE WHEN active_start > 0 THEN churned_subscribers::decimal / active_start ELSE 0 END) AS avg_monthly_churn_rate
    FROM 
        monthly_metrics
),
new_subscription_growth AS (
    -- Analyze average growth of new subscriptions over the last 3 months
    SELECT
        AVG(new_subs) AS avg_monthly_new_subscriptions
    FROM (
        SELECT
            DATE_TRUNC('month', s.start_date)::date AS month,
            COUNT(*) AS new_subs
        FROM
            subscriptions s
        WHERE
            s.start_date >= CURRENT_DATE - INTERVAL '3 months'
        GROUP BY
            DATE_TRUNC('month', s.start_date)
    ) AS monthly_new_subs
),
current_active_subscriptions AS (
    -- Get currently active subscriptions and their MRR
    SELECT
        COUNT(*) AS active_count,
        SUM(
            CASE
                WHEN p.recurrence_period = 'YEAR' THEN p.price / 12
                WHEN p.recurrence_period = 'QUARTER' THEN p.price / 3
                WHEN p.recurrence_period = 'SEMIANNUAL' THEN p.price / 6
                WHEN p.recurrence_period = 'WEEK' THEN p.price * 4.33
                ELSE p.price
            END
        ) AS total_current_mrr,
        AVG(
            CASE
                WHEN p.recurrence_period = 'YEAR' THEN p.price / 12
                WHEN p.recurrence_period = 'QUARTER' THEN p.price / 3
                WHEN p.recurrence_period = 'SEMIANNUAL' THEN p.price / 6
                WHEN p.recurrence_period = 'WEEK' THEN p.price * 4.33
                ELSE p.price
            END
        ) AS avg_subscription_mrr
    FROM
        subscriptions s
    JOIN
        plans p ON s.plan_id = p.id
    JOIN
        transaction_statuses ts ON s.status_id = ts.id
    WHERE
        ts.status = 'Active'
        AND p.currency_code = 'BRL'
),
projection_data AS (
    SELECT
        hc.avg_monthly_churn_rate,
        nsg.avg_monthly_new_subscriptions,
        cas.active_count,
        cas.total_current_mrr,
        cas.avg_subscription_mrr
    FROM
        historical_churn hc,
        new_subscription_growth nsg,
        current_active_subscriptions cas
),
projected_growth AS (
    -- Month-by-month projection for the next 12 months
    SELECT
        0 AS month_number,
        CURRENT_DATE AS month_date,
        pd.active_count AS projected_subscribers,
        pd.total_current_mrr AS projected_mrr
    FROM
        projection_data pd
    
    UNION ALL
    
    SELECT
        pg.month_number + 1 AS month_number,
        (pg.month_date + INTERVAL '1 month')::date AS month_date,
        -- Formula: Current Subscribers - Churn + New Subscribers
        ROUND(pg.projected_subscribers * (1 - pd.avg_monthly_churn_rate) + pd.avg_monthly_new_subscriptions) AS projected_subscribers,
        ROUND((pg.projected_subscribers * (1 - pd.avg_monthly_churn_rate) + pd.avg_monthly_new_subscriptions) * pd.avg_subscription_mrr, 2) AS projected_mrr
    FROM
        projected_growth pg,
        projection_data pd
    WHERE
        pg.month_number < 12  -- Project 12 months ahead
)
SELECT
    month_number,
    TO_CHAR(month_date, 'YYYY-MM') AS month,
    projected_subscribers,
    projected_mrr,
    projected_mrr * 12 AS projected_arr,
    CASE
        WHEN month_number > 0 THEN
            ROUND(((projected_mrr - LAG(projected_mrr) OVER (ORDER BY month_number)) * 100.0 / 
                  NULLIF(LAG(projected_mrr) OVER (ORDER BY month_number), 0)), 1)
        ELSE NULL
    END AS mrr_growth_pct
FROM
    projected_growth
ORDER BY
    month_number;
```


**Interpreting the Results**:


**1. MRR Projection Based on Active Subscriptions**:
- This projection considers only existing subscriptions and their expected duration
- Useful for estimating "committed MRR" without additional growth


**2. Projection with Churn and Growth**:
- More realistic, incorporates historical churn rates and new subscriber acquisition
- Shows both month-over-month growth and year-over-year growth
- `projected_arr` (Annual Recurring Revenue) is the annualized MRR (× 12)


**Optimization**:
- Recursive time series generation can be heavy; consider materializing results
- Adjust projection horizon as needed (currently 6 months for projection 1 and 12 months for projection 2)


**Additional Considerations**:
- These projections don't consider potential price changes or new product launches
- For more sophisticated models, consider including seasonality and business-specific events
- In larger companies, project by product segments or acquisition channels separately


(Ref: Analytics Examples, ID analytics_examples_001)


## Conclusion


The SQL queries presented in this document provide a comprehensive foundation for data analysis and metrics extraction from the `joaocastanheira_bancodedados` database. They cover critical business aspects, from revenue and sales to customer retention, affiliate performance, and technical optimization.


### Practical Applications


These queries can be used to:
- Build real-time monitoring dashboards
- Generate periodic reports for stakeholders
- Feed prediction and planning models
- Identify growth opportunities and improvement areas
- Direct marketing and product development investments


### Recommendations for Efficient Use


1. **Performance Optimization**:
   - For frequent queries, consider creating materialized views or aggregation tables
   - Monitor the execution plan (EXPLAIN ANALYZE) to identify bottlenecks
   - Use appropriate indexes to improve performance


2. **Automation and Scheduling**:
   - Configure automatic execution of critical queries at regular intervals
   - Store historical results for trend analysis
   - Implement alerts for metrics that fall below acceptable thresholds


3. **Adaptation to Specific Needs**:
   - Modify date ranges in queries as needed
   - Adjust filters and groupings to focus on specific segments
   - Combine queries to create more complex analyses and deeper insights


4. **Visualization and Communication**:
   - Export results to visualization tools like Tableau, Power BI, or Metabase
   - Create presentations for different audiences (executives, technical team, marketing)
   - Establish clear KPIs based on extracted metrics


(Ref: Analytics Examples, ID analytics_examples_001)
```