CREATE TABLE student
  (Student_ID             NUMBER(4),
   School                 VARCHAR2 (2),
   Sex                    VARCHAR2 (1),
   Age                    NUMBER(2) CONSTRAINT student_age_cc CHECK ((Age <= 24) AND (Age >= 15)),
   Adress                 VARCHAR2 (15),
   Famsize                VARCHAR2 (15),
   Parents_status         VARCHAR2 (15),
   School_choice_reason   VARCHAR2 (15),
   Guardian               VARCHAR2 (15),
   Travel_time            NUMBER (3),
   Failures               NUMBER (2) DEFAULT 0,
   School_support         NUMBER(1),
   Family_support         NUMBER(1),
   Paid_classes           NUMBER(1),
   Father_ID              NUMBER(4),
   Mother_ID              NUMBER(4),
   CONSTRAINT student_studentid_pk PRIMARY KEY (Student_ID));
   
DESCRIBE student; 

CREATE TABLE parent
    (Parent_ID      NUMBER(4),
     Parent_edu     NUMBER(1) CONSTRAINT parent_edu_cc CHECK ((Parent_edu <= 5) AND (Parent_edu > 0)),
     Parent_job     VARCHAR(15),
     CONSTRAINT parend_parentid_pk PRIMARY KEY (Parent_ID));
     
DESCRIBE parent; 

ALTER TABLE student
ADD CONSTRAINT student_fatherid_fk
FOREIGN KEY (Father_ID)
REFERENCES parent(Parent_ID)
ON DELETE SET NULL;

ALTER TABLE student
ADD CONSTRAINT student_matherid_fk
FOREIGN KEY (Mother_ID)
REFERENCES parent(Parent_ID)
ON DELETE SET NULL;

DESCRIBE student; 

ALTER TABLE student
DROP COLUMN Paid_classes;

ALTER TABLE student
DROP COLUMN Schoo;_support;

# Will be an error
ALTER TABLE student
DROP COLUMN Student_ID;

# Why we should add CASCADE CONSTRAINTS even in case we use ON DELETE SET NULL?
DROP TABLE parent
CASCADE CONSTRAINTS;

################################################################################
ALTER TABLE student
DROP COLUMN Paid_classes;

ALTER TABLE student
DROP COLUMN School_support;

ALTER TABLE student
DROP COLUMN Adress;

ALTER TABLE student
DROP COLUMN Famsize;

ALTER TABLE student
DROP COLUMN School_choice_reason;

ALTER TABLE student
DROP COLUMN Parents_status;

ALTER TABLE student
DROP COLUMN Guardian;

ALTER TABLE student
DROP COLUMN Travel_time;

ALTER TABLE student
DROP COLUMN Failures;

ALTER TABLE student
DROP COLUMN Family_support;
#################################################################################

INSERT INTO student VALUES(1, 'DC', 'F', 19, Null, Null);
INSERT INTO student VALUES(2, 'MS', 'M', 21, Null, Null);
INSERT INTO student VALUES(3, 'MS', 'F', 22, Null, Null);

INSERT INTO parent VALUES(1001, 3, 'CEO');
INSERT INTO parent VALUES(1002, 1, 'musician');
INSERT INTO parent VALUES(1003, 3, '---');
INSERT INTO parent VALUES(1004, 3, '---');
INSERT INTO parent VALUES(1005, 3, '---');
INSERT INTO parent VALUES(1006, 3, Null);

UPDATE student
SET Mother_ID = 1001
WHERE Student_ID = 1;

UPDATE student
SET Father_ID = 1003
WHERE Student_ID = 1;

INSERT INTO student VALUES(4, 'MS', 'M', 22, 1005, 1006);

SELECT * FROM student;

DELETE FROM student
WHERE Sex = 'F';

SELECT * FROM student;

# Not NULL
INSERT INTO student VALUES(Null, 'DC', 'F', 19, Null, Null);

# FK
INSERT INTO student VALUES(1, 'DC', 'F', 19, 12, 13);

# CHECK CONSTRAINT
INSERT INTO student VALUES(1, 'DC', 'F', 44, NULL, NULL);

### OPERATIONS
INSERT INTO student VALUES(1, 'DC', 'F', 19, Null, Null);
INSERT INTO student VALUES(2, 'MS', 'M', 21, Null, Null);
INSERT INTO student VALUES(3, 'MS', 'F', 22, Null, Null);

INSERT INTO parent VALUES(1001, 3, 'CEO');
INSERT INTO parent VALUES(1002, 1, 'musician');
INSERT INTO parent VALUES(1003, 3, '---');
INSERT INTO parent VALUES(1004, 3, '---');
INSERT INTO parent VALUES(1005, 3, '---');
INSERT INTO parent VALUES(1006, 3, Null);

UPDATE student
SET Mother_ID = 1001
WHERE Student_ID = 1;

UPDATE student
SET Father_ID = 1003
WHERE Student_ID = 1;

INSERT INTO student VALUES(4, 'MS', 'M', 22, 1005, 1006);

DELETE FROM student
WHERE Sex = 'F';

SELECT * FROM student;

