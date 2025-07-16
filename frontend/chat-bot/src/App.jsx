import React from 'react';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import './index.css';

function App() {
  return (
    <div className="app">
      <Sidebar />
      <ChatWindow />
    </div>
  );
}

export default App;