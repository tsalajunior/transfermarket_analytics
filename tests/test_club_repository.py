from types import SimpleNamespace
from unittest.mock import MagicMock

from app.repositories.club_repository import ClubRepository


def test_get_all_clubs():

    repo = ClubRepository(None)

    club1 = SimpleNamespace(
        id=1,
        name="FC Barcelona"
    )

    club2 = SimpleNamespace(
        id=2,
        name="Real Madrid"
    )

    query = MagicMock()

    query.order_by.return_value.all.return_value = [
        club1,
        club2
    ]

    repo.db = MagicMock()
    repo.db.query.return_value = query

    result = repo.get_all_clubs()

    assert len(result) == 2

    assert result[0].id == 1
    assert result[0].name == "FC Barcelona"

    assert result[1].id == 2
    assert result[1].name == "Real Madrid"

    repo.db.query.assert_called_once()
    query.order_by.assert_called_once()
    # query.all.assert_called_once()
    #
    query.order_by.return_value.all.assert_called_once()

def test_get_club_details():

    repo = ClubRepository(None)

    # ---- Club ----

    club = SimpleNamespace(
        id=1,
        name="Real Madrid",
        country="Spain",
        league=SimpleNamespace(
            name="LaLiga"
        )
    )

    # ---- Team stats ----

    team_stats = SimpleNamespace(
        market_value=1250000000,
        average_market_value=52083333,
        average_age=26.4,
        goals=84,
        assists=59
    )

    # ---- Top scorer ----

    top_scorer = SimpleNamespace(
        name="Kylian Mbappé",
        goals=35
    )

    # ---- Top assist ----

    top_assist = SimpleNamespace(
        name="Jude Bellingham",
        assists=14
    )

    # ---------- query 1 : club ----------

    query_club = MagicMock()
    query_club.filter.return_value.first.return_value = club

    # ---------- query 2 : players count ----------

    query_players = MagicMock()
    query_players.filter.return_value.count.return_value = 24

    # ---------- query 3 : team stats ----------

    query_stats = MagicMock()
    (
        query_stats
        .join.return_value
        .filter.return_value
        .first.return_value
    ) = team_stats

    # ---------- query 4 : top scorer ----------

    query_scorer = MagicMock()
    (
        query_scorer
        .join.return_value
        .filter.return_value
        .order_by.return_value
        .first.return_value
    ) = top_scorer

    # ---------- query 5 : top assist ----------

    query_assist = MagicMock()
    (
        query_assist
        .join.return_value
        .filter.return_value
        .order_by.return_value
        .first.return_value
    ) = top_assist

    repo.db = MagicMock()

    repo.db.query.side_effect = [
        query_club,
        query_players,
        query_stats,
        query_scorer,
        query_assist
    ]

    result = repo.get_club_details(1)

    assert result["id"] == 1
    assert result["name"] == "Real Madrid"
    assert result["country"] == "Spain"
    assert result["league"] == "LaLiga"

    assert result["players_count"] == 24

    assert result["top_scorer"]["name"] == "Kylian Mbappé"
    assert result["top_scorer"]["goals"] == 35

    assert result["top_assist"]["name"] == "Jude Bellingham"
    assert result["top_assist"]["assists"] == 14

    assert result["total_market_value"] == 1250000000.0
    assert result["average_market_value"] == 52083333.0
    assert result["average_age"] == 26.4
    assert result["total_goals"] == 84
    assert result["total_assists"] == 59

def test_get_players_by_club():

    repo = ClubRepository(None)

    player1 = SimpleNamespace(
        id=1,
        name="Kylian Mbappé",
        position="Centre-Forward",
        market_value_eur=180000000,

        appearances=42,
        goals=35,
        assists=8,
        minutes_played=3300,
        goals_per_90=0.95,
        assists_per_90=0.22,
        goal_contribution_per_90=1.17
    )

    player2 = SimpleNamespace(
        id=2,
        name="Vinicius Junior",
        position="Left Winger",
        market_value_eur=170000000,

        appearances=40,
        goals=22,
        assists=15,
        minutes_played=3150,
        goals_per_90=0.63,
        assists_per_90=0.43,
        goal_contribution_per_90=1.06
    )

    query = MagicMock()

    (
        query
        .join.return_value
        .filter.return_value
        .order_by.return_value
        .all.return_value
    ) = [
        player1,
        player2
    ]

    repo.db = MagicMock()
    repo.db.query.return_value = query

    result = repo.get_players_by_club(1)

    assert len(result) == 2

    assert result[0].name == "Kylian Mbappé"
    assert result[0].goals == 35

    assert result[1].name == "Vinicius Junior"
    assert result[1].assists == 15

    repo.db.query.assert_called_once()
    query.join.assert_called_once()
    query.join.return_value.filter.assert_called_once()
    query.join.return_value.filter.return_value.order_by.assert_called_once()
    query.join.return_value.filter.return_value.order_by.return_value.all.assert_called_once()

def test_get_clubs_market_value():

    repo = ClubRepository(None)

    club1 = SimpleNamespace(
        club="Real Madrid",
        market_value=1250000000
    )

    club2 = SimpleNamespace(
        club="Manchester City",
        market_value=1180000000
    )

    query = MagicMock()

    (
        query
        .join.return_value
        .group_by.return_value
        .order_by.return_value
        .limit.return_value
        .all.return_value
    ) = [
        club1,
        club2
    ]

    repo.db = MagicMock()
    repo.db.query.return_value = query

    result = repo.get_clubs_market_value()

    assert len(result) == 2

    assert result[0].club == "Real Madrid"
    assert result[0].market_value == 1250000000

    assert result[1].club == "Manchester City"
    assert result[1].market_value == 1180000000

    repo.db.query.assert_called_once()
    query.join.assert_called_once()
    query.join.return_value.group_by.assert_called_once()
    query.join.return_value.group_by.return_value.order_by.assert_called_once()
    query.join.return_value.group_by.return_value.order_by.return_value.limit.assert_called_once_with(20)
    query.join.return_value.group_by.return_value.order_by.return_value.limit.return_value.all.assert_called_once()




