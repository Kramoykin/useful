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

-- Take the information from student table
SELECT * FROM student;

-- Update the student table
UPDATE student
SET major = 'Bio'
WHERE major = 'Biology';

-- Take the information from student table
SELECT * FROM student;

-- Update the student table
UPDATE student
SET name = 'Tom', major = 'undecided'
WHERE student_id = 4;

-- Take the information from student table
SELECT * FROM student;


-- Update the student table
UPDATE student
SET major = 'Biochemistry'
WHERE major = 'Bio' OR major = 'Chemistry';

-- Take the information from student table
SELECT * FROM student;

-- Update the student table
UPDATE student
SET major = 'undecided';

-- Take the information from student table
SELECT * FROM student;

-- Delete specific rows from student table
DELETE FROM student
WHERE student_id = 5;

-- Take the information from student table
SELECT * FROM student;