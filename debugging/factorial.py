#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémentation de n pour éviter la boucle infinie
    return result

# Vérification si un argument a été passé au script
if len(sys.argv) < 2:
    print("Usage: python3 factorial.py <number>")
    sys.exit(1)

# Vérification si l'argument est un entier valide
try:
    f = factorial(int(sys.argv[1]))
    print(f)  # Affichage du résultat
except ValueError:
    print("Veuillez fournir un entier valide.")
    sys.exit(1)
