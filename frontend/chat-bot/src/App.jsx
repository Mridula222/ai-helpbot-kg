import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import './index.css';

function App() {
  const [chatHistory, setChatHistory] = useState([]);

  const startNewChat = () => {
    setChatHistory([]); // Clears old messages
  };

  return (
    <div className="app">
      <Sidebar onNewChat={startNewChat} />
      <ChatWindow chatHistory={chatHistory} setChatHistory={setChatHistory} />
    </div>
  );
}

export default App;
