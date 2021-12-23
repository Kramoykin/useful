#1) Create a sequence and trigger for your table to automatically fill in the "id" value

CREATE TABLE student
  (Student_ID             NUMBER(4),
   Fname                  VARCHAR(15),
   School                 VARCHAR2 (2),
   Sex                    VARCHAR2 (1),
   Age                    NUMBER(2) CONSTRAINT student_age_cc CHECK ((Age <= 24) AND (Age >= 15)),
   CONSTRAINT student_studentid_pk PRIMARY KEY (Student_ID));

CREATE SEQUENCE student_sqnc START WITH 1;

CREATE  
TRIGGER ins_student_trg BEFORE INSERT  
ON student 
FOR EACH ROW BEGIN 
    :NEW.Student_ID := student_sqnc.NEXTVAL; 
END;
/

INSERT INTO student VALUES(10, 'Kate', 'ms', 'F', 22);
INSERT INTO student VALUES(NULL, 'Karl', 'ms', 'M', 22);
INSERT INTO student(Fname) VALUES ('Malone');

SELECT * FROM student

# 2. Create a trigger that fills the table for saving logs, containing information about who and when will make changes to the table and what changes (which Conditional Predicates,  and which row (primary key))

CREATE TABLE student
  (Student_ID             NUMBER(4),
   Fname                  VARCHAR(15),
   School                 VARCHAR2 (2),
   Sex                    VARCHAR2 (1),
   Age                    NUMBER(2) CONSTRAINT student_age_cc CHECK ((Age <= 24) AND (Age >= 15)),
   CONSTRAINT student_studentid_pk PRIMARY KEY (Student_ID));

CREATE TABLE student_log
    (Student_ID   NUMBER(4),
     Log_Date     DATE,
     Action       VARCHAR(15));
     
INSERT INTO student VALUES(1, 'Kate', 'ms', 'F', 22);
INSERT INTO student VALUES(2, 'Karl', 'ms', 'M', 22);

CREATE TRIGGER student_trg 
BEFORE UPDATE OR DELETE ON student 
FOR EACH ROW 
BEGIN 
    IF UPDATING THEN
        INSERT INTO student_log VALUES(:NEW.Student_ID, SYSDATE, 'UPDATING');
    END IF;
    IF DELETING THEN
        INSERT INTO student_log VALUES(:OLD.Student_ID, SYSDATE, 'DELETING');
    END IF;
END;
/

SELECT * FROM student;

UPDATE student
SET School = 'DC'
WHERE Student_ID = 1;

DELETE FROM student
WHERE Student_ID = 2;

SELECT * FROM student;

SELECT * FROM student_log;
