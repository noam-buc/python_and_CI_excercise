from src.main import highest_number

def test_highest_numbers_man():
    result = highest_number(10, 29)
    assert result == 29
    result = highest_number(8, 5)
    assert result == 8