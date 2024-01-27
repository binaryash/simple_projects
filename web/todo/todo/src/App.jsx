import React, { useState } from 'react';
import './App.css';

const TodoItem = ({ todo, onDelete}) => {
  return (
    <div className="todo-item">
      {todo.text}
      <button onClick={() => onDelete(todo.id)}>Delete</button>
    </div>
  );
};

const TodoList = ({ todos, onDelete }) => {
  return (
    <div className="todo-list">
      {todos.map((todo) => (
        <TodoItem key={todo.id} todo={todo} onDelete={onDelete} />
      ))}
    </div>
  );
};

const TodoForm = ({ onAdd }) => {
  const [text, setText] = useState('');

  const handleAdd = () => {
    if (text.trim() !== ''){
      onAdd(text);
      setText('');
    }
  };

  return(
    <div className="todo-form">
      <input
      type="text"
      value={text}
      onChange={(e) => setText(e.target.value)}
      placeholder="Add a new task"
      />
      <button onClick={handleAdd}>Add</button>
    </div>
  );
};

function App(){
  const [todos, setTodos] = useState([]);

  const handleAddTodo = (text) => {
    const newTodo = {
      id: Date.now(),
      text,
    };
    setTodos([...todos, newTodo]);
  };

  const handleDeleteTodo = (id) => {
    const updatedTodos = todos.filter((todo) => todo.id !== id);
    setTodos(updatedTodos);
  };

  return (
    <div className="App">
      <h1>Todo List</h1>
      <TodoForm onAdd={handleAddTodo} />
      <TodoList todos={todos} onDelete={handleDeleteTodo} />
    </div>
  );
}

export default App;