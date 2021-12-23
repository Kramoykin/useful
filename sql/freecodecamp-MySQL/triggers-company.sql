-- CREATE TABLE triggers_test (
-- 	message VARCHAR(100)
-- );

-- DELIMITER $$
-- 	TRIGGER mu_trigger BEFORE INSERT
--     ON employee
--     FOR EACH ROW BEGIN
-- 		IF NEW.sex = 'M' THEN
-- 			INSERT INTO triggers_test VALUES('added male employee');
-- 		ELSEIF NEW.sex = 'F' THEN
-- 			INSERT INTO triggers_test VALUES('added female employee');
-- 		ELSE
-- 			INSERT INTO triggers_test VALUES('added other employee');
-- 		END IF;
-- 	END $$
-- DELIMITER ;

-- INSERT INTO employee
-- VALUES(110, 'Kevin', 'Malone', '1978-02-19', 'M', 69000, 106, 3);

-- INSERT INTO employee
-- VALUES(111, 'Pam', 'Beesly', '1988-02-19', 'F', 69000, 106, 3);

-- DELIMITER $$
-- CREATE
-- 	TRIGGER my_trigger1 BEFORE INSERT
--     ON employee
--     FOR EACH ROW BEGIN
-- 		INSERT INTO triggers_test VALUES(NEW.first_name);
-- 	END $$
-- DELIMITER ;

-- INSERT INTO employee
-- VALUES(112, 'Dwait', 'Shroot', '1978-02-19', 'M', 69000, 106, 3);

SELECT * FROM employee;

SELECT * FROM triggers_test;



