import ollama
from sqlalchemy.orm import Session
from backend.models.database import get_db
from backend.models.chat_history import ChatHistory

# ✅ Function to generate AI responses
def generate_response(user_input: str, use_rag=False, qa=None):
    """Generate response from DeepSeek R1 (Regular chat or RAG-based)."""
    try:
        if use_rag and qa:
            response = qa(user_input)["result"]  # Use RetrievalQA if enabled
        else:
            response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": user_input}])
            response = response["message"]["content"]
        
        return response
    except Exception as e:
        print(f"❌ Error generating response: {e}")
        return "I'm having trouble responding. Please try again."

# ✅ Function to save messages in chat history
def save_chat_message(user_id: int, message: str, response: str, chat_id=None):
    """Save chat messages under the correct chat session."""
    db: Session = next(get_db())
    try:
        if not user_id:
            print("❌ Error: user_id is None!")
            return None

        if chat_id:
            # ✅ Append to the existing chat session instead of creating a new one
            chat = db.query(ChatHistory).filter(ChatHistory.id == chat_id).first()
            if chat:
                title = chat.title  # ✅ Keep the same title
            else:
                print("⚠ Chat ID not found, creating a new chat session!")
                chat_id = None  # ✅ Reset chat_id to create a new session

        if not chat_id:
            title = message[:30] + "..." if len(message) > 30 else message  # ✅ Generate title only for the first message

        chat_entry = ChatHistory(user_id=user_id, title=title, message=message, response=response)

        db.add(chat_entry)
        db.commit()
        db.refresh(chat_entry)

        print(f"✅ Message saved: {message} (Chat ID: {chat_entry.id}, Title: {chat_entry.title})")

        return chat_entry
    except Exception as e:
        db.rollback()
        print(f"❌ Error saving chat: {e}")
        return None
    finally:
        db.close()
# ✅ Function to retrieve chat history
def get_chat_history(user_id: int, title: str = None):
    """Retrieve chat history by user, optionally filtering by title."""
    db: Session = next(get_db())
    try:
        query = db.query(ChatHistory).filter(ChatHistory.user_id == user_id)
        if title:
            query = query.filter(ChatHistory.title == title)
        return query.order_by(ChatHistory.timestamp).all()
    finally:
        db.close()
