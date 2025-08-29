import { createRoutesFromElements, createBrowserRouter, Route } from "react-router-dom";

import App from './App.js';
import TodoList from "./TodoList.js";
import TodoAdd from "./TodoAdd";
import TodoDetail from "./TodoDetail.js";
import Error404 from "./Error404.js";
import Register from './Register.js';
import { getTodos, addTodo, getTodo, actTodo, register } from "./api.js";


// import todos from './todos.js';

const router = createBrowserRouter(
	createRoutesFromElements(
		<Route path='/' element={<App />}>
			{/* <Route index={true} element={<TodoList list={todos} />} /> */}
			{/* <Route index={true} element={<TodoList />} /> */}
			<Route index={true} element={<TodoList />}
				loader={getTodos} />
			{/* <Route path='add' element={<TodoAdd />} /> */}
			<Route path='add' element={<TodoAdd />}
				action={addTodo} />
			<Route path=':key' element={<TodoDetail />}
				loader={getTodo} action={actTodo}
				errorElement={<Error404 />} />
			<Route path='register' element={<Register />}
				action={register} />
		</Route>
	)
);

export default router;
