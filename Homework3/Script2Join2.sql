-- Получение статусов доставок с именем и фамилией клиента
SELECT 
    s.status,
    c.first_name,
    c.last_name 
FROM shippings AS s 
LEFT JOIN customers AS c 
     ON s.customer = c.customer_id;