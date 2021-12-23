#INSERT INTO branch VALUES(4, 'Buffalo', NULL, NULL);

#SELECT *
#FROM branch

-- Find all branches and the names of their managers
# Doesn't print info about Buffalo branch
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
JOIN branch
ON employee.emp_id = branch.mgr_id;

-- Find all branches and the names of their managers
# All info from emloyee but not from branch
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
LEFT JOIN branch
ON employee.emp_id = branch.mgr_id;

-- Find all branches and the names of their managers
# All info from branch but not from employee (prints Buffalo too)
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
RIGHT JOIN branch
ON employee.emp_id = branch.mgr_id;

