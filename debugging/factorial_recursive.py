#!/usr/bin/python3
"""
Script de calcul de factorielle.

Ce script calcule la factorielle d'un nombre entier positif fourni en argument 
de ligne de commande.

Usage:
    python3 factorial.py <nombre>

Arguments:
    nombre (int): Un entier positif dont on veut calculer la factorielle

Retourne:
    Affiche le résultat de la factorielle

Exemples:
    $ python3 factorial.py 5
    120
    
    $ python3 factorial.py 0
    1
"""

import sys

def factorial(n):
    """
    Calcule la factorielle d'un nombre entier positif.
    
    La factorielle de n (notée n!) est le produit des nombres entiers positifs
    inférieurs ou égaux à n. Par convention, 0! = 1.
    
    Args:
        n (int): Le nombre dont on veut calculer la factorielle
        
    Returns:
        int: La factorielle de n
        
    Raises:
        RecursionError: Si n est trop grand et cause un dépassement de pile
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Vérifie qu'un argument a été fourni
if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <nombre>")
    sys.exit(1)

try:
    # Convertit l'argument en entier et calcule la factorielle
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Erreur: veuillez fournir un nombre entier valide")
except RecursionError:
    print("Erreur: nombre trop grand, dépassement de pile")
