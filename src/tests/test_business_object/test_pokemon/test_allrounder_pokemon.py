import pytest

from business_object.pokemon.allrounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


@pytest.mark.parametrize(
    "stat_current, expected",
    [
        (Statistic(sp_atk=0, sp_def=0), 1.0),
        (Statistic(sp_atk=50, sp_def=50), 1.5),  # 1 + (50+50)/200 = 1.5
        (Statistic(sp_atk=100, sp_def=100), 2.0),  # 1 + (100+100)/200 = 2.0
    ],
)
def test_get_allrounder_attack_coef(stat_current, expected):
    p = AllRounderPokemon(stat_current=stat_current)

    assert p.get_pokemon_attack_coef() == expected
