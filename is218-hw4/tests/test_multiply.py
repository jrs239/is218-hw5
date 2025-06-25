from commands.multiply import Multiply
from decimal import Decimal

def test_multiply():
    multiply = Multiply()
    assert multiply.execute(Decimal("4"), Decimal("3")) == 12
    assert multiply.execute(Decimal("0"), Decimal("999")) == 0