from app.scraper.players_scraper import PlayerScraper

scraper = PlayerScraper()

soup = scraper.get_players(
    "/fc-paris-saint-germain/startseite/verein/583/saison_id/2025"
)

table = soup.find_all("table")[1]

rows = table.find_all("tr")

print(f"{len(rows)} lignes trouvées\n")

for row in rows[:5]:
    print("=" * 80)
    print(row.prettify()[:3000])