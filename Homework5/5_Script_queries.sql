-- Выборка топ 5 арендаторов с наибольшей арендной платой в 2026 году с указанием вида деятельности
SELECT 
    dt.company_name,
    dt.business_type,
    SUM (fl.lease_amount) AS sum_of_lease
FROM fact_lease fl
JOIN dim_tenant dt ON fl.tenant_sk = dt.tenant_sk
JOIN dim_month dm ON fl.month_sk = dm.month_sk
WHERE dm.year = 2026
GROUP BY dt.company_name, dt.business_type
ORDER BY sum_of_lease DESC
LIMIT 5;
    
-- Выборка договоров аренды, которые заканчиваются в 2026 году
SELECT 
    dt.company_name,
    da.source_agreement_id,
    dp.address,
    dp.unit_number,
    dp.area_sqm,
    da.end_date
FROM dim_agreement da 
JOIN fact_lease fl ON da.agreement_sk = fl.agreement_sk
JOIN dim_tenant dt ON fl.tenant_sk = dt.tenant_sk
JOIN dim_property dp ON fl.property_sk = dp.property_sk
WHERE a.end_date BETWEEN current_date AND '2027-01-01'
GROUP BY dt.company_name, da.source_agreement_id, dp.address, dp.unit_number, dp.area_sqm, da.end_date
ORDER BY da.end_date;

-- Какой процент помещений занят в разрезе локаций и времени начиная c 2020 года
SELECT 
    dp.address,
    dm.year,
    dm.month,
    ROUND(
        (SUM(fl.lease_area) / SUM(dp.area_sqm)* 100.0), 2) AS "Процент занятости"
FROM fact_lease fl
JOIN dim_property dp ON fl.property_sk = dp.property_sk
JOIN dim_month dm ON fl.month_sk = dm.month_sk
WHERE dm.year >= 2020
GROUP BY dp.address, dm.year, dm.month, dm.month_sk
ORDER BY dm.month_sk DESC;

-- Выборка видов деятельности по показателю арендной платы за 1 м.кв. в разрезе лет с 2020 года для понимания наиболее выгодных арендаторов
SELECT 
    dm.year,
    dt.business_type,
    ROUND(
        SUM(fl.lease_amount) / NULLIF(SUM(fl.lease_area), 0),2) AS "Доход с 1 м кв"
FROM fact_lease fl
JOIN dim_tenant dt ON fl.tenant_sk = dt.tenant_sk
JOIN dim_month dm ON fl.month_sk = dm.month_sk
WHERE dm.year >= 2020
GROUP BY dt.business_type, dm.year
ORDER BY "Доход с 1 м кв" DESC;

