# `System_Known_Patterns.md` 
```markdown
---
title: "Known Patterns and Canonical Responses: Hotmart-Kiwify Database"
id: "system_known_patterns_001"
doc_type: "meta_learning"
doc_version: "1.0"
date_created: "2025-04-23"
date_updated: "2025-04-23"
author: "Documentation Team"
db_name: "joaocastanheira_bancodedados"
db_version: "1.0"
doc_status: "Active"
environment: "All"
language: "en"
response_languages: ["pt-BR", "en"]
technical_terms_preservation: "strict"
original_language: "pt-BR"
related_docs: ["core_db_architecture_001", "core_db_design_principles_001", "core_db_glossary_001", "system_learning_evolution_001"]
tables_in_focus: ["transactions", "subscriptions", "customers", "plans", "platform_commission", "transaction_status_history", "subscription_status_history"]
technical_terms: {
  "table_names": [
    "transactions", "subscriptions", "customers", "plans", "platform_commission",
    "transaction_status_history", "subscription_status_history", "transaction_items",
    "products", "transaction_statuses", "commission_participants"
  ],
  "column_names": [
    "id", "transaction_id", "customer_id", "subscription_id", "order_date", 
    "is_subscription", "offer_price", "status_id", "payment_method", "recurrence_number",
    "start_date", "end_date", "cancel_date", "next_billing_date", "name", "email",
    "phone_local_code", "phone_number", "created_at", "updated_at", "price",
    "currency_code", "recurrence_period", "trial_days", "change_date", "reason",
    "amount", "source", "participant_id", "payment_date", "plan_id", "product_id", "status"
  ],
  "transaction_statuses": [
    "Aprovada", "Approved", "Reembolsada", "Refunded", "Chargeback Confirmado", 
    "Confirmed Chargeback", "Cancelada pelo Cliente", "Canceled by Customer", 
    "Cancelada por Inadimplência", "Canceled due to Delinquency", 
    "Cancelada pela Plataforma", "Canceled by Platform", "Pendente", "Pending",
    "Recusada", "Refused", "Concluída", "Completed", "Inadimplente", "Delinquent",
    "Ativa", "Active", "Trial"
  ],
  "data_types": [
    "DATE", "TIMESTAMP", "NUMERIC", "VARCHAR", "BOOLEAN", "INTERVAL",
    "INTEGER", "TEXT", "SERIAL", "TIMESTAMP WITH TIME ZONE", "JSONB",
    "DATE_TRUNC", "EXTRACT", "AGE"
  ],
  "sql_keywords": [
    "SELECT", "FROM", "WHERE", "JOIN", "LEFT JOIN", "CROSS JOIN", "GROUP BY", 
    "ORDER BY", "LIMIT", "UNION ALL", "CASE", "WHEN", "THEN", "ELSE", "END",
    "COUNT", "SUM", "AVG", "MIN", "MAX", "ROUND", "COALESCE", "NULLIF",
    "WITH", "AS", "EXTRACT", "BETWEEN", "IN", "EXISTS", "NOT EXISTS", "IS NULL",
    "AND", "OR", "NOT", "LIKE", "DATE_TRUNC", "INTERVAL", "GENERATE_SERIES",
    "ROW_NUMBER", "OVER", "PARTITION BY", "DISTINCT", "TO_CHAR", "POWER"
  ],
  "payment_platforms": [
    "Hotmart", "Kiwify"
  ],
  "payment_methods": [
    "credit_card", "boleto", "pix"
  ],
  "recurrence_periods": [
    "MONTH", "YEAR", "QUARTER", "SEMIANNUAL", "WEEK", "ONE_TIME"
  ],
  "commission_types": [
    "AFFILIATE", "PRODUCER", "COPRODUCER", "AFFILIATE_REFUND", "PRODUCER_REFUND", 
    "COPRODUCER_REFUND", "REFUND_"
  ],
  "metrics": [
    "MRR", "Monthly Recurring Revenue", "churn", "ARR", "Annual Recurring Revenue",
    "New MRR", "Expansion MRR", "Contraction MRR", "Churned MRR", "Net New MRR"
  ],
  "programming_terms": [
    "ORM", "Object-Relational Mapping", "CRUD", "API", "webhook", "SQL", "CTE",
    "idempotency", "atomicity", "log", "pseudocode"
  ]
}
embedding_guide_concepts: [
  "query patterns", "frequently asked questions", "canonical response", "common workflows", 
  "recurring use cases", "best practices", "troubleshooting", "problem solving", 
  "FAQ", "typical scenarios", "complex questions", "standardized response", 
  "quick reference guide", "response templates", "standardized explanations", 
  "anti-patterns", "malformed questions", "common errors", "misconceptions", 
  "supplementary information", "additional context", "response refinement", 
  "canonical examples", "standard processes", "business flows"
]
---


# Known Patterns and Canonical Responses: Hotmart-Kiwify Database


## Overview


This document records recurring query patterns and their canonical responses for the RAG system of the `joaocastanheira_bancodedados` database. It serves as a knowledge repository of crystallized knowledge about the most common use cases, frequently asked questions, and best practices that emerge from system usage.


Unlike a simple FAQ, this document:
1. Captures the **complete context** needed to answer the most frequent questions
2. Provides **standardized and reviewed responses** that can be used as references
3. Documents **typical workflows** that involve multiple operations or queries
4. Identifies **anti-patterns and misconceptions** common among users
5. Continuously evolves as new patterns are identified


The canonical responses recorded here reflect not only the correct technical knowledge but also the most effective way to communicate this knowledge to users.


(Ref: System Known Patterns, ID system_known_patterns_001)


## Frequently Asked Questions and Canonical Responses


### Transaction Management


#### "How do I identify if a transaction is part of a recurring subscription?"


**Canonical Response:**


To identify if a transaction is associated with a subscription, you can check two fields in the `transactions` table:


1. The `is_subscription` field which will be `TRUE` for subscription transactions
2. The `subscription_id` field which contains the reference to the associated subscription


A subscription transaction will also have the `recurrence_number` field, indicating which charge of the subscription it represents (1 for the first, 2 for the second, etc.).


**SQL Example for Identification:**


```sql
SELECT 
    t.id,
    t.transaction_id AS external_id,
    t.is_subscription,
    t.subscription_id,
    t.recurrence_number,
    t.order_date,
    s.subscription_id AS subscription_external_id,
    p.name AS plan_name
FROM 
    transactions t
LEFT JOIN 
    subscriptions s ON t.subscription_id = s.id
LEFT JOIN 
    plans p ON s.plan_id = p.id
WHERE 
    t.transaction_id = 'YOUR_TRANSACTION_ID_HERE'
    -- or: t.customer_id = (SELECT id FROM customers WHERE email = 'customer@example.com')
