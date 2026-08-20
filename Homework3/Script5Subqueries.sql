-- Все клиенты, которые сделали заказ с максимальной суммой
SELECT 
    c.first_name,
    c.last_name,
    o.amount
FROM orders AS o 
JOIN customers AS c ON o.customer_id = c.customer_id 
WHERE amount = (SELECT MAX(amount) FROM orders);