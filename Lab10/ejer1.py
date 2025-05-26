# -*- coding: utf-8 -*-

def infix_to_postfix(tokens):
    # Reglas de fuerza de los signos
    fuerza = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    resultado = []  # Aquí va el resultado final
    pila = []       # Aquí guardamos los signos

    for token in tokens:
        if token.isalnum():  # Si es letra o número
            resultado.append(token)
        elif token in fuerza:  # Si es un signo
            while pila and pila[-1] in fuerza and fuerza[pila[-1]] >= fuerza[token]:
                resultado.append(pila.pop())
            pila.append(token)
        elif token == '(':  # Si es paréntesis abierto
            pila.append(token)
        elif token == ')':  # Si es paréntesis cerrado
            while pila and pila[-1] != '(':
                resultado.append(pila.pop())
            pila.pop()  # Sacamos el '('

    # Sacamos lo que quede en la pila
    while pila:
        resultado.append(pila.pop())

    return resultado

print(infix_to_postfix(['2', '+', '3']))  # ➜ ['2', '3', '+']
print(infix_to_postfix(['2', '+', '3', '*', '4']))  # ➜ ['2', '3', '4', '*', '+']
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']))  # ➜ ['2', '3', '+', '4', '*']
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']))  # ➜ ['1', '2', '+', '3', '4', '-', '*']
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']))  # ➜ ['a', 'b', 'c', '*', 'd', '/', '+']