```


**Additional Notes:**
- The first transaction of a subscription will have `recurrence_number = 1`
- To query all transactions of a specific subscription, filter by `subscription_id`
- Transactions prior to a plan change will have the original `plan_id`, not the current one


(Ref: System Known Patterns, ID system_known_patterns_001)


#### "How do I track a refund or chargeback in the system?"


**Canonical Response:**


Refunds and chargebacks are recorded in three complementary ways in the system:


1. **Transaction Status:** The original transaction will have its `status_id` changed to the ID corresponding to 'Refunded' (for voluntary refunds) or 'Confirmed Chargeback' (for disputes contested by the customer).


2. **Status History:** A new record will be created in the `transaction_status_history` table documenting the change, including the date and reason.


3. **Commission Refunds:** When a transaction is refunded, commission refund records are created in the `platform_commission` table with `source` containing 'REFUND' and negative values to represent the refund.


**SQL Example to verify the history of a refunded transaction:**


```sql
-- 1. Check current status
SELECT 
    t.id,
    t.transaction_id AS external_id,
    ts.status AS current_status,
    t.order_date,
    t.offer_price
FROM 
    transactions t
JOIN 
    transaction_statuses ts ON t.status_id = ts.id
WHERE 
    t.transaction_id = 'YOUR_TRANSACTION_ID_HERE';


-- 2. Check status change history
SELECT 
    tsh.change_date,
    ts.status,
    tsh.reason
FROM 
    transaction_status_history tsh
JOIN 
    transaction_statuses ts ON tsh.status_id = ts.id
JOIN 
    transactions t ON tsh.transaction_id = t.id
WHERE 
    t.transaction_id = 'YOUR_TRANSACTION_ID_HERE'
ORDER BY 
    tsh.change_date;


-- 3. Check commission refunds
SELECT 
    pc.amount,
    pc.source,
    pc.created_at,
    cp.name AS participant_name
FROM 
    platform_commission pc
JOIN 
    commission_participants cp ON pc.participant_id = cp.id
JOIN 
    transactions t ON pc.transaction_id = t.id
WHERE 
    t.transaction_id = 'YOUR_TRANSACTION_ID_HERE'
    AND pc.source LIKE '%REFUND%'
ORDER BY 
    pc.created_at;
```


**Additional Notes:**
- Partial refunds follow the same flow, but with proportional values
- The time between the refund and commission refunds may vary depending on the platform
- Transactions with confirmed chargebacks usually follow an additional dispute flow


(Ref: System Known Patterns, ID system_known_patterns_001)


### Subscription Management


#### "How do I identify canceled subscriptions and the reason for cancellation?"


**Canonical Response:**


Canceled subscriptions can be identified by the `status_id` in the `subscriptions` table, which will be linked to one of the following statuses: 'Canceled by Customer', 'Canceled due to Delinquency', or 'Canceled by Platform'.


To get the specific reason for cancellation, you need to query the `subscription_status_history` table, which records the history of all status changes, including the reason provided at the time of cancellation.


**SQL Example to list canceled subscriptions with reasons:**


```sql
-- List canceled subscriptions with detailed information
SELECT 
    s.id,
    s.subscription_id AS external_id,
    c.name AS customer_name,
    c.email AS customer_email,
    p.name AS plan_name,
    ts.status AS current_status,
    s.start_date,
    s.cancel_date,
    -- Get the cancellation reason from the status history
    (SELECT ssh.reason 
     FROM subscription_status_history ssh
     WHERE ssh.subscription_id = s.id
     AND ssh.status_id = s.status_id
     ORDER BY ssh.change_date DESC
     LIMIT 1) AS cancellation_reason
FROM 
    subscriptions s
JOIN 
    customers c ON s.customer_id = c.id
JOIN 
    plans p ON s.plan_id = p.id
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
WHERE 
    ts.status IN ('Canceled by Customer', 'Canceled due to Delinquency', 'Canceled by Platform')
    -- Optional filters:
    -- AND s.cancel_date BETWEEN '2023-01-01' AND '2023-11-30'
    -- AND p.name LIKE '%Premium%'
ORDER BY 
    s.cancel_date DESC;
```


**SQL Example for cancellation reason analysis:**


```sql
-- Aggregated analysis of cancellation reasons
SELECT 
    ts.status AS cancellation_type,
    ssh.reason,
    COUNT(*) AS total_cancellations,
    ROUND(AVG(EXTRACT(DAY FROM (s.cancel_date - s.start_date))), 1) AS avg_days_as_subscriber
FROM 
    subscriptions s
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
JOIN 
    subscription_status_history ssh ON s.id = ssh.subscription_id AND ssh.status_id = s.status_id
WHERE 
    ts.status IN ('Canceled by Customer', 'Canceled due to Delinquency', 'Canceled by Platform')
    AND s.cancel_date BETWEEN '2023-01-01' AND '2023-11-30'
GROUP BY 
    ts.status, ssh.reason
ORDER BY 
    total_cancellations DESC;
```


**Additional Notes:**
- Cancellation reasons may vary depending on the platform of origin
- For cancellations due to delinquency, also check the last failed transaction
- The cancellation date (`cancel_date`) indicates when the cancellation was requested, while `end_date` indicates when the subscription actually ended or will end


(Ref: System Known Patterns, ID system_known_patterns_001)


#### "How do trial periods work in subscriptions?"


**Canonical Response:**


The trial period (free trial) is primarily managed through the `plans` table, which contains the `trial_days` field defining the duration in days of the trial period.


When a subscription with a trial is created:


1. The record is inserted in the `subscriptions` table with status 'Active' or 'Trial'
2. The `start_date` reflects the start of the trial period
3. The first charge is scheduled for after the trial ends, reflected in `next_billing_date`
4. The first transaction is only generated after the trial ends, if the customer does not cancel before


**SQL Example to identify subscriptions in trial period:**


```sql
-- Identify subscriptions currently in trial period
SELECT 
    s.id,
    s.subscription_id AS external_id,
    c.name AS customer_name,
    c.email AS customer_email,
    p.name AS plan_name,
    p.trial_days,
    s.start_date AS trial_start_date,
    (s.start_date + (p.trial_days * INTERVAL '1 day')) AS trial_end_date,
    s.next_billing_date AS first_charge_date,
    CASE 
        WHEN CURRENT_DATE BETWEEN s.start_date AND (s.start_date + (p.trial_days * INTERVAL '1 day')) THEN 'In Trial'
        ELSE 'Trial Completed'
    END AS trial_status
FROM 
    subscriptions s
JOIN 
    customers c ON s.customer_id = c.id
JOIN 
    plans p ON s.plan_id = p.id
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
WHERE 
    p.trial_days > 0
    AND ts.status IN ('Active', 'Trial') -- Depending on platform implementation
    AND (
        -- Still in trial
        CURRENT_DATE <= (s.start_date + (p.trial_days * INTERVAL '1 day'))
        -- OR trial ended in the last 7 days
        OR (s.start_date + (p.trial_days * INTERVAL '1 day')) BETWEEN (CURRENT_DATE - INTERVAL '7 days') AND CURRENT_DATE
    )
