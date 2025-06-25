from commands.divide import Divide
from decimal import Decimal
import pytest

def test_divide():
    divide = Divide()
    assert divide.execute(Decimal("10"), Decimal("2")) == 5

def test_divide_by_zero():
    divide = Divide()
    with pytest.raises(ZeroDivisionError):
        divide.execute(Decimal("10"), Decimal("0"))
