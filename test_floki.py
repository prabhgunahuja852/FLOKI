from floki import speak, wish_me, tell_day_time


def test_speak(capsys):
    speak("Hello")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Floki: Hello"


def test_wish_me(capsys):
    wish_me()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Floki: Hello, I am Floki. How may I help you today?"


def test_tell_day_time(capsys):
    tell_day_time()
    captured = capsys.readouterr()
    assert "Today is" in captured.out
    assert "and the current time is" in captured.out