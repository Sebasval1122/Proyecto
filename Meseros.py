import random
class Inscripcion:
    ins = str(input("Desea ingresar al mesero: "))
    def __init__(self, nombre: str, id: int, clave: int,meseros) -> None:
        self.nombre = nombre
        self.id = id
        self.clave = clave
        self.meseros=[]
    if ins=="Si":
        nombre=str(input("Ingrese el Nombre: "))
        id=int(input("Ingrese el id: "))
        clave=random.randrange(0,11)
    def inscri (self,nombre,id,clave):
        self.meseros.append(nombre,id,clave)
class Mesa:
    def __init__(self, mesas: int) -> None:
        self.mesa = list(range(1, mesas + 1))
        
    def generar_mesas(self):
        print(self.mesa)
    
num_mesas = int(input("Ingrese el número de mesas del restaurante: "))
restaurante = Mesa(num_mesas)
restaurante.generar_mesas()
asignar=str(input("Desea asignar mesas Si/No: "))
if asignar=="Si":
        asig=int(input("Que mesa desea asignar: "))
        print("La mesa asignada es: ",asig)
class Cuenta:
    def __init__(self, menu) -> None:
        self.menu = menu
        self.pedidos = []
    def agregar_pedido(self, elemento, cantidad):
        if elemento in self.menu:
            total_elemento = self.menu[elemento] * cantidad
            self.pedidos.append({"elemento": elemento, "cantidad": cantidad, "total": total_elemento})
        else:
            print(f"El elemento '{elemento}' no está en el menú.")
    def mostrar_cuenta(self):
        print("Cuenta:")
        for pedido in self.pedidos:
            print(f"Elemento: {pedido['elemento']}")
            print(f"Cantidad pedida: {pedido['cantidad']}")
            print(f"Total: {pedido['total']}")
            print("-" * 20)
menu = {"Perro": 10.000, "Sancocho": 15.000, "Frijoles": 15.000, "Casuela": 22.000, "Salchipapa": 12.000}
cuenta = Cuenta(menu)
while True:
    elemento_pedido = input("Ingrese qué comió el cliente (o escriba 'fin' para terminar): ")
    if elemento_pedido.lower() == "fin":
        break
    cantidad_pedida = int(input(f"Ingrese cuántas veces se pidió '{elemento_pedido}': "))
    cuenta.agregar_pedido(elemento_pedido, cantidad_pedida)
cuenta.mostrar_cuenta()
print(Inscripcion.inscri)