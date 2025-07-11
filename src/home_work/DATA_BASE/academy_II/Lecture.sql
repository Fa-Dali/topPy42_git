INSERT INTO Lecture (LectureRoom, SubjectId, TeacherId) VALUES
('Аудитория 101', (SELECT id FROM Subject WHERE Name='Высшая математика'), (SELECT id FROM Teacher WHERE Name='Александр')),
('Аудитория 202', (SELECT id FROM Subject WHERE Name='Программирование'), (SELECT id FROM Teacher WHERE Name='Игорь')),
('Аудитория 303', (SELECT id FROM Subject WHERE Name='История России'), (SELECT id FROM Teacher WHERE Name='Анна')),
('Аудитория 404', (SELECT id FROM Subject WHERE Name='Литература зарубежная'), (SELECT id FROM Teacher WHERE Name='Павел')),
('Аудитория 505', (SELECT id FROM Subject WHERE Name='Общая биология'), (SELECT id FROM Teacher WHERE Name='Марина')),
('Аудитория 606', (SELECT id FROM Subject WHERE Name='Органическая химия'), (SELECT id FROM Teacher WHERE Name='Виктор')),
('Аудитория 707', (SELECT id FROM Subject WHERE Name='Макроэкономика'), (SELECT id FROM Teacher WHERE Name='Елена')),
('Аудитория 808', (SELECT id FROM Subject WHERE Name='Теоретическая физика'), (SELECT id FROM Teacher WHERE Name='Михаил'));