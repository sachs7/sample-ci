import calculator
import pytest


class TestCalculator:

    @pytest.mark.parametrize("test_input_1, test_input_2, expected", [
        (3, 5, 8),
        (-10, 10, 0),
        (2, 2, 4)
    ])
    def test_addition(self, test_input_1, test_input_2, expected):
        assert calculator.add(test_input_1, test_input_2) == expected

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 10 == calculator.divide(100, 10)
