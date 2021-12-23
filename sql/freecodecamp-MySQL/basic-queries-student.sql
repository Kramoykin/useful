-- Delete the table 
DROP TABLE student;

-- Create the table
CREATE TABLE student(
	student_id INT,
    name VARCHAR(20),
    major VARCHAR(20),
    PRIMARY KEY(student_id)
);

-- Fill the table
INSERT INTO student VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
INSERT INTO student VALUES(3, 'Claire', 'Chemistry');
INSERT INTO student VALUES(4, 'Jack', 'Biology');
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');

-- Take the info from student table
SELECT * 
FROM student
ORDER BY student_id DESC
LIMIT 2;

-- Take the info from student table
SELECT * 
FROM student
WHERE name IN ('Claire', 'Kate');