### SQL JOINS

1) Write a query in SQL to display the full name (first and last name) of employee with ID and name of the country presently where he is working.

SELECT first_name, last_name, country_id, country_name
FROM hr.employees INNER JOIN hr.departments USING(department_id)
    INNER JOIN hr.locations USING(location_id)
        INNER JOIN hr.countries USING(country_id)

2) Write a query in SQL to display the department name and number of employees in each of the department

SELECT department_name, COUNT(employee_id) AS EMP_NUM
FROM (SELECT department_name, employee_id
FROM hr.employees INNER JOIN hr.departments USING(department_id))
GROUP BY department_name

3) Write a query in SQL to display full name (first and last name), job title, starting and ending date of last jobs for those employees with worked without a commission percentage

SELECT employee_id, first_name, last_name, job_title, commission_pct, LAST_JOB_START, LAST_JOB_END
FROM hr.jobs INNER JOIN hr.employees USING(job_id)
    INNER JOIN 
         (
         SELECT employee_id, MAX(start_date) AS LAST_JOB_START, MAX(end_date) AS LAST_JOB_END
         FROM hr.job_history
         GROUP BY employee_id
         ) USING(employee_id) 
WHERE commission_pct IS NULL

4) Write a query in SQL to display the full name (first and last name), and salary of those employees who working in any department located in London

SELECT first_name, last_name, salary, city
FROM hr.employees em INNER JOIN hr.departments dpt ON(em.department_id = dpt.department_id)
    INNER JOIN hr.locations loc ON(dpt.location_id = loc.location_id)
WHERE city = 'London'

5) Write a query in SQL to display the employee ID, job name, number of days worked in for all those jobs in department 80

SELECT jh.employee_id, j.job_title, (end_date - start_date) AS DAYS_TOTAL, job_title, department_id
FROM hr.job_history jh INNER JOIN hr.jobs j USING(job_id)
WHERE department_id = 80

6) Write a query in SQL to display the department name, full name (first and last name) of manager, and their city.

SELECT department_name, first_name, last_name, employee_id, city
FROM hr.locations loc INNER JOIN hr.departments dpt ON(loc.location_id = dpt.location_id) 
    INNER JOIN hr.employees emp ON(dpt.manager_id = emp.employee_id)
    
7) Write a query in SQL to display the country name, city, and number of those departments where at least 2 employees are working.

SELECT country_name, city, COUNT(EMP_NUM)
FROM (
    SELECT department_id, COUNT(employee_id) AS EMP_NUM 
    FROM hr.employees 
    GROUP BY department_id
    HAVING COUNT(employee_id) >= 2
    )
    INNER JOIN hr.departments USING(department_id)
        INNER JOIN hr.locations USING(location_id)
            INNER JOIN hr.countries USING(country_id)
GROUP BY country_name, city

8) For each employee, display the first name, last name, department number and department name.

SELECT first_name, last_name, department_id, department_name
FROM hr.employees LEFT OUTER JOIN hr.departments USING(department_id)
WHERE first_name LIKE 'K%'

###SELECT first_name, last_name, department_id, department_name
###FROM hr.employees INNER JOIN hr.departments USING(department_id)

9) Display the first name, last name, department number and department name, for all employees in departments 50 or 90.

SELECT first_name, last_name, department_id, department_name
FROM hr.employees LEFT OUTER JOIN hr.departments USING(department_id)
WHERE department_id = 50 OR department_id = 90
ORDER BY department_id DESC

### SELECT first_name, last_name, department_id, department_name
### FROM hr.employees INNER JOIN hr.departments USING(department_id)
### WHERE department_id = 50 OR department_id = 90
### ORDER BY department_id DESC

10) For each department, display the department name, city, and state province.

SELECT department_name, city, state_province
FROM hr.departments LEFT OUTER JOIN hr.locations USING(location_id)
WHERE department_name LIKE '% %'

###SELECT department_name, city, state_province
###FROM hr.departments INNER JOIN hr.locations USING(location_id)

11) For each employee, display the full name, department name, city, and state province.

SELECT first_name, last_name, department_name, city, state_province
FROM hr.employees LEFT OUTER JOIN hr.departments USING(department_id)
    LEFT OUTER JOIN hr.locations USING(location_id)
WHERE department_name IS NULL OR state_province IS NULL

###SELECT first_name, last_name, department_name, city, state_province
###FROM hr.employees INNER JOIN hr.departments USING(department_id)
###    INNER JOIN hr.locations USING(location_id)
    
12) Display the full name, department name, city, and state province, for all employees whose last name contains the letter a.

SELECT first_name, last_name, department_name, city, state_province
FROM hr.employees LEFT OUTER JOIN hr.departments USING(department_id)
    LEFT OUTER JOIN hr.locations USING(location_id)
WHERE last_name LIKE '%a%' AND first_name LIKE 'K%'

###SELECT first_name, last_name, department_name, city, state_province
###FROM hr.employees INNER JOIN hr.departments USING(department_id)
###    INNER JOIN hr.locations USING(location_id)
###WHERE last_name LIKE '%a%'
