-- Create the table
CREATE TABLE student(
	student_id INT,
    name VARCHAR(20),
    major VARCHAR(20),
    PRIMARY KEY(student_id)
);

-- Describe table
DESCRIBE student;

-- Delete the table 
DROP TABLE student;

-- Add column
ALTER TABLE student ADD gpa DECIMAL(3, 2); 

-- Remove column
ALTER TABLE student DROP COLUMN gpa; 


