-- Добавляем двух новых сотрудников в Employees
INSERT INTO employees (firstname, lastname, department, salary)
VALUES ('Ronald', 'Karelson', 'Sales', 57000),
('Elon','Nomusk', 'CyberSecurity', 78000);

--Выбираем всех сотрудников из таблицы Employees
SELECT *
FROM employees;

-- Выбираем имена и фамилии сотрудников IT отдела
SELECT 
    e.firstname,
    e.lastname 
FROM employees e 
WHERE e.department = 'IT';

-- Обновляем зарплату Alice Smith 
UPDATE employees  
SET salary = 65000.00
WHERE firstname = 'Alice' AND lastname ='Smith';

-- Удаление сотрудника Eve Davis
DELETE 
FROM employees 
WHERE firstname = 'Eve' AND lastname = 'Davis';

-- Проверяем изменения
SELECT * 
FROM employees;