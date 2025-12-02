import pytest

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Negative numbers do not have factorials")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# --- Normal cases ---
def test_factorial_of_1():
    assert factorial(1) == 1 ,"Test Failed because values do not match"

def test_factorial_of_3():
    assert factorial(3) == 6 ,"Test Failed because values do not match"

def test_factorial_of_5():
    assert factorial(5) == 120 ,"Test Failed because values do not match"

# --- Edge cases ---
def test_factorial_of_0():
    result = factorial(0)
    print(f"Testing factorial(0), expected 1, got {result}")
    assert result == 1
    
def test_factorial_of_large_number():
    assert factorial(10) == 36288

def test_factorial_of_20():
    assert factorial(20) == 24329020081766400

def test_factorial_of_100():
    assert factorial(100) > 0  # Just check it runs without error

# --- Invalid inputs ---
def test_factorial_of_negative_number():
    try:
        factorial(-1)
    except ValueError as e:
        print(f"Testing factorial(-1), caught expected exception: {e}")
        assert True
    else:
        assert False, "ValueError was not raised"


def test_factorial_of_float():
    try:
        factorial(3.5)
    except TypeError as e:
        print(f"Testing factorial(3.5), caught expected exception: {e}")
        assert True
    else:
        assert False, "TypeError was not raised"

def test_factorial_of_string():
    try:
        factorial("5")
    except TypeError as e:
        print(f"Testing factorial('5'), caught expected exception: {e}")
        assert True
    else:
        assert False, "TypeError was not raised"
