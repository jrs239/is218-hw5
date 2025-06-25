from commands.subtract import Subtract
from decimal import Decimal

def test_subtract():
    subtract = Subtract()
    assert subtract.execute(Decimal("5"), Decimal("2")) == 3
    assert subtract.execute(Decimal("2"), Decimal("5")) == -3
