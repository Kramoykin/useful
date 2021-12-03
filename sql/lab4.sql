## AGGREGATE FUNCTIONS

1) Find the average salary of employees working in the department 80. Table s_еmp.

SELECT department_id, COUNT(employee_id) 
AS employee_count, AVG(salary) AS avg_salary 
FROM hr.employees 
WHERE department_id = 80
GROUP BY department_id

2) To return the department numbers, which have the lowest salary of employees less 3000

SELECT department_id, COUNT(employee_id) 
AS employee_count, MIN(salary) AS min_salary 
FROM hr.employees 
GROUP BY department_id
HAVING  MIN(salary) < 3000

3) To return average annual salary by department. The department numbers in ascending

SELECT department_id, COUNT(employee_id) 
AS employee_count, AVG(salary) AS avg_salary 
FROM hr.employees 
GROUP BY department_id
ORDER BY department_id

4) To return the number of employees from department with minimum salary less than average minimum salary by all departments and  more then 5000.Table hr_employees.

SELECT department_id, COUNT(employee_id) 
AS employee_count, MIN(salary) AS min_salary
FROM hr.employees 
GROUP BY department_id
HAVING  MIN(salary) < (SELECT AVG(MIN(salary))
                        FROM hr.employees 
                        GROUP BY department_id)
AND MIN(salary) > 5000


