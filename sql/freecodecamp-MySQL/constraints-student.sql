-- Delete the table 
DROP TABLE student;

-- Create the table
CREATE TABLE student(
	student_id INT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) UNIQUE,
    PRIMARY KEY(student_id)
);

-- Fill the table
INSERT INTO student VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
-- INSERT INTO student VALUES(3, NULL, 'Chemistry'); -> Will not work (NOT NULL)
-- INSERT INTO student VALUES(4, 'Jack', 'Biology'); -> Will not work (UNIQUE)
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');

-- Take the information from student table
SELECT * FROM student;


-- Delete the table 
DROP TABLE student;

-- Create the table
CREATE TABLE student(
	student_id INT,
    name VARCHAR(20),
    major VARCHAR(20) DEFAULT 'undecided',
    PRIMARY KEY(student_id)
);

-- Fill the table
INSERT INTO student VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
INSERT INTO student(student_id, name) VALUES(3, 'Claire'); -- -> Will work due to default value 
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');

-- Take the information from student table
SELECT * FROM student;


-- Create the table
CREATE TABLE student(
	student_id INT AUTO_INCREMENT,
    name VARCHAR(20),
    major VARCHAR(20) DEFAULT 'undecided',
    PRIMARY KEY(student_id)
);

-- Fill the table
INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Kate', 'Sociology');

-- Take the information from student table
SELECT * FROM student;