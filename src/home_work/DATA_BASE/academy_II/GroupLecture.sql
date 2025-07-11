INSERT INTO GroupLecture (GroupId, LectureId) VALUES
((SELECT id FROM Groups WHERE Name='1-ИСП'), (SELECT id FROM Lecture WHERE LectureRoom='Аудитория 101')),
((SELECT id FROM Groups WHERE Name='2-МАТ'), (SELECT id FROM Lecture WHERE LectureRoom='Аудитория 202')),
((SELECT id FROM Groups WHERE Name='3-ФИЗ'), (SELECT id FROM Lecture WHERE LectureRoom='Аудитория 303')),
((SELECT id FROM Groups WHERE Name='4-ЛИТ'), (SELECT id FROM Lecture WHERE LectureRoom='Аудитория 404')),
((SELECT id FROM Groups WHERE Name='5-ИСТ'), (SELECT id FROM Lecture WHERE LectureRoom='Аудитория 505')),
((SELECT id FROM Groups WHERE Name='6-БИОЛ'), (SELECT id FROM Lecture WHERE LectureRoom='Аудитория 606')),
((SELECT id FROM Groups WHERE Name='7-ХИМ'), (SELECT id FROM Lecture WHERE LectureRoom='Аудитория 707')),
((SELECT id FROM Groups WHERE Name='8-ЭКО'), (SELECT id FROM Lecture WHERE LectureRoom='Аудитория 808'));