ORDER BY 
    (s.start_date + (p.trial_days * INTERVAL '1 day'));
```


**Additional Notes:**
- If the customer cancels during the trial, the `status_id` will change to 'Canceled by Customer' without generating a transaction
- The exact implementation of trials may vary between platforms (Hotmart vs Kiwify)
- Some plans may offer a "paid trial" with a reduced value, which will generate an initial transaction
- For reporting purposes, subscriptions canceled during the trial are generally not counted as churn


(Ref: System Known Patterns, ID system_known_patterns_001)


### Data Analysis and Metrics


#### "How do I correctly calculate MRR (Monthly Recurring Revenue)?"


**Canonical Response:**


MRR (Monthly Recurring Revenue) is a crucial metric in subscription businesses. To calculate it correctly using the `joaocastanheira_bancodedados` database, you need to:


1. **Normalize all plans to a monthly basis**:
   - Annual plans are divided by 12
   - Quarterly plans are divided by 3
   - Semiannual plans are divided by 6
   - Weekly plans are multiplied by 4.33 (average weeks per month)


2. **Include only active subscriptions** (status = 'Active')


3. **Calculate for a specific point in time** (e.g., the last day of the month)


**SQL Example to calculate current MRR:**


```sql
-- Current MRR calculation
SELECT 
    SUM(
        CASE 
            WHEN p.recurrence_period = 'YEAR' THEN p.price / 12
            WHEN p.recurrence_period = 'QUARTER' THEN p.price / 3
            WHEN p.recurrence_period = 'SEMIANNUAL' THEN p.price / 6
            WHEN p.recurrence_period = 'WEEK' THEN p.price * 4.33
            ELSE p.price -- Assume monthly periodicity as default
        END
    ) AS current_mrr,
    COUNT(DISTINCT s.id) AS active_subscriptions,
    SUM(
        CASE 
            WHEN p.recurrence_period = 'YEAR' THEN p.price / 12
            WHEN p.recurrence_period = 'QUARTER' THEN p.price / 3
            WHEN p.recurrence_period = 'SEMIANNUAL' THEN p.price / 6
            WHEN p.recurrence_period = 'WEEK' THEN p.price * 4.33
            ELSE p.price
        END
    ) / NULLIF(COUNT(DISTINCT s.id), 0) AS average_mrr_per_subscription
FROM 
    subscriptions s
JOIN 
    plans p ON s.plan_id = p.id
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
WHERE 
    ts.status = 'Active'
    AND p.currency_code = 'BRL'; -- Filter by currency for consistency
```


**SQL Example to calculate MRR evolution over time:**


```sql
-- Month by month MRR evolution
WITH RECURSIVE monthly_dates AS (
    -- Generate sequence of monthly dates for historical analysis
    SELECT generate_series(
        DATE_TRUNC('month', '2023-01-01'::date),
        DATE_TRUNC('month', CURRENT_DATE),
        '1 month'::interval
    ) AS month_date
),
active_subscriptions_by_month AS (
    -- For each month, determine which subscriptions were active
    SELECT 
        DATE_TRUNC('month', d.month_date)::date AS month,
        s.id AS subscription_id,
        p.price AS original_price,
        p.recurrence_period,
        CASE 
            WHEN p.recurrence_period = 'YEAR' THEN p.price / 12
            WHEN p.recurrence_period = 'QUARTER' THEN p.price / 3
            WHEN p.recurrence_period = 'SEMIANNUAL' THEN p.price / 6
            WHEN p.recurrence_period = 'WEEK' THEN p.price * 4.33
            ELSE p.price -- Assume monthly periodicity as default
        END AS normalized_monthly_revenue
    FROM 
        monthly_dates d
    CROSS JOIN subscriptions s
    JOIN plans p ON s.plan_id = p.id
    JOIN transaction_statuses ts ON s.status_id = ts.id
    WHERE 
        -- Subscription was active on the last day of the month
        s.start_date <= (d.month_date + INTERVAL '1 month - 1 day')
        AND (s.end_date IS NULL OR s.end_date >= (d.month_date + INTERVAL '1 month - 1 day'))
        -- We consider the current status for simplification, but ideally
        -- should check the status at the specific time of the month
        AND ts.status = 'Active'
        AND p.currency_code = 'BRL'
)
SELECT 
    month,
    COUNT(DISTINCT subscription_id) AS active_subscriptions,
    ROUND(SUM(normalized_monthly_revenue), 2) AS mrr,
    ROUND(SUM(normalized_monthly_revenue) * 12, 2) AS arr -- Annual Recurring Revenue
FROM 
    active_subscriptions_by_month
GROUP BY 
    month
ORDER BY 
    month;
```


**Additional Notes:**
- MRR should always be calculated in a single currency (BRL in the examples)
- For companies with revenues in multiple currencies, currency conversion needs to be implemented
- "New MRR" represents revenue from new subscriptions
- "Expansion MRR" represents increased revenue from plan upgrades
- "Contraction MRR" represents decreased revenue from downgrades
- "Churned MRR" represents revenue lost from cancellations
- "Net New MRR" is the sum of New + Expansion - Contraction - Churned


(Ref: System Known Patterns, ID system_known_patterns_001)


#### "How do I correctly calculate the churn rate?"


**Canonical Response:**


The churn rate (cancellation rate) is a crucial metric for subscription businesses, representing the proportion of customers or revenue lost in a period. There are two main ways to calculate churn:


1. **Customer Churn**: Percentage of subscribers who canceled relative to the total number of active subscribers at the beginning of the period.


2. **Revenue Churn**: Percentage of recurring revenue (MRR) lost due to cancellations relative to the total MRR at the beginning of the period.


**SQL Example for monthly customer churn:**


```sql
-- Monthly customer churn calculation
WITH monthly_periods AS (
    -- Generate monthly periods for analysis
    SELECT 
        DATE_TRUNC('month', date_series)::date AS period_start,
        (DATE_TRUNC('month', date_series) + INTERVAL '1 month - 1 day')::date AS period_end
    FROM 
        GENERATE_SERIES(
            DATE_TRUNC('month', CURRENT_DATE - INTERVAL '12 months'),
            DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month'),
            '1 month'::interval
        ) AS date_series
),
monthly_metrics AS (
    -- Calculate metrics for each monthly period
    SELECT 
        mp.period_start,
        mp.period_end,
        -- Active subscribers at start of period
        COUNT(DISTINCT CASE 
            WHEN s.start_date < mp.period_start
                AND (s.end_date IS NULL OR s.end_date >= mp.period_start)
            THEN s.id
        END) AS active_start,
        -- Subscribers who canceled during the period
        COUNT(DISTINCT CASE 
            WHEN s.cancel_date BETWEEN mp.period_start AND mp.period_end
                AND ts.status IN ('Canceled by Customer', 'Canceled due to Delinquency', 'Canceled by Platform')
            THEN s.id
        END) AS churned_subscribers
    FROM 
        monthly_periods mp
    CROSS JOIN subscriptions s
    JOIN transaction_statuses ts ON s.status_id = ts.id
    GROUP BY 
        mp.period_start, mp.period_end
)
SELECT 
    TO_CHAR(period_start, 'YYYY-MM') AS month,
    active_start AS subscribers_at_start,
    churned_subscribers AS subscribers_churned,
    ROUND((churned_subscribers * 100.0) / NULLIF(active_start, 0), 2) AS monthly_churn_rate_pct,
    -- Annualized calculation (monthly compounded)
    ROUND(
        (1 - POWER(1 - (churned_subscribers::decimal / NULLIF(active_start, 0)), 12)) * 100,
        2
    ) AS annualized_churn_rate_pct
