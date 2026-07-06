from app.scraper.transfermarkt_client import TransfermarktClient


client = TransfermarktClient()

html = client.get(
    "https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1"
)

print("Ligue 1" in html)
print("Paris Saint-Germain" in html)