import React, { useState } from 'react';

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    console.log('File uploaded:', file);
    // TODO: Send to backend or preview
  }
};

function ChatWindow() {
  const [inputValue, setInputValue] = useState('');
  const [messages, setMessages] = useState([
    {
      sender: 'bot',
      text: `🤖 Hi there! I'm your AI assistant. I can help with brainstorming ideas, answering questions, or discussing any topic you're interested in. How can I assist with your hackathon project today?`,
    },
  ]);

  const handleSend = () => {
    if (!inputValue.trim()) return;

    const userMessage = { sender: 'user', text: inputValue };
    setMessages((prev) => [...prev, userMessage]);
    setInputValue('');

    // Fake bot reply after delay
    setTimeout(() => {
      const botReply = {
        sender: 'bot',
        text: generateBotResponse(inputValue),
      };
      setMessages((prev) => [...prev, botReply]);
    }, 800); // delay in ms
  };

  // Dummy reply logic – you can make it smarter later
  const generateBotResponse = (userInput) => {
    return `🤖 You said: "${userInput}". That's interesting! How can I help further?`;
  };

  return (
    <div className="chat-window">
      <div className="chat-header">
        <div>
          <h3>Project Brainstorming</h3>
          <span className="status">🟢 Active now</span>
        </div>
        <div className="header-actions">
          <span>GPT-4</span>
        </div>
      </div>

      <div className="chat-body">
        <div className="intro-box">
          <h2><i className="fa-solid fa-robot"></i> Welcome to AI Assistant</h2>
          <p>Ask me anything from technical questions to design advice!</p>
          <div className="suggestions">
            <button onClick={() => setInputValue('Hackathon ideas')}>Hackathon ideas</button>
            <button onClick={() => setInputValue('Tech stack advice')}>Tech stack advice</button>
            <button onClick={() => setInputValue('UI/UX best practices')}>UI/UX best practices</button>
          </div>
        </div>

        {/* Render messages */}
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>

      <div className="chat-input">
        <label htmlFor="file-upload" className="upload-button">
          <i className="fas fa-plus"></i>
        </label>
        <input
          type="file"
          id="file-upload"
          style={{ display: 'none' }}
          onChange={(e) => handleFileUpload(e)}
        />

        <input
          placeholder="Message AI Assistant..."
          className="chat-text-input"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
        />

        <button className="send-button" onClick={handleSend}>➤</button>
      </div>
    </div>
  );
}

export default ChatWindow;
