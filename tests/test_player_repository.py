from types import SimpleNamespace
from unittest.mock import MagicMock
from datetime import date

from app.repositories.player_repository import PlayerRepository
from app.models.player import Player
from app.models.stat import PlayerStat


def test_get_all_players():

    # Fake Session Object
    db = MagicMock()

    # Fake Players
    players = [
        SimpleNamespace(
            id=1,
            name="Kylian Mbappé",
            club=SimpleNamespace(name="Real Madrid")
        ),
        SimpleNamespace(
            id=2,
            name="Erling Haaland",
            club=SimpleNamespace(name="Manchester City")
        )
    ]

    (
        db.query.return_value
        .order_by.return_value
        .all.return_value
    ) = players

    repo = PlayerRepository(db)

    result = repo.get_all_players()

    assert len(result) == 2

    assert result[0]["id"] == 1
    assert result[0]["name"] == "Kylian Mbappé"
    assert result[0]["club"] == "Real Madrid"

    assert result[1]["id"] == 2
    assert result[1]["name"] == "Erling Haaland"
    assert result[1]["club"] == "Manchester City"

    db.query.assert_called_once_with(Player)

def test_search_players():

    player = SimpleNamespace(
        id=1,
        name="Kylian Mbappé",
        nationality="France",
        position="Centre-Forward",
        market_value_eur=180000000,
        club=SimpleNamespace(name="Real Madrid")
    )

    query = MagicMock()
    query.filter.return_value = query
    query.limit.return_value = query
    query.all.return_value = [player]

    db = MagicMock()
    db.query.return_value = query

    repo = PlayerRepository(db)

    result = repo.search_players("Mbappé")

    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["name"] == "Kylian Mbappé"
    assert result[0]["club"] == "Real Madrid"

    db.query.assert_called_once()
    query.filter.assert_called_once()
    query.limit.assert_called_once_with(20)
    query.all.assert_called_once()

def test_get_player_details():

    player = SimpleNamespace(
        id=1,
        name="Kylian Mbappé",
        birth_date=date(1998, 12, 20),
        nationality="France",
        position="Centre-Forward",
        market_value_eur=180000000,
        club=SimpleNamespace(id=99, name="Real Madrid")
    )

    stats = SimpleNamespace(
        season="25/26",
        competition="LaLiga",
        goals=35,
        assists=8,
        appearances=42,
        minutes_played=3300,
        goals_per_90=0.95,
        assists_per_90=0.22,
        goal_contribution_per_90=1.17
    )

    # First query: Player
    player_query = MagicMock()
    player_query.filter.return_value = player_query
    player_query.first.return_value = player

    # Second query: PlayerStat
    stats_query = MagicMock()
    stats_query.filter.return_value = stats_query
    stats_query.first.return_value = stats

    db = MagicMock()

    # The two consecutive calls to db.query(...)
    db.query.side_effect = [
        player_query,
        stats_query
    ]

    repo = PlayerRepository(db)

    result = repo.get_player_details(1)

    assert result["id"] == 1
    assert result["name"] == "Kylian Mbappé"
    assert result["club"]["name"] == "Real Madrid"
    assert result["club"]["id"] == 99

    assert result["stats"]["season"] == "25/26"
    assert result["stats"]["competition"] == "LaLiga"

    assert result["stats"]["goals"] == 35
    assert result["stats"]["assists"] == 8
    assert result["stats"]["appearances"] == 42
    assert result["stats"]["minutes_played"] == 3300

    assert result["stats"]["goals_per_90"] == 0.95
    assert result["stats"]["assists_per_90"] == 0.22
    assert result["stats"]["goal_contribution_per_90"] == 1.17

    assert db.query.call_count == 2

    db.query.assert_any_call(Player)
    db.query.assert_any_call(PlayerStat)

