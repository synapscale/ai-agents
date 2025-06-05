# `Core_DB_Design_Principles.md` 


```markdown
---
title: "Core Database Design Principles for Unified Database"
id: "core_db_design_001"
doc_type: "design_principles"
doc_version: "1.2"
date_created: "2025-04-23"
date_updated: "2025-04-24"
author: "João Castanheira"
db_name: "joaocastanheira_bancodedados"
db_version: "1.0"
doc_status: "Approved"
environment: "Production"
language: "en"
response_languages: ["pt-BR", "en"]
technical_terms_preservation: "strict"
original_language: "pt-BR"
related_docs: [
  "core_db_arch_001", 
  "platform_integration_strategy_001", 
  "core_db_glossary_001", 
  "ref_db_schema_001", 
  "domain_customers_ecosystem_001", 
  "domain_products_catalog_001", 
  "domain_transactions_lifecycle_001", 
  "domain_subscriptions_management_001", 
  "domain_commission_system_001", 
  "domain_platform_integration_details_001"
]
technical_terms: {
  "table_names": [
    "customers", "addresses", "customer_logs", "products", "plans", 
    "offers", "transactions", "transaction_items", "transaction_status_history", 
    "transaction_fees", "subscriptions", "subscription_status_history", 
    "commission_participants", "platform_commission", "participant_addresses", 
    "transaction_statuses", "platform_transaction_payment_history", 
    "platform_utm_history", "platform_software_invoice_history", 
    "platform_sale_offer_history", "masked_customers"
  ],
  "column_names": [
    "id", "product_id", "platform_origin", "customer_id", "transaction_id", 
    "payment_gateway", "offer_price", "platform_fee_amount", "partner_commission_amount", 
    "producer_net_amount", "currency_code", "order_date", "status_id", "card_brand", 
    "email", "name", "document", "document_type", "phone_local_code", "phone_number", 
    "created_at", "updated_at", "metadata", "is_subscription", "recurrence_period",
    "subscription_id", "utm_campaign", "utm_source", "utm_medium"
  ],
  "sql_keywords": [
    "CREATE TABLE", "CREATE TYPE", "CREATE OR REPLACE FUNCTION", "CREATE TRIGGER", "CREATE VIEW",
    "SELECT", "FROM", "WHERE", "JOIN", "GROUP BY", "ORDER BY", "HAVING", 
    "INSERT", "UPDATE", "DELETE", "SERIAL", "PRIMARY KEY", "FOREIGN KEY", 
    "REFERENCES", "UNIQUE", "NOT NULL", "ENUM", "CONSTRAINT", "TIMESTAMP", 
    "WITH TIME ZONE", "DEFAULT", "CURRENT_TIMESTAMP", "NULL", "VARCHAR", 
    "TEXT", "BOOLEAN", "NUMERIC", "INTEGER", "SMALLINT", "DATE_TRUNC", 
    "CASE", "WHEN", "THEN", "ELSE", "END", "COUNT", "SUM", "MIN", "MAX", 
    "AS", "ON", "BETWEEN", "AND", "OR", "IS NULL", "IS NOT NULL", "DISTINCT",
    "VACUUM", "ANALYZE", "REINDEX"
  ],
  "database_operations": [
    "VACUUM", "ANALYZE", "REINDEX", "EXPLAIN ANALYZE"
  ],
  "custom_types": [
    "payment_method_enum"
  ]
}
embedding_guide_concepts: [
  "database design principles", 
  "normalization", 
  "primary keys", 
  "foreign keys", 
  "data types", 
  "database naming conventions", 
  "referential integrity", 
  "null handling", 
  "strategic indexing", 
  "database security", 
  "schema evolution", 
  "database performance", 
  "database scalability", 
  "data governance", 
  "SQL best practices", 
  "data auditing", 
  "table partitioning", 
  "query optimization", 
  "multi-platform integration", 
  "data mapping"
]
---


# Core Database Design Principles for Unified Database


This document details the principles and conventions that guided the design of the `joaocastanheira_bancodedados` database. Adhering to these principles ensures consistency, integrity, performance, and maintainability of the schema over time.


(Ref: DB Design Principles, ID core_db_design_001)


## Design Principles and Architectural Decisions


The database design was guided by several fundamental principles that influenced architectural decisions, seeking to balance integrity, traceability, flexibility, and performance.


### 1. Balanced Normalization


The schema was normalized up to Third Normal Form (3NF) in most cases, with some strategic exceptions:


- **Strict Normalization** was applied to core tables such as `customers`, `products`, `transactions`, and `subscriptions` to minimize redundancy and maintain consistency.
- **Controlled Denormalization** was allowed in specific areas to optimize frequent queries or preserve historical data, such as calculated fields directly in the `transactions` table (`offer_price`, `platform_fee_amount`, etc.) or in the `platform_*` tables that function as historical snapshots.
- **Platform Data Normalization** occurs as part of the integration process, mapping different terminologies and structures from external platforms to our unified internal model, as detailed in the **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)** document.


### 2. Historical Preservation and Auditing


A central principle of the design is the ability to track important changes over time:


- **History Tables** (`customer_logs`, `transaction_status_history`, `subscription_status_history`) record all changes to key entities.
- **Universal Timestamping** with `created_at` and `updated_at` fields in all tables, with automatic updates via triggers.
- **Immutable Snapshots** in tables like `platform_sale_offer_history` to preserve the exact state at the time of the transaction.


### 3. Unified Identifiers with Origin Preservation


To enable the unification of data from multiple platforms:


- **Dual ID System** with:
  - Internal sequential ID (e.g., `id` as SERIAL PRIMARY KEY)
  - Original platform ID (e.g., `transaction_id` + `payment_gateway`)
- **Composite Uniqueness Constraints** to ensure that records of the same entity on different platforms are not duplicated:
  ```sql
  CONSTRAINT uq_transaction_gateway UNIQUE (transaction_id, payment_gateway)
  ```


### 4. Custom Enumerated Types


For fields with predefined values, PostgreSQL enumerated types were created:


```sql
CREATE TYPE payment_method_enum AS ENUM (
    'credit_card',
    'debit_card',
    'boleto',
    'pix',
    -- other values...
);
```


Advantages of this approach:
- Validation of values at the database level.
- Better semantic documentation.
- Avoids the need for lookup tables for simple lists.
- Facilitates type checking in queries.


### 5. Functions and Triggers for Consistency


The use of triggers to maintain data consistency, especially for timestamping:


```sql
CREATE OR REPLACE FUNCTION update_updated_at_column() RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
END;
$$;


