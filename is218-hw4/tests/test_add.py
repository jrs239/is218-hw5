from commands.add import Add
from decimal import Decimal

def test_add():
    add = Add()
    assert add.execute(Decimal("2"), Decimal("3")) == 5
    assert add.execute(Decimal("0"), Decimal("0")) == 0
