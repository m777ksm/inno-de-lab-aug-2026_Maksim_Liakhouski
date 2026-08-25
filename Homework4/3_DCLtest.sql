-- тест1 под hr_user 
SELECT *
FROM employees;

-- тест2 под hr_user 
INSERT INTO employees (employeeid, firstname, lastname, department, salary, email)
VALUES (5, 'John', 'Brooks', 'Finance', 55000.00, 'jhonb@bye.by');

-- тест 3 
INSERT INTO employees (employeeid, firstname, lastname, department, salary, email)
VALUES (5, 'John', 'Brooks', 'Finance', 55000.00, 'jhonb@bye.by');

-- тест 3 апдейт
UPDATE employees 
SET email = 'johnbr@bye.by'
WHERE employeeid = 5;