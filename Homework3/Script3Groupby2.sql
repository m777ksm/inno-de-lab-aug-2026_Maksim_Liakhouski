-- Подсчет количества заказов и среднюю сумму по каждому товару
SELECT 
    item,
    count (order_id),
    AVG(amount) AS avg_amount
FROM orders
GROUP BY item;