FROM 
    monthly_metrics
WHERE 
    active_start > 0
ORDER BY 
    period_start;
```


**SQL Example for monthly revenue churn:**


```sql
-- Monthly revenue (MRR) churn calculation
WITH monthly_periods AS (
    -- Generate monthly periods for analysis
    SELECT 
        DATE_TRUNC('month', date_series)::date AS period_start,
        (DATE_TRUNC('month', date_series) + INTERVAL '1 month - 1 day')::date AS period_end
    FROM 
        GENERATE_SERIES(
            DATE_TRUNC('month', CURRENT_DATE - INTERVAL '12 months'),
            DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month'),
            '1 month'::interval
        ) AS date_series
),
normalized_mrr AS (
    -- Normalize recurring value per subscription
    SELECT
        s.id AS subscription_id,
        s.start_date,
        s.end_date,
        s.cancel_date,
        ts.status,
        CASE 
            WHEN p.recurrence_period = 'YEAR' THEN p.price / 12
            WHEN p.recurrence_period = 'QUARTER' THEN p.price / 3
            WHEN p.recurrence_period = 'SEMIANNUAL' THEN p.price / 6
            WHEN p.recurrence_period = 'WEEK' THEN p.price * 4.33
            ELSE p.price
        END AS monthly_recurring_revenue
    FROM 
        subscriptions s
    JOIN 
        plans p ON s.plan_id = p.id
    JOIN 
        transaction_statuses ts ON s.status_id = ts.id
    WHERE
        p.currency_code = 'BRL'
),
monthly_mrr_metrics AS (
    -- Calculate MRR metrics for each period
    SELECT 
        mp.period_start,
        mp.period_end,
        -- Active MRR at start of period
        SUM(CASE 
            WHEN nm.start_date < mp.period_start
                AND (nm.end_date IS NULL OR nm.end_date >= mp.period_start)
            THEN nm.monthly_recurring_revenue
            ELSE 0
        END) AS mrr_start,
        -- MRR canceled during the period
        SUM(CASE 
            WHEN nm.cancel_date BETWEEN mp.period_start AND mp.period_end
                AND nm.status IN ('Canceled by Customer', 'Canceled due to Delinquency', 'Canceled by Platform')
            THEN nm.monthly_recurring_revenue
            ELSE 0
        END) AS mrr_churned
    FROM 
        monthly_periods mp
    CROSS JOIN normalized_mrr nm
    GROUP BY 
        mp.period_start, mp.period_end
)
SELECT 
    TO_CHAR(period_start, 'YYYY-MM') AS month,
    ROUND(mrr_start, 2) AS mrr_at_start,
    ROUND(mrr_churned, 2) AS mrr_churned,
    ROUND((mrr_churned * 100.0) / NULLIF(mrr_start, 0), 2) AS monthly_mrr_churn_rate_pct,
    -- Annualized calculation (monthly compounded)
    ROUND(
        (1 - POWER(1 - (mrr_churned / NULLIF(mrr_start, 0)), 12)) * 100,
        2
    ) AS annualized_mrr_churn_rate_pct
FROM 
    monthly_mrr_metrics
WHERE 
    mrr_start > 0
ORDER BY 
    period_start;
```


**Additional Notes:**
- Revenue churn is generally more accurate for assessing financial impact
- Annualizing the monthly rate uses compounding (1 - (1 - monthly_rate)^12)
- There are variations in methodology, such as accounting for downgrades as partial churn
- For retention, use the formula: Retention = 100% - Churn
- "Net churn" also considers expansion (negative when expansion exceeds churn)
- Segmenting churn by plan, subscription duration, or channel can provide valuable insights


(Ref: System Known Patterns, ID system_known_patterns_001)


### Common Workflows


#### "How do I map a customer's complete journey from first purchase to cancellation?"


**Canonical Response:**


Mapping a customer's complete journey involves querying multiple tables to gather information about all interactions, transactions, and status changes. The complete process includes:


1. **Customer identification** (table `customers`)
2. **All transactions** (table `transactions`)
3. **Subscription history** (table `subscriptions`)
4. **Status changes** (tables `transaction_status_history` and `subscription_status_history`)
5. **Products/plans purchased** (tables `products`, `plans` via `transaction_items`)


**SQL Example to map a customer's complete journey:**


```sql
-- Parameters: customer identifier
-- Replace with specific email or ID
WITH client_params AS (
    SELECT 
        (SELECT id FROM customers WHERE email = 'customer@example.com') AS customer_id
),
customer_data AS (
    -- Basic customer information
    SELECT 
        c.id,
        c.name,
        c.email,
        c.created_at AS customer_since,
        c.phone_local_code||c.phone_number AS phone
    FROM 
        customers c, client_params cp
    WHERE 
        c.id = cp.customer_id
),
purchase_history AS (
    -- Complete transaction history
    SELECT 
        t.id,
        t.transaction_id AS external_id,
        t.order_date,
        ts.status AS transaction_status,
        t.payment_method,
        t.offer_price,
        t.is_subscription,
        t.subscription_id,
        p.name AS product_name,
        pl.name AS plan_name,
        COALESCE(pl.recurrence_period, 'ONE_TIME') AS purchase_type
    FROM 
        transactions t
    JOIN 
        transaction_statuses ts ON t.status_id = ts.id
    LEFT JOIN 
        transaction_items ti ON t.id = ti.transaction_id
    LEFT JOIN 
        products p ON ti.product_id = p.id
    LEFT JOIN 
        subscriptions s ON t.subscription_id = s.id
    LEFT JOIN 
        plans pl ON COALESCE(s.plan_id, ti.plan_id) = pl.id
    WHERE 
        t.customer_id = (SELECT customer_id FROM client_params)
    ORDER BY 
        t.order_date
),
subscription_history AS (
    -- Subscription history and status changes
    SELECT 
        s.id,
        s.subscription_id AS external_id,
        s.start_date,
        s.end_date,
        s.cancel_date,
        pl.name AS plan_name,
        ts.status AS current_status,
        ssh.change_date,
        prev_ts.status AS previous_status,
        ssh.reason AS change_reason
    FROM 
        subscriptions s
    JOIN 
        transaction_statuses ts ON s.status_id = ts.id
    JOIN 
        plans pl ON s.plan_id = pl.id
    LEFT JOIN 
        subscription_status_history ssh ON s.id = ssh.subscription_id
    LEFT JOIN 
        transaction_statuses prev_ts ON ssh.status_id = prev_ts.id
    WHERE 
        s.customer_id = (SELECT customer_id FROM client_params)
    ORDER BY 
        s.start_date, ssh.change_date
),
customer_journey AS (
    -- Consolidate all events into a single timeline
    
    -- Transaction events
    SELECT 
        ph.order_date AS event_date,
        'Transaction' AS event_type,
        ph.transaction_status AS event_status,
        'Purchase: '||ph.product_name||CASE WHEN ph.is_subscription THEN ' (Subscription)' ELSE ' (One-time)' END||' - '||ph.payment_method AS event_description,
        ph.offer_price AS amount,
        ph.external_id AS reference_id
    FROM 
        purchase_history ph
    
    UNION ALL
    
    -- Subscription events (start)
    SELECT 
        sh.start_date AS event_date,
        'Subscription' AS event_type,
        'Started' AS event_status,
        'Subscription start: '||sh.plan_name AS event_description,
        NULL AS amount,
        sh.external_id AS reference_id
    FROM 
        subscription_history sh
    WHERE 
        sh.previous_status IS NULL -- Only initial start
        
    UNION ALL
    
    -- Subscription status change events
    SELECT 
        sh.change_date AS event_date,
        'Subscription' AS event_type,
        sh.current_status AS event_status,
        'Changed to '||sh.current_status||CASE WHEN sh.change_reason IS NOT NULL 
             THEN ': '||sh.change_reason
             ELSE ''
        END AS event_description,
        NULL AS amount,
        sh.external_id AS reference_id
    FROM 
        subscription_history sh
    WHERE 
        sh.previous_status IS NOT NULL -- Only status changes
)
-- Final result
SELECT 
    cd.name AS customer_name,
    cd.email AS customer_email,
    cd.phone AS customer_phone,
    cd.customer_since,
    cj.event_date,
    cj.event_type,
    cj.event_status,
    cj.event_description,
    cj.amount,
    cj.reference_id
