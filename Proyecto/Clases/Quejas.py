class Qjas:
    def __init__(self):
        self.quejas = []

    def ing_quejas(self, mesas):
        while True:
            queja = input("Ingrese la queja (o escriba 'fin' para terminar): ")
            if queja.lower() == 'fin':
                break
            queja_mesa = str(input("Ingrese la mesa que se quejó: "))
            if queja_mesa in mesas.mesas:
                self.quejas.append((queja, queja_mesa))
                print(f"Queja registrada: {queja} en la mesa {queja_mesa}")
            else:
                print(f"La mesa {queja_mesa} no está disponible o ya fue asignada.")
        return self.quejas
