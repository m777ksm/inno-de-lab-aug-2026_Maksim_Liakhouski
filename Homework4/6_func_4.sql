BEGIN;
-- Вставить нового сотрудника. Использовать RETURNING для EmployeeID вновь вставленного сотрудника. Ищем ID проекта 'Website Redesign
WITH new_employee AS ( 
    INSERT INTO employees (firstname, lastname, department, salary, email)
    VALUES ('Robert', 'Karelson', 'IT', 73000.00, 'robk@bye.by')
    RETURNING employeeid
), 
    current_project AS (
    SELECT projectid 
    FROM projects
    WHERE projectname = 'Website Redesign'
)
-- назначить на проект 'Website Redesign' с 80 отработанными часами, в рамках одной транзакции. 
INSERT INTO employeeprojects (employeeid, projectid, hoursworked)
VALUES (
    (SELECT employeeid FROM new_employee), (SELECT projectid FROM current_project), 80
);
COMMIT;