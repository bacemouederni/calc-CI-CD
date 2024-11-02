"""
La librairie calc permet de faire les opérations basiques de calcul entre deux entiers.
"""

def add(arg1: int, arg2: int) -> int:
    try:
        return int(arg1) + int(arg2)
    except ValueError: 
        return "Erreur : Vous devez entrer deux entiers."

def sous(arg1: int, arg2: int) -> int:
    try:
        return int(arg1) - int(arg2)
    except ValueError: 
        return "Erreur : Un des arguments n'est pas un entier."

def mult(arg1: int, arg2: int) -> int:
    try:
        return int(arg1) * int(arg2)
    except ValueError: 
        return "Erreur : Un des arguments n'est pas un entier."

def div(arg1: int, arg2: int) -> float:
    try:
        return int(arg1) / int(arg2)
    except ValueError: 
        return "Erreur : Un des arguments n'est pas un entier."
    except ZeroDivisionError:
        return "Erreur : Vous ne pouvez pas diviser par 0."

def modulo(arg1: int, arg2: int) -> int:
    try:
        return int(arg1) % int(arg2)
    except ValueError:
        return "Erreur : Un des arguments n'est pas un entier."

def ope(operateur: str, arg1: int, arg2: int):
    if operateur == '+':
        return add(arg1, arg2)        
    elif operateur == '%':
        return modulo(arg1, arg2)
    elif operateur == '-':
        return sous(arg1, arg2)
    elif operateur == 'x' or operateur == '*':
        return mult(arg1, arg2)
    elif operateur == '/':
        return div(arg1, arg2)
    else:
        return f"Erreur : L'opérateur '{operateur}' n'est pas reconnu."
