from datetime import date
from types import SimpleNamespace

from app.repositories.player_repository import PlayerRepository


def test_build_player_summary(repo, player, stats):

    result = repo._build_player_summary(player, stats)

    assert result["id"] == 1
    assert result["player"] == "Kylian Mbappé"
    assert result["age"] == 27
    assert result["nationality"] == "France"
    assert result["position"] == "Centre-Forward"
    assert result["club"] == "Real Madrid"

    assert result["market_value_eur"] == 180000000.0

    assert result["goals"] == 35
    assert result["assists"] == 8
    assert result["appearances"] == 42
    assert result["minutes_played"] == 3300
    assert result["goals_per_90"] == 0.95
    assert result["assists_per_90"] == 0.22
    assert result["goal_contribution_per_90"] == 1.17

def test_build_comparison_player(repo, player, stats):

    result = repo._build_comparison_player(player, stats)

    assert result["id"] == 1
    assert result["name"] == "Kylian Mbappé"
    assert result["age"] == 27
    assert result["nationality"] == "France"
    assert result["position"] == "Centre-Forward"
    assert result["club"] == "Real Madrid"

    assert result["market_value_eur"] == 180000000.0

    assert result["goals"] == 35
    assert result["assists"] == 8
    assert result["appearances"] == 42
    assert result["minutes_played"] == 3300
    assert result["goals_per_90"] == 0.95
    assert result["assists_per_90"] == 0.22
    assert result["goal_contribution_per_90"] == 1.17

    