from project import draw_chips, add_integers

def test_draw_chips_positive():
    assert draw_chips(3) == 3
    assert draw_chips(0) == 0

def test_draw_chips_negative():
    assert draw_chips(-2) == -2
    assert draw_chips(-5) == -5

def test_add_integers():
    assert add_integers(2, 3) == 5
    assert add_integers(-2, -3) == -5
    assert add_integers(5, -3) == 2
    assert add_integers(2, -7) == -5
    assert add_integers(0, 0) == 0
