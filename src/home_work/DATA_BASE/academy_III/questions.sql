-- ========= ЗАДАНИЕ 1 =========
-- 1. Количество преподавателей кафедры "Электротехника"
ALTER TABLE Teacher ADD COLUMN DepartmentId UUID;

-- Заполните этот столбец нужным значением!

SELECT COUNT(*) AS teacher_count
FROM Teacher t
JOIN Department d ON t.DepartmentId = d.Id
WHERE d.Name = 'Электротехника';

-- 2. Количество лекций, которые читает преподаватель "Жанна Иванова":
SELECT COUNT(*)
FROM Lecture l
JOIN Teacher t ON l.TeacherId = t.Id
WHERE t.Name = 'Жанна' AND t.Surname = 'Иванова';

-- 3. Количество занятий, проводимых в группе "ИТ-1":
SELECT COUNT(*)
FROM GroupLecture gl
JOIN Groups g ON gl.GroupId = g.Id
WHERE g.Name = 'ИТ-1';

-- 4. Названия аудиторий и количество лекций, проводимых в них:
SELECT g.Name AS Audience_Name, COUNT(gl.LectureId) AS Number_Lectures
FROM Groups g
LEFT JOIN GroupLecture gl ON g.Id = gl.GroupId
GROUP BY g.Name;

-- 5. Количество студентов, посещающих лекции преподавателя "Денис Жуков":
SELECT COUNT(DISTINCT gs.StudentId)
FROM GroupStudent gs
JOIN GroupLecture gl ON gs.GroupId = gl.GroupId
JOIN Lecture l ON gl.LectureId = l.Id
JOIN Teacher t ON l.TeacherId = t.Id
WHERE t.Name = 'Денис' AND t.Surname = 'Жуков';

-- 6. Средняя ставка преподавателей факультета "Теплотехника":
SELECT AVG(CAST(t.Salary AS numeric)) AS average_salary
FROM Teacher t
JOIN Department d ON t.DepartmentId = d.Id
WHERE d.FacultyId IN (SELECT f.Id FROM Faculty f WHERE f.Name = 'Теплотехника');

-- 7. Минимальное и максимальное количество студентов среди всех групп:
SELECT MIN(students_per_group.students_count) AS min_students_count,
       MAX(students_per_group.students_count) AS max_students_count
FROM (
    SELECT g.Id, COUNT(gs.StudentId) AS students_count
    FROM Groups g
    LEFT JOIN GroupStudent gs ON g.Id = gs.GroupId
    GROUP BY g.Id
) AS students_per_group;

-- 8. Средний фонд финансирования кафедр:
SELECT AVG(CAST(d.Financing AS numeric)) AS average_financing
FROM Department d;

-- 9. Полные имена преподавателей и количество читаемых ими дисциплин:
SELECT CONCAT(t.Name, ' ', t.Surname) AS Full_Name, COUNT(DISTINCT l.SubjectId) AS Disciplines_Count
FROM Teacher t
JOIN Lecture l ON t.Id = l.TeacherId
GROUP BY t.Id;

-- 10. Количество лекций в каждый день недели:
SELECT EXTRACT(DOW FROM l.Date) AS DayOfWeek, COUNT(l.Id) AS Num_Lectures
FROM Lecture l
GROUP BY DayOfWeek
ORDER BY DayOfWeek;

-- 11. Номера аудиторий и количество кафедр, чьи лекции в них читаются:
SELECT g.Name AS Audience_Name, COUNT(DISTINCT d.Id) AS Dept_Count
FROM Groups g
JOIN GroupLecture gl ON g.Id = gl.GroupId
JOIN Lecture l ON gl.LectureId = l.Id
JOIN Teacher t ON l.TeacherId = t.Id
JOIN Department d ON t.DepartmentId = d.Id
GROUP BY g.Name;

-- 12. Названия факультетов и количество дисциплин, которые на них читаются:
SELECT f.Name AS Faculty_Name, COUNT(DISTINCT s.Id) AS Subject_Count
FROM Faculty f
JOIN Department d ON f.Id = d.FacultyId
JOIN Teacher t ON d.Id = t.DepartmentId
JOIN Lecture l ON t.Id = l.TeacherId
JOIN Subject s ON l.SubjectId = s.Id
GROUP BY f.Name;

-- 13. Количество лекций для каждой пары преподаватель–аудитория:
SELECT CONCAT(t.Name, ' ', t.Surname) AS Teacher_Full_Name, g.Name AS Audience_Name, COUNT(*) AS Num_Lectures
FROM Teacher t
JOIN Lecture l ON t.Id = l.TeacherId
JOIN GroupLecture gl ON l.Id = gl.LectureId
JOIN Groups g ON gl.GroupId = g.Id
GROUP BY t.Id, g.Id;

-- ========= ЗАДАНИЕ 2 =========

-- 1. Вывести номера корпусов, если суммарный фонд финансирования расположенных в них кафедр превышает 100000:
SELECT Building
FROM Department
GROUP BY Building
HAVING SUM(Financing::numeric) > 100000;

