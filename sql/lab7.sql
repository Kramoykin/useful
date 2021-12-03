### SQL HIERARCHICAL QUERRIES

1) Return the name of each employee in department 20, each manager above that employee in the hierarchy, the number of levels between manager and employee, and the path between the two.

SELECT last_name "EMPLOYEE", CONNECT_BY_ROOT last_name "MANAGER",
   (LEVEL-1) "LAYERS_NUM", SYS_CONNECT_BY_PATH(last_name, '/') "PATH"
   FROM hr.employees
   WHERE department_id = 20
   CONNECT BY PRIOR employee_id = manager_id;

2) Return list employees  in a hierarchy view with their subordinates underneath them with salary more then 12000

SELECT employee_id, last_name "EMPLOYEE", manager_id "MNG_ID",  (LEVEL-1) "LAYERS_NUM", salary
FROM hr.employees
WHERE salary > 12000
START WITH manager_id is null
CONNECT BY PRIOR employee_id = manager_id

3) Does King have any authority over Hunold?

SELECT SYS_CONNECT_BY_PATH(last_name, '/') as Path
   FROM hr.employees
   WHERE last_name = 'Hunold'
   START WITH manager_id is null
   CONNECT BY PRIOR employee_id = manager_id;
   
4) Return sum the salaries of all employees in department headed by Blake from 2 lavel

SELECT SUM(salary)
FROM hr.employees
START WITH manager_id =
    (SELECT employee_id
    FROM hr.employees
    WhERE last_name = 'Kochhar')
CONNECT BY PRIOR employee_id = manager_id

5) Return list employees with level sorting by name with their manager name

SELECT employee_id, manager_id, first_name, last_name, level,
 PRIOR last_name as Manager
FROM hr.employees
START WITH manager_id is null
CONNECT BY PRIOR employee_id = manager_id
ORDER SIBLINGS BY last_name

6) Return first_name, last_name and salary for employee with id = 100 for 5 times

SELECT first_name, last_name, salary
FROM hr.employees
START WITH employee_id = 100
CONNECT BY rownum <= 5

7) Print tree-like representation of employees hierarchy for all employees with last names starting with K.

SELECT lpad(' ', 2*LEVEL)||last_name as Tree
FROM hr.employees
WHERE last_name LIKE 'K%'
START WITH manager_id is null
CONNECT BY PRIOR employee_id = manager_id
ORDER SIBLINGS BY last_name

8) Print employee_id, manager_id, first_name, last_name, level, is leaf or not, manager_name and CEO last name for all employees

SELECT employee_id, manager_id, first_name, last_name, level,
 CONNECT_BY_ISLEAF as IsLeaf,
 PRIOR last_name as Manager,
 CONNECT_BY_ROOT last_name as CEO
FROM hr.employees
START WITH manager_id is null
CONNECT BY PRIOR employee_id = manager_id

