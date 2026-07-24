from app.scraper.player_stats_scraper import (
    PlayerStatsScraper
)
scraper = PlayerStatsScraper()
import traceback
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

# players = cursor.fetchall()
players = [
    (566, "Aarón Anselmino", "1145504")
]

print(
    f"{len(players)} players found"
)

# for player_id, name, tm_id in players:
#     print(tm_id,name)
#     try:

#         print(
#             f"\nScraping stats : {name}"
#         )

#         stats = scraper.get_ligue1_stats(
#             tm_id
#         )
#         print("Saving:", name)
#         save_player_stats(
#             conn,
#             player_id,
#             stats
#         )

#         print(
#             f"OK | "
#             f"M={stats['appearances']} "
#             f"B={stats['goals']} "
#             f"A={stats['assists']}"
#         )

#     except Exception as e:

#         conn.rollback()

#         print(
#             f"\nERREUR {name}"
#         )

#         traceback.print_exc()

for player_id, name, tm_id in players:

    print(f"\n========== {name} ({tm_id}) ==========")

    try:

        stats = scraper.get_ligue1_stats(tm_id)

        print(stats)

        save_player_stats(
            conn,
            player_id,
            stats
        )

        print("Saved successfully.")

    except Exception:

        conn.rollback()

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