--Представление с именем IT_Department_View, которое показывает EmployeeID, FirstName, LastName и Salary только для сотрудников из 'IT'
CREATE VIEW IT_Department_View AS 
SELECT 
    employeeid,
    firstname,
    lastname,
    salary
FROM employees 
WHERE department LIKE '%IT%';

SELECT * FROM IT_Department_View;