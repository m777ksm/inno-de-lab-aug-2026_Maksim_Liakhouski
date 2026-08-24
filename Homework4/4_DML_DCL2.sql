-- В одной транзакции вставляем новый проект и назначаем на него двух существующих сотрудников с количеством HoursWorked в EmployeeProjects
BEGIN;
INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate) 
VALUES ('Data Engineering', 170000.00, '2026-08-21', '2026-12-17');
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked) 
VALUES (1, LASTVAL(), 160),
    (3, LASTVAL(), 170);
COMMIT;