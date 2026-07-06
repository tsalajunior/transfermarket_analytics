from app.scraper.players_scraper import PlayerScraper

scraper = PlayerScraper()

players = scraper.get_players(
    "/fc-paris-saint-germain/startseite/verein/583/saison_id/2025"
)

print(f"{len(players)} joueurs trouvés\n")

for player in players[:5]:
    print(player)