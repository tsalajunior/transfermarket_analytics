import requests
import json

class PlayerStatsScraper:

    BASE_URL = "https://tmapi.transfermarkt.technology"

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

    def get_ligue1_stats(
        self,
        player_tm_id,
        season="25/26"
    ):

        player_tm_id = str(player_tm_id)

        if "/" in player_tm_id:
            player_tm_id = player_tm_id.split("/")[-1]

        url = (
            f"{self.BASE_URL}/player/"
            f"{player_tm_id}/performance-game"
        )

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        performances = data.get(
            "data",
            {}
        ).get(
            "performance",
            []
        )

        stats = {
            "competition": "FR1",
            "season": season,
            "appearances": 0,
            "goals": 0,
            "assists": 0,
            "minutes_played": 0,
            "yellow_cards": 0,
            "red_cards": 0,
        }

        for match in performances:

            game_info = match.get(
                "gameInformation",
                {}
            )

            competition = game_info.get(
                "competitionId"
            )

            season_info = game_info.get(
                "season",
                {}
            )

            match_season = season_info.get(
                "nonCyclicalName",
                ""
            )

            # print(
            #     f"competition={competition} | "
            #     f"season={match_season}"
            # )

            if competition != "FR1":
                continue

            if match_season != season:
                continue

            stats["appearances"] += 1

            statistics = match.get(
                "statistics",
                {}
            )

            goal_stats = statistics.get(
                "goalStatistics",
                {}
            )

            playing_stats = statistics.get(
                "playingTimeStatistics",
                {}
            )

            card_stats = statistics.get(
                "cardStatistics",
                {}
            )

            stats["goals"] += int(
                goal_stats.get(
                    "goalsScoredTotal"
                ) or 0
            )

            stats["assists"] += int(
                goal_stats.get(
                    "assists"
                ) or 0
            )

            stats["minutes_played"] += int(
                playing_stats.get(
                    "playedMinutes"
                ) or 0
            )

            stats["yellow_cards"] += int(
                card_stats.get(
                    "yellowCardGross"
                ) or 0
            )

            stats["red_cards"] += int(
                card_stats.get(
                    "redCardGross"
                ) or 0
            )
        return stats