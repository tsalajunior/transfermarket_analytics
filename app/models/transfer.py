from sqlalchemy import Column, Integer, Date, Numeric, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False, index=True)
    from_club_id = Column(Integer, ForeignKey("clubs.id"))
    to_club_id = Column(Integer, ForeignKey("clubs.id"))
    transfer_date = Column(Date, index=True)
    season = Column(String(10))            # ex: "2024/25"
    fee_eur = Column(Numeric(14, 2))       # NULL = libre / prêt
    transfer_type = Column(String(50))     # transfer / loan / free / return
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    player = relationship("Player", foreign_keys=[player_id])
    from_club = relationship("Club", foreign_keys=[from_club_id])
    to_club = relationship("Club", foreign_keys=[to_club_id])