CREATE TRIGGER trigger_update_customers_updated_at
    BEFORE UPDATE ON customers
    FOR EACH ROW
    EXECUTE PROCEDURE update_updated_at_column();
```


### 6. Referential Integrity and ON DELETE Rules


Data integrity between tables is maintained through foreign keys (`FOREIGN KEY`) with appropriate `ON DELETE` rules:


- **ON DELETE CASCADE**: For history/detail tables that should not exist without the parent record (e.g., `transaction_items` referencing `transactions`).
- **ON DELETE RESTRICT** (default behavior) or **ON DELETE SET NULL**: For relationships where the child record can potentially exist without the parent, or where deletion of the parent should be prevented if there are children.


### 7. Flexibility for Platform-Specific Metadata


`metadata` field (JSONB) in tables like `platform_transaction_payment_history` to store platform-specific data without needing to alter the main schema, allowing extensibility and preservation of original details.


(Ref: DB Design Principles, ID core_db_design_001)


## Primary Key and Identifier Strategy


The foundation of any robust relational model is identifier management. We adopted a hybrid strategy for primary keys and external identifiers.


### Internal Primary Keys (PKs)


**Principle**: Use auto-incrementing sequential primary keys (`SERIAL` in PostgreSQL) for internal identifiers of each table.


**Justification**:
- **Performance**: `SERIAL`s are ideal for primary and foreign keys in terms of indexing performance, storage, and join speed, especially in common transactional and analytical workloads.
- **Simplicity**: They are easy to generate and manage by the database itself.
- **Space**: They occupy less disk space and cache memory compared to UUIDs.


**Implementation**:
```sql
CREATE TABLE example (
    id SERIAL PRIMARY KEY, -- Internal primary key
    -- other fields
);
```


### External Identifiers


**Principle**: Preserve original identifiers from external platforms as dedicated columns, ensuring uniqueness when combined with the platform origin.


**Justification**:
- **Traceability**: Allows mapping internal records back to source systems for debugging, reconciliation, and auditing.
- **Multi-platform Uniqueness**: The combination of external ID and platform origin guarantees unique identification of the entity *within* our system.


**Implementation**:
```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_id VARCHAR(100) NOT NULL, -- ID on the source platform
    platform_origin VARCHAR(100) NOT NULL, -- Platform name
    -- other fields
    CONSTRAINT uq_product_platform UNIQUE (product_id, platform_origin) -- Ensures uniqueness of combination
);
```


(Ref: DB Design Principles, ID core_db_design_001)


## Normalization Strategy and Data Modeling


We sought a balance between data integrity and query performance, with 3NF as a base and strategic denormalization when justified.


Normalization in the context of multi-platform integration goes beyond simple tabular organization of data. It includes mapping and unifying concepts between different platforms, as detailed in the **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)** document. For example, the `transaction_statuses` table serves as a central point for normalizing the different status names that come from various platforms.


(Detailed content about 3NF, Strategic Denormalization, and Vocabulary Modeling (Lookup vs. ENUM) already covered in the "Design Principles and Architectural Decisions" section above.)


## Naming Conventions and Standards


Consistent naming is vital for the readability and maintainability of the schema.


**Principles**:
- **Tables**: Names in English, snake_case, plural (e.g., `customers`, `transactions`).
- **Columns**: Names in English, snake_case, singular (e.g., `customer_id`, `order_date`).
- **Primary Keys**: `id` (SERIAL standard).
- **Foreign Keys**: `[referenced_table_name]_id` (e.g., `customer_id` referencing `customers.id`).
- **Indexes**: `idx_[table_name]_[indexed_columns]` (e.g., `idx_transactions_customer_id`).
- **Unique Constraints**: `uq_[table_name]_[columns]` (e.g., `uq_product_platform`).
- **ENUM Types**: `[type_name]_enum` (e.g., `payment_method_enum`).
- **Functions**: `[action]_[entity]_column` or `[action]_[purpose]` (e.g., `update_updated_at_column`).
- **Triggers**: `trigger_[action]_[table_name]_[purpose]` (e.g., `trigger_update_customers_updated_at`).


**Justification**:
- **Consistency**: Facilitates reading and writing queries by any team member.
- **Self-documentation**: The column or table name already suggests its purpose and, in the case of FKs, the referenced table.
- **Compatibility**: snake_case is a common standard in databases and programming languages.


### Comment Conventions


Extensive documentation at the schema level:


- **Table Comments**: General description of the table's purpose.
- **Column Comments**: Clear definition of each field, including units or formats when applicable.
- **Type Comments**: Explanation of enumerated values and their use.


```sql
COMMENT ON TABLE customers IS 'Central repository of customer information, unifying data from various platforms.';
COMMENT ON COLUMN customers.email IS 'Customer''s main email, used for login and communication. Must be unique.';
```


(Ref: DB Design Principles, ID core_db_design_001)


## Data Types and Precision Standards


The correct choice of data types is crucial for integrity and efficiency.


**Principles**:
- **Monetary Values**: Use `NUMERIC(15, 4)` for all financial values.
- **Timestamps**: Use `TIMESTAMP WITH TIME ZONE`.
- **Strings**: Use `VARCHAR` with appropriate length or `TEXT` for long texts.
- **Booleans**: Use `BOOLEAN`.
- **Semi-structured Data**: Use `JSONB`.


**Justification**:
- **NUMERIC**: Ensures exact precision for financial calculations, avoiding floating-point errors. (15 digits total, 4 after the decimal point is sufficient for most currencies).
- **TIMESTAMP WITH TIME ZONE**: Stores the exact moment in time, regardless of the server or client timezone, avoiding problems with daylight saving time and regional differences.
- **VARCHAR/TEXT**: `VARCHAR` with a limit helps enforce size restrictions when applicable; `TEXT` is flexible for long descriptions.
- **BOOLEAN**: Efficient native type for true/false values.
- **JSONB**: Efficient storage of JSON data for flexible metadata, supporting indexing and queries.


(Ref: DB Design Principles, ID core_db_design_001)


## Handling Null Data and API Variations


Incomplete or variable data from external APIs is a common challenge.


**Principle**: Use `NULL` explicitly to indicate the absence of a known or applicable value. Avoid "magic" default values (like empty strings or zeros) to represent absence, unless zero is a valid and meaningful value.


**Justification**:
- **Semantic Clarity**: `NULL` unequivocally communicates that information is missing or not applicable.
- **Precise Queries**: Allows easy filtering for present (`IS NOT NULL`) or absent (`IS NULL`) data.


**Approach for Platform Variations**:
- **Universal Fields**: Columns that exist for most platforms are created directly in the main table and marked as `NOT NULL` if they are always expected, or allow `NULL` if they are optional or specific to some platforms.
- **Specific/Rare Fields**: Data that is very specific to a platform or rarely provided can be stored in `JSONB` columns in the main table or in dedicated auxiliary tables.


**Example**: The `card_brand` field in the `transactions` table allows `NULL` because not all payment methods use cards.


This data handling approach is applied in the normalization process described in **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)**, where data from different formats and structures are mapped to the unified model.


(Ref: DB Design Principles, ID core_db_design_001)


## Indexing Strategy


Indexes are crucial for read performance.


**Principle**: Create indexes based on expected query patterns, focusing on columns used in `WHERE`, `JOIN`, `ORDER BY`, and `GROUP BY` clauses.


**Justification**:
- **Query Performance**: Dramatically reduces execution time for queries that filter or sort large volumes of data.


### Applied Index Types


- **Single-Column Indexes**: For common filters (e.g., email, status).
- **Composite Indexes**: For filters that frequently combine multiple columns (e.g., `(product_id, platform_origin)`). The order of columns in the composite index follows selectivity or the most common query pattern.
- **Expression Indexes**: For queries that use functions on columns (e.g., `lower(email)`).
- **Partial Indexes**: To optimize queries on data subsets (e.g., active or recent transactions).


**Ongoing Process**: Indexing is not a one-time task. It involves continuous monitoring of performance metrics, analysis of execution plans for slow queries (`EXPLAIN ANALYZE`), and adjustment of indexes as data access patterns evolve.


(Ref: DB Design Principles, ID core_db_design_001)


## Performance and Scalability Considerations


To ensure that the database maintains good performance even with significant growth, several strategies have been implemented:


### 1. Strategic Indexing (Reinforcement)


Beyond basic indexes on primary and foreign keys, the schema includes:


- **Composite Indexes** for common filter patterns (e.g., `idx_subscriptions_next_billing_date` to facilitate locating subscriptions about to be charged).
- **Partial Indexes** for relevant data subsets.
- **Indexes on Search Fields** frequently used in WHERE clauses (e.g., `email`, `transaction_id`).


### 2. Partitioning


For tables that tend to grow significantly, consider partitioning by:


- **Time**: Partitioning by month/year for historical tables like `transaction_status_history`.
- **Platform**: Potential partitioning by `payment_gateway` to distribute load.


### 3. Calculated Columns and Statistics


- **Calculated Columns**: Store frequently used calculated values to avoid constant recalculations.
- **Updated Statistics**: Ensure PostgreSQL maintains updated statistics so the query optimizer chooses the best execution plans (`ANALYZE`).


### 4. Cleanup and Archiving Strategies


- **Retention Policies**: Define how long to keep detailed historical data.
- **Archiving**: Move old data to archive tables or long-term storage systems when necessary.
- **Aggregation**: Consider aggregation of historical data for long-term analysis.


### 5. Optimized Data Types (Reinforcement)


- **Use of VARCHAR with Limits**: Instead of TEXT when appropriate.
- **ENUMs**: Use of enumerated types that are more efficient than strings for predefined values.
- **Appropriate Numeric Types**: NUMERIC(15,4) for monetary values, but smaller types (INTEGER, SMALLINT) when appropriate.


(Ref: DB Design Principles, ID core_db_design_001)


## Data Security and Governance Guidelines


Security and data governance are critical aspects of this database, which handles sensitive customer and financial information.


### 1. Access Control


- **Principle of Least Privilege**: Users and applications should have only the minimum necessary privileges.
- **Separate Users by Function**: Create distinct database roles (e.g., read, read/write, administrator).
- **Masking of Sensitive Data**: For non-production environments, use views or functions to mask personal data.
  ```sql
  -- Example of view with masked data for development/testing
  CREATE VIEW masked_customers AS
  SELECT
      id,
      MD5(email) AS email,
      SUBSTRING(name, 1, 1)||REPEAT('*', LENGTH(name) - 1) AS name,
      '******' AS document
  FROM
      customers;
  ```


### 2. Auditing and Monitoring


- **Change Logs**: Already implemented through history tables (`customer_logs`, etc.).
- **Query Logs**: Configure logging of critical or extensive queries.
- **Anomaly Alerts**: Monitor suspicious patterns (unusual access, bulk changes).


### 3. Personal Data Protection (LGPD/GDPR)


- **Data Classification**: Identify and document fields with personal data.
- **Anonymization Process**: Define and implement procedures to anonymize data when requested.
  ```sql
  -- Example of anonymization procedure
  UPDATE customers
  SET
      name = 'Anonymized Customer',
      email = CONCAT('anonymized_', id, '@anonymous.com'),
      phone_local_code = NULL,
      phone_number = NULL,
      document_type = NULL
  WHERE id = ?;
  ```
- **Limited Retention**: Implement personal data retention policies.


### 4. Backup and Recovery


- **Regular Backups**: Define frequency (daily, incremental) and retention.
- **Recovery Tests**: Periodically validate restoration capability.
- **Defined RPO/RTO**: Establish and pursue Recovery Point Objectives and Recovery Time Objectives.


(Ref: DB Design Principles, ID core_db_design_001)


## Schema Evolution and Extension


The database schema will evolve with business requirements and platform integrations.


**Principle**: Manage all schema changes (addition of tables/columns, type modifications, etc.) using a database versioning and migration system.


**Justification**:
- **Consistency**: Ensures that the schema in all environments is consistent and traceable.
- **Automation**: Allows applying changes reliably and repeatably.
- **Traceability**: Creates a clear history of all schema modifications.


### Implementation Guidelines


- **Migration Tool**: Use a tool like Flyway or Liquibase.
- **Idempotent Scripts**: Write migration scripts that can be executed multiple times without undesired side effects.
- **Backward Compatibility**: Prioritize schema changes that are compatible with previous versions of the application.
- **Review Process**: All schema change proposals must go through a peer review process.


### Introduction of New Platforms


To add support for a new sales platform:


1. **Compatibility Validation**: Verify if the new platform's data fits the existing model.
2. **Status Mapping**: Add mappings from the new platform's statuses to normalized statuses.
3. **Enum Extension**: If necessary, add new values to enumerated types.
4. **Import Scripts**: Develop ETL routines specific to the new platform.


The **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)** document provides detailed guidelines on how to integrate new platforms into the existing system.


### New Business Models


The schema supports extension for new business models (e.g., usage-based pricing, marketplace, physical products) by adding tables or fields as needed, maintaining the core structure.


(Ref: DB Design Principles, ID core_db_design_001)


## Strategies for Common Queries


The database design efficiently supports various common analytical and operational queries. Below are examples of how the data can be queried to obtain business insights, demonstrating the applicability of the design principles.


### 1. Unified Financial Reports


Example: Total revenue by month, including all platforms:


```sql
SELECT
    DATE_TRUNC('month', t.order_date) AS month,
    t.payment_gateway,
    SUM(t.offer_price) AS gross_revenue,
    SUM(t.platform_fee_amount) AS platform_fees,
    SUM(t.partner_commission_amount) AS commission_fees,
    SUM(t.producer_net_amount) AS net_revenue,
    t.currency_code
