INSERT INTO Faculty (Name) VALUES 
    ('Инженерный'),
    ('Психолого-педагогический'),
    ('Экономический'),
    ('Юридический'),
    ('Энергетический');

INSERT INTO Department (Building, Financing, Name, FacultyId) VALUES 
    (1, '10000', 'Электротехника', (SELECT Id FROM Faculty WHERE Name='Инженерный')),
    (2, '8000', 'Педагогика и психология', (SELECT Id FROM Faculty WHERE Name='Психолого-педагогический')),
    (3, '12000', 'Бухгалтерский учет и аудит', (SELECT Id FROM Faculty WHERE Name='Экономический')),
    (4, '15000', 'Гражданско-правовая дисциплина', (SELECT Id FROM Faculty WHERE Name='Юридический')),
    (5, '18000', 'Теплоэнергетика', (SELECT Id FROM Faculty WHERE Name='Энергетический'));

INSERT INTO Curator (Name, Surname) VALUES 
    ('Андрей', 'Степанов'),
    ('Валерия', 'Чернышова'),
    ('Николай', 'Новиков'),
    ('Виктория', 'Корнилова'),
    ('Михаил', 'Зотов');

INSERT INTO Subject (Name) VALUES 
    ('Микроэкономика'),
    ('Макроэкономика'),
    ('Финансовая отчетность'),
    ('Трудовое право'),
    ('Теплотехника');

INSERT INTO Teacher (IsProfessor, Name, Salary, Surname) VALUES 
    (TRUE, 'Денис', '60000', 'Жуков'),
    (FALSE, 'Александра', '55000', 'Рябцева'),
    (TRUE, 'Георгий', '65000', 'Шевченко'),
    (FALSE, 'Жанна', '50000', 'Иванова'),
    (TRUE, 'Константин', '70000', 'Карпов');

INSERT INTO Groups (Name, Year, DepartmentId) VALUES 
    ('ИТ-1', 1, (SELECT Id 
					FROM Department 
					WHERE Name='Электротехника')), 
    ('ПП-2', 2, (SELECT Id 
					FROM Department 
					WHERE Name='Педагогика и психология')), 
    ('БУА-3', 3, (SELECT Id 
					FROM Department 
					WHERE Name='Бухгалтерский учет и аудит')),
    ('ГРП-4', 4, (SELECT Id 
					FROM Department 
					WHERE Name='Гражданско-правовая дисциплина')),
    ('ТЕ-5', 5, (SELECT Id 
					FROM Department 
					WHERE Name='Теплоэнергетика'));

INSERT INTO GroupCurator (CuratorId, GroupId) VALUES 
    ((SELECT Id FROM Curator WHERE Name='Андрей' AND Surname='Степанов'), (SELECT Id FROM Groups WHERE Name='ИТ-1')),
    ((SELECT Id FROM Curator WHERE Name='Валерия' AND Surname='Чернышова'), (SELECT Id FROM Groups WHERE Name='ПП-2')),
    ((SELECT Id FROM Curator WHERE Name='Николай' AND Surname='Новиков'), (SELECT Id FROM Groups WHERE Name='БУА-3')),
    ((SELECT Id FROM Curator WHERE Name='Виктория' AND Surname='Корнилова'), (SELECT Id FROM Groups WHERE Name='ГРП-4')),
    ((SELECT Id FROM Curator WHERE Name='Михаил' AND Surname='Зотов'), (SELECT Id FROM Groups WHERE Name='ТЕ-5'));

INSERT INTO Student (Name, Rating, Surname) VALUES 
    ('Леонид', 4, 'Серов'),
    ('Оксана', 5, 'Матвеева'),
    ('Борис', 3, 'Ершов'),
    ('Анжелика', 4, 'Костина'),
    ('Станислав', 5, 'Баранов');

INSERT INTO GroupStudent (GroupId, StudentId) VALUES 
    ((SELECT Id FROM Groups WHERE Name='ИТ-1'), (SELECT Id FROM Student WHERE Name='Леонид' AND Surname='Серов')),
    ((SELECT Id FROM Groups WHERE Name='ПП-2'), (SELECT Id FROM Student WHERE Name='Оксана' AND Surname='Матвеева')),
    ((SELECT Id FROM Groups WHERE Name='БУА-3'), (SELECT Id FROM Student WHERE Name='Борис' AND Surname='Ершов')),
    ((SELECT Id FROM Groups WHERE Name='ГРП-4'), (SELECT Id FROM Student WHERE Name='Анжелика' AND Surname='Костина')),
    ((SELECT Id FROM Groups WHERE Name='ТЕ-5'), (SELECT Id FROM Student WHERE Name='Станислав' AND Surname='Баранов'));

INSERT INTO Lecture (Date, SubjectId, TeacherId) VALUES 
    ('2023-10-09', (SELECT Id FROM Subject WHERE Name='Микроэкономика'), (SELECT Id FROM Teacher WHERE Name='Денис' AND Surname='Жуков')),
    ('2023-10-10', (SELECT Id FROM Subject WHERE Name='Макроэкономика'), (SELECT Id FROM Teacher WHERE Name='Александра' AND Surname='Рябцева')),
    ('2023-10-11', (SELECT Id FROM Subject WHERE Name='Финансовая отчетность'), (SELECT Id FROM Teacher WHERE Name='Георгий' AND Surname='Шевченко')),
    ('2023-10-12', (SELECT Id FROM Subject WHERE Name='Трудовое право'), (SELECT Id FROM Teacher WHERE Name='Жанна' AND Surname='Иванова')),
    ('2023-10-13', (SELECT Id FROM Subject WHERE Name='Теплотехника'), (SELECT Id FROM Teacher WHERE Name='Константин' AND Surname='Карпов'));

INSERT INTO GroupLecture (GroupId, LectureId) VALUES 
    ((SELECT Id FROM Groups WHERE Name='ИТ-1'), (SELECT Id FROM Lecture WHERE Date='2023-10-09')),
    ((SELECT Id FROM Groups WHERE Name='ПП-2'), (SELECT Id FROM Lecture WHERE Date='2023-10-10')),
    ((SELECT Id FROM Groups WHERE Name='БУА-3'), (SELECT Id FROM Lecture WHERE Date='2023-10-11')),
    ((SELECT Id FROM Groups WHERE Name='ГРП-4'), (SELECT Id FROM Lecture WHERE Date='2023-10-12')),
    ((SELECT Id FROM Groups WHERE Name='ТЕ-5'), (SELECT Id FROM Lecture WHERE Date='2023-10-13'));


