import requests
from config import API_URL


def api_get(endpoint, params=None):
    try:
        response = requests.get(
            API_URL + endpoint,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.HTTPError:
        return None

    except requests.RequestException:
        return None

