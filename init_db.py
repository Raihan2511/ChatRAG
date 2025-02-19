from backend.models.database import Base, engine

def initialize_database():
    print("Creating database tables...")
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    initialize_database()

