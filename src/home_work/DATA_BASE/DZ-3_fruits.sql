CREATE TABLE fruits_and_vegetables (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	type VARCHAR(20) CHECK(type IN ('овощ', 'фрукт')) NOT NULL,
	color VARCHAR(50) NOT NULL,
	colories DECIMAL(5, 2) NOT NULL,
	description TEXT
);

INSERT INTO fruits_and_vegetables (name, type, color, colories, description) VALUES
	('Помидор', 'овощ', 'Красный', 18.00, 'Плоды томата.'),
	('Огурец', 'овощ', 'Зелёный', 15.00, 'Свежий зелёный огурец.'),
	('Морковь', 'овощ', 'Оранжевый', 41.00, 'Корнеплод, богатый витаминами.'),
	('Капуста', 'овощ', 'Белый', 25.00, 'Обычная белокочанная капуста.'),
	('Апельсин', 'фрукт', 'Оранжевый', 47.00, 'Яркий цитрусовый фрукт.'),
	('Яблоко', 'фрукт', 'Зелёный', 52.00, 'Полезный кисло-сладкий фрукт.'),
	('Клубника', 'фрукт', 'Красный', 32.00, 'Маленькие сладкие ягоды.'),
	('Арбуз', 'фрукт', 'Зелёный снаружи, красный внутри', 30.00, 'Летняя бахчевая культура.'),
	('Авокадо', 'фрукт', 'Зелёный', 160.00, 'Маслянистый экзотический фрукт.'),
	('Брокколи', 'овощ', 'Зелёный', 34.00, 'Полезный вид капусты.');

-- Отображение всех овощей с калорийностью меньше указанной
SELECT * FROM fruits_and_vegetables
WHERE type = 'овощ' AND colories < 50;

-- Отображение всех фруктов с калорийностью в указанном диапазоне
SELECT * FROM fruits_and_vegetables
WHERE type = 'фрукт' AND colories BETWEEN 50 AND 80;

-- Отображение всех овощей, в названии которых есть указанное слово
SELECT * FROM fruits_and_vegetables
WHERE type = 'овощ' AND LOWER(name) LIKE '%капуста';

-- Отображение всех овощей и фруктов, в описании которых встречается
-- указанное слово
SELECT * FROM fruits_and_vegetables
WHERE LOWER(description) LIKE '%витамин%';

-- Показать все овощи и фрукты, у которых цвет желтый или красный
SELECT * FROM fruits_and_vegetables
WHERE LOWER(color) IN ('жёлтый', 'красный');

-- Показать количество овощей
SELECT COUNT(*) AS vegetable_count
FROM fruits_and_vegetables
WHERE type = 'овощ';

-- Показать количество фруктов
SELECT COUNT(*) AS fruit_count
FROM fruits_and_vegetables
WHERE type = 'фрукт';

-- Показать количество овощей и фруктов заданногоцвета
SELECT COUNT(*) AS count_by_color
FROM fruits_and_vegetables
WHERE color = 'синий';

-- Показать количество овощей и фруктов каждого цвета
SELECT color, COUNT(*) AS total_per_color
FROM fruits_and_vegetables
GROUP BY color;

-- Показать цвет с минимальным количеством овощейи фруктов
SELECT color, COUNT(*) AS min_count
FROM fruits_and_vegetables
GROUP BY color
ORDER BY min_count ASC
LIMIT 1;

-- Показать цвет с максимальным количеством овощей и фруктов
SELECT color, COUNT(*) AS max_count
FROM fruits_and_vegetables
GROUP BY color
ORDER BY max_count DESC
LIMIT 1;

-- Показать минимальную калорийность овощей и фруктов
SELECT MIN(colories) AS min_calories
FROM fruits_and_vegetables;

-- Показать максимальную калорийность овощей ифруктов
SELECT MAX(colories) AS max_calories
FROM fruits_and_vegetables;

-- Показать среднюю калорийность овощей и фруктов
SELECT AVG(colories) AS avg_calories
FROM fruits_and_vegetables;

-- Показать фрукт с минимальной калорийностью
SELECT *
FROM fruits_and_vegetables
WHERE type = 'фрукт'
ORDER BY colories ASC
LIMIT 1;


-- Показать фрукт с максимальной калорийностью
SELECT *
FROM fruits_and_vegetables
WHERE type = 'фрукт'
ORDER BY colories DESC
LIMIT 1;
