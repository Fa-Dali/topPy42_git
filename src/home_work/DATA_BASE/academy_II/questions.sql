-- Вывести все возможные пары строк преподавателей и групп.
-- SELECT t.Name || ' ' || t.Surname AS teacher_fullname, g.Name AS group_name
-- FROM Teacher t CROSS JOIN Groups g;

-- Вывести названия факультетов, фонд финансирования 
-- кафедр которых превышает фонд финансирования факультета.
-- SELECT f.Name AS faculty_name
-- FROM Facultie f
-- INNER JOIN Department d ON f.Id = d.FacultyId
-- WHERE d.Financing > f.Financing;

-- -- Вывести фамилии кураторов групп и названия групп, 
-- -- которые они курируют.
-- SELECT c.Surname AS curator_surname, g.Name AS group_name
-- FROM Curator c
-- INNER JOIN GroupCurator gc ON c.Id = gc.CuratorId
-- INNER JOIN Groups g ON gc.GroupId = g.Id;

-- -- Вывести имена и фамилии преподавателей, которые 
-- -- читают лекции у группы “3-ФИЗ”.
-- SELECT DISTINCT t.Name || ' ' || t.Surname AS teacher_fullname
-- FROM Teacher t
-- INNER JOIN Lecture l ON t.Id = l.TeacherId
-- INNER JOIN GroupLecture gl ON l.Id = gl.LectureId
-- INNER JOIN Groups g ON gl.GroupId = g.Id
-- WHERE g.Name = '3-ФИЗ';

-- -- Вывести фамилии преподавателей и названия факультетов, 
-- -- на которых они читают лекции.
-- SELECT DISTINCT t.Surname AS teacher_surname, f.Name AS faculty_name
-- FROM Teacher t
-- INNER JOIN Lecture l ON t.Id = l.TeacherId
-- INNER JOIN GroupLecture gl ON l.Id = gl.LectureId
-- INNER JOIN Groups g ON gl.GroupId = g.Id
-- INNER JOIN Department d ON g.DepartmentId = d.Id
-- INNER JOIN Facultie f ON d.FacultyId = f.Id;

-- -- Вывести названия кафедр и названия групп, которые к ним относятся.
-- SELECT d.Name AS department_name, g.Name AS group_name
-- FROM Department d
-- INNER JOIN Groups g ON d.Id = g.DepartmentId;

-- -- Вывести названия дисциплин, 
-- -- которые читает преподаватель “Samantha Adams”.
-- SELECT s.Name AS subject_name
-- FROM Subject s
-- INNER JOIN Lecture l ON s.Id = l.SubjectId
-- INNER JOIN Teacher t ON l.TeacherId = t.Id
-- WHERE t.Name = 'Виктор' AND t.Surname = 'Петрович';

-- -- Вывести названия кафедр, на которых читается дисциплина.
-- SELECT DISTINCT d.Name AS department_name
-- FROM Department d
-- INNER JOIN Lecture l ON d.Id = l.SubjectId;

-- -- Вывести названия групп, которые относятся 
-- -- к факультету “Computer Science”.
-- SELECT g.Name AS group_name
-- FROM Groups g
-- INNER JOIN Department d ON g.DepartmentId = d.Id
-- INNER JOIN Facultie f ON d.FacultyId = f.Id
-- WHERE f.Name = 'Исторический факультет';

-- -- Вывести названия групп 3-го курса, а также 
-- -- название факультетов, к которым они относятся.
-- SELECT g.Name AS group_name, f.Name AS faculty_name
-- FROM Groups g
-- INNER JOIN Department d ON g.DepartmentId = d.Id
-- INNER JOIN Facultie f ON d.FacultyId = f.Id
-- WHERE g.Year = 3;

-- -- Вывести полные имена преподавателей и лекции, 
-- -- которые они читают (названия дисциплин и групп), 
-- -- причем отобрать только те лекции, которые читаются 
-- -- в аудитории “Аудитория 505”.
-- SELECT CONCAT(t.Name, ' ', t.Surname) AS teacher_fullname,
--        s.Name AS subject_name,
--        g.Name AS group_name
-- FROM Teacher t
-- INNER JOIN Lecture l ON t.Id = l.TeacherId
-- INNER JOIN Subject s ON l.SubjectId = s.Id
-- INNER JOIN GroupLecture gl ON l.Id = gl.LectureId
-- INNER JOIN Groups g ON gl.GroupId = g.Id
-- WHERE l.LectureRoom = 'Аудитория 505';









