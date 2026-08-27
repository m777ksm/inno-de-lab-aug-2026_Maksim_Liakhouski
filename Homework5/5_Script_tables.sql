-- Таблица измерений. Объекты аренды
CREATE TABLE dim_property (
    property_sk SERIAL PRIMARY KEY,
    source_property_id INT NOT NULL,
    address VARCHAR(200) NOT NULL,
    unit_number VARCHAR(50) NOT NULL,
    area_sqm NUMERIC(10,2) NOT NULL
);

-- Таблица измерений. Арендаторы
CREATE TABLE dim_tenant (
    tenant_sk SERIAL PRIMARY KEY,
    source_tenant_id INT NOT NULL,
    company_name VARCHAR(200) NOT NULL,
    unp VARCHAR(10) NOT NULL,
    business_type VARCHAR(100) NOT NULL
);

-- Таблица измерений. Договоры аренды
CREATE TABLE dim_agreement (
    agreement_sk SERIAL PRIMARY KEY,
    source_agreement_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

-- Таблица измерений. Месяцы 
CREATE TABLE dim_month (
    month_sk INT PRIMARY KEY,
    source_date_id DATE NOT NULL,
    year INT NOT NULL,
    quarter INT NOT NULL,
    month INT NOT NULL
);

-- Таблица фактов: Фактическая аренда
CREATE TABLE fact_lease (
    lease_sk SERIAL PRIMARY KEY,
    property_sk INT REFERENCES dim_property(property_sk),
    tenant_sk INT REFERENCES dim_tenant(tenant_sk),
    agreement_sk INT REFERENCES dim_agreement(agreement_sk),
    month_sk INT REFERENCES dim_month(month_sk),
    lease_amount NUMERIC(10,2),
    utility_payments NUMERIC(10,2),
    operating_expenses NUMERIC(10,2),
    lease_area NUMERIC(10,2),
    is_occupied BOOLEAN
);