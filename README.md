# base2base

**A Python library that converts numbers between any base from 2 to 62.**

[![PyPI version](https://img.shields.io/pypi/v/base2base)](https://pypi.org/project/base2base/)
[![Python versions](https://img.shields.io/pypi/pyversions/base2base)](https://pypi.org/project/base2base/)
[![License](https://img.shields.io/github/license/net-trap/base2base)](LICENSE)

## Installation

You can install **base2base** from [PyPI](https://pypi.org/) using:

```bash
pip install base2base
```

## For testing or development from source, you can clone this repository:

```bash
git clone https://github.com/net-trap/base2base.git
```
```bash
cd base2base
```
```bash
python setup.py install
```

## How to use it

```python
from base2base import convert

# Convert a binary string "101010" (base=2) to base 16
result_hex = convert("101010", 2, 16)
print(result_hex)  # "2A"

# Convert decimal 999 to base 62
result_base62 = convert("999", 10, 62)
print(result_base62)  # "g7"
```

## Additional Functions

The package also provides these functions:

```python
to_decimal(num_str: str, src_base: int) -> int
```
Converts a number string num_str from base src_base to a decimal integer.

```python
from_decimal(decimal_value: int, dst_base: int) -> str
```
Converts a decimal integer decimal_value to a string in base dst_base.
