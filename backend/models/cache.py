from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.database import Base

class Cache(Base):
    __tablename__ = "cache"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Optional relationship with users
    question = Column(Text, nullable=False)  # Cache question
    response = Column(Text, nullable=False)  # Cached response
    frequency = Column(Integer, default=1)  # Number of times the question was asked

    user = relationship("User", back_populates="cache", foreign_keys=[user_id])
