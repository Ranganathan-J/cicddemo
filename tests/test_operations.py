"""Tests for calculator operations."""

import pytest

from calculator.operations import add, divide, multiply, power, subtract


class TestAdd:
    def test_add_positive_numbers(self) -> None:
        assert add(2, 3) == 5.0

    def test_add_negative_numbers(self) -> None:
        assert add(-1, -2) == -3.0

    def test_add_floats(self) -> None:
        assert add(1.5, 2.5) == 4.0

    def test_add_zero(self) -> None:
        assert add(0, 5) == 5.0


class TestSubtract:
    def test_subtract_basic(self) -> None:
        assert subtract(10, 3) == 7.0

    def test_subtract_negative_result(self) -> None:
        assert subtract(3, 10) == -7.0


class TestMultiply:
    def test_multiply_positive(self) -> None:
        assert multiply(3, 4) == 12.0

    def test_multiply_by_zero(self) -> None:
        assert multiply(5, 0) == 0.0

    def test_multiply_floats(self) -> None:
        assert multiply(2.5, 4) == 10.0


class TestDivide:
    def test_divide_basic(self) -> None:
        assert divide(10, 2) == 5.0

    def test_divide_floats(self) -> None:
        assert divide(7.5, 2.5) == 3.0

    def test_divide_by_zero_raises(self) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


# class TestPower:
#     def test_power_positive_exponent(self) -> None:
#         assert power(2, 3) == 8.0

#     def test_power_zero_exponent(self) -> None:
#         assert power(5, 0) == 1.0

#     def test_power_negative_exponent(self) -> None:
#         assert power(2, -1) == 0.5

#     def test_power_fractional_exponent(self) -> None:
#         assert power(9, 0.5) == 3.0
