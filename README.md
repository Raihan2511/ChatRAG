# Chatrag - AI Chatbot with PDF-Based RAG and Multi-LLM Support

Chatrag is a ChatGPT-style AI assistant that supports both free-form conversation and document-based question answering. Built with Streamlit, it integrates multiple large language models (LLMs) and uses Retrieval-Augmented Generation (RAG) to answer questions based on uploaded PDF documents.

## Features

* LLM-based conversational AI (DeepSeek R1 via Ollama, Gemini via API)
* Retrieval-Augmented Generation (RAG) for PDF Q\&A
* Persistent chat history using Neon DB (PostgreSQL) and MySQL
* Session titles and organized chat navigation
* Searchable sidebar with previous chats
* Smooth, responsive user interface

## Tech Stack

| Component      | Technology                       |
| -------------- | -------------------------------- |
| Frontend       | Streamlit                        |
| Backend        | Python                           |
| LLMs           | DeepSeek R1 (Ollama), Gemini API |
| RAG Retrieval  | FAISS                            |
| PDF Processing | PyMuPDF / pdfplumber             |
| Databases      | Neon DB (PostgreSQL), MySQL      |

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Raihan2511/ChatRAG.git
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your Environment

Create a configuration file (e.g., `config.toml`, `.env`, or `.streamlit/secrets.toml`) to store your database URLs and API keys. This includes:

* Neon DB connection URL
* MySQL connection URL
* Gemini API key

**Note**: Do not hardcode credentials in your code. Use secure configuration management.

### 4. Initialize the Database

Run the script to set up necessary tables and schema:

```bash
python init_db.py
```

### 5. Set Up the LLMs

* Install and run DeepSeek R1 locally using [Ollama](https://ollama.ai/):

```bash
ollama pull deepseek-r1:1.5b
ollama serve
```

* Ensure your Gemini API access is set correctly in your configuration.

### 6. Launch the Application

```bash
streamlit run app.py
```

## Usage

1. Sign in or register to start a chat.
2. Use the chat interface to ask open-ended questions.
3. Upload a PDF file to enable document-based Q\&A.
4. View and manage past conversations from the sidebar.
5. Use the search feature to quickly find previous messages.

## Configuration

To keep credentials secure, store them in a configuration file. Here's an example format (do not include real values in public repositories):

```toml
[settings]
NEON_DB_URL = "<your_neon_db_url>"
MYSQL_DB_URL = "<your_mysql_url>"
GEMINI_API_KEY = "<your_gemini_api_key>"
```

## Future Improvements

* Google login integration
* Voice command support
* Multimodal input (images + text)
* Custom LLM selector in UI
* Admin analytics dashboard

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
