-- поиск всех заказов из таблицы orders, у которых сумма больше 1000
SELECT 
   first_name ,
   last_name ,
   age,
   country 
FROM customers
WHERE country = 'USA' AND age>25;