FROM
    transactions t
JOIN
    transaction_statuses ts ON t.status_id = ts.id
WHERE
    ts.status = 'Approved'
    AND t.order_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY
    DATE_TRUNC('month', t.order_date), t.payment_gateway, t.currency_code
ORDER BY
    month, t.payment_gateway;
```
(Ref: DB Design Principles, ID core_db_design_001)


### 2. Subscription Analysis and Recurring Revenue


Example: MRR (Monthly Recurring Revenue) calculation:


```sql
SELECT
    DATE_TRUNC('month', t.order_date) AS month,
    COUNT(DISTINCT s.id) AS active_subscriptions,
    SUM(
        CASE
            WHEN p.recurrence_period = 'MONTH' THEN t.offer_price
            WHEN p.recurrence_period = 'YEAR' THEN t.offer_price / 12
            WHEN p.recurrence_period = 'QUARTER' THEN t.offer_price / 3
            ELSE t.offer_price -- Consider other periods or one-time charges in subscriptions
        END
    ) AS monthly_recurring_revenue
FROM
    subscriptions s
JOIN
    transactions t ON s.id = t.subscription_id -- Joins recurring transactions to subscription
JOIN
    transaction_statuses ts ON t.status_id = ts.id
JOIN
    plans p ON s.plan_id = p.id
