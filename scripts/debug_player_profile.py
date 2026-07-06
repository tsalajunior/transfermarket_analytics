# import requests
# from bs4 import BeautifulSoup
# from app.scraper.player_profile_scraper import PlayerProfileScraper

# scraper = PlayerProfileScraper()

# url = (
#     scraper.BASE_URL +
#     "/nuno-mendes/profil/spieler/578876"
# )

# response = requests.get(
#     url,
#     headers=scraper.headers,
#     timeout=30
# )

# response.raise_for_status()

# soup = BeautifulSoup(
#     response.text,
#     "html.parser"
# )

# print("\n===== FOOT STRUCTURE =====")

# foot = None

# for span in soup.select("span.info-table__content--regular"):

#     text = span.get_text(strip=True)

#     if text == "Foot:":

#         print("Label trouvé :", text)

#         value = span.find_next(
#             "span",
#             class_="info-table__content--bold"
#         )

#         if value:
#             foot = value.get_text(strip=True).lower()
#             print("Valeur trouvée :", foot)

#         break

# print("\n===== RESULTAT =====")
# print("foot =", foot)

# import requests
# from bs4 import BeautifulSoup
# from app.scraper.player_profile_scraper import PlayerProfileScraper

# scraper = PlayerProfileScraper()

# url = (
#     scraper.BASE_URL +
#     "/nuno-mendes/profil/spieler/578392"
# )

# response = requests.get(
#     url,
#     headers=scraper.headers,
#     timeout=30
# )

# response.raise_for_status()

# soup = BeautifulSoup(
#     response.text,
#     "html.parser"
# )

# print("\n===== RECHERCHE DU MOT FOOT =====")

# for tag in soup.find_all(string=True):

#     text = tag.strip()

#     if "foot" in text.lower():

#         print("\n------------------")
#         print(text)

#         parent = tag.parent

#         if parent:
#             print(parent)

import requests
from bs4 import BeautifulSoup
from app.scraper.player_profile_scraper import PlayerProfileScraper

scraper = PlayerProfileScraper()

url = (
    scraper.BASE_URL +
    "/nuno-mendes/profil/spieler/616341"
)

response = requests.get(
    url,
    headers=scraper.headers,
    timeout=30
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

for span in soup.select("span.info-table__content--regular"):

    if span.get_text(strip=True) == "Foot:":

        print("LABEL TROUVÉ")
        print(span)

        print("\nPARENT :")
        print(span.parent)

        print("\nENFANTS DU PARENT :")

        for child in span.parent.children:
            print(repr(child))

        break
print(url)
print(response.url)
print(soup.title.get_text())