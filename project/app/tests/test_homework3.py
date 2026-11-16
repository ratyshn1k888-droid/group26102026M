import pytest
from utils.utils_homework3 import calculate_discount, is_even, get_full_name


# Тести calculate_discount

def test_calculate_discount_20():
    assert calculate_discount(100, 20) == 80


def test_calculate_discount_50():
    assert calculate_discount(200, 50) == 100


def test_calculate_discount_0():
    assert calculate_discount(100, 0) == 100


def test_calculate_discount_zero_price():
    assert calculate_discount(0, 20) == 0


def test_calculate_discount_other():
    assert calculate_discount(150, 10) == 135


# Тести is_even

def test_is_even_positive():
    assert is_even(8) == True


def test_is_even_odd():
    assert is_even(7) == False


def test_is_even_negative():
    assert is_even(-4) == True


def test_is_even_negative_odd():
    assert is_even(-5) == False


def test_is_even_zero():
    assert is_even(0) == True


# Тести get_full_name

def test_get_full_name():
    assert get_full_name('Ivan', 'Petrov') == 'Ivan Petrov'


def test_get_full_name_short():
    assert get_full_name('Al', 'Li') == 'Al Li'


def test_get_full_name_long():
    assert get_full_name('Alexander', 'Peterson') == 'Alexander Peterson'


def test_get_full_name_one_symbol():
    assert get_full_name('A', 'B') == 'A B'


def test_get_full_name_other():
    assert get_full_name('Mykhailo', 'Shevchenko') == 'Mykhailo Shevchenko'