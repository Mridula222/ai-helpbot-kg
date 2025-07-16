import React from 'react';

function ChatWindow() {
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
          <h2>Welcome to AI Assistant</h2>
          <p>Ask me anything from technical questions to design advice!</p>
          <div className="suggestions">
            <button>Hackathon ideas</button>
            <button>Tech stack advice</button>
            <button>UI/UX best practices</button>
          </div>
        </div>

        <div className="message bot">
          🤖 Hi there! I'm your AI assistant. I can help with brainstorming ideas, answering questions, or discussing any topic you're interested in. How can I assist with your hackathon project today?
        </div>
      </div>

      <div className="chat-input">
        <input placeholder="Message AI Assistant..." />
        <button>➤</button>
      </div>
    </div>
  );
}

export default ChatWindow;