JOIN
    transaction_statuses subts ON s.status_id = subts.id
WHERE
    ts.status = 'Approved' -- Consider only approved transactions
    AND subts.status = 'Active' -- Consider only active subscriptions in the period
    AND t.is_subscription = true -- Only recurrence transactions
    AND t.order_date BETWEEN '2023-01-01' AND '2023-12-31' -- Filter by period
GROUP BY
    DATE_TRUNC('month', t.order_date)
ORDER BY
    month;
```
(Ref: DB Design Principles, ID core_db_design_001)


### 3. Unified Customer Analysis


Example: Customer value (LTV) considering multiple platforms:


```sql
SELECT
    c.id,
    c.email,
    c.name,
    COUNT(DISTINCT t.id) AS transactions_count,
    SUM(t.offer_price) AS total_spend,
    MIN(t.order_date) AS first_purchase_date,
    MAX(t.order_date) AS last_purchase_date,
    COUNT(DISTINCT t.payment_gateway) AS platforms_used
FROM
    customers c
JOIN
    transactions t ON c.id = t.customer_id
JOIN
    transaction_statuses ts ON t.status_id = ts.id
WHERE
    ts.status = 'Approved'
GROUP BY
    c.id, c.email, c.name
ORDER BY
    total_spend DESC;
```
(Ref: DB Design Principles, ID core_db_design_001)


### 4. Unified Marketing Performance


Example: Conversions and revenue by campaign:


```sql
SELECT
    puh.utm_campaign,
    puh.utm_source,
    puh.utm_medium,
    COUNT(DISTINCT t.id) AS conversions,
    SUM(t.offer_price) AS revenue,
    SUM(t.offer_price) / COUNT(DISTINCT t.id) AS average_order_value
