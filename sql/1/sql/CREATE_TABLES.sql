CREATE TABLE Students ( 
    Student_ID int primary key, 
    School varchar2(255), 
    Age int, 
    Adress varchar2(255), 
    Famsize varchar2(255), 
    Parents_status varchar2(255), 
    School_choice_reason varchar2(255), 
    Guardian varchar2(255), 
    Travel_time int, 
    Study_time int, 
    School_support int, 
    Parent_support int, 
    Paid_classes int 
); 

CREATE TABLE Parents ( 
    Student_ID int primary key,
    Mother_edu int,
    Father_edu int,
    Mother_job varchar2(255),
    Father_job varchar2(255)
);

CREATE TABLE Social_info (
    Student_ID int primary key,
    Activities int,
    Nursary int,
    Higher int,
    Internet_access int,
    Romantic int,
    Family_relationship int,
    Free_time int,
    Go_out int,
    Daily_consumption int,
    Weekend_consumption int,
    Health int,
    Absences int
);
