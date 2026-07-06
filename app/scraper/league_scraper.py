import re

from bs4 import BeautifulSoup

from app.scraper.transfermarkt_client import TransfermarktClient


class LeagueScraper:

    def __init__(self):
        self.client = TransfermarktClient()

    def get_clubs(self, league_url: str):

        html = self.client.get(league_url)

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

            match = re.search(r"/verein/(\d+)", href)

            if not match:
                continue

            clubs.append(
                {
                    "tm_id": match.group(1),
                    "name": name,
                    "url": href,
                }
            )

        return clubs