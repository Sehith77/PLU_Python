USE company;

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    CourseID INT
);

INSERT INTO Course (CourseID, CourseName)
VALUES
(101, 'Python'),
(102, 'Java');

INSERT INTO Student (StudentID, Name, CourseID)
VALUES
(1, 'Rahul', 101),
(2, 'Neha', 102),
(3, 'Aman', 101);

SELECT Student.Name, Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID;

SELECT Student.Name, Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID
WHERE Course.CourseName = 'Python';

CREATE VIEW PythonStudents AS
SELECT Student.Name, Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID
WHERE Course.CourseName = 'Python';

SELECT * FROM PythonStudents;