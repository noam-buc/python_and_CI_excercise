from src.main import difference, highest_number


def test_difference():
    result = difference(8, 6)
    assert result == 2
    result = difference(23, 26)
    assert result == 3


def test_highest_numbers_man():
    result = highest_number(10, 29)
    assert result == 29
    result = highest_number(8, 5)
    assert result == 8