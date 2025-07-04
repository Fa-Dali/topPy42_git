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

-- Отображение всей информации из таблицы с овощами и фруктами
SELECT * FROM fruits_and_vegetables;

-- Отображение всех овощей
SELECT * FROM fruits_and_vegetables where type = 'овощ';

-- Отображение всех фруктов
SELECT * FROM fruits_and_vegetables WHERE type = 'фрукт';

-- Отображение всех названий овощей и фруктов
select name FROM fruits_and_vegetables;

-- Отображение всех цветов. Цвета должны быть уникальными
SELECT DISTINCT color FROM fruits_and_vegetables;

-- Отображение фруктов конкретного цвета (например, красного)
SELECT * FROM fruits_and_vegetables WHERE type = 'фрукт' AND LOWER(color) = 'красный';

-- Отображение овощей конкретного цвета (например, оранжевого)
SELECT * FROM fruits_and_vegetables WHERE type = 'овощ' AND LOWER(color) = 'оранжевый';