FROM
    platform_utm_history puh
JOIN
    transactions t ON puh.transaction_id = t.id
JOIN
    transaction_statuses ts ON t.status_id = ts.id
WHERE
    ts.status = 'Approved'
    AND t.order_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY
    puh.utm_campaign, puh.utm_source, puh.utm_medium
ORDER BY
    revenue DESC;
```
(Ref: DB Design Principles, ID core_db_design_001)


## Best Practices for Use and Maintenance


To ensure the integrity and performance of the database over time, it is recommended to follow these practices:


### 1. Regular Maintenance


- **VACUUM**: Schedule VACUUM ANALYZE regularly to reclaim space and update statistics.
- **Index Reconstruction**: Rebuild fragmented indexes periodically (`REINDEX`).
- **Bloat Monitoring**: Check and correct bloated tables and indexes.


### 2. Efficient Queries


- **Avoid SELECT ***: Always list only the necessary columns.
- **Limit on Large Queries**: Use LIMIT/OFFSET to paginate large results.
- **Efficient Joins**: Ensure that joins are done on indexed columns.
- **Subqueries vs CTEs**: Prefer CTEs (WITH) for better readability and, in many cases, performance.
- **EXPLAIN ANALYZE**: Use to understand and optimize the execution plan of slow queries.


### 3. Transactions and Concurrency


- **Short Transactions**: Avoid long transactions that lock resources.
- **Appropriate Isolation**: Choose the appropriate isolation level for each operation.
- **Avoid Deadlocks**: Access tables always in the same order in complex transactions.


### 4. Continuous Monitoring


- **Slow Queries**: Monitor and optimize queries that take longer than expected (using `pg_stat_statements`).
- **Resource Utilization**: Track CPU, memory, IO, and disk space usage.
- **Locks and Waits**: Identify and resolve contention for locks.
- **Data Growth**: Plan capacity based on growth trends.


### 5. Documentation


- **Keep Comments Updated**: Ensure that new fields and tables have descriptive comments.
- **Document Complex Queries**: Add explanatory comments to critical or complex queries.
- **Report Catalog**: Maintain a library of frequently used queries with documentation.


(Ref: DB Design Principles, ID core_db_design_001)


## Resources and References


### Related Documentation


- **[Unified Database Architecture](core_db_arch_001)**: Overview and organization into domains.
- **[Multi-platform Integration Strategy](platform_integration_strategy_001)**: Details on how data from multiple platforms are integrated and normalized.
- **[Unified Database Glossary of Terms](core_db_glossary_001)**: Definitions of technical and business terms.
- **[Detailed Database Schema Reference](ref_db_schema_001)**: Complete SQL definitions of all objects.
- **[Customer Ecosystem Domain](domain_customers_ecosystem_001)**: Details about the customer domain.
- **[Product Catalog Domain](domain_products_catalog_001)**: Details about the product domain.
- **[Transaction Lifecycle Domain](domain_transactions_lifecycle_001)**: Details about the transaction domain.
- **[Subscription Management Domain](domain_subscriptions_management_001)**: Details about the subscription domain.
- **[Commission System Domain](domain_commission_system_001)**: Details about the commission domain.
- **[Platform Integration Details Domain](domain_platform_integration_details_001)**: Details about the platform integration domain.


### Tool Recommendations


- **Monitoring**: pgAdmin, pg_stat_statements, pgBadger, Datadog, New Relic.
- **Maintenance**: pg_repack, pg_stat_monitor.
- **Backup**: pg_dump, Barman, Cloud Provider Managed Backups.
- **Migrations**: Flyway, Liquibase.


### Contacts and Support


For questions related to database design and maintenance:


- **Technical Responsible**: [Name of DBA or Data Architect]
- **Support Email**: [Data Team Email]
- **Internal Documentation**: [Link to Wiki or Expanded Documentation]


(Ref: DB Design Principles, ID core_db_design_001)


## Conclusion


The design principles outlined in this document form the backbone of the `joaocastanheira_bancodedados` database. By following these guidelines for keys, normalization, naming, data types, null handling, referential integrity, indexing, security, and evolution, we ensure that the database remains a reliable, efficient, and adaptable data foundation to support current and future business needs. The strategies for performance, security, and maintenance, along with the best practices for use, are essential for the longevity and success of this unified system.


A fundamental principle that runs through all aspects of this design is the ability to integrate and normalize data from multiple platforms, as detailed in the **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)** document. This approach allows the system to evolve organically to incorporate new data sources without compromising its core structure.


(Ref: DB Design Principles, ID core_db_design_001)
```