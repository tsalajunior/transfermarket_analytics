from app.scraper.player_stats_scraper import (
    PlayerStatsScraper
)

scraper = PlayerStatsScraper()

import traceback
from app.scraper.player_stats_scraper import (
    PlayerStatsScraper
)

from app.core.database import (
    get_connection,
    save_player_stats
)

scraper = PlayerStatsScraper()

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
    SELECT
        id,
        name,
        tm_id
    FROM players
    WHERE tm_id IS NOT NULL
""")

players = cursor.fetchall()

print(
    f"{len(players)} joueurs trouvés"
)

for player_id, name, tm_id in players:

    try:

        print(
            f"\nScraping stats : {name}"
        )

        stats = scraper.get_ligue1_stats(
            tm_id
        )

        save_player_stats(
            conn,
            player_id,
            stats
        )

        print(
            f"OK | "
            f"M={stats['appearances']} "
            f"B={stats['goals']} "
            f"A={stats['assists']}"
        )

    except Exception as e:

        conn.rollback()

        print(
            f"\nERREUR {name}"
        )

        traceback.print_exc()

cursor.close()
conn.close()

# from app.scraper.player_stats_scraper import (
#     PlayerStatsScraper
# )

# scraper = PlayerStatsScraper()

# stats = scraper.get_ligue1_stats(
#     616341  # Nuno Mendes
# )

# print(stats)