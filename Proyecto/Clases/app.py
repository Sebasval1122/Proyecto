import Meseros
import Mesas
inscribir_mesero = input("¿Desea inscribir a un mesero? (Si/No): ")
mesero = None
if inscribir_mesero.lower() == "si":
    mesero = Meseros.Inscripcion.inscribir_mesero()
asignar_mesas = input("¿Desea asignar mesas? (Si/No): ")
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
menu = {"Perro": 10.000, "Sancocho": 15.000, "Frijoles": 15.000, "Casuela": 22.000, "Salchipapa": 12.000}
cuenta = Meseros.Cuenta(menu, Meseros.Meserosquesetienen.meseros)
while True:
    print(menu)
    elemento_pedido = input("Ingrese qué comió el cliente (o escriba 'fin' para terminar): ")
    if elemento_pedido.lower() == "fin" or elemento_pedido.lower() == "Fin":
        break
    cantidad_pedida = int(input(f"Ingrese cuántas veces se pidió '{elemento_pedido}': "))
    print(Meseros.Meserosquesetienen.meseros)
    mesero = input("Ingrese el nombre del mesero que atendió: ")
    cuenta.agregar_pedido(elemento_pedido, cantidad_pedida, mesero)
cuenta.mostrar_cuenta()