from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True)
    tm_id = Column(String(50), unique=True, index=True)
    name = Column(String(255), nullable=False)
    country = Column(String(100))
    url = Column(String(500))
    league_id = Column(Integer, ForeignKey("leagues.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    transfers_in = relationship("Transfer", foreign_keys="Transfer.to_club_id")
    transfers_out = relationship("Transfer", foreign_keys="Transfer.from_club_id")
    league = relationship("League", back_populates="clubs")
    players = relationship("Player", back_populates="club", cascade="all, delete-orphan")


