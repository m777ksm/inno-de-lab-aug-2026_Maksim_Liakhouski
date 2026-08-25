-- Для любого проекта, у которого еще нет EndDate (EndDate IS NULL), установить EndDate на один год позже его StartDate.
UPDATE 
    projects p 
SET enddate = p.startdate + INTERVAL '1 year'
WHERE p.enddate IS NULL;
