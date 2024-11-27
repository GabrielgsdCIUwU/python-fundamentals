from src.is_valid_walk import is_valid_walk

def test_is_valid_walk():
    assert is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
    assert is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) is False
    assert is_valid_walk(['w']) is False
    assert is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) is False