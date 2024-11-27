from src.is_triangle import is_triangle

def test_is_triangle():
    assert is_triangle(1, 2, 2)
    assert is_triangle(4, 2, 3)
    assert is_triangle(5, 1, 5)
    assert is_triangle(2, 2, 2)
    
    assert is_triangle(7, 2, 2) is False
    assert is_triangle(1, 2, 3) is False
    assert is_triangle(1, 3, 2) is False
    assert is_triangle(3, 1, 2) is False
    assert is_triangle(5, 1, 2) is False
    assert is_triangle(1, 2, 5) is False
    assert is_triangle(2, 5, 1) is False
    assert is_triangle(-1, 2, 3) is False
    assert is_triangle(1, -2, 3) is False
    assert is_triangle(1, 2, -3) is False
    assert is_triangle(0, 2, 3) is False