Ventas = [45000, 120000, 8000, 300000]
with open("Ventas.txt", "w", encoding="utf-8") as f:

    for nombre in Ventas:

        f.write(str(nombre) + "\n")

with open("Ventas.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        print(i, linea.strip())