FROM 
    customer_data cd
CROSS JOIN 
    customer_journey cj
ORDER BY 
    cj.event_date;
```


**Extensions and Variations:**


For more specific analysis, you can derive queries for:


1. **Time to First Purchase:**
```sql
SELECT 
    c.id,
    c.name,
    c.email,
    c.created_at AS registration_date,
    MIN(t.order_date) AS first_purchase_date,
    EXTRACT(EPOCH FROM (MIN(t.order_date) - c.created_at)) / 86400 AS days_to_first_purchase
FROM 
    customers c
JOIN 
    transactions t ON c.id = t.customer_id
JOIN 
    transaction_statuses ts ON t.status_id = ts.id
WHERE 
    ts.status = 'Approved'
    AND c.id = [CUSTOMER_ID]
GROUP BY 
    c.id, c.name, c.email, c.created_at;
```


2. **Sequence of Products Purchased:**
```sql
SELECT 
    ROW_NUMBER() OVER (ORDER BY t.order_date) AS purchase_number,
    t.order_date,
    p.name AS product_name,
    t.offer_price,
    CASE WHEN t.is_subscription THEN 'Subscription' ELSE 'One-time Purchase' END AS purchase_type
FROM 
    transactions t
JOIN 
    transaction_items ti ON t.id = ti.transaction_id
JOIN 
    products p ON ti.product_id = p.id
JOIN 
    transaction_statuses ts ON t.status_id = ts.id
WHERE 
    t.customer_id = [CUSTOMER_ID]
    AND ts.status = 'Approved'
ORDER BY 
    t.order_date;
```


**Additional Notes:**
- This journey analysis can be extended to include other interactions (e.g., support, login)
- For customers with many transactions, consider filtering by period or limiting results
- The mapping can be visualized in tools like Tableau or Power BI
- For large-scale analysis, consider creating a materialized view of the basic customer journey


(Ref: System Known Patterns, ID system_known_patterns_001)


#### "How do I identify and recover customers at high risk of churn?"


**Canonical Response:**


Identifying customers at high risk of churn (cancellation) involves analyzing various behavioral signals. In the `joaocastanheira_bancodedados` database, we can identify these customers using different indicators:


1. **Subscribers with recent payment failures**
2. **Subscribers with decreasing usage patterns** (requires integration with usage system)
3. **Customers similar to those who have already canceled** (cohort analysis)
4. **Customers approaching critical dates** (subscription anniversary, end of promotional period)


**SQL Example to identify subscribers with recent payment failures:**


```sql
-- Subscribers with recent payment failures
SELECT 
    c.id AS customer_id,
    c.name AS customer_name,
    c.email,
    s.subscription_id AS external_subscription_id,
    p.name AS plan_name,
    ts.status AS subscription_status,
    s.next_billing_date,
    -- Last failed charge attempt
    (SELECT MAX(t.order_date)
     FROM transactions t
     JOIN transaction_statuses tst ON t.status_id = tst.id
     WHERE t.subscription_id = s.id
     AND tst.status IN ('Refused', 'Pending')
     AND t.order_date > CURRENT_DATE - INTERVAL '60 days') AS last_failed_charge_date,
    -- Total number of recent failures
    (SELECT COUNT(*)
     FROM transactions t
     JOIN transaction_statuses tst ON t.status_id = tst.id
     WHERE t.subscription_id = s.id
     AND tst.status IN ('Refused', 'Pending')
     AND t.order_date > CURRENT_DATE - INTERVAL '90 days') AS recent_failed_charges,
    -- Total successful transactions
    (SELECT COUNT(*)
     FROM transactions t
     JOIN transaction_statuses tst ON t.status_id = tst.id
     WHERE t.subscription_id = s.id
     AND tst.status = 'Approved') AS total_successful_charges,
    -- Date of last approved transaction
    (SELECT MAX(t.order_date)
     FROM transactions t
     JOIN transaction_statuses tst ON t.status_id = tst.id
     WHERE t.subscription_id = s.id
     AND tst.status = 'Approved') AS last_successful_charge_date
FROM 
    customers c
JOIN 
    subscriptions s ON c.id = s.customer_id
