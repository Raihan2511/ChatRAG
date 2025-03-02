# ChatGPT Clone with DeepSeek R1 and RAG Integration

## 📌 Project Overview
This project is a **ChatGPT Clone** built using **Streamlit**, integrating **DeepSeek R1 (1.5B)** for AI chat responses and **Retrieval-Augmented Generation (RAG)** for answering PDF-based questions. It provides a seamless conversational experience with memory retention and allows users to extract information from uploaded documents.

## ✨ Features
✅ **ChatGPT-Like UI** with a sidebar for chat history  
✅ **DeepSeek R1 (1.5B) Model** for AI-based chat  
✅ **Full Chat Memory** - AI remembers previous messages in a session  
✅ **RAG Integration** - Upload a PDF and ask questions about it  
✅ **MySQL Database** - Stores chat history and user authentication  
✅ **Session Persistence** - Chats remain active after page refresh  
✅ **Auto-Scrolling Chat** for a seamless experience  
✅ **Efficient Search Feature** - Users can quickly find past conversations  
✅ **Chat Categorization** - Organize chats by topic or session  


### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Start the MySQL Database**
Ensure MySQL is running and update **`backend/models/database.py`** with your credentials.

### 5️⃣ **Initialize Database**
```bash
python backend/models/database.py
```

### 6️⃣ **Run DeepSeek R1 Locally**
Ensure Ollama and DeepSeek R1 are installed:
```bash
ollama pull deepseek-r1:1.5b
ollama serve
```

### 7️⃣ **Start the ChatGPT Clone**
```bash
streamlit run app.py
```

## 📝 Usage
1️⃣ **Sign Up & Log In** to access the chat.  
2️⃣ **Chat with DeepSeek R1** just like ChatGPT.  
3️⃣ **Upload a PDF** (in the sidebar) and ask questions about it.  
4️⃣ **Click on a chat title in the sidebar** to load past conversations.  
5️⃣ **Continue conversations seamlessly** from saved chats.  

## 🛠 Technologies Used
- **Frontend:** Streamlit
- **Backend:** Python (FastAPI for database operations)
- **Database:** MySQL
- **AI Model:** DeepSeek R1 (1.5B) via Ollama
- **Vector Search:** FAISS (for RAG PDF search)

## ⚡ API Endpoints (If Needed)
| Endpoint       | Method | Description             |
|---------------|--------|-------------------------|
| `/chat`       | POST   | Get AI response         |
| `/upload`     | POST   | Upload and process PDF  |
| `/history`    | GET    | Retrieve chat history   |

## 📌 Future Improvements
🔹 Add support for **Google Login**  
🔹 Implement **voice-based chat**  
🔹 Enable **multimodal AI (images & text)**  
🔹 Improve **response personalization** using user-specific context  
🔹 Enhance **document processing speed** for faster retrieval  

## 💡 Contributing
Pull requests are welcome! Feel free to fork the repo and submit changes.

## 📜 License
This project is open-source under the **MIT License**.

---
🎉 **Enjoy chatting with your AI assistant!** 🚀

