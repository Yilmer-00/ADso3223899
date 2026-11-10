import json

class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, precio, stock):
        self.productos.append({"producto": producto, "precio": precio, "stock": stock})

    def guardar(self, archivo):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.productos, f, indent=4, ensure_ascii=False)

    def cargar(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            self.productos = json.load(f)

    def mostrar(self):
        for p in self.productos:
            print(f"- {p['producto']} | Precio: ${p['precio']} | Stock: {p['stock']}")

carrito1 = CarritoCompras()
carrito1.agregar_producto("Camisa", 45000, 2)
carrito1.agregar_producto("Gorra", 30000, 1)
carrito1.guardar("carrito.json")

carrito2 = CarritoCompras()
carrito2.cargar("carrito.json")
carrito2.mostrar()