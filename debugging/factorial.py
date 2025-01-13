#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Le factoriel n'est pas défini pour les nombres négatifs.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Corrige la boucle infinie
    return result

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Veuillez fournir un seul argument entier positif.")
        
        # Convertir l'argument en entier
        n = int(sys.argv[1])
        
        # Calculer et afficher le factoriel
        f = factorial(n)
        print(f"Le factoriel de {n} est {f}")
    
    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
