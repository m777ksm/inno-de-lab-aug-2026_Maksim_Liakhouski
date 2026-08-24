--Увеличить Salary всех сотрудников в отделе 'HR' на 10%
UPDATE employees
SET salary = salary * 1.1
WHERE department = 'HR';

-- Обновить Department любого сотрудника с Salary выше 70000.00 на 'Senior IT'
UPDATE employees
SET department = 'Senior IT'
WHERE salary > 70000.00;

-- Удалить всех сотрудников, которые не назначены ни на один проект в таблице EmployeeProjects
DELETE FROM employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM employeeprojects e2 
    WHERE e2.employeeid = e.employeeid 
    );
