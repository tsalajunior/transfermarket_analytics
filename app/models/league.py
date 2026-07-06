from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True)
    tm_id = Column(String(50), unique=True, index=True)   # ID Transfermarkt
    name = Column(String(255), nullable=False)
    country = Column(String(100))
    tier = Column(Integer)  # 1 = première division
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    clubs = relationship("Club", back_populates="league", cascade="all, delete-orphan")
