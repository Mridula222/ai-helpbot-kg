import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import './index.css';

function App() {
  const [messages, setMessages] = useState([
    {
      sender: 'bot',
      text: `🤖 Hi! I’m your MOSDAC AI assistant. I’m here to help you find satellite data, mission info, and answer your questions about the MOSDAC portal. How can I assist you today?`,
    },
  ]);

  const startNewChat = () => {
    setMessages([
      {
        sender: 'bot',
        text: `🤖 Hi! I’m your MOSDAC AI assistant. I’m here to help you find satellite data, mission info, and answer your questions about the MOSDAC portal. How can I assist you today?`,
      },
    ]);
  };

  return (
    <div className="app">
      <Sidebar onNewChat={startNewChat} />
      <ChatWindow messages={messages} setMessages={setMessages} />
    </div>
  );
}

export default App;
