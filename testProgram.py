import io
from random import randint
import random
from unittest.mock import Mock
import payCalculator

def test_payCalculator_prints_correct_result(capfd, monkeypatch):
    rate = float(randint(1, 100))
    hours = randint(1, 40)
    input = [rate, hours]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    payCalculator.calculatePay()

    out, err = capfd.readouterr()
    expected = "Pay: "+str(rate * hours)+"\n"
    assert out == expected
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
def test_payCalculator_prints_error_withOver40Hours(capfd, monkeypatch):
    rate = float(randint(1, 100))
    hours = randint(41, 100)
    input = [rate, hours]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    payCalculator.calculatePay()
    otHours = hours-40
    out, err = capfd.readouterr()
    expected = "Pay: "+str(rate * 40+otHours*1.5*rate)+"\n"
    assert out == expected
