def dividir_seguro(a, b):
    if b == 0:
        print("Aviso: No se puede dividir entre cero.")
        return None
    return a / b

print(dividir_seguro(10, 2))
print(dividir_seguro(5, 0))