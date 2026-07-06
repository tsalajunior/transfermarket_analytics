from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Float
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class PlayerStat(Base):
    __tablename__ = "player_stats"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False, index=True)
    club_id = Column(Integer, ForeignKey("clubs.id"))
    season = Column(String(10), nullable=False)          
    competition = Column(String(100))                    
    appearances = Column(Integer, default=0)
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    minutes_played = Column(Integer, default=0)
    yellow_cards = Column(Integer, default=0)
    red_cards = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    goals_per_90 = Column(Float)
    assists_per_90 = Column(Float)
    goal_contribution_per_90 = Column(Float)

    __table_args__ = (
        UniqueConstraint("player_id", "season", "competition", name="uq_player_season_comp"),
    )

    player = relationship("Player", back_populates="stats")
    club = relationship("Club")

    