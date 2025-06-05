# `Core_DB_Glossary.md` 


```markdown
---
title: "Unified Database Glossary"
id: "core_db_glossary_001"
doc_type: "glossary"
doc_version: "1.2"
date_created: "2025-04-23"
date_updated: "2025-04-24"
author: "João Castanheira"
db_name: "joaocastanheira_bancodedados"
db_version: "1.0"
doc_status: "Active"
environment: "Production"
language: "en"
response_languages: ["pt-BR", "en"]
technical_terms_preservation: "strict"
original_language: "pt-BR"
related_docs: [
  "core_db_arch_001", 
  "core_db_design_001", 
  "platform_integration_strategy_001",
  "ref_db_schema_details_001",
  "ref_api_mapping_guide_001"
]
technical_terms: {
  "table_names": [
    "customers", "addresses", "customer_logs", "products", "plans", 
    "offers", "transactions", "transaction_items", "transaction_status_history", 
    "transaction_fees", "subscriptions", "subscription_status_history", 
    "commission_participants", "platform_commission", "participant_addresses", 
    "transaction_statuses", "platform_transaction_payment_history", 
    "platform_utm_history", "platform_software_invoice_history", 
    "platform_sale_offer_history"
  ],
  "column_names": [
    "id", "customer_id", "product_id", "plan_id", "offer_id", "transaction_id", 
    "subscription_id", "platform_id", "platform_origin", "payment_gateway", 
    "status_id", "source", "is_subscription", "recurrence_number", 
    "offer_price", "platform_fee_amount", "partner_commission_amount", 
    "producer_net_amount", "email", "name", "document", "document_type", 
    "created_at", "updated_at", "billing_cycle", "trial_days",
    "subscriber_id", "card_brand", "order_date", "payment_method", 
    "payment_type", "currency_code", "recurrence_period", "metadata"
  ],
  "data_types": [
    "SERIAL", "VARCHAR", "TEXT", "NUMERIC", "BOOLEAN", 
    "TIMESTAMP WITH TIME ZONE", "INTEGER", "JSONB"
  ],
  "sql_keywords": [
    "PRIMARY KEY", "FOREIGN KEY", "REFERENCES", "CONSTRAINT", 
    "UNIQUE", "NOT NULL", "DEFAULT", "ON DELETE CASCADE", 
    "ON DELETE RESTRICT", "ON DELETE SET NULL"
  ],
  "enum_types": [
    "payment_method_enum", "payment_type_enum"
  ],
  "enum_values": [
    "credit_card", "debit_card", "boleto", "pix", "paypal", 
    "bank_transfer", "digital_wallet", "SINGLE_PAYMENT", "INSTALLMENT_PAYMENT"
  ],
  "status_values": [
    "Approved", "Refunded", "Canceled", "Pending", "Failed", "Active", "Inactive"
  ]
}
embedding_guide_concepts: [
  "database terminology", 
  "unified vocabulary", 
  "term normalization", 
  "technical definitions", 
  "multi-platform glossary", 
  "transaction terminology", 
  "subscription terminology", 
  "commission terminology", 
  "integration terminology", 
  "concept mapping",
  "platform abstraction",
  "terminology standardization"
]
---


# Unified Database Glossary


## Technical Terms Reserved (Do Not Translate)


> **Critical Preservation Note**: The terms listed below should NEVER be translated, altered, or modified in any context. They represent technical entity names in the database that must be preserved exactly as they are.


| Technical Term | Type | Description |
|---------------|------|-----------|
| `customers` | Table | Stores unified customer information across platforms |
| `addresses` | Table | Stores addresses associated with customers |
| `customer_logs` | Table | Records changes to customer data |
| `products` | Table | Unified product catalog across platforms |
| `plans` | Table | Subscription plan definitions |
| `offers` | Table | Specific offers for products or plans |
| `transactions` | Table | Financial transaction records across platforms |
| `transaction_items` | Table | Items included in each transaction |
| `transaction_status_history` | Table | History of transaction status changes |
| `transaction_fees` | Table | Fees applied to transactions |
| `subscriptions` | Table | Active and historical subscriptions |
| `subscription_status_history` | Table | History of subscription status changes |
| `commission_participants` | Table | Details of participants eligible for commissions |
| `platform_commission` | Table | Commission records per transaction |
| `participant_addresses` | Table | Addresses of commission participants |
| `transaction_statuses` | Table | Normalized definition of transaction statuses |
| `platform_transaction_payment_history` | Table | Platform-specific payment history |
| `platform_utm_history` | Table | UTM data captured in transactions |
| `platform_software_invoice_history` | Table | Invoice records |
| `platform_sale_offer_history` | Table | Snapshot of offers at the time of sale |


## Purpose


This glossary establishes a consistent and standardized vocabulary for understanding and operating the `joaocastanheira_bancodedados` database. The objective is to provide a central reference of technical terms, entities, and concepts that are fundamental to the system's operation, especially in the context of its platform-agnostic architecture.


Terminology standardization is particularly important considering that this database unifies data from multiple platforms, each with its own vocabulary and conventions. The terminology defined here represents the normalized concepts after the integration process described in **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)**.


(Ref: Database Glossary, ID core_db_glossary_001)


## Fundamental Terms


### A


#### Affiliate
A participant who promotes third-party products and receives commission for generated sales. In the database, it is represented as a record in the `commission_participants` table with an appropriate value in the `source` field.


#### Adapter (Platform Adapter)
Software component responsible for converting raw data from a specific platform (such as Hotmart or Kiwify) to the normalized database format. Implements a common interface that abstracts the differences between APIs. For implementation details, see **[Multi-platform Integration Strategy - Platform-Specific Adapters](platform_integration_strategy_001.md#platform-specific-adapters)**.


### B


#### Billing Cycle
Interval between recurring charges in a subscription. Represented in the `billing_cycle` field of the `subscriptions` table. Common examples include "MONTHLY" and "YEARLY".


### C


#### Checkout
Purchase completion process that results in a transaction. In the database context, corresponds to a record in the `transactions` table that is not part of a recurring subscription.


#### Chunking
Process of dividing long documents into smaller pieces (chunks) to optimize retrieval in RAG (Retrieval-Augmented Generation) systems. Important for effective indexing of this database's documentation.


#### Commission
Monetary value paid to a participant (producer, affiliate, co-producer) for a transaction. Recorded in the `platform_commission` table.


#### Commission Participant
Entity (producer, affiliate, co-producer) that receives a portion of transaction revenue, recorded in the `commission_participants` table.


#### Co-producer
Participant who collaborates in creating or selling a product and receives a portion of the revenue. In the database, it is represented as a record in the `commission_participants` table with an appropriate value in the `source` field.


#### Customer
Entity that makes purchases or subscribes to products. Represented by the `customers` table and uniquely identified by the normalized email address.


### D


#### Denormalization
Process of adding controlled redundancy to a normalized schema to improve read performance for specific queries. Technique selectively applied in this database for frequently queried fields.


### E


#### Embedding
Vector representation of text or data in a multidimensional space, capturing semantic meaning for similarity searches in RAG systems. Used to efficiently index and query this database's documentation.


#### ETL Pipeline
Process (Extract, Transform, Load) used to extract data from source platforms, transform it to the unified model, and load it into the database. Implemented according to the **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)**.


### H


#### Historical Storage
Design strategy where important changes to entities (such as status changes) are recorded in dedicated history tables, such as `transaction_status_history` and `subscription_status_history`.


### I


#### Indexing
Creation of data structures (indexes) that accelerate row retrieval from a table based on values from one or more columns. Important strategy for optimizing query performance in this database.


#### Installment Payment
Payment method where the total amount is divided into multiple partial payments over time. Represented as `INSTALLMENT_PAYMENT` in the `payment_type_enum`.


### J


#### JSONB
Data type in PostgreSQL for efficiently storing semi-structured data in JSON format, with indexing support. Used to store platform-specific metadata that doesn't fit into the normalized relational model.


### L


#### Lookup Table
Auxiliary table used to store a set of values (e.g., transaction status) that can be referenced by other tables, facilitating normalization and flexibility. The `transaction_statuses` table is an example of a lookup table in this database.


### M


#### Multi-platform Identification
Design strategy where each entity has a sequential internal ID (`id`) for internal references, while preserving the original identifiers from external platforms (such as `product_id` + `platform_origin` for products). This approach is essential for unifying data from different sources. For details on this strategy, see **[Multi-platform Integration Strategy - Unique Identification with Traceability](platform_integration_strategy_001.md#unique-identification-with-traceability)**.


### N


#### Normalized Status
Standardized representation of a transaction or subscription state, regardless of the terminology used by the source platform. Stored in the `transaction_statuses` table and referenced by `status_id` in `transactions` and `subscriptions`. The mapping process between original platform statuses and these normalized values is detailed in **[Multi-platform Integration Strategy - Transaction Status Mapping](platform_integration_strategy_001.md#transaction-status-mapping)**.


#### NUMERIC(p, s)
Exact precision numeric data type in PostgreSQL, ideal for monetary values (`NUMERIC(15, 4)` in this DB). `p` is the total precision, `s` is the scale (digits after the decimal point).


### O


#### Offer
Specific combination of a product or plan with particular commercial conditions (price, payment form, etc.). Represented by the `offers` table and uniquely identified by the combination of `offer_id` and `platform_origin`.


#### Offer Snapshot
Copy of offer details at the time of sale, preserved for historical reference even if the offer is later modified. Stored in the `platform_sale_offer_history` table.


#### ON DELETE CASCADE
FK rule specifying that if the referenced row in the parent table is deleted, the corresponding rows in the child table will also be automatically deleted. Applied in relationships where child records have no meaning without the parent record.


#### ON DELETE RESTRICT
FK rule (default behavior) that prevents deletion of a row in the parent table if there are corresponding rows in the child table. Protects against deletions that would break referential integrity.


#### ON DELETE SET NULL
FK rule specifying that if the referenced row in the parent table is deleted, the foreign key columns in the corresponding rows in the child table will be set to `NULL`. Used when the relationship is optional.


### P


#### Payment Gateway
System responsible for payment processing. In this database context, refers to the platform that processed the transaction (e.g., "Hotmart", "Kiwify"). Stored in the `payment_gateway` field of the `transactions` table and the `payment_gateway` field of the `subscriptions` table. This field is one of the identifiers that, along with the original platform IDs, allows unified entity identification. See more in **[Multi-platform Integration Strategy - Entity Identification and Reconciliation](platform_integration_strategy_001.md#entity-identification-and-reconciliation)**.


#### Payment Method
Form used by the customer to make the payment. In the database, it is normalized as an enumerated type `payment_method_enum`, with values such as "credit_card", "boleto", "pix", etc. The normalization process of these values from different platform terminologies is described in **[Multi-platform Integration Strategy - Vocabulary Mapping](platform_integration_strategy_001.md#vocabulary-mapping)**.


#### Payment Type
Classification of payment as single or installment. In the database, it is normalized as an enumerated type `payment_type_enum`, with values "SINGLE_PAYMENT" (one-time) or "INSTALLMENT_PAYMENT" (in installments).


#### Platform Event
Notification sent by an external platform (via webhook or other mechanism) informing about a significant occurrence, such as a new sale, status change, or subscription cancellation. These events are normalized by the integration system before affecting the database. The processing of these events is detailed in **[Multi-platform Integration Strategy - Normalization Process](platform_integration_strategy_001.md#normalization-process)**.


#### Platform Fee
Amount charged by the sales platform (such as Hotmart or Kiwify) on a transaction. Recorded in the `transaction_fees` table with the appropriate type.


#### Platform of Origin
External system from which the data was originally extracted (e.g., "Hotmart", "Kiwify"). Stored in the `platform_origin` fields across various tables and used as part of the composite identification for imported entities. This concept is fundamental to the platform-agnostic architecture, allowing unification of data from multiple sources while preserving their origin. For details on how the system handles multiple platforms, see **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)**.


#### Plan
Recurring subscription configuration, defining product, price, and conditions such as billing cycle and trial period. Represented by the `plans` table and uniquely identified by the combination of `plan_id` and `platform_origin`.


#### Principle of Least Privilege
Security concept dictating that users or systems should have only the data access permissions strictly necessary to perform their functions. Applied in database permission configuration.


#### Producer
Main creator of a product, who receives the majority of revenue after deductions for fees and commissions. In the database, it is represented as a record in the `commission_participants` table with an appropriate value in the `source` field.


#### Product
Basic item for sale, which can be sold directly or through subscription plans. Represented by the `products` table and uniquely identified by the combination of `product_id` and `platform_origin`.


### R


#### RAG (Retrieval-Augmented Generation)
AI architecture that combines text generation by LLMs with information retrieval from an external knowledge base (such as this documentation). This documentation is optimized for use in RAG systems.


#### Recurrence
Periodic charge made as part of a subscription. Represented as a record in the `transactions` table with `is_subscription` = true and linked to a subscription through the `subscription_id` field.


#### Recurrence Number
Sequential counter that identifies the position of a recurring transaction within a subscription. For example, the third monthly charge will have `recurrence_number` = 3. Stored in the `recurrence_number` field of the `transactions` table.


#### Referential Integrity
Set of rules ensuring that relationships between tables (via FKs) are valid and consistent. Implemented through foreign keys with appropriate constraints.


#### Refund
Return of the amount paid for a transaction. Represented as a status change of the transaction to "Refunded" in the `transaction_status_history` table.


### S


#### Schema Versioning
Practice of tracking and managing changes to the database structure over time, typically using migration tools. Essential for controlled database evolution.


#### SERIAL
Pseudotype in PostgreSQL that creates a sequence, sets the column as `NOT NULL`, and assigns a default value from the next sequence, commonly used for auto-incrementing primary keys (such as the `id` field in most tables).


#### Single Payment
One-time payment made in full at the time of purchase. Represented as `SINGLE_PAYMENT` in the `payment_type_enum`.


#### snake_case
Naming convention where words are separated by underscores (e.g., `column_name`). Standard for table and column names in this DB, consistent throughout the data model.


#### Subscriber ID
Unique identifier of the subscriber in the platform of origin. Stored in the `subscriber_id` field of the `subscriptions` table.


#### Subscription
Recurring payment agreement for access to a product or service over time. Represented by the `subscriptions` table and uniquely identified by the combination of `subscription_id` and `payment_gateway`.


#### Subscription ID
Unique identifier of the subscription in the platform of origin. Stored in the `subscription_id` field of the `subscriptions` table.


### T


#### Third Normal Form (3NF)
Database normalization level ensuring that all columns in a table depend only on the primary key and not on other non-key columns. Basis for this database's design, ensuring data integrity.


#### TIMESTAMP WITH TIME ZONE
Data type in PostgreSQL that stores an absolute point in time, automatically adjusting to time zones. Essential for accurately recording chronological events, used in the `created_at`, `updated_at`, and other timestamp fields.


#### Transaction
Record of a sale or recurring charge. Represented by the `transactions` table and uniquely identified by the combination of `transaction_id` and `payment_gateway`.


#### Transaction Item
Product, plan, or offer acquired in a specific transaction. Represented in the `transaction_items` table, which relates a transaction to the acquired products, plans, or offers.


#### Trial
Initial free period in a subscription. Configured in the `trial_days` field of the `plans` table.


### U


#### UNIQUE Constraint
Rule ensuring that all values in a column (or set of columns) are distinct within the table. Used to implement uniqueness, such as the combination of `product_id` and `platform_origin` in the `products` table.


### Y


#### YAML Front Matter
Metadata block at the top of a Markdown file, delimited by `---`, used to provide structured information about the document for systems like RAG. Used throughout this database's documentation.


(Ref: Database Glossary, ID core_db_glossary_001)


## Main Entity Identifiers


The table below summarizes how the main entities are identified in the database, combining sequential internal IDs with external identifiers from the source platforms:


| Entity | Internal ID | External ID | Uniqueness |
|----------|------------|------------|-----------|
| Customer | `customers.id` | `customers.customer_id` | `customers.email` (unique) |
| Product | `products.id` | `products.product_id` | `(product_id, platform_origin)` |
| Plan | `plans.id` | `plans.plan_id` | `(plan_id, platform_origin)` |
| Offer | `offers.id` | `offers.offer_id` | `(offer_id, platform_origin)` |
| Transaction | `transactions.id` | `transactions.transaction_id` | `(transaction_id, payment_gateway)` |
| Subscription | `subscriptions.id` | `subscriptions.subscription_id` | `(subscription_id, payment_gateway)` |
| Participant | `commission_participants.id` | `commission_participants.platform_id` | `(platform_id, platform_origin)` |


For more details on the strategy for identifying and reconciling entities across platforms, see **[Multi-platform Integration Strategy - Entity Identification and Reconciliation](platform_integration_strategy_001.md#entity-identification-and-reconciliation)**.


(Ref: Database Glossary, ID core_db_glossary_001)


## Platform-Specific Vocabulary


The table below presents examples of how common concepts are referred to in different platforms and their normalized representation in the database:


| Normalized Concept | Hotmart Term | Kiwify Term | Database Field |
|----------------------|---------------|--------------|--------------------------|
| Customer | "Buyer" | "Customer" | `customers` |
| Product | "Product" | "Product" | `products` |
| Plan | "Plan" | "Plan" | `plans` |
| Transaction | "Purchase" | "Checkout" | `transactions` |
| Subscription | "Subscription" | "Subscription" | `subscriptions` |
| Affiliate | "Affiliate" | "Affiliate" | `commission_participants` (source = "AFFILIATE") |
| Producer | "Producer" | "Owner" | `commission_participants` (source = "PRODUCER") |
| Commission | "Commission" | "Commission" | `platform_commission` |
| Status: Approved | "APPROVED" | "paid" | `transaction_statuses.status = 'Approved'` |
| Status: Refunded | "REFUNDED" | "refunded" | `transaction_statuses.status = 'Refunded'` |
| Status: Canceled | "CANCELED" | "canceled" | `transaction_statuses.status = 'Canceled'` |


This table illustrates the importance of the normalization process implemented by the **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)**. For a complete and updated list of mappings between platform-specific terms and the normalized vocabulary, see the **[API Mapping Guide](ref_api_mapping_guide_001.md)** document.


(Ref: Database Glossary, ID core_db_glossary_001)


## Conventions and Nomenclature


### Table Naming Conventions


- **Main tables**: Plural name, representing the entity (e.g., `customers`, `products`)
- **History tables**: Suffix `_history` or `_logs` (e.g., `transaction_status_history`, `customer_logs`)
- **Mapping tables**: Prefix indicating the domain (e.g., `platform_commission`, `platform_utm_history`)


### Column Naming Conventions


- **Primary keys**: Always `id`
- **Foreign keys**: Singular name of the referenced table + `_id` (e.g., `customer_id`, `product_id`)
- **External identifiers**: Descriptive name of the ID type (e.g., `transaction_id`, `subscription_id`)
- **Platform of origin**: Consistently `platform_origin` or `payment_gateway` depending on the context
- **Timestamps**: Always `created_at` and `updated_at` for temporal tracking


These conventions are consistent throughout the database, facilitating understanding and navigation between related tables.


For more details on the technical conventions adopted, see **[Database Design Principles - Technical Conventions](core_db_design_001.md#technical-conventions)**.


(Ref: Database Glossary, ID core_db_glossary_001)


## Specialized Data Types


### Enumerated Types


The database uses PostgreSQL enumerated types (ENUM) to ensure consistency in categorical values:


#### payment_method_enum
Enumerates the accepted payment methods:
- `credit_card`: Credit Card
- `debit_card`: Debit Card
- `boleto`: Boleto (Brazilian payment slip)
- `pix`: PIX (Brazilian instant payment)
- `paypal`: PayPal
- `bank_transfer`: Bank Transfer
- `digital_wallet`: Digital Wallets (e.g., Google Pay, Apple Pay)
- Other values (see complete schema)


#### payment_type_enum
Classifies the payment type:
- `SINGLE_PAYMENT`: One-time payment
- `INSTALLMENT_PAYMENT`: Payment in installments


The normalization process of original platform values to these enumerated types is implemented by the **[Multi-platform Integration Strategy - Payment Method Mapping](platform_integration_strategy_001.md#payment-method-mapping)**.


### Data Types for Common Fields


- **Identifiers**: Usually VARCHAR to preserve original format
- **Monetary values**: NUMERIC(15, 4) for precision with 4 decimal places
- **Dates and timestamps**: TIMESTAMP WITH TIME ZONE to preserve timezone
- **Long texts**: TEXT for content of variable or unknown length
- **Booleans**: BOOLEAN for flags and binary indicators


For complete details on the data types used in each table, see **[Detailed Schema Reference](ref_db_schema_details_001.md)**.


(Ref: Database Glossary, ID core_db_glossary_001)


## Conclusion


This glossary provides a solid terminological foundation for understanding the structure and operation of the `joaocastanheira_bancodedados` database. The standardization of terms is especially important considering that the database unifies data from multiple platforms with different terminologies.


The terms and concepts defined in this document reflect the platform-agnostic nature of the design, where different data sources are normalized to a consistent model as detailed in the **[Multi-platform Integration Strategy](platform_integration_strategy_001.md)**.


It is recommended that all users and developers working with this database familiarize themselves with this terminology to ensure clear and consistent communication.


(Ref: Database Glossary, ID core_db_glossary_001)
```