JOIN 
    plans p ON s.plan_id = p.id
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
WHERE 
    -- With status indicating payment problem
    (ts.status = 'Delinquent'
    -- OR had recent failure but still active
    OR EXISTS (
        SELECT 1
        FROM transactions t
        JOIN transaction_statuses tst ON t.status_id = tst.id
        WHERE t.subscription_id = s.id
        AND tst.status IN ('Refused', 'Pending')
        AND t.order_date > CURRENT_DATE - INTERVAL '30 days'
    )
    AND ts.status = 'Active')
    -- Prioritize the most critical cases (close to cancellation)
    AND (s.next_billing_date IS NULL OR s.next_billing_date < CURRENT_DATE + INTERVAL '15 days')
ORDER BY 
    -- Order by criticality (delinquent first, then by next billing date)
    CASE WHEN ts.status = 'Delinquent' THEN 0 ELSE 1 END,
    s.next_billing_date;
```


**SQL Example to identify customers approaching critical dates:**


```sql
-- Subscribers approaching critical dates (anniversary, end of discount)
SELECT 
    c.id AS customer_id,
    c.name AS customer_name,
    c.email,
    s.subscription_id AS external_subscription_id,
    p.name AS plan_name,
    s.start_date,
    -- Subscription anniversary
    (s.start_date + INTERVAL '1 year' * EXTRACT(YEAR FROM AGE(CURRENT_DATE, s.start_date)) + INTERVAL '1 year') AS upcoming_anniversary,
    EXTRACT(DAY FROM (s.start_date + INTERVAL '1 year' * EXTRACT(YEAR FROM AGE(CURRENT_DATE, s.start_date)) + INTERVAL '1 year') - CURRENT_DATE) AS days_to_anniversary,
    -- Current subscription duration in days
    EXTRACT(DAY FROM AGE(CURRENT_DATE, s.start_date)) AS days_as_subscriber,
    -- Last transaction
    (SELECT MAX(t.order_date)
     FROM transactions t
     JOIN transaction_statuses tst ON t.status_id = tst.id
     WHERE t.subscription_id = s.id
     AND tst.status = 'Approved') AS last_payment_date,
    -- Customer classification
    CASE 
        -- About to complete first year (critical decision point)
        WHEN EXTRACT(DAY FROM AGE(CURRENT_DATE, s.start_date)) BETWEEN 330 AND 365 THEN 'Approaching first anniversary'
        -- Multiple years, close to anniversary
        WHEN EXTRACT(DAY FROM (s.start_date + INTERVAL '1 year' * EXTRACT(YEAR FROM AGE(CURRENT_DATE, s.start_date)) + INTERVAL '1 year') - CURRENT_DATE) BETWEEN 0 AND 30 THEN 'Approaching subscription anniversary'
        -- Recent subscribers (first 30 days are also critical)
        WHEN EXTRACT(DAY FROM AGE(CURRENT_DATE, s.start_date)) BETWEEN 0 AND 30 THEN 'New subscriber (first 30 days)'
        -- Long-term subscribers without additional purchases
        WHEN EXTRACT(DAY FROM AGE(CURRENT_DATE, s.start_date)) > 180 
             AND NOT EXISTS (
                 SELECT 1 FROM transactions t
                 JOIN transaction_items ti ON t.id = ti.transaction_id
                 JOIN transaction_statuses tst ON t.status_id = tst.id
                 WHERE t.customer_id = c.id
                 AND t.is_subscription = FALSE
                 AND tst.status = 'Approved'
             ) THEN 'Long-term subscriber without additional purchases'
        ELSE 'Regular'
    END AS risk_category
FROM 
    customers c
JOIN 
    subscriptions s ON c.id = s.customer_id
JOIN 
    plans p ON s.plan_id = p.id
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
WHERE 
    ts.status = 'Active'
    AND (
        -- Approaching one-year anniversary (critical renewal point)
        (EXTRACT(DAY FROM AGE(CURRENT_DATE, s.start_date)) BETWEEN 330 AND 365)
        -- OR approaching any subscription anniversary
        OR (EXTRACT(DAY FROM (s.start_date + INTERVAL '1 year' * EXTRACT(YEAR FROM AGE(CURRENT_DATE, s.start_date)) + INTERVAL '1 year') - CURRENT_DATE) BETWEEN 0 AND 30)
        -- OR new subscribers (first 30 days are critical for establishing value)
        OR (EXTRACT(DAY FROM AGE(CURRENT_DATE, s.start_date)) BETWEEN 0 AND 30)
        -- OR long-term subscribers without additional engagement
        OR (EXTRACT(DAY FROM AGE(CURRENT_DATE, s.start_date)) > 180
            AND NOT EXISTS (
                SELECT 1 FROM transactions t
                JOIN transaction_items ti ON t.id = ti.transaction_id
                JOIN transaction_statuses tst ON t.status_id = tst.id
                WHERE t.customer_id = c.id
                AND t.is_subscription = FALSE
                AND tst.status = 'Approved'
            ))
    )
ORDER BY 
    CASE 
        WHEN EXTRACT(DAY FROM AGE(CURRENT_DATE, s.start_date)) BETWEEN 330 AND 365 THEN 1
        WHEN EXTRACT(DAY FROM (s.start_date + INTERVAL '1 year' * EXTRACT(YEAR FROM AGE(CURRENT_DATE, s.start_date)) + INTERVAL '1 year') - CURRENT_DATE) BETWEEN 0 AND 30 THEN 2
        WHEN EXTRACT(DAY FROM AGE(CURRENT_DATE, s.start_date)) BETWEEN 0 AND 30 THEN 3
        ELSE 4
    END,
    days_to_anniversary;
```


**Recovery Strategies:**


After identifying customers at risk, common recovery strategies include:


1. **For payment problems:**
   - Proactive communication about expired card or payment failure
   - Offer alternative payment methods
   - Implement automatic retry with increasing interval


2. **For subscription anniversaries:**
   - Value reinforcement communication (usage summary, success stories)
   - Renewal incentive offer (discount, gift, additional feature)
   - Feedback survey to identify friction points


3. **For low engagement:**
   - Use case-based reactivation (tutorials, webinars)
   - Extended or refreshed onboarding program
   - Personalized contact to understand needs


**Additional Notes:**
- Ideally, combine transactional data with usage/behavioral data
- Predictive models can enhance risk identification using machine learning
- Customer segmentation allows retention strategies to be personalized
- Customer Health Score metrics can aggregate multiple indicators


(Ref: System Known Patterns, ID system_known_patterns_001)


## Common Anti-Patterns and Misconceptions


### Incorrect Understandings About the Database


#### "Every transaction is associated with a single product"


**Misconception:** A common assumption is that each transaction (record in the `transactions` table) is associated with exactly one product.


**Reality:** A transaction can be associated with multiple products through the intermediate table `transaction_items`. This structure allows for "cart" type transactions with multiple items or products.


**Correct Example:**
```sql
-- List all products in a specific transaction
SELECT 
    t.transaction_id AS transaction_external_id,
    t.order_date,
    p.name AS product_name,
    ti.quantity,
    ti.unit_price,
    (ti.quantity * ti.unit_price) AS item_total
FROM 
    transactions t
