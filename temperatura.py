import tkinter as tk
from tkinter import ttk

# definimos la ventana Toplevel()...
def abrir_ventana():
    ventana = tk.Toplevel()
    ventana.title("Conversión de Temperatura")
    ventana.geometry("300x300")
# ventana emergente...
    ttk.Label(ventana, text="Ingrese temperatura en °C:").pack(pady=5)
    entrada = ttk.Entry(ventana)
    entrada.pack(pady=5)

    resultado = ttk.Label(ventana, text="")
    resultado.pack(pady=5)

# Función para convertir de °C a °F...
    def convertir_a_fahrenheit():
        try:
            temp_celsius = float(entrada.get())
            temp_fahrenheit = (temp_celsius * 9/5) + 32
            resultado.config(text=f"{temp_fahrenheit:.2f} °F")
        except ValueError:
            resultado.config(text="Entrada inválida")

# Función para convertir de °C a °kelvin...
    def convertir_a_kelvin():
        try:
            temp_celsius = float(entrada.get())
            temp_kelvin = temp_celsius + 273.15
            resultado.config(text=f"{temp_kelvin:.2f} K")
        except ValueError:
            resultado.config(text="Entrada inválida")
# Definimos un botón para borrar los campos ingresados... 
    def borrar():
        entrada.delete(0, tk.END)
        resultado.config(text="")

    ttk.Button(ventana, text="Convertir a °F", command=convertir_a_fahrenheit).pack(pady=5) # botón convertidor de °C a °F...
    ttk.Button(ventana, text="Convertir a Kelvin", command=convertir_a_kelvin).pack(pady=5) # botón convertidor de °C a °K...
    ttk.Button(ventana, text="Borrar", command=borrar).pack(pady=5) # botón de borrar...
    ttk.Button(ventana, text="Salir", command=ventana.destroy).pack(pady=5) # botón de salir...

if __name__ == "__main__":
    abrir_ventana()
