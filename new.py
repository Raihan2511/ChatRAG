from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import event
import time

# Database connection details
username = 'root'
password = ''
hostname = 'localhost'
port = '3306'
database_name = 'pub'

# Connect to MySQL database
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}:{port}/{database_name}')
Base = declarative_base()

# Define a class to map to the 'books' table
class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(Integer)
    genre=Column(String)
    publication_year = Column(Integer)
    author_id = Column(Integer)
   

# Define a function to handle modifications to the 'books' table after insertion
def books_table_insert_listener(mapper, connection, target):
    print("New record inserted into 'books' table!")

# Attach the event listener to the 'after_insert' event for the Book class
event.listen(Book, 'after_insert', books_table_insert_listener)

# Create a session to use the listener
Session = sessionmaker(bind=engine)
session = Session()

# Create an instance of the Book class
new_book = Book(
    book_id=5006, 
    title='Example Book Title', 
    genre='action',
    publication_year=2015,
    author_id=1
)



# Add the new book to the session and commit it to the database
session.add(new_book)
session.commit()

# Keep the script running indefinitely to listen for modifications
while True:
    time.sleep(1)  # Sleep for 1 second before checking for modifications