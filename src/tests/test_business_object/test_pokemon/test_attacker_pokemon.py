import pytest

from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


@pytest.mark.parametrize(
    "stat_current, expected",
    [
        (Statistic(speed=0, attack=0), 1.0),
        (Statistic(speed=50, attack=50), 1.5),
        (Statistic(speed=100, attack=100), 2.0),
    ],
)
def test_get_pokemon_attack_coef_param(stat_current, expected):
    p = AttackerPokemon(stat_current=stat_current)

    assert p.get_pokemon_attack_coef() == expected
