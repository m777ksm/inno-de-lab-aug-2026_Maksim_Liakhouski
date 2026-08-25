-- Создаем пользователя роль с именем hr_user и паролем
CREATE USER hr_user
WITH PASSWORD 'qwerty';

-- Предоставим hr_user право SELECT на таблицу Employees
GRANT SELECT ON TABLE employees TO hr_user;

-- Предоставляем права INSERT и UPDATE to hr_user
GRANT INSERT, UPDATE ON TABLE employees TO hr_user;


