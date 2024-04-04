import random
class Inscripcion:
    @staticmethod
    def inscribir_mesero():
        nombre = input("Ingrese el nombre del mesero: ")
        id_mesero = int(input("Ingrese el ID del mesero: "))
        clave = random.randrange(0, 11)
        return {"nombre": nombre, "id": id_mesero, "clave": clave}
class Mesa:
    def __init__(self, cantidad_mesas: int) -> None:
        self.mesas = list(range(1, cantidad_mesas + 1))
    def generar_mesas(self):
        print("Mesas disponibles:", self.mesas)
    def asignar_mesa(self, num_mesa):
        if num_mesa in self.mesas:
            self.mesas.remove(num_mesa)
            print(f"La mesa {num_mesa} ha sido asignada.")
        else:
            print(f"La mesa {num_mesa} no está disponible.")
inscribir_mesero = input("¿Desea inscribir a un mesero? (Si/No): ")
mesero = None
if inscribir_mesero.lower() == "si":
    mesero = Inscripcion.inscribir_mesero()
asignar_mesas = input("¿Desea asignar mesas? (Si/No): ")
if asignar_mesas.lower() == "si":
    num_mesas = int(input("Ingrese el número de mesas del restaurante: "))
    restaurante = Mesa(num_mesas)
    restaurante.generar_mesas()
    while True:
        num_mesa = int(input("Ingrese el número de mesa que desea asignar: "))
        restaurante.asignar_mesa(num_mesa)
        continuar = input("¿Desea asignar otra mesa? (Si/No): ")
        if continuar.lower() != "si":
            break
print("Mesero inscrito:", mesero)
class Meserosquesetienen:
    meseros = [{"Juan": 516103215}, {"Carlos": 2135456654}, {"Pedro": 651564684}]
class Cuenta:
    def __init__(self, menu, mesero) -> None:
        self.menu = menu
        self.pedidos = []
        self.mesero = mesero
    def agregar_pedido(self, elemento, cantidad,mesero):
        self.mesero=str(input("Ingrese el nombre del mesero que atendio: "))
        if elemento in self.menu:
            total_elemento = self.menu[elemento] * cantidad
            self.pedidos.append({"elemento": elemento, "cantidad": cantidad, "total": total_elemento, "mesero": self.mesero})
        else:
            print(f"El elemento '{elemento}' no está en el menú.")
    def mostrar_cuenta(self):
        print("Cuenta:")
        for pedido in self.pedidos:
            print(f"Elemento: {pedido['elemento']}")
            print(f"Cantidad pedida: {pedido['cantidad']}")
            print(f"Total: {pedido['total']}")
            print(f"Mesero: {pedido['mesero']}")
menu = {"Perro": 10.000, "Sancocho": 15.000, "Frijoles": 15.000, "Casuela": 22.000, "Salchipapa": 12.000}
cuenta = Cuenta(menu, Meserosquesetienen.meseros)
while True:
    print(menu)
    elemento_pedido = input("Ingrese qué comió el cliente (o escriba 'fin' para terminar): ")
    if elemento_pedido.lower() == "fin" or elemento_pedido.lower() == "Fin":
        break
    cantidad_pedida = int(input(f"Ingrese cuántas veces se pidió '{elemento_pedido}': "))
    print(Meserosquesetienen.meseros)
    mesero = input("Ingrese el nombre del mesero que atendió: ")
    cuenta.agregar_pedido(elemento_pedido, cantidad_pedida, mesero)
cuenta.mostrar_cuenta()
