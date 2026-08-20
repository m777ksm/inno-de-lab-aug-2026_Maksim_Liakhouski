-- Подсчет количества клиентов в каждой стране
SELECT 
    country,
    count(*)
FROM customers AS c
GROUP BY country;

