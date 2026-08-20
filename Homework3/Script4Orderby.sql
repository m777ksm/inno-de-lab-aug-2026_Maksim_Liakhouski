
-- Список клиентов по убыванию возраста
SELECT 
  first_name,
  last_name,
  age 
FROM customers
ORDER BY age DESC;
