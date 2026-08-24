-- Создать функцию для расчета бонуса 10% от зарплаты
CREATE OR REPLACE FUNCTION CalculateAnnualBonus(
    employeeid INT, 
    salary NUMERIC (10, 2)
)
RETURNS NUMERIC (10, 2) 
LANGUAGE plpgsql
AS $$
DECLARE
    bonus NUMERIC (10, 2);
BEGIN
        bonus := salary * 0.10;
    RETURN bonus;
END;
$$;

-- Используем эту функцию в операторе SELECT, чтобы увидеть потенциальный бонус для каждого сотрудника.
SELECT 
    e.employeeid,
    e.firstname,
    e.lastname,
    CalculateAnnualBonus (employeeid, salary) AS bonus
FROM employees e;