JOIN 
    transaction_items ti ON t.id = ti.transaction_id
JOIN 
    products p ON ti.product_id = p.id
WHERE 
    t.transaction_id = 'YOUR_TRANSACTION_ID_HERE';
```


(Ref: System Known Patterns, ID system_known_patterns_001)


#### "The status in the transactions/subscriptions table is a simple text field"


**Misconception:** Many users try to filter directly by status strings like 'Approved', 'Canceled', etc. in the `transactions` or `subscriptions` table.


**Reality:** Statuses are normalized and stored as references (foreign keys) to the `transaction_statuses` table. This provides consistency and multifunctionality but requires joins for status-based queries.


**Incorrect Example:**
```sql
-- Incorrect approach
SELECT * FROM transactions WHERE status = 'Approved';
```


**Correct Example:**
```sql
-- Correct approach
SELECT 
    t.*
FROM 
    transactions t
JOIN 
    transaction_statuses ts ON t.status_id = ts.id
WHERE 
    ts.status = 'Approved';
```


(Ref: System Known Patterns, ID system_known_patterns_001)


#### "Subscriptions always start with a successful transaction"


**Misconception:** It's common to assume that every subscription in the `subscriptions` table starts with a successful transaction in the `transactions` table.


**Reality:** Subscriptions with a trial period can be created without an initial transaction. The first transaction will only occur when the trial period ends, if the customer doesn't cancel before.


**Verification Example:**
```sql
-- Check subscriptions without initial transaction
SELECT 
    s.id,
    s.subscription_id AS external_id,
    c.name AS customer_name,
    c.email,
    p.name AS plan_name,
    p.trial_days,
    s.start_date,
    ts.status AS subscription_status
FROM 
    subscriptions s
JOIN 
    customers c ON s.customer_id = c.id
JOIN 
    plans p ON s.plan_id = p.id
JOIN 
    transaction_statuses ts ON s.status_id = ts.id
LEFT JOIN 
    transactions t ON s.id = t.subscription_id AND t.recurrence_number = 1
WHERE 
    t.id IS NULL  -- No initial transaction
    AND p.trial_days > 0  -- With trial period
    AND s.start_date >= CURRENT_DATE - INTERVAL '90 days';  -- Recent
```


(Ref: System Known Patterns, ID system_known_patterns_001)


### Common Errors in Queries and Analyses


#### "Calculating MRR by summing all subscription transactions in the month"


**Anti-Pattern:** A common mistake is calculating MRR (Monthly Recurring Revenue) by summing all subscription transactions that occurred in a given month.


**Problem:** This approach is incorrect because:
1. It includes both first-time sales and renewals without distinction
2. It doesn't normalize different periodicities (annual, quarterly, etc.)
3. It doesn't represent the actual recurring value at the end of the month (snapshot)


**Correct Approach:**
```sql
-- Correct MRR calculation (snapshot on the last day of the month)
WITH month_end_dates AS (
    SELECT 
        DATE_TRUNC('month', date_series) + INTERVAL '1 month - 1 day' AS month_end
    FROM 
        GENERATE_SERIES(
            DATE_TRUNC('month', CURRENT_DATE - INTERVAL '12 months'),
            DATE_TRUNC('month', CURRENT_DATE),
            '1 month'::interval
        ) AS date_series
),
active_subscriptions AS (
    SELECT 
        med.month_end,
        s.id AS subscription_id,
        p.price AS original_price,
        p.recurrence_period,
        CASE 
            WHEN p.recurrence_period = 'YEAR' THEN p.price / 12
            WHEN p.recurrence_period = 'QUARTER' THEN p.price / 3
            WHEN p.recurrence_period = 'SEMIANNUAL' THEN p.price / 6
            WHEN p.recurrence_period = 'WEEK' THEN p.price * 4.33
            ELSE p.price
        END AS normalized_monthly_revenue
    FROM 
        month_end_dates med
    CROSS JOIN subscriptions s
    JOIN plans p ON s.plan_id = p.id
    WHERE 
        s.start_date <= med.month_end
        AND (s.end_date IS NULL OR s.end_date > med.month_end)
        AND p.currency_code = 'BRL'
)
SELECT 
    TO_CHAR(month_end, 'YYYY-MM') AS month,
    COUNT(DISTINCT subscription_id) AS active_subscriptions,
    ROUND(SUM(normalized_monthly_revenue), 2) AS mrr
FROM 
    active_subscriptions
GROUP BY 
    month_end
ORDER BY 
    month_end;
```


(Ref: System Known Patterns, ID system_known_patterns_001)


#### "Ignoring currency normalization in global analyses"


**Anti-Pattern:** In systems that process transactions in multiple currencies, a common error is to aggregate values directly without currency normalization.


**Problem:** This approach leads to incorrect results because it sums values in different currencies as if they were equivalent (e.g., 100 BRL + 100 USD ≠ 200 in any currency).


**Example of Correct Approach:**
```sql
-- Analysis with currency normalization (conceptual - requires exchange rate table)
WITH exchange_rates AS (
    -- Conceptual table with exchange rates for each period
    -- In practice, you would need a real source of rates
    SELECT 
        '2023-01-01'::date AS rate_date,
        'USD' AS from_currency,
        'BRL' AS to_currency,
        5.20 AS exchange_rate
    UNION ALL
    SELECT '2023-01-01'::date, 'EUR', 'BRL', 6.10
    -- Add other rates and dates
),
normalized_transactions AS (
    SELECT 
        t.id,
        t.transaction_id,
        t.order_date,
        t.currency_code,
        t.offer_price AS original_price,
        -- Normalize to BRL (base currency)
        CASE 
            WHEN t.currency_code = 'BRL' THEN t.offer_price
            ELSE t.offer_price * (
                SELECT er.exchange_rate 
                FROM exchange_rates er
                WHERE er.from_currency = t.currency_code
                AND er.to_currency = 'BRL'
                AND er.rate_date <= t.order_date
                ORDER BY er.rate_date DESC
                LIMIT 1
            )
        END AS price_in_brl
    FROM 
        transactions t
    WHERE 
        t.order_date BETWEEN '2023-01-01' AND '2023-11-30'
)
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    currency_code,
    COUNT(*) AS transaction_count,
    SUM(original_price) AS revenue_original,
    SUM(price_in_brl) AS revenue_normalized_brl
FROM 
    normalized_transactions
GROUP BY 
    DATE_TRUNC('month', order_date),
    currency_code
ORDER BY 
    month, currency_code;