def test_compare_players(monkeypatch):

    repo = PlayerRepository(None)

    player1 = SimpleNamespace(
        id=1,
        name="Kylian Mbappé",
        birth_date=date(1998, 12, 20),
        nationality="France",
        position="Centre-Forward",
        market_value_eur=180000000,
        club=SimpleNamespace(name="Real Madrid")
    )

    stats1 = SimpleNamespace(
        goals=35,
        assists=8,
        appearances=42,
        minutes_played=3300,
        goals_per_90=0.95,
        assists_per_90=0.22,
        goal_contribution_per_90=1.17
    )

    player2 = SimpleNamespace(
        id=2,
        name="Erling Haaland",
        birth_date=date(2000, 7, 21),
        nationality="Norway",
        position="Centre-Forward",
        market_value_eur=170000000,
        club=SimpleNamespace(name="Manchester City")
    )

    stats2 = SimpleNamespace(
        goals=31,
        assists=5,
        appearances=39,
        minutes_played=3150,
        goals_per_90=0.89,
        assists_per_90=0.14,
        goal_contribution_per_90=1.03
    )

    def fake_get_player_with_stats(player_id, season):
        if player_id == 1:
            return (player1, stats1)
        if player_id == 2:
            return (player2, stats2)

    monkeypatch.setattr(
        repo,
        "_get_player_with_stats",
        fake_get_player_with_stats
    )

    result = repo.compare_players(1, 2)

    assert result is not None

    assert result["player1"]["name"] == "Kylian Mbappé"
    assert result["player1"]["goals"] == 35
    assert result["player1"]["club"] == "Real Madrid"

    assert result["player2"]["name"] == "Erling Haaland"
    assert result["player2"]["goals"] == 31
    assert result["player2"]["club"] == "Manchester City"

def test_get_most_valuable_players():

    repo = PlayerRepository(None)

    player1 = SimpleNamespace(
        id=1,
        name="Kylian Mbappé",
        birth_date=date(1998, 12, 20),
        nationality="France",
        position="Centre-Forward",
        market_value_eur=180000000,
        club=SimpleNamespace(name="Real Madrid")
    )

    player2 = SimpleNamespace(
        id=2,
        name="Erling Haaland",
        birth_date=date(2000, 7, 21),
        nationality="Norway",
        position="Centre-Forward",
        market_value_eur=170000000,
        club=SimpleNamespace(name="Manchester City")
    )

    fake_query = MagicMock()

    fake_query.filter.return_value = fake_query
    fake_query.order_by.return_value = fake_query
    fake_query.limit.return_value = fake_query
    fake_query.all.return_value = [player1, player2]

    repo.db = MagicMock()
    repo.db.query.return_value = fake_query

    result = repo.get_most_valuable_players()

    assert len(result) == 2

    assert result[0]["player"] == "Kylian Mbappé"
    assert result[0]["market_value"] == 180000000.0

    assert result[1]["player"] == "Erling Haaland"
    assert result[1]["market_value"] == 170000000.0

def test_get_top_scorers(mocker):

    repo = PlayerRepository(None)

    player = SimpleNamespace(
        id=1,
        name="Kylian Mbappé",
        birth_date=date(1998, 12, 20),
        nationality="France",
        position="Centre-Forward",
        market_value_eur=180000000,
        club=SimpleNamespace(name="Real Madrid")
    )

    stats = SimpleNamespace(
        goals=35,
        assists=8,
        appearances=42,
        minutes_played=3300,
        goals_per_90=0.95,
        assists_per_90=0.22,
        goal_contribution_per_90=1.17
    )

    query = mocker.Mock()

    (
        query.join.return_value
             .filter.return_value
             .order_by.return_value
             .limit.return_value
             .all.return_value
    ) = [(player, stats)]

    repo.db = mocker.Mock()
    repo.db.query.return_value = query

    result = repo.get_top_scorers()

    assert len(result) == 1

    player_result = result[0]

    assert player_result["player"] == "Kylian Mbappé"
    assert player_result["goals"] == 35
    assert player_result["assists"] == 8
    assert player_result["appearances"] == 42
    assert player_result["club"] == "Real Madrid"
    assert player_result["market_value_eur"] == 180000000.0