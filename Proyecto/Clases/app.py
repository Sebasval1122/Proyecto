import Meseros
import Mesas
import Venta
import Capacidad
import Quejas
import Exep
from QR import GeneradorQR

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
        self.generador_qr = GeneradorQR()

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

    def generar_menu_qr(self):
        lista_alimentos = list(self.menu.keys())
        self.generador_qr.generar_qr(lista_alimentos, "menu_restaurante_qr.png")
        print("Código QR del menú generado y guardado como menu_restaurante_qr.png")

    def mesero_con_mas_ventas(self):
        return self.analizador_ventas.mesero_con_mas_ventas()
