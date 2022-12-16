from random import randint
import payCalculator

def test_payCalculator_prints_error_withNonNumericHoursBonus(capfd, monkeypatch):
    hours = 'njdvnjkfdfdb'
    input = [10, hours]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    payCalculator.calculatePay()

    out, err = capfd.readouterr()
    expected = 'Error, please enter numeric input\n'
    assert out == expected
def test_payCalculator_prints_error_withNonNumericPayBonus(capfd, monkeypatch):
    rate = 'bljhkjbbj'
    hours = randint(1, 100)
    input = [rate, hours]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    payCalculator.calculatePay()

    out, err = capfd.readouterr()
    expected = 'Error, please enter numeric input\n'
    assert out == expected
