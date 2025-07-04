-- Таблица Кафедры - Departments
CREATE TABLE departments (
	id SERIAL PRIMARY KEY,
	financing NUMERIC(15, 2) DEFAULT 0 NOT NULL CHECK(financing >= 0),
	name VARCHAR(100) UNIQUE NOT NULL
);

-- Таблица Факультеты - Faculties
CREATE TABLE faculties (
	id SERIAL PRIMARY KEY,
	dean TEXT NOT NULL,
	name VARCHAR(100) UNIQUE NOT NULL
);

-- DROP TABLE groups;
-- Таблица Группы - groups
CREATE TABLE groups (
	id SERIAL PRIMARY KEY,
	name VARCHAR(20) UNIQUE NOT NULL,
	rating INTEGER NOT NULL CHECK(rating BETWEEN 0 AND 5),
	year INTEGER NOT NULL CHECK(year BETWEEN 1 AND 5)
);

-- Таблица Преподаватели - teachers
CREATE TABLE teachers (
	id SERIAL PRIMARY KEY,
	employment_date DATE NOT NULL CHECK(employment_date >= '01.01.1990'),
	is_assistant BOOLEAN DEFAULT FALSE NOT NULL,
	is_professor BOOLEAN DEFAULT FALSE NOT NULL,
	name TEXT NOT NULL,
	position TEXT NOT NULL,
	premium DECIMAL(10, 2) DEFAULT 0 NOT NULL CHECK(premium >= 0),
	salary DECIMAL(10, 2) NOT NULL CHECK(salary >= 0),
	surname TEXT NOT NULL
);

-- Данные по кафедрам
INSERT INTO departments (financing, name) VALUES
	('100000', 'Физика'),
	('80000', 'Химия'),
	('70000', 'Биология'),
	('120000', 'Информатика'),
	('90000', 'История'),
	('60000', 'Экономика'),
	('110000', 'Психология'),
	('50000', 'Право'),
	('130000', 'География'),
	('75000', 'Экология'),
	('105000', 'Литература'),
	('95000', 'Философия');

-- Данные факультетов
INSERT INTO faculties (dean, name) VALUES
	('Иван Петров', 'Физико-математический факультет'),
	('Анна Смирнова', 'Естественно-научный факультет'),
	('Сергей Иванов', 'Филологический факультет'),
	('Евгений Кузнецов', 'Экономический факультет'),
	('Дмитрий Романов', 'Исторический факультет'),
	('Михаил Федоров', 'Юридический факультет'),
	('Александра Сергеева', 'Педагогический факультет'),
	('Наталья Михайловская', 'Медицинский факультет'),
	('Андрей Сергеевич', 'Архитектурный факультет'),
	('Владимир Иванович', 'Политехнический факультет'),
	('Светлана Викторовна', 'Музыкально-художественный факультет'),
	('Антон Алексеевич', 'Социально-гуманитарный факультет');

-- Данные групп
INSERT INTO groups (name, rating, year) VALUES
	('ФИЗИКА-1', 4, 3),
	('ХИМИЯ-1', 3, 2),
	('БИОЛОГИЯ-1', 5, 1),
	('ИНФОРМАЦИЯ-1', 4, 4),
	('ИСТОРИЯ-1', 4, 2),
	('ЭКОНОМИКА-1', 3, 3),
	('ПСИХОЛОГИЯ-1', 5, 1),
	('ПРАВО-1', 4, 4),
	('ГЕОГРАФИЯ-1', 3, 2),
	('ЭКОЛОГИЯ-1', 5, 1),
	('ЛИТЕРАТУРА-1', 4, 3),
	('ФИЛОСОФИЯ-1', 3, 2),
	('ФИЗИКА-2', 4, 4),
	('ХИМИЯ-2', 3, 1),
	('БИОЛОГИЯ-2', 5, 2),
	('ИНФОРМАЦИЯ-2', 4, 3),
	('ИСТОРИЯ-2', 4, 1),
	('ЭКОНОМИКА-2', 3, 4),
	('ПСИХОЛОГИЯ-2', 5, 2),
	('ПРАВО-2', 4, 1),
	('ГЕОГРАФИЯ-2', 3, 3),
	('ЭКОЛОГИЯ-2', 5, 4),
	('ЛИТЕРАТУРА-2', 4, 2),
	('ФИЛОСОФИЯ-2', 3, 1);

