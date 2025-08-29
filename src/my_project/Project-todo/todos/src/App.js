// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

// =========================================================================
import { useState, useEffect } from 'react';
// import initialTodos from './todos.js';
import { Outlet, NavLink } from 'react-router-dom';
// import TodoList from './TodoList.js';
// import TodoAdd from './TodoAdd.js';
import { setStateChengeHandeler } from './api';

export default function App() {
  // const [todos, setTodos] = useState(initialTodos);
  // const [showMenu, setShowMenu] = useState(false);============

  // const setDone = key => {
  //   const newTodos = [...todos];
  //   // const deed = todos.find(current => current.key === key);
  //   const deed = newTodos.find(current => current.key === key);
  //   if (deed)
  //     deed.done = true;
  //   setTodos(newTodos);
  // };

  // const del = key => {
  //   const newTodos = todos.filter(current => current.key !== key);
  //   setTodos(newTodos);
  // };

  // const add = deed => {
  //   setTodos([...todos, deed]);
  // };

  const [showMenu, setShowMenu] = useState(false);

  const handleBurgerClick = evt => {
    evt.preventDefault();
    setShowMenu(!showMenu);
  };

  const [user, setUser] = useState();

  const authStateChanged = __user => {
    setUser(__user);
  };

  useEffect(() => {
    const unsubscribe = setStateChengeHandeler(authStateChanged);
    return () => {unsubscribe()};
  }, [])

  return (
    <div className="container">

      <nav className="navbar is-light">

        <div className="navbar-brand">
          <NavLink
            to='/'
            className={({ isActive }) =>
              'navbar-item is-uppercase' + (isActive ? ' is-active' : '')
            }
          >
            {user ? user.email : 'Мой список дел'}
          </NavLink>

          <a href='/'
            className={showMenu ?
              'navbar-burger is-active' :
              'navbar-burger'}
            onClick={handleBurgerClick}
          >
            <span></span>
            <span></span>
            <span></span>
            <span></span>
          </a>
        </div>

        {/* <div className='navbar-menu'> */}
        <div className={showMenu ?
          'navbar-menu is-active' :
          'navbar-menu'}
          onClick={handleBurgerClick}
        >
          <div className='navbar-start'>
            {user && (
              <NavLink
              to='/add'
              className={({ isActive }) =>
                'navbar-item' + (isActive ? ' is-active' : '')
              }
            >
              Создать дело
            </NavLink>
            )}
            {!user && (
              <NavLink to="/register"
              className={({ isActive }) =>
              'navbar-item' + (isActive ? 'is-active' : '')}
              >
                Зарегистрироваться
              </NavLink>
            )}

          </div>
        </div>

      </nav>

      <main className="content px-6 py-6">
        {/* <h1>Список</h1> */}
        {/* <TodoList list={todos} setDone={setDone} /> */}

        {/* <TodoList list={todos} setDone={setDone} del={del} /> */}
        {/* <TodoAdd add={add} /> */}

        <Outlet />
      </main>

    </div>
  );

}
