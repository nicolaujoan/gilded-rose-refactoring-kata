import pytest
from gilded_rose import Sulfuras
from test_collector import TestAutomata

# day 0
sulfuras1 = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
sulfuras2 = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)

# getting all sulfuras results from stdout.gr
EXPECTED_REPS_1 = TestAutomata.getExpectedReps("stdout.gr", "Sulfuras")


@pytest.mark.sulfuras
def test_sulfuras():
    assert 0 == 0