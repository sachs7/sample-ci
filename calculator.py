"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    """
    Add two numbers
    :param first_term: first number
    :param second_term: second number
    :return: sum of the two numbers
    """
    return first_term + second_term


def subtract(first_term, second_term):
    """
    Subtract two numbers
    :param first_term: first number
    :param second_term: second number
    :return: difference of the two numbers
    """
    return first_term - second_term


def multiply(first_term, second_term):
    """
    Multiply two numbers
    :param first_term: first number
    :param second_term: second number
    :return: product of the two numbers
    """
    print("Multiplying {} and {}".format(first_term, second_term))
    return first_term * second_term


def divide(first_term, second_term):
    """
    Divide two numbers
    :param first_term: first number
    :param second_term: second number
    :return: quotient of the two numbers
    """
    return first_term // second_term
