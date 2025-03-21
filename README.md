# 🚀 ChatGPT Clone with DeepSeek R1 & RAG-Powered PDF Q&A  

## 📌 Project Overview  
This project is a **ChatGPT-like AI Assistant** built using **Streamlit**, powered by a **Large Language Model (LLM)**—**DeepSeek R1 (1.5B)**—for intelligent conversation. It seamlessly integrates **Retrieval-Augmented Generation (RAG)**, enabling users to **upload PDFs** and ask questions based on the document’s content.  

With **real-time chat history storage** in **MySQL**, users can continue conversations across sessions without losing context. The chatbot supports both **free-text AI conversation** and **document-based Q&A**, making it a **powerful hybrid AI assistant**.  

## ✨ Key Features  
👉 **Conversational AI with LLM** – Chat with **DeepSeek R1 (1.5B)** like ChatGPT  
👉 **Retrieval-Augmented Generation (RAG)** – Ask questions about uploaded PDFs  
👉 **Persistent Chat Memory** – AI retains chat history for seamless conversations  
👉 **MySQL-Backed Chat History** – Stores past conversations for easy retrieval  
👉 **Real-Time Sidebar Chat History** – Quickly access previous discussions  
👉 **Auto-Generated Titles** – Organizes chat sessions efficiently  
👉 **Smooth UI with Auto-Scrolling** – Fast and intuitive user experience  

## ⚙️ How It Works  

### 🔹 **1. LLM-Powered Chat**  
- The chatbot uses **DeepSeek R1 (1.5B)**, a **Large Language Model (LLM)** optimized for **natural language understanding and generation**.  
- Users can interact **just like ChatGPT**, receiving **intelligent responses** based on context.  

### 🔹 **2. RAG-Based PDF Q&A**  
- Users can **upload PDFs** (e.g., reports, research papers, contracts).  
- The system extracts text, converts it into **vector embeddings**, and stores it in **FAISS (vector search database)**.  
- When users ask a question, the **retrieval module** finds the most relevant parts of the document.  
- The **LLM (DeepSeek R1)** then generates a response **using both retrieved content & its general knowledge**.  

### 🔹 **3. Efficient Chat History Management**  
- **All chat messages** are stored in **MySQL**, linked to each user.  
- The sidebar **displays past chat sessions**, enabling users to **resume conversations anytime**.  
- A **search function** allows users to find **specific past interactions** quickly.  

## 🏰 Tech Stack  
| Component   | Technology Used   |  
|------------|------------------|  
| **Frontend**  | Streamlit (UI Framework)  |  
| **Backend**  | Python (FastAPI for Database Operations)  |  
| **LLM (AI Model)**  | DeepSeek R1 (1.5B) via Ollama  |  
| **Database**  | MySQL (Chat History & User Data)  |  
| **RAG System**  | FAISS (Vector Database for Document Retrieval)  |  
| **Authentication**  | Secure User Login System  |  

## 📌 Installation Guide  

### 1️⃣ **Install Dependencies**  
```bash  
pip install -r requirements.txt  
```  

### 2️⃣ **Start MySQL & Initialize Database**  
Ensure MySQL is running and update **`config.py`** with your credentials:  
```bash  
python init_db.py
```  

### 3️⃣ **Run DeepSeek R1 Locally**  
Ensure **Ollama** and **DeepSeek R1** are installed:  
```bash  
ollama pull deepseek-r1:1.5b  
ollama serve  
```  

### 4️⃣ **Start the ChatGPT Clone**  
```bash  
streamlit run app.py  
```  

## 📝 How to Use  
1️⃣ **Sign Up & Log In** – Access the chat system.  
2️⃣ **Chat with AI (LLM)** – Just like ChatGPT, but powered by **DeepSeek R1**.  
3️⃣ **Upload a PDF** – Ask questions about it, and the **RAG system retrieves** relevant information.  
4️⃣ **Resume Previous Conversations** – Click on a chat title in the sidebar.  
5️⃣ **Search Past Chats** – Quickly find specific discussions.  

## 🚀 Future Improvements  
🔹 **Google Login Integration** for seamless authentication  
🔹 **Voice-Based AI Chat** for hands-free interaction  
🔹 **Multimodal AI (Images & Text)** to analyze both text and visuals  
🔹 **Enhanced Response Personalization** based on user behavior  

## 💡 Contributing  
Pull requests are welcome! Fork the repo and submit changes to improve the AI system.  

## 🐝 License  
This project is open-source under the **MIT License**. 

