<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DeekTalks Pro | Developed by Deepak Katal</title>
    <!-- Modern Fonts & Icons -->
    <link href="https://fonts.googleapis.com" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com">
    
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Outfit', sans-serif; }
        
        body { background: #0f172a; display: flex; height: 100vh; color: white; overflow: hidden; }

        /* Sidebar Styling */
        .sidebar {
            width: 260px; background: rgba(15, 23, 42, 0.95);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            display: flex; flex-direction: column; padding: 20px;
        }
        .new-chat {
            border: 1px solid #38bdf8; color: #38bdf8; padding: 12px;
            border-radius: 10px; cursor: pointer; text-align: center;
            font-weight: bold; margin-bottom: 20px; transition: 0.3s;
        }
        .new-chat:hover { background: #38bdf8; color: #020617; }

        /* Main Content */
        .main-content { flex: 1; display: flex; flex-direction: column; position: relative; }
        
        .header { 
            padding: 20px; text-align: center; font-size: 1.5rem; font-weight: 700;
            color: #38bdf8; border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }

        #chat-box { 
            flex: 1; overflow-y: auto; padding: 40px 15%; 
            display: flex; flex-direction: column; gap: 20px;
        }

        .msg { padding: 15px 20px; border-radius: 18px; max-width: 80%; line-height: 1.6; }
        .user-msg { align-self: flex-end; background: #38bdf8; color: #0f172a; font-weight: 500; }
        .ai-msg { align-self: flex-start; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255,255,255,0.1); }

        /* Developed By Tag - Fixed above input */
        .dev-tag {
            text-align: center; padding: 10px; font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.4); letter-spacing: 1px;
        }
        .dev-tag b { color: #38bdf8; }

        /* Input Bar */
        .input-area { padding: 10px 15% 30px; display: flex; gap: 10px; }
        .input-container {
            flex: 1; background: #1e293b; border-radius: 15px;
            display: flex; align-items: center; padding: 5px 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        input { flex: 1; background: transparent; border: none; color: white; padding: 12px; outline: none; }
        
        .icon-btn { color: #94a3b8; cursor: pointer; padding: 10px; font-size: 1.2rem; }
        .send-btn { background: #38bdf8; border: none; width: 40px; height: 40px; border-radius: 10px; cursor: pointer; }
    </style>
</head>
<body>

    <div class="sidebar">
        <div class="new-chat" onclick="location.reload()">+ New Chat</div>
        <p style="font-size: 0.7rem; color: #475569; text-transform: uppercase;">History</p>
        <div style="margin-top: 10px; color: #94a3b8; font-size: 0.9rem;">No recent chats</div>
    </div>

    <div class="main-content">
        <div class="header">DeekTalks Pro</div>
        <div id="chat-box">
            <div class="msg ai-msg">Hey! I'm Deek. How can I help you today?</div>
        </div>

        <!-- Developed By Tag -->
        <div class="dev-tag">Developed by <b>Deepak Katal</b></div>

        <div class="input-area">
            <div class="input-container">
                <i class="fas fa-microphone icon-btn" onclick="alert('Mic Active!')"></i>
                <input type="text" id="user-input" placeholder="Ask anything..." autocomplete="off">
                <button class="send-btn" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net"></script>
    <script>
        const input = document.getElementById("user-input");
        const chatBox = document.getElementById("chat-box");

        function scrollToBottom() { chatBox.scrollTop = chatBox.scrollHeight; }

        async function sendMsg() {
            const text = input.value.trim();
            if (!text) return;
            chatBox.innerHTML += `<div class="msg user-msg">${text}</div>`;
            input.value = "";
            scrollToBottom();

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
                const data = await response.json();
                chatBox.innerHTML += `<div class="msg ai-msg">${marked.parse(data.response)}</div>`;
                scrollToBottom();
            } catch (e) {
                chatBox.innerHTML += `<div class="msg ai-msg" style="color:red">Error! Server check karo.</div>`;
            }
        }
        input.addEventListener("keypress", (e) => { if (e.key === "Enter") sendMsg(); });
    </script>
</body>
</html>
