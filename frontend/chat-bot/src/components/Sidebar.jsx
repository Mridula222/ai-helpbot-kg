import React from "react";

function Sidebar({ onNewChat }) {
  return (
    <div className="sidebar">
      <h2>✨ AI Assistant</h2>
      <button className="new-chat" onClick={onNewChat}>+ New Chat</button>
      <input className="search" placeholder="Search chats..." />

      <div className="chat-list">
        <div className="chat-item">Satellite Data Queries</div>
        <div className="chat-item">Mission Updates & Info</div>
        <div className="chat-item">Data Access & Download Help</div>
        <div className="chat-item">Data Visualization Tips</div>
        <div className="chat-item">MOSDAC Portal Guide</div>
      </div>
      <div className="user-section">
        <p className="User"><i className="fa-solid fa-user"></i> User</p>
        <p className="Free"><i className="fa-solid fa-bolt"></i> Free Plan</p>
      </div>
    </div>
  );
}

export default Sidebar;
