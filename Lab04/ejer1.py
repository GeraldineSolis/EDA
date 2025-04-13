def reverse_string(input_string):
    # Crear una pila
    stack = []

    for char in input_string:
        stack.append(char)

    
    reversed_string = '' 
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Ejemplo de uso
original_string = "Hola Mundo"
reversed_version = reverse_string(original_string)
print(f"Cadena original: {original_string}")
print(f"Cadena invertida: {reversed_version}")