import { useLoaderData, Link, useSubmit } from "react-router-dom";

// export default function TodoList(props) {
export default function TodoList() {
	const list = useLoaderData();

	const submit = useSubmit();

	const handleDoneClick = key => {
		submit(null, {action: `/${key}`, method: 'patch'});
	};

	const handleDeleteCklick = key => {
		submit(null, {action: `/${key}`, method: 'delete'});
	};

	return (

		<section>
			<h1>Задачи</h1>
			<table className="table is-hoverable is-fullwidth">
				<tbody>
					{/* {props.list.map(item => ( */}
					{list.map(item => (
						<tr key={item.key}>
							<td>
								<Link to={`/${item.key}`}>
									{item.done && <del>{item.title}</del>}
									{!item.done && item.title}
								</Link>
							</td>
							<td>
								<button
									className="button is-success"
									title="Выполнено"
									disabled={item.done}
									// onClick={ () => {props.setDone(item.key)}}
									onClick={ () => {handleDoneClick(item.key)}}
								>
									&#9745;
								</button>
							</td>
							<td>
								<button
									className="button is-danger"
									title="Удалить"
									// onClick={ () => props.del(item.key)}
									onClick={ () => {handleDeleteCklick(item.key)}}
								>
									&#9746;
								</button>
							</td>
						</tr>
					))}
				</tbody>
			</table>
		</section>
	);
}
