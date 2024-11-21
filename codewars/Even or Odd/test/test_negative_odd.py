from src.even_or_odd import even_or_odd

def test_negative_odd():
    assert even_or_odd(-1) == "Odd"
    assert even_or_odd(-3) == "Odd"