import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import './index.css';

function App() {
  const [messages, setMessages] = useState(() => {
    // Load saved messages from localStorage if available, else default welcome message
    const saved = localStorage.getItem('chatHistory');
    return saved
      ? JSON.parse(saved)
      : [
          {
            sender: 'bot',
            text: `🤖 Hi! I’m your MOSDAC AI assistant. I’m here to help you find satellite data, mission info, and answer your questions about the MOSDAC portal. How can I assist you today?`,
          },
        ];
  });

  // Save messages to localStorage every time they change
  useEffect(() => {
    localStorage.setItem('chatHistory', JSON.stringify(messages));
  }, [messages]);

  const startNewChat = () => {
    const newChat = [
      {
        sender: 'bot',
        text: `🤖 Hi! I’m your MOSDAC AI assistant. I’m here to help you find satellite data, mission info, and answer your questions about the MOSDAC portal. How can I assist you today?`,
      },
    ];
    setMessages(newChat);
    localStorage.setItem('chatHistory', JSON.stringify(newChat)); // Reset localStorage too
  };

  return (
    <div className="app">
      <Sidebar onNewChat={startNewChat} />
      <ChatWindow messages={messages} setMessages={setMessages} />
    </div>
  );
}

export default App;
