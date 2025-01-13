#!/usr/bin/python3
import sys

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # This was the missing decrement
    return result

try:
    if len(sys.argv) < 2:
        raise IndexError("Please provide a number as command line argument")
    f = factorial(int(sys.argv[1]))
    print(f)
except (ValueError, TypeError, IndexError) as e:
    print(f"Error: {e}", file=sys.stderr)
