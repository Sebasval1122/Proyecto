import random
import Mesas

# Capacidad
def capacidadre(mesas):
    try:
        if len(Mesas.Mesa.generar_mesas) > 30:
            mesas_2 = int(input("Cuantas son de dos personas: "))
            mesas_4 = int(input("Ingrese el número de mesas de cuatro personas: "))
            mesas_2_total = mesas_2 * 2
            mesas_4_total = mesas_4 * 4
            print(f"La cantidad de personas para mesas de dos es de: {mesas_2_total}")
            print(f"La cantidad de personas para mesas de cuatro es de: {mesas_4_total}")
    except Exception as e:
        print("Error al calcular la capacidad:", e)

# Meseros
def inscribir_mesero():
    try:
        nombre = input("Ingrese el nombre del mesero: ")
        id_mesero = int(input("Ingrese el ID del mesero: "))
        clave = random.randrange(0, 11)
        return {"nombre": nombre, "id": id_mesero, "clave": clave}
    except Exception as e:
        print("Error al inscribir mesero:", e)

# Quejas
def ing_quejas(quejas, mesas):
    try:
        while True:
            queja = input("Ingrese la queja (o escriba 'fin' para terminar): ")
            if queja.lower() == 'fin':
                break
            queja_mesa = int(input("Ingrese la mesa que se quejó: "))
            if queja_mesa in mesas.mesas:
                quejas.append((queja, queja_mesa))
                print(f"Queja registrada: {queja} en la mesa {queja_mesa}")
            else:
                print(f"La mesa {queja_mesa} no está disponible o ya fue asignada.")
        return quejas
    except Exception as e:
        print("Error al registrar queja:", e)
