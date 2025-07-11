INSERT INTO Department (Name, Financing, FacultyId) VALUES
('Кафедра математики', '300000'::money, (SELECT id FROM Facultie WHERE Name='Физико-математический факультет')),
('Кафедра информатики', '250000'::money, (SELECT id FROM Facultie WHERE Name='Физико-математический факультет')),
('Кафедра физики', '200000'::money, (SELECT id FROM Facultie WHERE Name='Физико-математический факультет')),
('Кафедра литературы', '250000'::money, (SELECT id FROM Facultie WHERE Name='Филологический факультет')),
('Кафедра истории', '200000'::money, (SELECT id FROM Facultie WHERE Name='Исторический факультет')),
('Кафедра биологии', '150000'::money, (SELECT id FROM Facultie WHERE Name='Биологический факультет')),
('Кафедра химии', '180000'::money, (SELECT id FROM Facultie WHERE Name='Химический факультет')),
('Кафедра экономики', '400000'::money, (SELECT id FROM Facultie WHERE Name='Экономический факультет'));