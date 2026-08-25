-- Найти ProjectName всех проектов, в которых 'Bob Johnson' работал более 150 часов
SELECT 
    p.projectname
FROM projects p 
JOIN employeeprojects e2 ON p.projectid = e2.projectid 
JOIN employees e ON e.employeeid = e2.employeeid 
WHERE e.firstname = 'Bob' 
AND e.lastname = 'Johnson'
AND e2.hoursworked > 150;

SELECT 
    p.projectname
FROM projects p
WHERE p.projectid IN (
   SELECT 
       e2.projectid 
   FROM employeeprojects e2 
   WHERE e2.hoursworked > 150
   AND e2.employeeid = (
       SELECT 
           employeeid
       FROM employees e
       WHERE firstname = 'Bob' AND lastname = 'Johnson'
       )
 );