# converter.py

"""
converter.py
~~~~~~~~~~~~

A module that provides functions to convert numbers between any base from 2 to 62.
"""

# Allowed symbols for bases up to 62 (0-9, A-Z, a-z)
SYMBOLS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def to_decimal(num_str: str, src_base: int) -> int:
    """
    Convert a number represented as a string `num_str` from source base `src_base`
    into a decimal integer (base 10).

    :param num_str:  String representation of the number in the source base.
    :param src_base: The source base (range: 2–62).
    :return:         Decimal integer (base 10).
    :raises ValueError: If the source base is out of range or if an invalid character is encountered.
    """
    if not (2 <= src_base <= 62):
        raise ValueError(f"Source base must be between 2 and 62, got: {src_base}")

    decimal_value = 0
    for char in num_str:
        if char not in SYMBOLS:
            raise ValueError(f"Invalid character '{char}' in number string.")

        digit_value = SYMBOLS.index(char)
        if digit_value >= src_base:
            raise ValueError(
                f"Character '{char}' corresponds to value {digit_value}, "
                f"which is not valid for base {src_base}."
            )
        decimal_value = decimal_value * src_base + digit_value

    return decimal_value


def from_decimal(decimal_value: int, dst_base: int) -> str:
    """
    Convert a decimal integer `decimal_value` into a string representing the number
    in the target base `dst_base`.

    :param decimal_value: Decimal integer to be converted.
    :param dst_base:      The target base (range: 2–62).
    :return:              String representation of the number in the target base.
    :raises ValueError:   If the target base is out of range.
    """
    if not (2 <= dst_base <= 62):
        raise ValueError(f"Destination base must be between 2 and 62, got: {dst_base}")

    if decimal_value == 0:
        return "0"

    sign = ""
    if decimal_value < 0:
        sign = "-"
        decimal_value = -decimal_value

    result_chars = []
    while decimal_value > 0:
        remainder = decimal_value % dst_base
        result_chars.append(SYMBOLS[remainder])
        decimal_value //= dst_base

    return sign + "".join(reversed(result_chars))


def convert(num_str: str, src_base: int, dst_base: int) -> str:
    """
    Convert a string `num_str` from source base `src_base` to target base `dst_base`.

    :param num_str:  String representation of the number in the source base.
    :param src_base: The source base (2–62).
    :param dst_base: The target base (2–62).
    :return:         String representation of the number in the target base.
    """
    decimal_value = to_decimal(num_str, src_base)
    return from_decimal(decimal_value, dst_base)