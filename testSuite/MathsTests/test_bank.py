from pytest import mark

from Code.Maths.Bank import BankAccount

params_account = [(5000, 2600, 7600), (6892, 7000, 13892), (8965, 6000, 14965)]


@mark.parametrize("cash, amount, reference", params_account)
def test_deposit(cash, amount, reference):
    obj = BankAccount(cash)
    obj.deposit(amount)
    assert obj.current_balance == reference


def test_exception():
    obj = BankAccount(1000)
    try:
        obj.deposit(-100)
        assert False
    except ValueError as e:
        assert e.args[0] == "amount must be a positive number"

    try:
        obj.withdrawal(-100)
        assert False
    except ValueError as e:
        assert e.args[0] == "amount must be a positive number"


def test_movement():
    obj = BankAccount(1000)
    obj.withdrawal(200)
    obj.deposit(100)
    assert obj.movimiento == {1: -200, 2: 100}
