import calculator
import pytest


class TestCalculator:
    """
    Test class for the calculator module   
    """

    @pytest.mark.parametrize("test_input_1, test_input_2, expected", [
        (3, 5, 8),
        (-10, 10, 0),
        (2, 2, 4)
    ])
    def test_addition(self, test_input_1, test_input_2, expected):
        """
        Test the addition function of the calculator
        :param test_input_1: The first number to add
        :param test_input_2: The second number to add
        :param expected: The expected result
        :return: None
        """
        assert calculator.add(test_input_1, test_input_2) == expected

    def test_subtraction(self):
        """
        Test the subtraction function of the calculator
        :return: None
        """
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        """
        Test the multiplication function of the calculator
        :return: None
        """
        assert 0 == calculator.multiply(0, 10)
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        """
        Test the division function of the calculator
        :return: None
        """
        with pytest.raises(ZeroDivisionError):
            calculator.divide(10, 0)
        assert 10 == calculator.divide(100, 10)
