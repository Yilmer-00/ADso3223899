while True:
    try:
        numero = float(input("Número: "))
        break
    except ValueError:
        print("Eso no es un número")
print("Recibí:", numero)
