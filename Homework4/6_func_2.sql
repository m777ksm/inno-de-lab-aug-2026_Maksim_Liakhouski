-- Увеличить Budget всех проектов на 10%, если к ним назначен хотя бы один сотрудник из отдела 'IT'.
UPDATE projects p
SET budget = p.budget*1.1
FROM employeeprojects e2
JOIN employees e ON e2.employeeid = e.employeeid 
WHERE e.department LIKE '%IT%' 
    AND p.projectid = e2.projectid;