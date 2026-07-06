from app.scraper.league_scraper import LeagueScraper

scraper = LeagueScraper()

data = scraper.scrape(
    "https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1"
)

print(data)