import qrcode

class GeneradorQR:
    def generar_qr(self, lista_alimentos, nombre_archivo="codigo_qr.png"):
        texto = "\n".join(lista_alimentos)
        img = qrcode.make(texto)
        img.save(nombre_archivo)

alimentos = ["Perro", "Sancocho", "Frijoles", "Casuela", "Salchipapa"]
generador_qr = GeneradorQR()
generador_qr.generar_qr(alimentos, "menu_restaurante_qr.png")