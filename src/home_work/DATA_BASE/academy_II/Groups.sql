INSERT INTO Groups (Name, Year, DepartmentId) VALUES
('1-ИСП', 1, (SELECT id FROM Department WHERE Name='Кафедра информатики')),
('2-МАТ', 2, (SELECT id FROM Department WHERE Name='Кафедра математики')),
('3-ФИЗ', 3, (SELECT id FROM Department WHERE Name='Кафедра физики')),
('4-ЛИТ', 4, (SELECT id FROM Department WHERE Name='Кафедра литературы')),
('5-ИСТ', 5, (SELECT id FROM Department WHERE Name='Кафедра истории')),
('6-БИОЛ', 1, (SELECT id FROM Department WHERE Name='Кафедра биологии')),
('7-ХИМ', 2, (SELECT id FROM Department WHERE Name='Кафедра химии')),
('8-ЭКО', 3, (SELECT id FROM Department WHERE Name='Кафедра экономики'));