-- Данные о преподавателях
INSERT INTO teachers (employment_date, is_assistant, is_professor, name, position, premium, salary, surname) VALUES
	('2010-01-01', TRUE, FALSE, 'Алексей', 'Ассистент', 5000, 30000, 'Сергеев'),
	('2005-06-15', FALSE, TRUE, 'Марина', 'Доцент', 10000, 50000, 'Васильева'),
	('2015-09-01', FALSE, FALSE, 'Александр', 'Старший преподаватель', 7000, 40000, 'Николаев'),
	('2000-02-28', TRUE, TRUE, 'Ольга', 'Профессор', 15000, 60000, 'Петрова'),
	('2012-03-15', TRUE, FALSE, 'Павел', 'Ассистент', 6000, 35000, 'Андреев'),
	('2008-09-01', FALSE, TRUE, 'Виктор', 'Доцент', 12000, 55000, 'Семенов'),
	('2018-01-10', FALSE, FALSE, 'Валерия', 'Старший преподаватель', 8000, 45000, 'Кириллова'),
	('2002-05-20', TRUE, TRUE, 'Константин', 'Профессор', 16000, 65000, 'Романов'),
	('2014-07-05', TRUE, FALSE, 'Дарья', 'Ассистент', 7000, 40000, 'Шарова'),
	('2006-11-15', FALSE, TRUE, 'Борис', 'Доцент', 11000, 52000, 'Игнатьев'),
	('2016-03-20', FALSE, FALSE, 'Николай', 'Старший преподаватель', 9000, 48000, 'Дроздов'),
	('2003-08-10', TRUE, TRUE, 'Тамара', 'Профессор', 17000, 70000, 'Зубкова');

SELECT
	id,
	to_char(employment_date, 'DD.MM.YYYY') AS "Дата приема",
	is_assistant AS "Ассистент",
	is_professor AS "Профессор",
	name AS "Имя",
	surname AS "Фамилия",
	position AS "Статус",
	lpad(to_char(premium, 'FM999G999G999D99'), 15)AS "Премия",
	lpad(to_char(salary, 'FM999G999G999D99'), 15) AS "Оклад"
FROM public.teachers
ORDER BY id ASC

-- Вывести таблицу кафедр, но расположить ее поля в
-- обратном порядке.
SELECT
	name,
	to_char(financing, 'fm999g999'),
	id
FROM
	departments;

-- Вывести названия групп и их рейтинги
-- с уточнением имен полей именем таблицы.
SELECT
	groups.name as "Имя Группы",
	groups.rating as "Рейтинг группы"
FROM
	groups;

-- Вывести для преподавателей их фамилию,
-- процент ставки по отношению к надбавке и
-- процент ставки по отношению к зарплате (сумма ставки и надбавки).
SELECT
	surname,
	CASE WHEN premium <> 0 THEN ROUND((salary / premium) * 100, 2)
	ELSE NULL END AS "Процент оклада относительно премии",
	CASE WHEN premium <> 0 THEN ROUND((salary / (salary + premium)) * 100, 2)
	ELSE NULL END AS "Процент оклада к премии"
FROM
	teachers;

-- Вывести таблицу факультетов в виде одного поля
-- в следующем формате:
-- "Декан факультета [faculty] это [dean].".
SELECT CONCAT('Декан ',name,'  :  ',dean,'.') AS "ИНФОРМАЦИЯ"
FROM faculties;

-- Вывести фамилии преподавателей, которые являются
-- профессорами и ставка которых превышает 1050.
SELECT surname FROM teachers
WHERE is_professor = True AND salary > 1050;

-- Вывести названия кафедр, фонд финансирования
-- которых меньше 11000 или больше 25000.
SELECT name FROM departments
WHERE financing < 11000 AND financing > 25000;

-- Вывести названия факультетов кроме факультета
-- “Computer Science”.
SELECT Name
FROM Faculties
WHERE Name != 'Computer Science';

-- Вывести фамилии и должности преподавателей,
-- которые не являются профессорами
SELECT surname, position
FROM teachers
WHERE is_professor = False;

-- Вывести фамилии, должности, ставки и надбавки
-- ассистентов, у которых надбавка в диапазоне от 5000
-- до 10000
SELECT surname, position, salary, premium
FROM teachers
WHERE is_assistant = True AND premium BETWEEN 5000 AND 10000;

--Вывести фамилии и ставки ассистентов
SELECT surname, salary
FROM teachers
WHERE is_assistant = True;

-- Вывести фамилии и должности преподавателей, ко
-- торые были приняты на работу до 01.01.2000.
SELECT surname, position
FROM teachers
WHERE employment_date < '2010-01-01';

-- Вывести названия кафедр, которые в алфавитном порядке
-- располагаются до кафедры "Software Development”.
-- Выводимое поле должно иметь название “Name of Department”.
SELECT name AS "Литература"
FROM departments
WHERE name < 'Литература'
ORDER BY name;

-- Вывести фамилии ассистентов, имеющих зарплату
-- (сумма ставки и надбавки) не более 1200.
SELECT surname
FROM teachers
WHERE is_assistant = True AND (salary + premium) <= 50000;

-- Вывести названия групп 4-го курса, имеющих рейтинг
-- в диапазоне от 2 до 4.
SELECT name
FROM groups
WHERE year = 4 AND rating BETWEEN 2 AND 4;

-- Вывести фамилии ассистентов со ставкой меньше 20000
-- или надбавкой меньше 8000.
SELECT surname
FROM teachers
WHERE is_assistant = True AND (salary < 20000 OR premium < 8000);