```


**Note:** In practice, you would need a historical exchange rate source to implement this normalization accurately.


(Ref: System Known Patterns, ID system_known_patterns_001)


## Integration Workflows


### Processing Webhooks and Events


#### "How do I correctly process payment events from gateways?"


**Canonical Response:**


Processing payment events from gateways (Hotmart, Kiwify, etc.) follows a consistent pattern using the tables in the `joaocastanheira_bancodedados` database. The correct flow includes:


1. **Event validation** (authenticity, duplicity)
2. **Identification/creation of related records** (customer, product, etc.)
3. **Transaction update/creation**
4. **Status history recording**
5. **Specific actions for the event type** (approval, refund, etc.)


**Pseudocode for payment event processing:**


```
FUNCTION process_payment_event(payload):
    # 1. Validation and Normalization
    validate_signature(payload.signature)
    event_id = payload.event_id
    
    # Check for duplicity
    IF event_already_processed(event_id):
        RETURN "Event already processed"
    
    # Normalize status according to platform
    normalized_status = normalize_status(payload.status, payload.platform)
    
    # 2. Identification/Creation of Base Records
    customer_id = get_or_create_customer(payload.customer)
    product_id = get_or_create_product(payload.product)
    
    # 3. Main Processing
    transaction = get_transaction_by_external(payload.transaction_id, payload.platform)
    
    IF transaction DOES NOT EXIST:
        # New transaction
        transaction = create_new_transaction(
            customer_id,
            product_id,
            payload.amount,
            normalized_status,
            payload.payment_method,
            payload.platform,
            # other relevant fields
        )
    ELSE:
        # Transaction update
        previous_status = transaction.status
        
        IF previous_status != normalized_status:
            update_transaction_status(transaction.id, normalized_status)
            
            # 4. History Recording
            record_status_history(
                transaction.id,
                previous_status,
                normalized_status,
                payload.event_date,
                payload.reason||"Via webhook "||payload.platform
            )
            
            # 5. Specific Actions by Status Type
            IF normalized_status == "Approved":
                process_approval(transaction, payload)
                
            IF normalized_status == "Refunded":
                process_refund(transaction, payload)
                
            IF normalized_status == "Confirmed Chargeback":
                process_chargeback(transaction, payload)
    
    # Record successful processing
    record_processed_event(event_id, payload)
    RETURN "Event processed successfully"


FUNCTION process_approval(transaction, payload):
    # Process subscription if applicable
    IF payload.is_subscription:
        subscription = get_or_create_subscription(
            transaction,
            payload.customer_id,
            payload.plan_id,
            payload.start_date,
            # other relevant fields
        )
        
        # Link transaction to subscription
        link_transaction_subscription(transaction.id, subscription.id)
    
    # Process commissions
    IF payload.commissions:
        FOR EACH commission IN payload.commissions:
            participant_id = get_or_create_participant(commission.participant)
            record_commission(
                transaction.id,
                participant_id,
                commission.amount,
                commission.type
            )


FUNCTION process_refund(transaction, payload):
    # Refund commissions
    commissions = get_commissions(transaction.id)
    FOR EACH commission IN commissions:
        record_commission_refund(
            transaction.id,
            commission.participant_id,
            commission.amount * -1,
            "REFUND_" + commission.type
        )
    
    # Update subscription if it exists
    IF transaction.subscription_id:
        update_subscription_status(
            transaction.subscription_id,
            "Canceled due to Refund",
            payload.event_date,
            "Refund requested via " + payload.platform
        )
```


**Important Considerations:**


1. **Idempotency:** The system must ensure that the same event is not processed multiple times
2. **Atomicity:** Use database transactions to ensure that all operations are successful or none are
3. **Validation:** Verify the authenticity of the event (signature, origin, etc.)
4. **Detailed Logging:** Maintain detailed logs of all events received and processed
5. **Error Handling:** Implement retries for temporary failures and notification mechanism for persistent errors


**Example Status Mapping (Hotmart and Kiwify):**


|Original Status (Hotmart)|Original Status (Kiwify)|Normalized Status|
|---------------------------|--------------------------|----------------------------|
|`APPROVED`|`paid`|`Approved`|
|`DELAYED`|`waiting_payment`|`Pending`|
|`CANCELED`|`refused`|`Refused`|
|`REFUNDED`|`refunded`|`Refunded`|
|`CHARGEBACK`|`chargedback`|`Confirmed Chargeback`|
|`COMPLETED`|`completed`|`Completed`|
|`APPROVED_RECURRING`|`paid_renewal`|`Approved`|
|`INACTIVE`|`inactive`|`Canceled by Customer`|
|`OVERDUE`|`overdue`|`Delinquent`|


(Ref: System Known Patterns, ID system_known_patterns_001)


## Conclusion and Additional Resources


### When to Use Custom SQL vs. ORM


A frequent question is about when to use custom SQL versus ORM (Object-Relational Mapping) abstractions when working with the `joaocastanheira_bancodedados` database.


**Guidelines:**


1. **Use ORM for:**
   - Basic CRUD operations on individual entities
   - Simple queries with few relationships
   - Applications focused on development speed
   - Maintenance by developers with less SQL experience


2. **Use custom SQL for:**
   - Complex analytical queries with multiple joins
   - High-performance batch operations
   - Reports requiring window functions, complex CTEs
   - Situations where performance is critical
   - Operations where specific SQL semantics are important


**Example of SQL/ORM balance:**


```python
# Pseudocode - Example of hybrid approach


# For simple CRUD operations - use ORM
def create_new_customer(customer_data):
    customer = Customer(
        name=customer_data.name,
        email=customer_data.email,
        phone=customer_data.phone
    )
    db.add(customer)
    db.commit()
    return customer.id


# For complex analyses - use direct SQL
def calculate_churn_by_product(start_date, end_date):
    result = db.execute("""
        WITH churn_data AS (
            SELECT 
                p.name AS product_name,
                COUNT(DISTINCT CASE 
                    WHEN s.start_date < :start_date 
                        AND (s.end_date IS NULL OR s.end_date >= :start_date)
                    THEN s.id 
                END) AS active_start,
                COUNT(DISTINCT CASE 
                    WHEN s.cancel_date BETWEEN :start_date AND :end_date
                        AND ts.status IN ('Canceled by Customer', 'Canceled due to Delinquency')
                    THEN s.id 
                END) AS churned_subscribers
            FROM 
                subscriptions s
            JOIN 
                plans pl ON s.plan_id = pl.id
            JOIN 
                products p ON pl.product_id = p.id
            JOIN 
                transaction_statuses ts ON s.status_id = ts.id
            GROUP BY 
                p.name
        )
        SELECT 
            product_name,
            active_start,
            churned_subscribers,
            ROUND((churned_subscribers * 100.0) / NULLIF(active_start, 0), 2) AS churn_rate_pct
        FROM 
            churn_data
        WHERE 
            active_start > 0
        ORDER BY 
            churn_rate_pct DESC
    """, {"start_date": start_date, "end_date": end_date})
    
    return result.fetchall()
```


This document will continue to be updated as new usage patterns and common questions emerge in the use of the RAG system for the `joaocastanheira_bancodedados` database.


(Ref: System Known Patterns, ID system_known_patterns_001)
```