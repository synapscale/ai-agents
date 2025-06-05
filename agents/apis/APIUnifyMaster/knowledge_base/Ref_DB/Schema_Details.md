# `Ref_DB_Schema_Details.md` 


```markdown
---
title: "Technical Reference: Database Schema Details"
id: "ref_db_schema_details_001"
doc_type: "technical_reference"
doc_version: "1.0"
date_created: "2025-04-23" 
date_updated: "2025-04-24" 
author: "João Castanheira (Schema Extracted)"
db_name: "joaocastanheira_bancodedados"
db_version: "1.0"
doc_status: "Generated"
environment: "Production"
language: "en"
response_languages: ["pt-BR", "en"]
technical_terms_preservation: "strict"
original_language: "pt-BR"
related_docs: ["core_db_arch_001", "core_db_design_001", "core_db_glossary_001"]
db_engine: "PostgreSQL 13+"
tables_in_scope: [
    "addresses", "commission_participants", "customer_logs", "customers", 
    "offers", "participant_addresses", "plans", "platform_commission", 
    "platform_sale_offer_history", "platform_software_invoice_history", 
    "platform_transaction_payment_history", "platform_utm_history", "products", 
    "subscriptions", "subscription_status_history", "transaction_fees", 
    "transaction_items", "transaction_statuses", "transaction_status_history", 
    "transactions"
]
technical_terms: {
  "table_names": [
    "addresses", "commission_participants", "customer_logs", "customers", 
    "offers", "participant_addresses", "plans", "platform_commission", 
    "platform_sale_offer_history", "platform_software_invoice_history", 
    "platform_transaction_payment_history", "platform_utm_history", "products", 
    "subscriptions", "subscription_status_history", "transaction_fees", 
    "transaction_items", "transaction_statuses", "transaction_status_history", 
    "transactions"
  ],
  "column_names": [
    "id", "address", "neighborhood", "country", "city", "zip_code", "complement", 
    "number", "ip", "created_at", "updated_at", "state", "platform_id", 
    "platform_origin", "email", "name", "trader_name", "locale", "phone_local_code", 
    "phone_number", "document_type", "document_number", "customer_id", "field_name", "old_value", 
    "new_value", "changed_by", "address_id", "offer_id", "description", "plan_id", 
    "product_id", "payment_mode", "price", "currency_code", "participant_id", 
    "amount", "source", "code", "offer_name", "invoice_number", "invoice_series", 
    "invoice_key", "issue_date", "status", "xml_url", "pdf_url", "payment_method", 
    "payment_type", "installments", "value", "payment_date", "card_brand", 
    "card_last_digits", "bank_slip_barcode", "pix_code", "metadata", "utm_source", 
    "utm_medium", "utm_campaign", "utm_term", "utm_content", "capture_date", 
    "subscription_id", "subscriber_id", "initial_transaction_id", "payment_gateway", 
    "billing_cycle", "total_recurrences", "max_cycles", "last_update", "start_date", 
    "end_date", "status_id", "request_billet", "next_billing_date", "cancel_date", 
    "change_date", "reason", "fee_type", "total_amount", "fee_currency_code", 
    "base_amount", "fixed_amount", "quantity", "unit_price", "transaction_id", 
    "payment_engine", "installments_number", "gateway_transaction_id", "billet_url", 
    "billet_barcode", "base_price", "offer_price", "customer_paid_amount", 
    "platform_fee_amount", "distributable_amount", "partner_commission_amount", 
    "producer_net_amount", "is_subscription", "platform_subscription_id", 
    "recurrence_number", "tracking_source", "tracking_sck", "under_warranty", 
    "warranty_expire_date", "order_date"
  ],
  "enum_types": [
    "payment_method_enum", "payment_type_enum"
  ],
  "enum_values": [
    "credit_card", "debit_card", "two_credit_cards", "boleto", 
    "boleto_installment", "pix", "pix_credit_card", "bank_transfer", 
    "paypal", "digital_wallet", "intelligent_recovery", "account_balance", 
    "hotmart_balance", "other", "cryptocurrency", "SINGLE_PAYMENT", 
    "INSTALLMENT_PAYMENT"
  ],
  "sql_keywords": [
    "CREATE", "TABLE", "TYPE", "ENUM", "PRIMARY KEY", "REFERENCES", 
    "ON DELETE CASCADE", "DEFAULT", "CONSTRAINT", "UNIQUE", "INDEX",
    "BEFORE UPDATE", "FOR EACH ROW", "EXECUTE PROCEDURE", 
    "SERIAL", "VARCHAR", "TEXT", "NUMERIC", "BOOLEAN", 
    "TIMESTAMP WITH TIME ZONE", "INTEGER", "JSONB", "NOT NULL", "COMMENT"
  ],
  "functions": [
    "update_updated_at_column()"
  ]
}
embedding_guide_concepts: [
  "database schema", "table definition", "column definition", 
  "data types", "constraints", "primary keys", "foreign keys", 
  "indexes", "triggers", "database functions", "schema comments", 
  "SQL technical reference", "data structure", "physical data model"
]
---


# Technical Reference: Database Schema Details


This document provides a complete and detailed technical reference of the `joaocastanheira_bancodedados` database schema, extracted directly from SQL definitions. It includes details about tables, columns, data types, constraints, indexes, functions, and triggers.


**Note:** This document is generated from the current state of the schema and should be updated whenever modifications are made to the database structure.


(Ref: DB Schema Details, ID ref_db_schema_details_001)


## Custom Enumerated Types


### `payment_method_enum`


```sql
CREATE TYPE payment_method_enum AS ENUM (
    'credit_card',           -- Credit Card
    'debit_card',            -- Debit Card
    'two_credit_cards',      -- Payment with two cards
    'boleto',                -- Brazilian bank slip (one-time)
    'boleto_installment',    -- Brazilian bank slip (installments)
    'pix',                   -- PIX (Brazilian instant payment)
    'pix_credit_card',       -- PIX + Credit Card
    'bank_transfer',         -- Bank Transfer
    'paypal',                -- PayPal
    'digital_wallet',        -- Digital Wallets (e.g., Google Pay, Apple Pay)
    'intelligent_recovery',  -- Intelligent Recovery
    'account_balance',       -- Account Balance
    'hotmart_balance',       -- Hotmart Balance
    'other',                 -- Other methods
    'cryptocurrency'         -- Cryptocurrencies
);
COMMENT ON TYPE payment_method_enum IS 'Defines the payment methods accepted by the system (e.g., Credit Card, Boleto, PIX). Mapped from API strings.';
ALTER TYPE payment_method_enum OWNER TO doadmin;
```


### `payment_type_enum`


```sql
CREATE TYPE payment_type_enum AS ENUM (
    'SINGLE_PAYMENT',       -- One-time payment
    'INSTALLMENT_PAYMENT'   -- Payment in installments
);
COMMENT ON TYPE payment_type_enum IS 'Defines whether the payment was made as a single payment or in installments.';
ALTER TYPE payment_type_enum OWNER TO doadmin;
```


(Ref: DB Schema Details - Enums, ID ref_db_schema_details_001)


## Trigger Function


### `update_updated_at_column()`


```sql
CREATE OR REPLACE FUNCTION update_updated_at_column() RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
END;
$$;
COMMENT ON FUNCTION update_updated_at_column() IS 'Trigger function that automatically updates the updated_at column to the current timestamp whenever a row is modified.';
ALTER FUNCTION update_updated_at_column() OWNER TO doadmin;
```


(Ref: DB Schema Details - Trigger Function, ID ref_db_schema_details_001)


## Table Definitions


Below are the detailed definitions for each table in the schema, including structure, comments, indexes, and associated triggers.


---


### Table: `addresses`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS addresses (
    id           SERIAL PRIMARY KEY,
    address      VARCHAR(255),                              -- Street address
    neighborhood VARCHAR(100),                              -- Neighborhood
    country      VARCHAR(100),                              -- Country
    city         VARCHAR(100),                              -- City
    zip_code     VARCHAR(20),                               -- ZIP code
    complement   VARCHAR(255),                              -- Complement
    number       VARCHAR(20),                               -- Number
    ip           VARCHAR(45),                               -- Registration IP address
    created_at   TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at   TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    state        VARCHAR(100)                               -- State/Province
);
ALTER TABLE addresses OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE addresses IS 'Centralized repository of addresses, ensuring accuracy and traceability of customer locations.';
COMMENT ON COLUMN addresses.id IS 'Unique sequential identifier for the address.';
COMMENT ON COLUMN addresses.address IS 'Street address (Street, Avenue, etc.).';
COMMENT ON COLUMN addresses.neighborhood IS 'Neighborhood.';
COMMENT ON COLUMN addresses.country IS 'Country (ISO code or name).';
COMMENT ON COLUMN addresses.city IS 'City.';
COMMENT ON COLUMN addresses.zip_code IS 'Postal code (ZIP/CEP).';
COMMENT ON COLUMN addresses.complement IS 'Address complement (Block, Apt, etc.).';
COMMENT ON COLUMN addresses.number IS 'Building number.';
COMMENT ON COLUMN addresses.ip IS 'IP address associated with the address registration (if applicable).';
COMMENT ON COLUMN addresses.created_at IS 'Timestamp of record creation.';
COMMENT ON COLUMN addresses.updated_at IS 'Timestamp of the last record update.';
COMMENT ON COLUMN addresses.state IS 'State/Province of the address.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_addresses_zip_code ON addresses (zip_code);
CREATE INDEX IF NOT EXISTS idx_addresses_city ON addresses (city);
CREATE INDEX IF NOT EXISTS idx_addresses_country ON addresses (country);
CREATE INDEX IF NOT EXISTS idx_addresses_state ON addresses (state);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_addresses_updated_at BEFORE UPDATE ON addresses FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `commission_participants`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS commission_participants (
    id               SERIAL PRIMARY KEY,
    platform_id      VARCHAR(255) NOT NULL,                -- Platform ID
    platform_origin  VARCHAR(100) NOT NULL,                -- Platform name
    email            VARCHAR(255),                         -- Participant email
    name             VARCHAR(255),                         -- Full name
    trader_name      VARCHAR(255),                         -- Business name
    locale           VARCHAR(20),                          -- Location/language
    created_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    phone_local_code VARCHAR(10),                          -- Area code
    phone_number     VARCHAR(20),                          -- Phone number
    document_type    VARCHAR(10),                          -- Document type
    document_number    VARCHAR(55)                           -- Document Number
    CONSTRAINT uq_participant_platform UNIQUE (platform_id, platform_origin)
);
ALTER TABLE commission_participants OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE commission_participants IS 'Stores commission participants (Hotmart: producers, affiliates; Kiwify: affiliates, partners). Addresses are stored in the participant_addresses table.';
COMMENT ON COLUMN commission_participants.id IS 'Internal unique identifier for the participant.';
COMMENT ON COLUMN commission_participants.platform_id IS 'Participant identifier in the source platform.';
COMMENT ON COLUMN commission_participants.platform_origin IS 'Name of the platform from which this participant originated (e.g., "Hotmart", "Kiwify").';
COMMENT ON COLUMN commission_participants.email IS 'Main email of the participant.';
COMMENT ON COLUMN commission_participants.name IS 'Full name or business name.';
COMMENT ON COLUMN commission_participants.trader_name IS 'Commercial, fantasy, or affiliate name.';
COMMENT ON COLUMN commission_participants.locale IS 'Participant locale/language code (e.g., "pt_BR").';
COMMENT ON COLUMN commission_participants.created_at IS 'Timestamp of participant record creation.';
COMMENT ON COLUMN commission_participants.updated_at IS 'Timestamp of the last participant record update.';
COMMENT ON COLUMN commission_participants.phone_local_code IS 'Area code or country code of the participant\'s phone.';
COMMENT ON COLUMN commission_participants.phone_number IS 'Participant\'s phone number (without area code).';
COMMENT ON COLUMN commission_participants.document_type IS 'Type of participant\'s document (e.g., "CPF", "CNPJ", "PASSPORT").';
COMMENT ON COLUMN customers.document_number IS 'Number of customer\'s document (e.g., "000.000.000-00").';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_commission_participants_email ON commission_participants (email);
CREATE INDEX IF NOT EXISTS idx_commission_participants_platform_origin ON commission_participants (platform_origin);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_commission_participants_updated_at BEFORE UPDATE ON commission_participants FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `customer_logs`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS customer_logs (
    id          SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers ON DELETE CASCADE,
    field_name  VARCHAR(100) NOT NULL,                    -- Changed field name
    old_value   TEXT,                                     -- Previous value
    new_value   TEXT,                                     -- New value
    changed_by  VARCHAR(100) DEFAULT 'SYSTEM',            -- Who made the change
    created_at  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE customer_logs OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE customer_logs IS 'Audit table to track modifications to data in the customers table.';
COMMENT ON COLUMN customer_logs.id IS 'Unique identifier for the log record.';
COMMENT ON COLUMN customer_logs.customer_id IS 'Reference to the customer whose data was changed.';
COMMENT ON COLUMN customer_logs.field_name IS 'Name of the column in the customers table that was modified.';
COMMENT ON COLUMN customer_logs.old_value IS 'Field value before the change.';
COMMENT ON COLUMN customer_logs.new_value IS 'Field value after the change.';
COMMENT ON COLUMN customer_logs.changed_by IS 'Identification of the agent that made the change (system, user, API).';
COMMENT ON COLUMN customer_logs.created_at IS 'Timestamp of when the change was recorded.';
COMMENT ON COLUMN customer_logs.updated_at IS 'Timestamp of the last update to the log record (rarely used).';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_customer_logs_customer_id ON customer_logs (customer_id);
CREATE INDEX IF NOT EXISTS idx_customer_logs_created_at ON customer_logs (created_at);
```


