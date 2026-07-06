# scripts/debug_ligue1.py

from bs4 import BeautifulSoup

from app.scraper.transfermarkt_client import TransfermarktClient

client = TransfermarktClient()

html = client.get(
    "https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1"
)

soup = BeautifulSoup(html, "lxml")

tables = soup.find_all("table")

for i, table in enumerate(tables[:5]):

    print("\n")
    print("=" * 80)
    print(f"TABLE {i}")
    print("classes :", table.get("class"))
    print("=" * 80)

    print(table.get_text(" ", strip=True)[:500])