2. Вывести названия групп 3-го курса кафедры "Педагогика и психология", которые имеют более 2 пар в первую неделю:
WITH First_Week_Lectures AS (
    SELECT gl.GroupId, COUNT(*) AS Num_Lectures
    FROM GroupLecture gl
    JOIN Lecture l ON gl.LectureId = l.Id
    WHERE l.Date BETWEEN '2023-09-01' AND '2023-09-07'
    GROUP BY gl.GroupId
)
SELECT g.Name
FROM Groups g
JOIN Department d ON g.DepartmentId = d.Id
WHERE g.Year = 3 AND d.Name = 'Педагогика и психология'
AND g.Id IN (SELECT GroupId FROM First_Week_Lectures WHERE Num_Lectures > 2);

-- 3. Вывести названия групп, чей средний рейтинг студентов выше среднего рейтинга группы "ГРП-4":
WITH Average_Ratings AS (
    SELECT g.Id, AVG(s.Rating) AS Avg_Group_Rating
    FROM Groups g
    LEFT JOIN GroupStudent gs ON g.Id = gs.GroupId
    LEFT JOIN Student s ON gs.StudentId = s.Id
    GROUP BY g.Id
)
SELECT g.Name
FROM Groups g
JOIN Average_Ratings ar ON g.Id = ar.Id
WHERE ar.Avg_Group_Rating > (
    SELECT Avg_Group_Rating
    FROM Average_Ratings
    WHERE Id = (SELECT Id FROM Groups WHERE Name = 'ГРП-4')
);

-- 4. Вывести фамилии и имена преподавателей, чья ставка выше средней ставки профессоров:
SELECT Name, Surname
FROM Teacher
WHERE CAST(Salary AS numeric) > (
    SELECT AVG(CAST(Salary AS numeric))
    FROM Teacher
    WHERE IsProfessor = TRUE
);

-- 5. Вывести названия групп, у которых больше одного куратора:
SELECT g.Name
FROM Groups g
JOIN GroupCurator gc ON g.Id = gc.GroupId
GROUP BY g.Id
HAVING COUNT(gc.CuratorId) > 1;

-- 6. Вывести названия групп, чей средний рейтинг студентов меньше минимального рейтинга групп 1-го курса:
WITH Average_Ratings AS (
    SELECT g.Id, AVG(s.Rating) AS Avg_Group_Rating
    FROM Groups g
    LEFT JOIN GroupStudent gs ON g.Id = gs.GroupId
    LEFT JOIN Student s ON gs.StudentId = s.Id
    GROUP BY g.Id
)
SELECT g.Name
FROM Groups g
JOIN Average_Ratings ar ON g.Id = ar.Id
WHERE ar.Avg_Group_Rating < (
    SELECT MIN(Avg_Group_Rating)
    FROM Average_Ratings
    WHERE Id IN (SELECT Id FROM Groups WHERE Year = 1)
);

-- 7. Вывести названия факультетов, сумма фонда финансирования кафедр которых больше суммы фондов кафедры "Педагогика и психология":
SELECT f.Name
FROM Faculty f
JOIN Department d ON f.Id = d.FacultyId
GROUP BY f.Id
HAVING SUM(d.Financing) > (
    SELECT SUM(Financing)
    FROM Department
    WHERE FacultyId = (SELECT Id FROM Faculty WHERE Name = 'Педагогика и психология')
);

-- 8. Вывести названия дисциплин и полные имена преподавателей, читающих наибольшее количество лекций по ним:
WITH Most_Lectured_Subjects AS (
    SELECT SubjectId, COUNT(*) AS Num_Lectures
    FROM Lecture
    GROUP BY SubjectId
    ORDER BY Num_Lectures DESC
    LIMIT 1
)
SELECT DISTINCT s.Name AS Subject_Name, CONCAT(t.Name, ' ', t.Surname) AS Teacher_Full_Name
FROM Lecture l
JOIN Subject s ON l.SubjectId = s.Id
JOIN Teacher t ON l.TeacherId = t.Id
WHERE l.SubjectId IN (SELECT SubjectId FROM Most_Lectured_Subjects);

-- 9. Вывести название дисциплины, по которой читается наименьшее количество лекций:
SELECT s.Name
FROM Subject s
JOIN Lecture l ON s.Id = l.SubjectId
GROUP BY s.Id
ORDER BY COUNT(*) ASC
LIMIT 1;

-- 10. Вывести количество студентов и читаемые дисциплины на кафедре "Гражданско-правовая дисциплина":
SELECT COUNT(DISTINCT gs.StudentId) AS Total_Students, COUNT(DISTINCT l.SubjectId) AS Num_Disciplines
FROM Department d
JOIN Teacher t ON d.Id = t.DepartmentId
JOIN Lecture l ON t.Id = l.TeacherId
JOIN GroupLecture gl ON l.Id = gl.LectureId
JOIN GroupStudent gs ON gl.GroupId = gs.GroupId
WHERE d.Name = 'Гражданско-правовая дисциплина';







