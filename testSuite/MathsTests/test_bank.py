from pytest import mark

from Code.Maths.Bank import BankAccount

params_account = [(5000, 2600, 3000), (6892, 63, 7000), (8965, 6385, 7000)]


@mark.parametrize("cash, income, bill", params_account)
def test_balance(cash, income, bill):
    obj = BankAccount(cash, income, bill)

    assert obj
