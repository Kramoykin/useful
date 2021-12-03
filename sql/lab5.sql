## SUBQUERIES

1) Return the names, department name for employees receiving the same salary as Kochhar

SELECT FIRST_NAME, LAST_NAME,
DEPARTMENT_ID, SALARY
FROM hr.employees
WHERE SALARY = 
    (SELECT SALARY
        FROM hr.employees
        WHERE LAST_NAME = 'Kochhar')
        
2) Return the name and date of the control point for employees hired in the same year as an employee by the name of «PATEL». Date of the control point is start date plus 25 days.

SELECT FIRST_NAME, LAST_NAME,
(HIRE_DATE + 25) AS CONTROL_DATE
FROM hr.employees
WHERE EXTRACT(YEAR FROM HIRE_DATE) =
    (SELECT EXTRACT(YEAR FROM HIRE_DATE)
        FROM hr.employees
        WHERE LAST_NAME = 'Kochhar')
        
3) Return the departments and the average salary for each department where the average salary for the department is greater than the average salary for all employees.

SELECT DEPARTMENT_ID,
AVG(SALARY)
FROM hr.employees
GROUP BY DEPARTMENT_ID
HAVING AVG(SALARY) <
    (SELECT AVG(SALARY)
        FROM hr.employees)
        
5) Return all workers with salary > than salary of worker 132  and their dpt_id equals the dpt_id of worker 101, not including 101.

SELECT EMPLOYEE_ID, SALARY,
DEPARTMENT_ID
FROM hr.employees
WHERE SALARY > 
(SELECT SALARY
    FROM hr.employees
    WHERE EMPLOYEE_ID = 132)
AND DEPARTMENT_ID = 
    (SELECT DEPARTMENT_ID
        FROM hr.employees
        WHERE EMPLOYEE_ID = 101)
AND EMPLOYEE_ID != 101

6) Return  all workers whose salary is equal salary of one  worker from dpt 60, excluding workers in category 60, simply use this condition : AND dpt_id <> 80.

SELECT FIRST_NAME, LAST_NAME,
DEPARTMENT_ID, SALARY
FROM hr.employees
WHERE SALARY = 
    (SELECT SALARY
    FROM
        ( SELECT DEPARTMENT_ID, FIRST_NAME,
        LAST_NAME, SALARY
        FROM hr.employees
        WHERE DEPARTMENT_ID = 60
        ORDER BY dbms_random.value )
    WHERE rownum = 1)
AND DEPARTMENT_ID != 60

7) Return all employees of department 10, and the main query returns only those with a salary less than 10000.

SELECT EMPLOYEE_ID, SALARY,
DEPARTMENT_ID
FROM 
    (SELECT *
    FROM hr.employees
    WHERE DEPARTMENT_ID = 100)
WHERE SALARY < 10000
