from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    tm_id = Column(String(50), unique=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    birth_date = Column(Date)
    nationality = Column(String(100))
    position = Column(String(50))
    foot = Column(String(20))
    height_cm = Column(Integer)
    market_value_eur = Column(Numeric(14, 2), index=True)
    url = Column(String(500))
    club_id = Column(Integer, ForeignKey("clubs.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    club = relationship("Club", back_populates="players")
    stats = relationship("PlayerStat", back_populates="player")
