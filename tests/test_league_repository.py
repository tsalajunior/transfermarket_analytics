from types import SimpleNamespace
from unittest.mock import MagicMock

from app.repositories.league_repository import LeagueRepository


def test_get_all():

    repo = LeagueRepository(None)

    leagues = [
        SimpleNamespace(id=1, name="Premier League"),
        SimpleNamespace(id=2, name="LaLiga")
    ]

    query = MagicMock()
    query.all.return_value = leagues

    repo.db = MagicMock()
    repo.db.query.return_value = query

    result = repo.get_all()

    assert len(result) == 2
    assert result[0].name == "Premier League"
    assert result[1].name == "LaLiga"

    repo.db.query.assert_called_once()
    query.all.assert_called_once()

def test_get_league_dashboard():

    repo = LeagueRepository(None)

    league = SimpleNamespace(
        name="LaLiga",
        country="Spain"
    )

    clubs = [
        SimpleNamespace(id=1, league=league),
        SimpleNamespace(id=2, league=league)
    ]

    players = [
        SimpleNamespace(birth_date=None),
        SimpleNamespace(birth_date=None)
    ]

    query_clubs = MagicMock()
    query_clubs.filter.return_value.all.return_value = clubs

    query_market_value = MagicMock()
    query_market_value.filter.return_value.scalar.return_value = 1000000000

    query_players = MagicMock()
    query_players.filter.return_value.all.return_value = players

    query_goals = MagicMock()
    (
        query_goals
        .join.return_value
        .filter.return_value
        .scalar.return_value
    ) = 120

    query_assists = MagicMock()
    (
        query_assists
        .join.return_value
        .filter.return_value
        .scalar.return_value
    ) = 85

    query_count = MagicMock()
    query_count.filter.return_value.count.return_value = 2

    repo.db = MagicMock()

    repo.db.query.side_effect = [
        query_clubs,
        query_market_value,
        query_players,
        query_goals,
        query_assists,
        query_count
    ]

    result = repo.get_league_dashboard(1)

    assert result["league"] == "LaLiga"
    assert result["country"] == "Spain"
    assert result["clubs"] == 2
    assert result["players"] == 2
    assert result["total_market_value"] == 1000000000
    assert result["goals"] == 120
    assert result["assists"] == 85

def test_get_club_market_values():

    repo = LeagueRepository(None)

    rows = [
        SimpleNamespace(
            name="Real Madrid",
            market_value=1250000000
        ),
        SimpleNamespace(
            name="Barcelona",
            market_value=980000000
        )
    ]

    query = MagicMock()

    (
        query
        .join.return_value
        .filter.return_value
        .group_by.return_value
        .order_by.return_value
        .all.return_value
    ) = rows

    repo.db = MagicMock()
    repo.db.query.return_value = query

    result = repo.get_club_market_values(1)

    assert len(result) == 2
    assert result[0]["club"] == "Real Madrid"
    assert result[0]["market_value"] == 1250000000.0

def test_get_attack_scatter():

    repo = LeagueRepository(None)

    rows = [
        SimpleNamespace(
            club="Real Madrid",
            goals=85,
            assists=60
        ),
        SimpleNamespace(
            club="Barcelona",
            goals=75,
            assists=58
        )
    ]

    query = MagicMock()

    (
        query
        .join.return_value
        .join.return_value
        .filter.return_value
        .group_by.return_value
        .all.return_value
    ) = rows

    repo.db = MagicMock()
    repo.db.query.return_value = query

    result = repo.get_attack_scatter(1, "25/26")

    assert len(result) == 2
    assert result[0]["club"] == "Real Madrid"
    assert result[0]["goals"] == 85
    assert result[0]["assists"] == 60

def test_get_top_scorers():

    repo = LeagueRepository(None)

    rows = [
        SimpleNamespace(
            player="Mbappé",
            club="Real Madrid",
            goals=35
        ),
        SimpleNamespace(
            player="Lewandowski",
            club="Barcelona",
            goals=28
        )
    ]

    query = MagicMock()

    (
        query
        .join.return_value
        .join.return_value
        .filter.return_value
        .order_by.return_value
        .limit.return_value
        .all.return_value
    ) = rows

    repo.db = MagicMock()
    repo.db.query.return_value = query

    result = repo.get_top_scorers(1, "25/26")

    assert len(result) == 2
    assert result[0]["player"] == "Mbappé"
    assert result[0]["goals"] == 35

def test_get_most_offensive_clubs():

    repo = LeagueRepository(None)

    rows = [
        SimpleNamespace(
            club="Real Madrid",
            goals=85
        ),
        SimpleNamespace(
            club="Barcelona",
            goals=75
        )
    ]

    query = MagicMock()

    (
        query
        .join.return_value
        .join.return_value
        .filter.return_value
        .group_by.return_value
        .order_by.return_value
        .all.return_value
    ) = rows

    repo.db = MagicMock()
    repo.db.query.return_value = query

    result = repo.get_most_offensive_clubs(1, "25/26")

    assert len(result) == 2
    assert result[0]["club"] == "Real Madrid"
    assert result[0]["goals"] == 85