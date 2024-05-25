import tkinter as tk
from tkinter import messagebox
from app import App

class RestauranteGUI:
    def __init__(self, root):
        self.app = App()
        self.root = root
        self.root.title("Restaurante")

        # Frame para la inscripción de meseros
        self.frame_mesero = tk.Frame(root)
        self.frame_mesero.pack(pady=10)

        self.label_mesero = tk.Label(self.frame_mesero, text="Nombre del Mesero:")
        self.label_mesero.pack(side=tk.LEFT)
        self.entry_mesero = tk.Entry(self.frame_mesero)
        self.entry_mesero.pack(side=tk.LEFT)
        self.button_inscribir_mesero = tk.Button(self.frame_mesero, text="Inscribir Mesero", command=self.inscribir_mesero)
        self.button_inscribir_mesero.pack(side=tk.LEFT)

        # Frame para la asignación de mesas
        self.frame_mesas = tk.Frame(root)
        self.frame_mesas.pack(pady=10)

        self.label_mesas = tk.Label(self.frame_mesas, text="Número de Mesas:")
        self.label_mesas.pack(side=tk.LEFT)
        self.entry_mesas = tk.Entry(self.frame_mesas)
        self.entry_mesas.pack(side=tk.LEFT)
        self.button_asignar_mesas = tk.Button(self.frame_mesas, text="Asignar Mesas", command=self.asignar_mesas)
        self.button_asignar_mesas.pack(side=tk.LEFT)

        # Frame para agregar pedidos
        self.frame_pedido = tk.Frame(root)
        self.frame_pedido.pack(pady=10)

        self.label_pedido = tk.Label(self.frame_pedido, text="Elemento Pedido:")
        self.label_pedido.pack(side=tk.LEFT)
        self.entry_pedido = tk.Entry(self.frame_pedido)
        self.entry_pedido.pack(side=tk.LEFT)

        self.label_cantidad = tk.Label(self.frame_pedido, text="Cantidad:")
        self.label_cantidad.pack(side=tk.LEFT)
        self.entry_cantidad = tk.Entry(self.frame_pedido)
        self.entry_cantidad.pack(side=tk.LEFT)

        self.label_mesero_pedido = tk.Label(self.frame_pedido, text="Mesero:")
        self.label_mesero_pedido.pack(side=tk.LEFT)
        self.entry_mesero_pedido = tk.Entry(self.frame_pedido)
        self.entry_mesero_pedido.pack(side=tk.LEFT)

        self.button_agregar_pedido = tk.Button(self.frame_pedido, text="Agregar Pedido", command=self.agregar_pedido)
        self.button_agregar_pedido.pack(side=tk.LEFT)

        # Frame para ingresar quejas
        self.frame_queja = tk.Frame(root)
        self.frame_queja.pack(pady=10)

        self.label_queja = tk.Label(self.frame_queja, text="Ingrese la queja:")
        self.label_queja.pack(side=tk.LEFT)
        self.entry_queja = tk.Entry(self.frame_queja)
        self.entry_queja.pack(side=tk.LEFT)

        self.label_queja_mesa = tk.Label(self.frame_queja, text="Mesa que se quejó:")
        self.label_queja_mesa.pack(side=tk.LEFT)
        self.entry_queja_mesa = tk.Entry(self.frame_queja)
        self.entry_queja_mesa.pack(side=tk.LEFT)

        self.button_ingresar_queja = tk.Button(self.frame_queja, text="Ingresar Queja", command=self.ingresar_queja)
        self.button_ingresar_queja.pack(side=tk.LEFT)

        # Frame para generar QR del menú
        self.frame_qr = tk.Frame(root)
        self.frame_qr.pack(pady=10)

        self.button_generar_qr = tk.Button(self.frame_qr, text="Generar QR del Menú", command=self.generar_menu_qr)
        self.button_generar_qr.pack(side=tk.LEFT)

        # Frame para mostrar el mesero con más ventas
        self.frame_mas_ventas = tk.Frame(root)
        self.frame_mas_ventas.pack(pady=10)

        self.button_mas_ventas = tk.Button(self.frame_mas_ventas, text="Mesero con más ventas", command=self.mesero_con_mas_ventas)
        self.button_mas_ventas.pack(side=tk.LEFT)

    def inscribir_mesero(self):
        nombre_mesero = self.entry_mesero.get()
        if nombre_mesero:
            mesero = {'nombre': nombre_mesero, 'id': 0, 'clave': 0}  # Simplificación
            self.app.inscribir_mesero(mesero)
            messagebox.showinfo("Inscripción", f"Mesero {nombre_mesero} inscrito exitosamente.")
        else:
            messagebox.showerror("Error", "Debe ingresar un nombre de mesero.")

    def asignar_mesas(self):
        try:
            num_mesas = int(self.entry_mesas.get())
            self.app.asignar_mesas(num_mesas)
            messagebox.showinfo("Asignación de Mesas", f"Se han asignado {num_mesas} mesas.")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número válido de mesas.")

    def agregar_pedido(self):
        elemento_pedido = self.entry_pedido.get()
        try:
            cantidad_pedida = int(self.entry_cantidad.get())
            mesero_nombre = self.entry_mesero_pedido.get()
            self.app.agregar_pedido(elemento_pedido, cantidad_pedida, mesero_nombre)
            messagebox.showinfo("Pedido", f"Pedido de {cantidad_pedida} {elemento_pedido}(s) agregado.")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar una cantidad válida.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ingresar_queja(self):
        queja = self.entry_queja.get()
        queja_mesa = self.entry_queja_mesa.get()
        try:
            self.app.ingresar_queja(queja, queja_mesa)
            messagebox.showinfo("Queja", f"Queja registrada para la mesa {queja_mesa}.")
        except Exception as e:
            messagebox.showerror("Error al registrar queja", str(e))

    def generar_menu_qr(self):
        try:
            self.app.generar_menu_qr()
            messagebox.showinfo("QR Generado", "Código QR del menú generado y guardado como menu_restaurante_qr.png")
        except Exception as e:
            messagebox.showerror("Error al generar QR", str(e))

    def mesero_con_mas_ventas(self):
        try:
            mesero = self.app.mesero_con_mas_ventas()
            messagebox.showinfo("Mesero con más ventas", f"El mesero con más ventas es: {mesero}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteGUI(root)
    root.mainloop()
