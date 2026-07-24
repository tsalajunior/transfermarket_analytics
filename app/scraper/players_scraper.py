import re
import requests

from bs4 import BeautifulSoup


class PlayerScraper:

    BASE_URL = "https://www.transfermarkt.com"

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/137.0.0.0 Safari/537.36"
            )
        }

    def parse_market_value(self, value: str) -> int:
        if not value or value.strip() == "-":
            return 0

        value = value.replace("€", "").strip()

        try:

            if value.endswith("bn"):
                return int(float(value[:-2]) * 1_000_000_000)

            if value.endswith("m"):
                return int(float(value[:-1]) * 1_000_000)

            if value.endswith("k"):
                return int(float(value[:-1]) * 1_000)

        except ValueError:
            return 0

        return 0

    def get_players(self, club_url: str):

        if club_url.startswith("http"):
            url = club_url
        else:
            url = self.BASE_URL + club_url

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        players = []

        tables = soup.find_all("table")

        if len(tables) < 2:
            return players

        squad_table = tables[1]

        rows = squad_table.find_all("tr")

        for row in rows:

            try:

                player_link = row.select_one(
                    "td.hauptlink a"
                )

                if not player_link:
                    continue

                name = player_link.get_text(strip=True)

                href = player_link.get("href", "")

                match = re.search(
                    r"/spieler/(\d+)",
                    href
                )

                if not match:
                    continue

                tm_id = match.group(1)

                inline_rows = row.select(
                    "table.inline-table tr"
                )

                if len(inline_rows) < 2:
                    continue

                position = (
                    inline_rows[1]
                    .get_text(strip=True)
                )

                nationality_img = row.select_one(
                    "img.flaggenrahmen"
                )

                nationality = (
                    nationality_img.get("title")
                    if nationality_img
                    else None
                )

                market_value_link = row.select_one(
                    "td.rechts.hauptlink a"
                )

                market_value = 0

                if market_value_link:
                    market_value = self.parse_market_value(
                        market_value_link.get_text(strip=True)
                    )

                players.append({
                    "tm_id": tm_id,
                    "name": name,
                    "position": position,
                    "nationality": nationality,
                    "market_value": market_value,
                    "url": href
                })

            except Exception as e:
                print(f"Erreur joueur : {e}")
                continue

        return players