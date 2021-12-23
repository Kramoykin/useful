-- Find a list of employees and branch names
#Number of columns should be the same
#Datatypes should be the same
#Outputted name of the column is first_name -> not correct
SELECT first_name
FROM employee
UNION
SELECT branch_name
FROM branch;

-- Find a list of employees and branch names
#Fix the column name
SELECT first_name AS 'forename,branchname'
FROM employee
UNION
SELECT branch_name
FROM branch;

-- Find all the clients and branch suppliers
SELECT client_name, client.branch_id
FROM client
UNION
SELECT supplier_name, branch_supplier.branch_id
FROM branch_supplier;

-- Find a list of all moneys spent or earned by company
SELECT salary
FROM employee
UNION
SELECT total_sales
FROM works_with;

	



