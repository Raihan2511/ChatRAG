import ollama
from backend.models.database import get_db
from backend.models.chat_history import ChatHistory
from backend.models.cache import Cache
from sqlalchemy.orm import Session
from difflib import SequenceMatcher

# Function to compute similarity between two questions
def compute_similarity(q1, q2):
    return SequenceMatcher(None, q1.lower(), q2.lower()).ratio()

# Function to check cache for a similar question
def check_cache(db: Session, user_input: str):
    cache_entries = db.query(Cache).all()

    for entry in cache_entries:
        if compute_similarity(user_input, entry.question) > 0.85:  # Similarity threshold
            return entry.response
    
    return None

# Function to search chat history for a similar question
def search_history(db: Session, user_input: str):
    history_entries = db.query(ChatHistory).all()

    for entry in history_entries:
        if compute_similarity(user_input, entry.message) > 0.85:  # Similarity threshold
            return entry.response
    
    return None

# Function to store response in cache
def store_in_cache(db: Session, user_id: int, question: str, response: str):
    existing_entry = db.query(Cache).filter(Cache.question == question).first()

    if existing_entry:
        existing_entry.frequency += 1  # Update frequency
    else:
        # Ensure only 5 items in cache (remove least frequent if full)
        cache_count = db.query(Cache).count()
        if cache_count >= 5:
            least_frequent = db.query(Cache).order_by(Cache.frequency.asc()).first()
            if least_frequent:
                db.delete(least_frequent)
        
        new_cache_entry = Cache(user_id=user_id, question=question, response=response, frequency=1)
        db.add(new_cache_entry)

    db.commit()

# Function to store response in chat history
def store_in_history(db: Session, user_id: int, question: str, response: str, title: str = "Chat Session"):
    new_history = ChatHistory(user_id=user_id, title=title, message=question, response=response)
    db.add(new_history)
    db.commit()

# Main function to generate response
def generate_response(user_input: str, user_id: int, use_rag=False, qa=None):
    """Generate response from DeepSeek R1 (Regular chat or RAG-based) with cache & history."""
    db: Session = next(get_db())

    try:
        # Step 1: Check cache
        cached_response = check_cache(db, user_input)
        if cached_response:
            return cached_response

        # Step 2: Check chat history
        history_response = search_history(db, user_input)
        if history_response:
            return history_response

        # Step 3: Generate response using RAG or LLM
        if use_rag and qa:
            response = qa(user_input)["result"]
        else:
            response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": user_input}])
            response = response["message"]["content"]

        # Step 4: Store response in history and update cache
        # save_chat_message(db, user_id, user_input, response)
        store_in_cache(db, user_id, user_input, response)

        return response

    except Exception as e:
        print(f"❌ Error generating response: {e}")
        return "I'm having trouble responding. Please try again."

    finally:
        db.close()

# ✅ Function to generate AI responses
# def generate_response(user_input: str, use_rag=False, qa=None):
#     """Generate response from DeepSeek R1 (Regular chat or RAG-based)."""
#     try:
#         if use_rag and qa:
#             response = qa(user_input)["result"]  # Use RetrievalQA if enabled
#         else:
#             response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": user_input}])
#             response = response["message"]["content"]
        
#         return response
#     except Exception as e:
#         print(f"❌ Error generating response: {e}")
#         return "I'm having trouble responding. Please try again."

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
