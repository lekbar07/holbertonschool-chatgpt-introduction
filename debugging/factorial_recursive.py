#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les entiers négatifs.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <nombre_entier>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        f = factorial(number)
        print(f)
    except ValueError as e:
        print(f"Erreur : {e}")
        sys.exit(1)

