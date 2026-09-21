from app.calculator import add, subtract, multiply


def test_add():
    assert add(2,3)==5
def test_subtract():
    assert subtract(7,2)==5
def test_multiply():
    assert multiply(2,5)==10