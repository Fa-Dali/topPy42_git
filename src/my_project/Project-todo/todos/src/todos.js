const date1 = new Date(2025, 8, 26, 14, 30);
const date2 = new Date(2025, 8, 27, 1, 40);

const todos = [
	{
		title: 'Изучить React',
		desc: 'Да поскорее',
		image: '',
		done: true,
		createdAt: date1.toLocaleString(),
		key: date1.getTime()
	},
	{
		title: 'Написать первое React-приложение',
		desc: 'Список запланированных дел',
		image: '',
		done: false,
		createdAt: date2.toLocaleString(),
		key: date2.getTime()
	}
];
export default todos;
