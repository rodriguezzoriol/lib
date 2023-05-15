# funcions_math.py

import math

def suma(a, b):
    """Retorna la suma de dos nombres."""
    return a + b

def resta(a, b):
    """Retorna la resta de dos nombres."""
    return a - b

def multiplicacio(a, b):
    """Retorna el producte de dos nombres."""
    return a * b

def divisio(a, b):
    """Retorna la divisió de dos nombres."""
    if b == 0:
        return "Error: no es pot dividir per zero."
    else:
        return a / b

def arrel_quadrada(a):
    """Retorna l'arrel quadrada d'un nombre."""
    if a < 0:
        return "Error: l'arrel quadrada de nombres negatius no existeix."
    else:
        return math.sqrt(a)
