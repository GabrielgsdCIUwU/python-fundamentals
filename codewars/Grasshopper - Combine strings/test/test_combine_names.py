from src.combine_names import combine_names

def test_combine_names():
    assert combine_names("James", "Stevens") == "James Stevens"
    assert combine_names("Davy", "Back") == "Davy Back"
    assert combine_names("Arthur", "Dent") == "Arthur Dent"