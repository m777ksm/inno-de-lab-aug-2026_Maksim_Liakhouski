SELECT 
    CONCAT_WS(' ', c.first_name, c.last_name),
    c.country,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM customers AS c
JOIN orders AS o ON c.customer_id = o.customer_id 
JOIN shippings AS s ON c.customer_id = s.customer 
    WHERE s.status = 'Delivered' 
    GROUP BY c.customer_id
    HAVING COUNT(o.order_id)>1;