**Triggers:**
* No `update_updated_at_column` trigger defined for this table.


---


### Table: `customers`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS customers (
    id               SERIAL PRIMARY KEY,
    email            VARCHAR(255) UNIQUE,                  -- Customer email (unique)
    name             VARCHAR(255),                         -- Full name
    customer_id      VARCHAR(255),                         -- ID in the source platform
    address_id       INTEGER REFERENCES addresses,         -- Main address
    created_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    phone_local_code VARCHAR(10),                          -- Area code
    phone_number     VARCHAR(20),                          -- Phone number
    document_type    VARCHAR(10)                           -- Document type
    document_number    VARCHAR(55)                           -- Document Number
);
ALTER TABLE customers OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE customers IS 'Central repository of customer information, unifying data from various platforms.';
COMMENT ON COLUMN customers.id IS 'Internal unique identifier for the customer.';
COMMENT ON COLUMN customers.email IS 'Customer\'s main email, used for login and communication. Must be unique.';
COMMENT ON COLUMN customers.name IS 'Customer\'s full name.';
COMMENT ON COLUMN customers.customer_id IS 'Customer identifier in the source platform (e.g., Kiwify customer ID, Hotmart buyer ID, if applicable and useful).';
COMMENT ON COLUMN customers.address_id IS 'Reference to the customer\'s main address in the addresses table.';
COMMENT ON COLUMN customers.created_at IS 'Timestamp of customer record creation.';
COMMENT ON COLUMN customers.updated_at IS 'Timestamp of the last customer record update.';
COMMENT ON COLUMN customers.phone_local_code IS 'Area code or country code of the customer\'s phone.';
COMMENT ON COLUMN customers.phone_number IS 'Customer\'s phone number (without area code).';
COMMENT ON COLUMN customers.document_type IS 'Type of customer\'s document (e.g., "CPF", "CNPJ", "PASSPORT").';
COMMENT ON COLUMN customers.document_number IS 'Number of customer\'s document (e.g., "000.000.000-00").';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_customers_email ON customers (email);
CREATE INDEX IF NOT EXISTS idx_customers_customer_id ON customers (customer_id);
CREATE INDEX IF NOT EXISTS idx_customers_address_id ON customers (address_id);
CREATE INDEX IF NOT EXISTS idx_customers_email_lower ON customers (lower(email::text));
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_customers_updated_at BEFORE UPDATE ON customers FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `offers`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS offers (
    id              SERIAL PRIMARY KEY,
    offer_id        VARCHAR(100) NOT NULL,                 -- Offer ID in the platform
    platform_origin VARCHAR(100) NOT NULL,                 -- Platform name
    name            VARCHAR(255),                          -- Offer name
    description     TEXT,                                  -- Offer description
    plan_id         INTEGER REFERENCES plans,              -- Associated plan
    product_id      INTEGER REFERENCES products,           -- Associated product
    created_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    payment_mode    VARCHAR(50),                           -- Payment mode
    price           NUMERIC(15, 4),                        -- Base price
    currency_code   VARCHAR(3),                            -- Currency code
    CONSTRAINT uq_offer_platform UNIQUE (offer_id, platform_origin)
);
ALTER TABLE offers OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE offers IS 'Catalog of specific offers (checkout links, promotions) associated with products or plans, unifying data from platforms.';
COMMENT ON COLUMN offers.id IS 'Internal unique identifier for the offer.';
COMMENT ON COLUMN offers.offer_id IS 'Offer identifier in the source platform.';
COMMENT ON COLUMN offers.platform_origin IS 'Name of the platform from which this offer originated.';
COMMENT ON COLUMN offers.name IS 'Descriptive name of the offer.';
COMMENT ON COLUMN offers.description IS 'Detailed description of the offer conditions.';
COMMENT ON COLUMN offers.plan_id IS 'Reference to the associated plan (if it\'s a subscription offer).';
COMMENT ON COLUMN offers.product_id IS 'Reference to the associated product.';
COMMENT ON COLUMN offers.created_at IS 'Timestamp of offer record creation.';
COMMENT ON COLUMN offers.updated_at IS 'Timestamp of the last offer record update.';
COMMENT ON COLUMN offers.payment_mode IS 'Offer payment mode (e.g., "subscription", "one_time").';
COMMENT ON COLUMN offers.price IS 'Base price of the offer.';
COMMENT ON COLUMN offers.currency_code IS 'Currency code of the offer (e.g., "BRL", "USD").';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_offers_plan_id ON offers (plan_id);
CREATE INDEX IF NOT EXISTS idx_offers_product_id ON offers (product_id);
CREATE INDEX IF NOT EXISTS idx_offers_platform_origin ON offers (platform_origin);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_offers_updated_at BEFORE UPDATE ON offers FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `participant_addresses`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS participant_addresses (
    id             SERIAL PRIMARY KEY,
    participant_id INTEGER NOT NULL REFERENCES commission_participants ON DELETE CASCADE,
    address        VARCHAR(255),                          -- Street address
    neighborhood   VARCHAR(100),                          -- Neighborhood
    country        VARCHAR(100),                          -- Country
    city           VARCHAR(100),                          -- City
    zip_code       VARCHAR(20),                           -- ZIP code
    complement     VARCHAR(255),                          -- Complement
    number         VARCHAR(20),                           -- Number
    created_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    state          VARCHAR(100)                           -- State/Province
);
ALTER TABLE participant_addresses OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE participant_addresses IS 'Stores specific addresses of commission participants (affiliates, producers, co-producers).';
COMMENT ON COLUMN participant_addresses.id IS 'Internal unique identifier for the address.';
COMMENT ON COLUMN participant_addresses.participant_id IS 'Reference to the participant who owns this address.';
COMMENT ON COLUMN participant_addresses.address IS 'Street address (Street, Avenue, etc.).';
COMMENT ON COLUMN participant_addresses.neighborhood IS 'Neighborhood.';
COMMENT ON COLUMN participant_addresses.country IS 'Country (ISO code or name).';
COMMENT ON COLUMN participant_addresses.city IS 'City.';
COMMENT ON COLUMN participant_addresses.zip_code IS 'Postal code (ZIP/CEP).';
COMMENT ON COLUMN participant_addresses.complement IS 'Address complement (Block, Apt, etc.).';
COMMENT ON COLUMN participant_addresses.number IS 'Building number.';
COMMENT ON COLUMN participant_addresses.created_at IS 'Timestamp of record creation.';
COMMENT ON COLUMN participant_addresses.updated_at IS 'Timestamp of the last record update.';
COMMENT ON COLUMN participant_addresses.state IS 'State/Province of the address.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_participant_addresses_participant_id ON participant_addresses (participant_id);
CREATE INDEX IF NOT EXISTS idx_participant_addresses_country_city ON participant_addresses (country, city);
CREATE INDEX IF NOT EXISTS idx_participant_addresses_zip_code ON participant_addresses (zip_code);
CREATE INDEX IF NOT EXISTS idx_participant_addresses_state ON participant_addresses (state);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_participant_addresses_updated_at BEFORE UPDATE ON participant_addresses FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `plans`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS plans (
    id                  SERIAL PRIMARY KEY,
    plan_id             VARCHAR(100) NOT NULL,             -- Plan ID in the platform
    platform_origin     VARCHAR(100) NOT NULL,             -- Platform name
    name                VARCHAR(255),                      -- Plan name
    description         TEXT,                              -- Plan description
    product_id          INTEGER REFERENCES products,       -- Associated product
    created_at          TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    price               NUMERIC(15, 4),                    -- Base price
    currency_code       VARCHAR(3),                        -- Currency code
    recurrence_period   VARCHAR(20),                       -- Period (monthly, yearly)
    recurrence_interval INTEGER,                           -- Interval between charges
    trial_days          INTEGER,                           -- Free trial days
    max_cycles          INTEGER,                           -- Maximum cycles
    CONSTRAINT uq_plan_platform UNIQUE (plan_id, platform_origin)
);
ALTER TABLE plans OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE plans IS 'Catalog of plans (usually associated with subscriptions) linked to products, unifying data from platforms.';
COMMENT ON COLUMN plans.id IS 'Internal unique identifier for the plan.';
COMMENT ON COLUMN plans.plan_id IS 'Plan identifier in the source platform.';
COMMENT ON COLUMN plans.platform_origin IS 'Name of the platform from which this plan originated.';
COMMENT ON COLUMN plans.name IS 'Official name of the plan.';
COMMENT ON COLUMN plans.description IS 'Detailed description of what the plan includes.';
COMMENT ON COLUMN plans.product_id IS 'Reference to the main product to which this plan is associated.';
COMMENT ON COLUMN plans.created_at IS 'Timestamp of plan record creation.';
COMMENT ON COLUMN plans.updated_at IS 'Timestamp of the last plan record update.';
COMMENT ON COLUMN plans.price IS 'Base price of the plan per billing cycle.';
COMMENT ON COLUMN plans.currency_code IS 'Currency code of the plan price (e.g., "BRL", "USD").';
COMMENT ON COLUMN plans.recurrence_period IS 'Recurrence time unit (e.g., "MONTH", "YEAR", "WEEK").';
COMMENT ON COLUMN plans.recurrence_interval IS 'Time interval between recurrences.';
COMMENT ON COLUMN plans.trial_days IS 'Number of days in the free trial period.';
COMMENT ON COLUMN plans.max_cycles IS 'Maximum number of billing cycles (0 or NULL for infinite).';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_plans_product_id ON plans (product_id);
CREATE INDEX IF NOT EXISTS idx_plans_platform_origin ON plans (platform_origin);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_plans_updated_at BEFORE UPDATE ON plans FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `platform_commission`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS platform_commission (
    id             SERIAL PRIMARY KEY,
    transaction_id INTEGER NOT NULL REFERENCES transactions ON DELETE CASCADE,
    participant_id INTEGER NOT NULL REFERENCES commission_participants,
    amount         NUMERIC(15, 4) NOT NULL,                -- Commission amount
    currency_code  VARCHAR(3) NOT NULL,                    -- Currency code
    source         VARCHAR(100),                           -- Commission source
    created_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE platform_commission OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE platform_commission IS 'Records commissions (Hotmart: commissions; Kiwify: affiliate_commission, revenue_partners).';
COMMENT ON COLUMN platform_commission.id IS 'Internal unique identifier for the commission record.';
COMMENT ON COLUMN platform_commission.transaction_id IS 'Reference to the transaction that originated this commission.';
COMMENT ON COLUMN platform_commission.participant_id IS 'Reference to the participant who received the commission.';
COMMENT ON COLUMN platform_commission.amount IS 'Monetary value of the commission.';
COMMENT ON COLUMN platform_commission.currency_code IS 'ISO 4217 currency code in which the commission was paid.';
COMMENT ON COLUMN platform_commission.source IS 'Indicates the type/role of the participant that generated the commission (e.g., "PRODUCER", "AFFILIATE", "COPRODUCER").';
COMMENT ON COLUMN platform_commission.created_at IS 'Timestamp of this commission record creation.';
COMMENT ON COLUMN platform_commission.updated_at IS 'Timestamp of the last update to this commission record.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_platform_commission_transaction_id ON platform_commission (transaction_id);
CREATE INDEX IF NOT EXISTS idx_platform_commission_participant_id ON platform_commission (participant_id);
CREATE INDEX IF NOT EXISTS idx_platform_commission_currency_code ON platform_commission (currency_code);
CREATE INDEX IF NOT EXISTS idx_platform_commission_source ON platform_commission (source);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_platform_commission_updated_at BEFORE UPDATE ON platform_commission FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `platform_sale_offer_history`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS platform_sale_offer_history (
    id             SERIAL PRIMARY KEY,
    transaction_id INTEGER REFERENCES transactions,        -- Associated transaction
    code           VARCHAR(100),                           -- Offer code
    offer_id       VARCHAR(100),                           -- Offer ID
    offer_name     VARCHAR(255),                           -- Offer name
    description    VARCHAR(500),                           -- Offer description
    created_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE platform_sale_offer_history OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE platform_sale_offer_history IS 'Stores a snapshot of the offer used in a specific sale at the time of the transaction, ensuring historical traceability even if offers are later modified.';
COMMENT ON COLUMN platform_sale_offer_history.id IS 'Internal unique identifier.';
COMMENT ON COLUMN platform_sale_offer_history.transaction_id IS 'Reference to the transaction where this offer was used.';
COMMENT ON COLUMN platform_sale_offer_history.code IS 'Internal code or SKU of the offer/plan at the time of sale.';
COMMENT ON COLUMN platform_sale_offer_history.offer_id IS 'Offer ID in the source platform at the time of sale.';
COMMENT ON COLUMN platform_sale_offer_history.offer_name IS 'Offer name as displayed to the customer at the time of sale.';
COMMENT ON COLUMN platform_sale_offer_history.description IS 'Offer description valid at the time of sale.';
COMMENT ON COLUMN platform_sale_offer_history.created_at IS 'Timestamp of this historical record creation.';
COMMENT ON COLUMN platform_sale_offer_history.updated_at IS 'Timestamp of the last update to this historical record.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_platform_sale_offer_history_trans_id ON platform_sale_offer_history (transaction_id);
CREATE INDEX IF NOT EXISTS idx_platform_sale_offer_history_code ON platform_sale_offer_history (code);
CREATE INDEX IF NOT EXISTS idx_platform_sale_offer_history_offer_id ON platform_sale_offer_history (offer_id);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_platform_sale_offer_history_updated_at BEFORE UPDATE ON platform_sale_offer_history FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `platform_software_invoice_history`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS platform_software_invoice_history (
    id             SERIAL PRIMARY KEY,
    transaction_id INTEGER NOT NULL REFERENCES transactions ON DELETE CASCADE,
    invoice_number VARCHAR(100),                           -- Invoice number
    invoice_series VARCHAR(20),                            -- Invoice series
    invoice_key    VARCHAR(255) UNIQUE,                    -- Access key
    issue_date     TIMESTAMP WITH TIME ZONE,               -- Issue date
    status         VARCHAR(50),                            -- Invoice status
    xml_url        TEXT,                                   -- XML URL
    pdf_url        TEXT,                                   -- PDF URL
    created_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE platform_software_invoice_history OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE platform_software_invoice_history IS 'Stores information about invoices issued and associated with transactions, potentially via integration with invoicing software.';
COMMENT ON COLUMN platform_software_invoice_history.id IS 'Internal unique identifier for the invoice record.';
COMMENT ON COLUMN platform_software_invoice_history.transaction_id IS 'Reference to the corresponding transaction.';
COMMENT ON COLUMN platform_software_invoice_history.invoice_number IS 'Sequential number of the invoice.';
COMMENT ON COLUMN platform_software_invoice_history.invoice_series IS 'Invoice series.';
COMMENT ON COLUMN platform_software_invoice_history.invoice_key IS 'Unique access key of the e-invoice.';
COMMENT ON COLUMN platform_software_invoice_history.issue_date IS 'Timestamp of the invoice issuance.';
COMMENT ON COLUMN platform_software_invoice_history.status IS 'Current status of the invoice (e.g., "Issued", "Canceled").';
COMMENT ON COLUMN platform_software_invoice_history.xml_url IS 'Link to download the XML file.';
COMMENT ON COLUMN platform_software_invoice_history.pdf_url IS 'Link to download the PDF file (DANFE).';
COMMENT ON COLUMN platform_software_invoice_history.created_at IS 'Timestamp of invoice record creation.';
COMMENT ON COLUMN platform_software_invoice_history.updated_at IS 'Timestamp of the last update to the invoice record.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_plat_soft_inv_hist_trans_id ON platform_software_invoice_history (transaction_id);
CREATE INDEX IF NOT EXISTS idx_plat_soft_inv_hist_issue_date ON platform_software_invoice_history (issue_date);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_platform_software_invoice_history_updated_at BEFORE UPDATE ON platform_software_invoice_history FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `platform_transaction_payment_history`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS platform_transaction_payment_history (
    id                SERIAL PRIMARY KEY,
    transaction_id    INTEGER NOT NULL REFERENCES transactions ON DELETE CASCADE,
    payment_method    payment_method_enum,                 -- Payment method
    payment_type      payment_type_enum,                   -- Payment type
    installments      INTEGER,                             -- Installments number
    value             NUMERIC(15, 4),                      -- Paid amount
    payment_date      TIMESTAMP WITH TIME ZONE,            -- Payment date
    card_brand        VARCHAR(50),                         -- Card brand
    card_last_digits  VARCHAR(4),                          -- Last digits
    bank_slip_barcode TEXT,                                -- Bank slip barcode
    pix_code          TEXT,                                -- PIX code
    metadata          JSONB,                               -- Additional metadata
    created_at        TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE platform_transaction_payment_history OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE platform_transaction_payment_history IS 'Stores the specific details of each payment event or attempt associated with a transaction.';
COMMENT ON COLUMN platform_transaction_payment_history.id IS 'Internal unique identifier for the payment record.';
COMMENT ON COLUMN platform_transaction_payment_history.transaction_id IS 'Reference to the related transaction.';
COMMENT ON COLUMN platform_transaction_payment_history.payment_method IS 'Payment method used (mapped to ENUM).';
COMMENT ON COLUMN platform_transaction_payment_history.payment_type IS 'Payment type (mapped to ENUM).';
COMMENT ON COLUMN platform_transaction_payment_history.installments IS 'Number of installments (NULL or 1 for single payment).';
COMMENT ON COLUMN platform_transaction_payment_history.value IS 'Monetary value paid or attempted in this event.';
COMMENT ON COLUMN platform_transaction_payment_history.payment_date IS 'Timestamp of payment confirmation or processing.';
COMMENT ON COLUMN platform_transaction_payment_history.card_brand IS 'Credit/debit card brand, if applicable.';
COMMENT ON COLUMN platform_transaction_payment_history.card_last_digits IS 'Last 4 digits of the card, if applicable and allowed.';
COMMENT ON COLUMN platform_transaction_payment_history.bank_slip_barcode IS 'Bank slip barcode, if applicable.';
COMMENT ON COLUMN platform_transaction_payment_history.pix_code IS 'PIX code or key used, if applicable.';
COMMENT ON COLUMN platform_transaction_payment_history.metadata IS 'Additional data in JSON format (e.g., decline details, specific payment gateway ID).';
COMMENT ON COLUMN platform_transaction_payment_history.created_at IS 'Timestamp of this payment record creation.';
COMMENT ON COLUMN platform_transaction_payment_history.updated_at IS 'Timestamp of the last update to this payment record.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_plat_trans_pay_hist_trans_id ON platform_transaction_payment_history (transaction_id);
CREATE INDEX IF NOT EXISTS idx_plat_trans_pay_hist_pay_method ON platform_transaction_payment_history (payment_method);
CREATE INDEX IF NOT EXISTS idx_plat_trans_pay_hist_pay_date ON platform_transaction_payment_history (payment_date);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_platform_transaction_payment_history_updated_at BEFORE UPDATE ON platform_transaction_payment_history FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `platform_utm_history`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS platform_utm_history (
    id             SERIAL PRIMARY KEY,
    transaction_id INTEGER NOT NULL REFERENCES transactions ON DELETE CASCADE,
    utm_source     VARCHAR(255),                           -- Source
    utm_medium     VARCHAR(255),                           -- Medium
    utm_campaign   VARCHAR(255),                           -- Campaign
    utm_term       VARCHAR(255),                           -- Term
    utm_content    VARCHAR(255),                           -- Content
    capture_date   TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE platform_utm_history OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE platform_utm_history IS 'Stores UTM parameters captured at the time of a transaction for marketing tracking.';
COMMENT ON COLUMN platform_utm_history.id IS 'Internal unique identifier for the UTM record.';
COMMENT ON COLUMN platform_utm_history.transaction_id IS 'Reference to the associated transaction.';
COMMENT ON COLUMN platform_utm_history.utm_source IS 'utm_source parameter.';
COMMENT ON COLUMN platform_utm_history.utm_medium IS 'utm_medium parameter.';
COMMENT ON COLUMN platform_utm_history.utm_campaign IS 'utm_campaign parameter.';
COMMENT ON COLUMN platform_utm_history.utm_term IS 'utm_term parameter.';
COMMENT ON COLUMN platform_utm_history.utm_content IS 'utm_content parameter.';
COMMENT ON COLUMN platform_utm_history.capture_date IS 'Timestamp of UTM data capture.';
COMMENT ON COLUMN platform_utm_history.created_at IS 'Timestamp of UTM record creation.';
COMMENT ON COLUMN platform_utm_history.updated_at IS 'Timestamp of the last update to the UTM record.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_platform_utm_history_transaction_id ON platform_utm_history (transaction_id);
CREATE INDEX IF NOT EXISTS idx_platform_utm_history_source_medium ON platform_utm_history (utm_source, utm_medium);
CREATE INDEX IF NOT EXISTS idx_platform_utm_history_campaign ON platform_utm_history (utm_campaign);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_platform_utm_history_updated_at BEFORE UPDATE ON platform_utm_history FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `products`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS products (
    id              SERIAL PRIMARY KEY,
    product_id      VARCHAR(100) NOT NULL,                 -- Product ID in the source platform
    platform_origin VARCHAR(100) NOT NULL,                 -- Name of the source platform
    name            VARCHAR(255),                          -- Product name
    description     TEXT,                                  -- Detailed description
    created_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_product_platform UNIQUE (product_id, platform_origin)
);
ALTER TABLE products OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE products IS 'Unified catalog of products registered in various sales platforms.';
COMMENT ON COLUMN products.id IS 'Internal unique identifier for the product.';
COMMENT ON COLUMN products.product_id IS 'Product identifier in the source platform.';
COMMENT ON COLUMN products.platform_origin IS 'Name of the platform from which this product originated.';
COMMENT ON COLUMN products.name IS 'Official product name.';
COMMENT ON COLUMN products.description IS 'Complete product description.';
COMMENT ON COLUMN products.created_at IS 'Timestamp of product record creation.';
COMMENT ON COLUMN products.updated_at IS 'Timestamp of the last product record update.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_products_name ON products (name);
CREATE INDEX IF NOT EXISTS idx_products_platform_origin ON products (platform_origin);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_products_updated_at BEFORE UPDATE ON products FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `subscriptions`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS subscriptions (
    id                     SERIAL PRIMARY KEY,
    subscription_id        VARCHAR(100) NOT NULL,          -- Subscription ID in the platform
    subscriber_id          VARCHAR(100),                   -- Subscriber ID in the platform
    initial_transaction_id VARCHAR(100),                   -- Initial transaction ID
    customer_id            INTEGER REFERENCES customers,    -- Associated customer
    plan_id                INTEGER REFERENCES plans,        -- Associated plan
    payment_gateway        VARCHAR(100) NOT NULL,          -- Payment gateway
    billing_cycle          VARCHAR(50),                    -- Billing cycle
    total_recurrences      INTEGER,                        -- Total recurrences
    max_cycles             INTEGER,                        -- Maximum cycles
    last_update            TIMESTAMP WITH TIME ZONE,       -- Last update
    start_date             TIMESTAMP WITH TIME ZONE,       -- Start date
    end_date               TIMESTAMP WITH TIME ZONE,       -- End date
    created_at             TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at             TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status_id              INTEGER REFERENCES transaction_statuses, -- Current status
    request_billet         BOOLEAN DEFAULT false,          -- Billet request
    next_billing_date      TIMESTAMP WITH TIME ZONE,       -- Next billing date
    cancel_date            TIMESTAMP WITH TIME ZONE,       -- Cancellation date
    CONSTRAINT uq_subscription_gateway UNIQUE (subscription_id, payment_gateway)
);
ALTER TABLE subscriptions OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE subscriptions IS 'Record of all recurring subscriptions (Hotmart: subscriptions, Kiwify: subscriptions).';
COMMENT ON COLUMN subscriptions.id IS 'Internal unique identifier for the subscription.';
COMMENT ON COLUMN subscriptions.subscription_id IS 'Unique subscription identifier in the source platform (gateway).';
COMMENT ON COLUMN subscriptions.subscriber_id IS 'Subscriber identifier in the source platform (may be specific to the subscription).';
COMMENT ON COLUMN subscriptions.initial_transaction_id IS 'Reference to the ID of the initial purchase transaction in the source platform.';
COMMENT ON COLUMN subscriptions.customer_id IS 'Reference to the customer (subscriber) in the customers table.';
COMMENT ON COLUMN subscriptions.plan_id IS 'Reference to the plan associated with this subscription in the plans table.';
COMMENT ON COLUMN subscriptions.payment_gateway IS 'Name of the platform where the subscription is active.';
COMMENT ON COLUMN subscriptions.billing_cycle IS 'Recurrence period of the charge (e.g., "MONTHLY", "YEARLY").';
COMMENT ON COLUMN subscriptions.total_recurrences IS 'Total number of charges planned in the subscription plan (if applicable).';
COMMENT ON COLUMN subscriptions.max_cycles IS 'Maximum number of billing cycles allowed for this subscription (if applicable).';
COMMENT ON COLUMN subscriptions.last_update IS 'Timestamp of the last update received from the platform about this subscription.';
COMMENT ON COLUMN subscriptions.start_date IS 'Subscription start date.';
COMMENT ON COLUMN subscriptions.end_date IS 'Subscription end date (planned or effective).';
COMMENT ON COLUMN subscriptions.created_at IS 'Timestamp of subscription record creation in our database.';
COMMENT ON COLUMN subscriptions.updated_at IS 'Timestamp of the last update to the subscription record in our database.';
COMMENT ON COLUMN subscriptions.status_id IS 'Reference to the current subscription status (FK to transaction_statuses).';
COMMENT ON COLUMN subscriptions.request_billet IS 'Indicates if the subscriber requested payment via bank slip for recurrences.';
COMMENT ON COLUMN subscriptions.next_billing_date IS 'Expected date for the next subscription charge.';
COMMENT ON COLUMN subscriptions.cancel_date IS 'Date when the subscription was canceled, if applicable.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_subscriptions_subscriber_id ON subscriptions (subscriber_id);
CREATE INDEX IF NOT EXISTS idx_subscriptions_customer_id ON subscriptions (customer_id);
CREATE INDEX IF NOT EXISTS idx_subscriptions_plan_id ON subscriptions (plan_id);
CREATE INDEX IF NOT EXISTS idx_subscriptions_payment_gateway ON subscriptions (payment_gateway);
CREATE INDEX IF NOT EXISTS idx_subscriptions_start_date ON subscriptions (start_date);
CREATE INDEX IF NOT EXISTS idx_subscriptions_end_date ON subscriptions (end_date);
CREATE INDEX IF NOT EXISTS idx_subscriptions_status_id ON subscriptions (status_id);
CREATE INDEX IF NOT EXISTS idx_subscriptions_next_billing_date ON subscriptions (next_billing_date);
CREATE INDEX IF NOT EXISTS idx_subscriptions_cancel_date ON subscriptions (cancel_date);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_subscriptions_updated_at BEFORE UPDATE ON subscriptions FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `subscription_status_history`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS subscription_status_history (
    id              SERIAL PRIMARY KEY,
    subscription_id INTEGER NOT NULL REFERENCES subscriptions ON DELETE CASCADE,
    status_id       INTEGER NOT NULL REFERENCES transaction_statuses,
    change_date     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    reason          TEXT,                                   -- Change reason
    created_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE subscription_status_history OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE subscription_status_history IS 'Records the history of all status changes that a subscription has gone through over time.';
COMMENT ON COLUMN subscription_status_history.id IS 'Internal unique identifier for the history record.';
COMMENT ON COLUMN subscription_status_history.subscription_id IS 'Reference to the subscription whose status changed.';
COMMENT ON COLUMN subscription_status_history.status_id IS 'Reference to the new (standardized) status that the subscription assumed, using the transaction_statuses table.';
COMMENT ON COLUMN subscription_status_history.change_date IS 'Date and time when the change to this status effectively occurred (ideally the platform timestamp).';
COMMENT ON COLUMN subscription_status_history.reason IS 'Optional textual description explaining the reason for the status change.';
COMMENT ON COLUMN subscription_status_history.created_at IS 'Timestamp of this history record creation.';
COMMENT ON COLUMN subscription_status_history.updated_at IS 'Timestamp of the last update to this history record.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_subscription_status_history_sub_id ON subscription_status_history (subscription_id);
CREATE INDEX IF NOT EXISTS idx_subscription_status_history_status_id ON subscription_status_history (status_id);
CREATE INDEX IF NOT EXISTS idx_subscription_status_history_change_date ON subscription_status_history (change_date);
```


**Triggers:**
* No `update_updated_at_column` trigger defined for this table.


---


### Table: `transaction_fees`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS transaction_fees (
    id                SERIAL PRIMARY KEY,
    transaction_id    INTEGER NOT NULL REFERENCES transactions ON DELETE CASCADE,
    fee_type          VARCHAR(100) NOT NULL,               -- Fee type
    total_amount      NUMERIC(15, 4) NOT NULL,             -- Total amount
    fee_currency_code VARCHAR(3) NOT NULL,                 -- Currency code
    created_at        TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    base_amount       NUMERIC(15, 4),                      -- Base amount
    fixed_amount      NUMERIC(15, 4)                       -- Fixed amount
);
ALTER TABLE transaction_fees OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE transaction_fees IS 'Stores fees (Hotmart: hotmart_fee; Kiwify: payment.fee).';
COMMENT ON COLUMN transaction_fees.id IS 'Internal unique identifier for this fee record.';
COMMENT ON COLUMN transaction_fees.transaction_id IS 'Reference to the transaction on which this fee was charged.';
COMMENT ON COLUMN transaction_fees.fee_type IS 'Specific type of fee charged (Need to map from APIs, e.g., "PLATFORM_FEE", "GATEWAY_FEE").';
COMMENT ON COLUMN transaction_fees.total_amount IS 'Total fee amount (typically base_amount + fixed_amount).';
COMMENT ON COLUMN transaction_fees.fee_currency_code IS 'ISO 4217 currency code in which the fee was charged.';
COMMENT ON COLUMN transaction_fees.created_at IS 'Timestamp of this fee record creation.';
COMMENT ON COLUMN transaction_fees.updated_at IS 'Timestamp of the last update to this fee record.';
COMMENT ON COLUMN transaction_fees.base_amount IS 'Base fee amount (percentage of the transaction value).';
COMMENT ON COLUMN transaction_fees.fixed_amount IS 'Fixed fee amount (independent of the transaction value).';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_transaction_fees_transaction_id ON transaction_fees (transaction_id);
CREATE INDEX IF NOT EXISTS idx_transaction_fees_type ON transaction_fees (fee_type);
CREATE INDEX IF NOT EXISTS idx_transaction_fees_currency_code ON transaction_fees (fee_currency_code);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_transaction_fees_updated_at BEFORE UPDATE ON transaction_fees FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `transaction_items`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS transaction_items (
    id             SERIAL PRIMARY KEY,
    transaction_id INTEGER NOT NULL REFERENCES transactions ON DELETE CASCADE,
    offer_id       INTEGER REFERENCES offers,              -- Purchased offer
    product_id     INTEGER NOT NULL REFERENCES products,   -- Purchased product
    plan_id        INTEGER REFERENCES plans,               -- Purchased plan
    quantity       INTEGER DEFAULT 1,                      -- Quantity
    unit_price     NUMERIC(15, 4),                         -- Unit price
    created_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE transaction_items OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE transaction_items IS 'Details the individual items (products/offers/plans) that make up a transaction. Allows modeling carts with multiple items or order bumps.';
COMMENT ON COLUMN transaction_items.id IS 'Internal unique identifier for the item within the transaction.';
COMMENT ON COLUMN transaction_items.transaction_id IS 'Reference to the main transaction.';
COMMENT ON COLUMN transaction_items.offer_id IS 'Reference to the specific offer used (if applicable).';
COMMENT ON COLUMN transaction_items.product_id IS 'Reference to the purchased product.';
COMMENT ON COLUMN transaction_items.plan_id IS 'Reference to the purchased plan (especially for subscription items).';
COMMENT ON COLUMN transaction_items.quantity IS 'Quantity of units of this specific item.';
COMMENT ON COLUMN transaction_items.unit_price IS 'Price of one unit of this item at the time of the transaction (in the transaction currency).';
COMMENT ON COLUMN transaction_items.created_at IS 'Timestamp of this item record creation.';
COMMENT ON COLUMN transaction_items.updated_at IS 'Timestamp of the last update to this item record.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_transaction_items_transaction_id ON transaction_items (transaction_id);
CREATE INDEX IF NOT EXISTS idx_transaction_items_offer_id ON transaction_items (offer_id);
CREATE INDEX IF NOT EXISTS idx_transaction_items_product_id ON transaction_items (product_id);
CREATE INDEX IF NOT EXISTS idx_transaction_items_plan_id ON transaction_items (plan_id);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_transaction_items_updated_at BEFORE UPDATE ON transaction_items FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `transaction_statuses`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS transaction_statuses (
    id         SERIAL PRIMARY KEY,
    status     VARCHAR(50) NOT NULL UNIQUE,                -- Status name
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE transaction_statuses OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE transaction_statuses IS 'Normalizes API statuses (Hotmart: APPROVED->Approved, REFUNDED->Refunded; Kiwify: paid->Approved, refunded->Refunded).';
COMMENT ON COLUMN transaction_statuses.id IS 'Unique sequential identifier for the state.';
COMMENT ON COLUMN transaction_statuses.status IS 'Standardized state name (e.g., "Approved", "Declined", "Refunded", "Active", "Delinquent", "Canceled by Subscriber").';
COMMENT ON COLUMN transaction_statuses.created_at IS 'Timestamp of record creation.';
COMMENT ON COLUMN transaction_statuses.updated_at IS 'Timestamp of the last record update.';
```


**Indexes:**
* Primary key `id` is implicitly indexed.
* `UNIQUE` constraint on `status` automatically creates an index.


**Triggers:**
```sql
CREATE TRIGGER trigger_update_transaction_statuses_updated_at BEFORE UPDATE ON transaction_statuses FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


### Table: `transaction_status_history`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS transaction_status_history (
    id             SERIAL PRIMARY KEY,
    transaction_id INTEGER NOT NULL REFERENCES transactions ON DELETE CASCADE,
    status_id      INTEGER NOT NULL REFERENCES transaction_statuses,
    change_date    TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    reason         TEXT,                                   -- Change reason
    created_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE transaction_status_history OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE transaction_status_history IS 'Records the history of all status changes that a transaction has gone through.';
COMMENT ON COLUMN transaction_status_history.id IS 'Internal unique identifier for the history record.';
COMMENT ON COLUMN transaction_status_history.transaction_id IS 'Reference to the transaction whose status changed.';
COMMENT ON COLUMN transaction_status_history.status_id IS 'Reference to the new (standardized) status that the transaction assumed.';
COMMENT ON COLUMN transaction_status_history.change_date IS 'Date and time when the change to this status effectively occurred (ideally the platform timestamp).';
COMMENT ON COLUMN transaction_status_history.reason IS 'Optional textual description explaining the reason for the status change.';
COMMENT ON COLUMN transaction_status_history.created_at IS 'Timestamp of this history record creation.';
COMMENT ON COLUMN transaction_status_history.updated_at IS 'Timestamp of the last update to this history record.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_transaction_status_history_trans_id ON transaction_status_history (transaction_id);
CREATE INDEX IF NOT EXISTS idx_transaction_status_history_status_id ON transaction_status_history (status_id);
CREATE INDEX IF NOT EXISTS idx_transaction_status_history_change_date ON transaction_status_history (change_date);
```


**Triggers:**
* No `update_updated_at_column` trigger defined for this table.


---


### Table: `transactions`


**SQL Definition:**
```sql
CREATE TABLE IF NOT EXISTS transactions (
    id                        SERIAL PRIMARY KEY,
    transaction_id            VARCHAR(100) NOT NULL,               -- ID in the platform
    customer_id               INTEGER REFERENCES customers,        -- Associated customer
    payment_gateway           VARCHAR(100) NOT NULL,               -- Payment gateway
    status_id                 INTEGER REFERENCES transaction_statuses, -- Current status
    payment_type              payment_type_enum,                   -- Payment type
    payment_method            payment_method_enum,                 -- Payment method
    payment_engine            VARCHAR(100),                        -- Payment engine
    installments_number       INTEGER,                             -- Installments number
    gateway_transaction_id    VARCHAR(100),                        -- Gateway transaction ID
    card_brand                VARCHAR(50),                         -- Card brand
    card_last_digits          VARCHAR(4),                          -- Last digits
    billet_url                TEXT,                                -- Billet URL
    billet_barcode            VARCHAR(100),                        -- Barcode
    currency_code             VARCHAR(3) NOT NULL DEFAULT 'BRL',   -- Currency code
    base_price                NUMERIC(15, 4),                      -- Base price
    offer_price               NUMERIC(15, 4) NOT NULL,             -- Offer price
    customer_paid_amount      NUMERIC(15, 4),                      -- Amount paid
    platform_fee_amount       NUMERIC(15, 4) DEFAULT 0,            -- Platform fees
    distributable_amount      NUMERIC(15, 4),                      -- Distributable amount
    partner_commission_amount NUMERIC(15, 4) DEFAULT 0,            -- Commissions
    producer_net_amount       NUMERIC(15, 4),                      -- Net amount
    is_subscription           BOOLEAN DEFAULT false,               -- Is subscription?
    subscription_id           INTEGER REFERENCES subscriptions,    -- Associated subscription
    platform_subscription_id  VARCHAR(100),                        -- Subscription ID in the platform
    recurrence_number         INTEGER,                             -- Recurrence number
    tracking_source           VARCHAR(100),                        -- Traffic source
    tracking_sck              VARCHAR(100),                        -- Tracking SCK
    under_warranty            BOOLEAN DEFAULT false,               -- Under warranty?
    warranty_expire_date      TIMESTAMP WITH TIME ZONE,            -- Warranty expiration
    order_date                TIMESTAMP WITH TIME ZONE,            -- Order date
    created_at                TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at                TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_transaction_gateway UNIQUE (transaction_id, payment_gateway)
);
ALTER TABLE transactions OWNER TO doadmin;
```


**Comments:**
```sql
COMMENT ON TABLE transactions IS 'Central record of all transactions (Hotmart: purchases, Kiwify: checkouts). Also stores recurring transactions from subscriptions (Hotmart: subscription/transactions, Kiwify: recurring charges).';
COMMENT ON COLUMN transactions.id IS 'Internal unique identifier for the transaction.';
COMMENT ON COLUMN transactions.transaction_id IS 'Unique transaction identifier in the source platform (gateway).';
COMMENT ON COLUMN transactions.customer_id IS 'Reference to the customer associated with this transaction.';
COMMENT ON COLUMN transactions.payment_gateway IS 'Name of the payment platform where the transaction was processed (e.g., "Hotmart", "Kiwify").';
COMMENT ON COLUMN transactions.status_id IS 'Reference to the current transaction status (FK to transaction_statuses).';
COMMENT ON COLUMN transactions.payment_type IS 'Payment type (e.g., "SINGLE_PAYMENT", "INSTALLMENT_PAYMENT").';
COMMENT ON COLUMN transactions.payment_method IS 'Payment method used (e.g., "credit_card", "boleto", "pix").';
COMMENT ON COLUMN transactions.payment_engine IS 'Payment processor/engine (e.g., "Wirecard", "PagSeguro").';
COMMENT ON COLUMN transactions.installments_number IS 'Number of installments for installment payments.';
COMMENT ON COLUMN transactions.gateway_transaction_id IS 'Transaction identifier in the payment gateway.';
COMMENT ON COLUMN transactions.card_brand IS 'Card brand used (e.g., "Visa", "Mastercard").';
COMMENT ON COLUMN transactions.card_last_digits IS 'Last 4 digits of the card used.';
COMMENT ON COLUMN transactions.billet_url IS 'URL for viewing/printing the bank slip.';
COMMENT ON COLUMN transactions.billet_barcode IS 'Bank slip barcode for payment.';
COMMENT ON COLUMN transactions.currency_code IS 'ISO 4217 currency code used in the transaction (e.g., "BRL", "USD").';
COMMENT ON COLUMN transactions.base_price IS 'Original base price of the product/service before discounts/offers (informative).';
COMMENT ON COLUMN transactions.offer_price IS 'Effective price of the offer applied in this transaction. Base for calculating fees and commissions.';
COMMENT ON COLUMN transactions.customer_paid_amount IS 'Total amount effectively paid by the customer (includes installment interest, if any).';
COMMENT ON COLUMN transactions.platform_fee_amount IS 'Sum of all fees charged by the platform on this transaction (deducted from the seller).';
COMMENT ON COLUMN transactions.distributable_amount IS 'Remaining amount after platform fee deduction (offer_price - platform_fee_amount).';
COMMENT ON COLUMN transactions.partner_commission_amount IS 'Sum of commissions paid to all partners (Affiliates, Co-producers) in this transaction.';
COMMENT ON COLUMN transactions.producer_net_amount IS 'Final net amount for the producer after all deductions (distributable_amount - partner_commission_amount).';
COMMENT ON COLUMN transactions.is_subscription IS 'Indicates if this transaction is part of a subscription.';
COMMENT ON COLUMN transactions.subscription_id IS 'Reference to the associated subscription, if applicable.';
COMMENT ON COLUMN transactions.platform_subscription_id IS 'Subscription identifier in the source platform.';
COMMENT ON COLUMN transactions.recurrence_number IS 'Recurrence number for subscription transactions.';
COMMENT ON COLUMN transactions.tracking_source IS 'Source (SRC) tracking parameter identifying the sale origin.';
COMMENT ON COLUMN transactions.tracking_sck IS 'SCK tracking parameter for origin identification.';
COMMENT ON COLUMN transactions.under_warranty IS 'Indicates if the transaction is still within the warranty period.';
COMMENT ON COLUMN transactions.warranty_expire_date IS 'Date when the warranty expires.';
COMMENT ON COLUMN transactions.order_date IS 'Date when the order was placed.';
COMMENT ON COLUMN transactions.created_at IS 'Timestamp of record creation.';
COMMENT ON COLUMN transactions.updated_at IS 'Timestamp of the last record update.';
```


**Indexes:**
```sql
CREATE INDEX IF NOT EXISTS idx_transactions_customer_id ON transactions (customer_id);
CREATE INDEX IF NOT EXISTS idx_transactions_payment_gateway ON transactions (payment_gateway);
CREATE INDEX IF NOT EXISTS idx_transactions_order_date ON transactions (order_date);
CREATE INDEX IF NOT EXISTS idx_transactions_created_at ON transactions (created_at);
CREATE INDEX IF NOT EXISTS idx_transactions_subscription_id ON transactions (subscription_id);
CREATE INDEX IF NOT EXISTS idx_transactions_currency_code ON transactions (currency_code);
CREATE INDEX IF NOT EXISTS idx_transactions_status_id ON transactions (status_id);
CREATE INDEX IF NOT EXISTS idx_transactions_payment_method ON transactions (payment_method);
CREATE INDEX IF NOT EXISTS idx_transactions_platform_subscription_id ON transactions (platform_subscription_id);
CREATE INDEX IF NOT EXISTS idx_transactions_recurrence_number ON transactions (recurrence_number);
```


**Triggers:**
```sql
CREATE TRIGGER trigger_update_transactions_updated_at BEFORE UPDATE ON transactions FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
```


---


(Ref: DB Schema Details - Tables, ID ref_db_schema_details_001)
```