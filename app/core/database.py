from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings
import psycopg2

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_connection():

    return psycopg2.connect(
        settings.DATABASE_URL
    )

def save_player_stats(
    conn,
    player_id,
    stats
):

    minutes = stats["minutes_played"]

    if minutes > 0:

        stats["goals_per_90"] = round(
            (stats["goals"] * 90) / minutes,
            2
        )

        stats["assists_per_90"] = round(
            (stats["assists"] * 90) / minutes,
            2
        )

        stats["goal_contribution_per_90"] = round(
            ((stats["goals"] + stats["assists"]) * 90) / minutes,
            2
        )

    else:

        stats["goals_per_90"] = 0
        stats["assists_per_90"] = 0
        stats["goal_contribution_per_90"] = 0

    query = """
    INSERT INTO player_stats (
        player_id,
        season,
        competition,
        appearances,
        goals,
        assists,
        minutes_played,
        yellow_cards,
        red_cards,
        goals_per_90,
        assists_per_90,
        goal_contribution_per_90
    )
    VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    ON CONFLICT (
        player_id,
        season,
        competition
    )
    DO UPDATE SET
        appearances = EXCLUDED.appearances,
        goals = EXCLUDED.goals,
        assists = EXCLUDED.assists,
        minutes_played = EXCLUDED.minutes_played,
        yellow_cards = EXCLUDED.yellow_cards,
        red_cards = EXCLUDED.red_cards,
        goals_per_90 = EXCLUDED.goals_per_90,
        assists_per_90 = EXCLUDED.assists_per_90,
        goal_contribution_per_90 = EXCLUDED.goal_contribution_per_90,
        updated_at = CURRENT_TIMESTAMP
    """

    cursor = conn.cursor()

    cursor.execute(
        query,
        (
            player_id,
            stats["season"],
            stats["competition"],
            stats["appearances"],
            stats["goals"],
            stats["assists"],
            stats["minutes_played"],
            stats["yellow_cards"],
            stats["red_cards"],
            stats["goals_per_90"],
            stats["assists_per_90"],
            stats["goal_contribution_per_90"]
        )
    )

    conn.commit()