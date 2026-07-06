# scripts/extract_clubs.py

from bs4 import BeautifulSoup

from app.scraper.transfermarkt_client import TransfermarktClient

client = TransfermarktClient()

html = client.get(
    "https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1"
)

soup = BeautifulSoup(html, "lxml")

table = soup.find("table", class_="items")

clubs = []

for link in table.find_all("a", href=True):

    href = link["href"]

    if "/startseite/verein/" not in href:
        continue

    name = link.get_text(strip=True)

    if not name:
        continue

    clubs.append({
        "name": name,
        "url": href
    })

print(f"{len(clubs)} clubs trouvés\n")

for club in clubs:
    print(club)