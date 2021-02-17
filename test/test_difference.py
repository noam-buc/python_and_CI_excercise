from src.main import difference


def test_difference():
    result = difference(8, 6)
    assert result == 2
    result = difference(23, 26)
    assert result == 3
