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
INSERT INTO student VALUES(2, 'Kate', 'Sociology');

-- Fill some data with gaps
INSERT INTO student(student_id, name) VALUES(3, 'Claire');


-- Take the information from student table
SELECT * FROM student