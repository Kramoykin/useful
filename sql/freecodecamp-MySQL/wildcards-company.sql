-- Find any clients who are in LLC
SELECT *
FROM client
WHERE client_name LIKE '%LLC';

-- Find any branch suppliers who are in the label business
SELECT *
FROM branch_supplier
WHERE (supplier_name LIKE '%Label%') OR (supplier_name LIKE '%Lable%');

-- Find all employees born in february
SELECT *
FROM employee
WHERE birth_day LIKE '____-02%';

-- Find all client who are schools
SELECT *
FROM client
WHERE client_name LIKE '%school%';

	