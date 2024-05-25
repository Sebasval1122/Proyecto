import random
class Inscripcion:
    def inscribir_mesero():
        nombre = input("Ingrese el nombre del mesero: ")
        id_mesero = int(input("Ingrese el ID del mesero: "))
        clave = random.randrange(0, 11)
        return {"nombre": nombre, "id": id_mesero, "clave": clave}
class Meserosquesetienen:
    meseros = [{"Juan": 516103215}, {"Carlos": 2135456654}, {"Pedro": 651564684}].append(Inscripcion.inscribir_mesero)
class Cuenta:
    def __init__(self, menu, meseros):
        self.menu = menu
        self.meseros = meseros
        self.pedidos = []

    def agregar_pedido(self, elemento_pedido, cantidad_pedida):
        self.pedidos.append((elemento_pedido, cantidad_pedida))
        print(f"Pedido agregado: {cantidad_pedida} x {elemento_pedido}")
