import re
import requests

from bs4 import BeautifulSoup


class PlayerProfileScraper:

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

    def get_player_details(self, player_url: str):

        if player_url.startswith("http"):
            url = player_url
        else:
            url = self.BASE_URL + player_url

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

        details = {
            "birth_date": None,
            "height_cm": None,
            "foot": None
        }

        # ==========================
        # Date de naissance
        # ==========================

        birth_label = soup.find(
            string=lambda s:
            s and "Date of birth" in s
        )

        if birth_label:

            parent = birth_label.parent

            content = parent.find(
                "span",
                class_="data-header__content"
            )

            if content:

                match = re.search(
                    r"(\d{2}/\d{2}/\d{4})",
                    content.get_text(strip=True)
                )

                if match:
                    details["birth_date"] = match.group(1)

        # ==========================
        # Taille
        # ==========================

        height_label = soup.find(
            string=lambda s:
            s and "Height:" in s
        )

        if height_label:

            parent = height_label.parent

            content = parent.find(
                "span",
                class_="data-header__content"
            )

            if content:

                match = re.search(
                    r"(\d+[,.]\d+)",
                    content.get_text(strip=True)
                )

                if match:

                    height = float(
                        match.group(1)
                        .replace(",", ".")
                    )

                    details["height_cm"] = int(
                        height * 100
                    )

        # ==========================
        # Pied fort (nouveau format)
        # ==========================

        foot_label = soup.find(
            "span",
            class_="info-table__content info-table__content--regular",
            string=lambda s:
            s and "Foot" in s
        )

        if foot_label:

            foot_value = foot_label.find_next(
                "span",
                class_="info-table__content info-table__content--bold"
            )

            if foot_value:

                details["foot"] = (
                    foot_value
                    .get_text(strip=True)
                    .lower()
                )

        return details