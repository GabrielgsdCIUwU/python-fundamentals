from src.even_or_odd import even_or_odd

def test_negative_even():
    assert even_or_odd(-2) == "Even"
    assert even_or_odd(-4) == "Even"