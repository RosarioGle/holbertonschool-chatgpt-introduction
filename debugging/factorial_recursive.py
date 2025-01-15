#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("La factorielle n'est définie que pour les nombres positifs")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: ./script.py <nombre>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    f = factorial(n)
    print(f)
except ValueError as e:
    print(f"Erreur: {e}")
