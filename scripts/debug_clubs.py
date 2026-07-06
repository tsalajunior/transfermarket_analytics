# scripts/debug_clubs.py

from bs4 import BeautifulSoup

from app.scraper.transfermarkt_client import TransfermarktClient

client = TransfermarktClient()

html = client.get(
    "https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1"
)

soup = BeautifulSoup(html, "lxml")

table = soup.find("table", class_="items")

links = table.find_all("a", href=True)

for link in links[:30]:
    print(link.get_text(strip=True))
    print(link["href"])
    print("-" * 50)