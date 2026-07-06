# scripts/debug_psg.py

from app.scraper.clubs_scraper import ClubScraper

scraper = ClubScraper()

players = scraper.get_players(
    "/fc-paris-saint-germain/startseite/verein/583"
)

print(players[:3])