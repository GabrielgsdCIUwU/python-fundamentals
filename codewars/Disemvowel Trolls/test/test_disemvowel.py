from src.disemvowel import disemvowel

def test_disemvowel():
    assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"
    assert disemvowel("No offense but,\nYour writing is among the worst I've ever read") == "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"
    assert disemvowel("What are you, a communist?") == "Wht r y,  cmmnst?"