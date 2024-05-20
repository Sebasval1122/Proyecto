import Meseros
import Mesas
import Venta
import Quejas
import Exep  

# Función para inscribir mesero
def inscribir_mesero():
    inscribir_mesero = input("¿Desea inscribir a un mesero? (Si/No): ")
    if inscribir_mesero.lower() == "si":
        return Exep.inscribir_mesero()
    return None

# Lista para guardar los nombres de los meseros registrados
meseros = []
mesero = inscribir_mesero()
if mesero:
    meseros.append(mesero['nombre'])

# Asignación de mesas
asignar_mesas = input("¿Desea asignar mesas? (Si/No): ")
restaurante = None
if asignar_mesas.lower() == "si":
    num_mesas = int(input("Ingrese el número de mesas del restaurante: "))
    restaurante = Mesas.Mesa(num_mesas)
    restaurante.generar_mesas()
    while True:
        num_mesa = int(input("Ingrese el número de mesa que desea asignar: "))
        restaurante.asignar_mesa(num_mesa)
        continuar = input("¿Desea asignar otra mesa? (Si/No): ")
        if continuar.lower() != "si":
            break
print("Mesero inscrito:", mesero)

# Capacidad del restaurante
if restaurante is not None:
    Exep.capacidadre(restaurante)

# Cuenta
menu = {"Perro": 10.000, "Sancocho": 15.000, "Frijoles": 15.000, "Casuela": 22.000, "Salchipapa": 12.000}
cuenta = Meseros.Cuenta(menu, Meseros.Meserosquesetienen.meseros)
analizador_ventas = Venta.AnalizadorVentas()

while True:
    print(menu)
    elemento_pedido = input("Ingrese qué comió el cliente (o escriba 'fin' para terminar): ")
    if elemento_pedido.lower() == "fin":
        break
    cantidad_pedida = int(input(f"Ingrese cuántas veces se pidió '{elemento_pedido}': "))
    print("Meseros disponibles:", meseros)
    mesero_nombre = mesero['nombre'] if mesero else input("Ingrese el nombre del mesero que atendió: ")
    if mesero_nombre not in meseros:
        print("Mesero no registrado. Por favor inscriba al mesero primero.")
        continue
    cuenta.agregar_pedido(elemento_pedido, cantidad_pedida)  # Llamada con el número correcto de argumentos
    analizador_ventas.agregar_venta(mesero_nombre, menu[elemento_pedido] * cantidad_pedida)

cuenta.mostrar_cuenta()
analizador_ventas.mostrar_ventas()

# Quejas
quejas = input("¿Desea ingresar una queja (Si/No): ")
if quejas.lower() == "si":
    if restaurante is not None:
        qjas = Quejas.Qjas()
        Exep.ing_quejas(qjas, restaurante)
    else:
        print("No se han asignado mesas, no se pueden registrar quejas.")