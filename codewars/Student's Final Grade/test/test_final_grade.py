from src.final_grade import final_grade

def test_final_grade():
    assert final_grade(100, 12) == 100
    assert final_grade(85, 5) == 90
    assert final_grade(27, 10) == 90
    assert final_grade(27, 10) == 0
    assert final_grade(35, 10) == 0