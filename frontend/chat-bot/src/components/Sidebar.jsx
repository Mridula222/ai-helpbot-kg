import React from 'react';

function Sidebar() {
  return (
    <div className="sidebar">
      <h2>✨ AI Assistant</h2>
      <button className="new-chat">+ New Chat</button>
      <input className="search" placeholder="Search chats..." />
      <div className="chat-list">
        <div className="chat-item active">Project Brainstorming</div>
        <div className="chat-item">Marketing Strategy</div>
        <div className="chat-item">Code Debugging</div>
        <div className="chat-item">AI Ethics Discussion</div>
      </div>
      <div className="user-section">
        <p>User</p>
        <small>Free Plan</small>
      </div>
    </div>
  );
}

export default Sidebar;
