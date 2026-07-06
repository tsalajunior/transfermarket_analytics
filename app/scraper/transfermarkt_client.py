import requests


class TransfermarktClient:

    BASE_URL = "https://www.transfermarkt.com"

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/137.0 Safari/537.36"
        )
    }

    def get(self, url: str):

        response = requests.get(
            url,
            headers=self.HEADERS,
            timeout=30
        )

        response.raise_for_status()

        return response.text