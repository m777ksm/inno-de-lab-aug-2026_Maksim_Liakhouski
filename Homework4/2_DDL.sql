-- Создаем таблицу Departments
CREATE TABLE Departments (
    Departmentid SERIAL PRIMARY KEY, -- SERIAL for auto-incrementing integer IDs in PostgreSQL 
    DepartmentName VARCHAR(50) UNIQUE NOT NULL, 
    Location VARCHAR(50)
    ); 

--Добаляем в таблицу Employees новый столбец Email
ALTER TABLE Employees
ADD COLUMN Email VARCHAR(100);

-- Заполняем email
UPDATE employees
SET email = 'alices@bye.by'
WHERE employeeid = 1;

-- Заполняем email2
UPDATE employees
SET email = 'bobj@bye.by'
WHERE employeeid = 2;

-- Заполняем email3
UPDATE employees
SET email = 'charlieb@bye.by'
WHERE employeeid = 3;

-- Заполняем email4
UPDATE employees
SET email = 'dianap@bye.by'
WHERE employeeid = 4;

-- Заполняем email6
UPDATE employees
SET email = 'rolandk@bye.by'
WHERE employeeid = 6;

-- Заполняем email7
UPDATE employees
SET email = 'elonn@bye.by'
WHERE employeeid = 7;

-- Добавим ограничение  к столбцу email/employees
ALTER TABLE employees
ADD CONSTRAINT UQ_email UNIQUE (email);

-- Переимнование Location из таблицы Departments в OfficeLocation
ALTER TABLE departments 
RENAME COLUMN location TO OfficeLocation;

