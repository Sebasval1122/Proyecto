import Meseros
import Mesas
import Venta
import Capacidad
import Quejas
import Exep

class App:
    def __init__(self):
        self.meseros = []
        self.restaurante = None
        self.menu = {
            "Perro": 10000,
            "Sancocho": 15000,
            "Frijoles": 15000,
            "Casuela": 22000,
            "Salchipapa": 12000
        }
        self.cuenta = Meseros.Cuenta(self.menu, self.meseros)
        self.analizador_ventas = Venta.AnalizadorVentas()

    def inscribir_mesero(self, mesero):
        self.meseros.append(mesero['nombre'])

    def asignar_mesas(self, num_mesas):
        self.restaurante = Mesas.Mesa(num_mesas)
        self.restaurante.generar_mesas()

    def agregar_pedido(self, elemento_pedido, cantidad_pedida, mesero_nombre):
        if mesero_nombre in self.meseros:
            self.cuenta.agregar_pedido(elemento_pedido, cantidad_pedida)
            self.analizador_ventas.agregar_venta(mesero_nombre, self.menu[elemento_pedido] * cantidad_pedida)
        else:
            print("Mesero no registrado")

    def ingresar_queja(self, queja, queja_mesa):
        if self.restaurante:
            qjas = Quejas.Qjas()
            if queja_mesa in self.restaurante.mesas:
                qjas.ing_quejas(queja, queja_mesa)
            else:
                print(f"La mesa {queja_mesa} no está disponible o ya fue asignada.")
        else:
            print("No se han asignado mesas, no se pueden registrar quejas.")
