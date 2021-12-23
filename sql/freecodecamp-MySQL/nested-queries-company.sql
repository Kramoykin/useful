-- Find names of all employees who sold 
-- over 30,000 for a single client
SELECT employee.first_name, employee.last_name
FROM employee
WHERE employee.emp_id IN (
	SELECT works_with.emp_id
	FROM works_with
	WHERE works_with.total_sales > 30000
    );
    
-- Find all clients who are handled by the branch
-- that Michael Scott manages
# Limited for the ase where Michael can manage several branches 
SELECT *
FROM client
WHERE client.branch_id = 
	(SELECT branch.branch_id
	FROM branch
	WHERE branch.mgr_id = (
		SELECT employee.emp_id
		FROM employee
		WHERE employee.first_name = 'Michael' and employee.last_name = 'Scott'
		) LIMIT 1
	);
    
