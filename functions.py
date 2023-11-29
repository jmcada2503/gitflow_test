def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."

resultado = dividir(10, 2)
print(resultado)