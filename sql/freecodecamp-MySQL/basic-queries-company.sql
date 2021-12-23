-- SELECT -------------------------------------

-- Find all emloyees
SELECT *
FROM employee;

-- Find all clients
SELECT *
FROM client;

 -- Find all emloyees ordered by sex then name
SELECT *
FROM employee
ORDER BY sex, first_name, last_name;

-- Find the first 5 emloyees
SELECT *
FROM employee
LIMIT 5;

-- Find out all the different genders
SELECT DISTINCT sex
FROM employee;


-- FUNCTIONS -------------------------------------

-- Find the number of subordinates
-- COUNT() does not calculates NULL values
SELECT COUNT(super_id)
FROM employee;

-- Find average of female employees born after 1970
SELECT COUNT(emp_id)
FROM employee
WHERE sex = 'F' AND birth_day >= '1971-01-01';

-- Find the average of all employee's salaries
SELECT AVG(salary)
FROM employee;

-- Find out how many males and females there are
SELECT COUNT(sex), sex
FROM employee
GROUP BY sex;

-- Find the total sales for each salesman
SELECT sum(total_sales), emp_id
FROM works_with
GROUP BY emp_id;

