import tkinter as tk




conversiones_longitud = {
    "metros": 1.0,
    "kilómetros": 1000.0,
    "centímetros": 0.01,
    "milímetros": 0.001,
    "pies": 0.3048,
    "yardas": 0.9144,
    "millas": 1609.34,
    "pulgadas": 0.0254
}

def convertir_longitud(valor, unidad_origen, unidad_destino):
    # Paso 1: Convertir a la unidad base (metros)
    valor_en_metros = valor * conversiones_longitud[unidad_origen]

    # Paso 2: Convertir desde metros a la unidad destino
    resultado = valor_en_metros / conversiones_longitud[unidad_destino]

    return resultado

print(convertir_longitud(10, "kilómetros", "millas"))  # Resultado: ≈ 6.21
print(convertir_longitud(100, "pies", "metros"))       # Resultado: ≈ 30.48



def abrir_ventana():
    ventana = tk.Toplevel()
    ventana.title("Conversión de Longitud")
    ventana.geometry("300x420")


    tk.Label(ventana, text="Conversión de Longitud", font=("Arial", 14)).pack(pady=10)
    tk.Label(ventana, text="Valor:").pack(pady=5)
    valor_entry = tk.Entry(ventana)
    valor_entry.pack(pady=5)
    tk.Label(ventana, text="Unidad de origen:").pack(pady=5)
    unidad_origen_var = tk.StringVar(ventana) # Crear una variable StringVar para la unidad de origen
    unidad_origen_var.set("metros")  # Valor por defecto
    unidades_origen = list(conversiones_longitud.keys()) # Obtener las claves del diccionario de conversiones
    unidad_origen_menu = tk.OptionMenu(ventana, unidad_origen_var, *unidades_origen) # Crear un menú desplegable con las unidades de origen.
    unidad_origen_menu.pack(pady=5)
    tk.Label(ventana, text="Unidad de destino:").pack(pady=5)
    unidad_destino_var = tk.StringVar(ventana)
    unidad_destino_var.set("kilómetros")  # Valor por defecto
    unidades_destino = list(conversiones_longitud.keys())
    unidad_destino_menu = tk.OptionMenu(ventana, unidad_destino_var, *unidades_destino)
    unidad_destino_menu.pack(pady=5)
    resultado_label = tk.Label(ventana, text="Resultado: ")
    resultado_label.pack(pady=10)
    def realizar_conversion():
        try:
            valor = float(valor_entry.get())
            unidad_origen = unidad_origen_var.get()
            unidad_destino = unidad_destino_var.get()
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino) # Llamar a la función de conversión
            resultado_label.config(text=f"Resultado: {resultado:.2f} {unidad_destino}") # Formatear el resultado a 2 decimales
        except ValueError:
            resultado_label.config(text="Error: Valor no válido")
    tk.Button(ventana, text="Convertir", command=realizar_conversion).pack(pady=10)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=5)
    ventana.grab_set()  # Capturar eventos de la ventana
    ventana.focus_set()  # Enfocar la ventana
    ventana.protocol("WM_DELETE_WINDOW", ventana.destroy)  # Manejar el cierre de la ventana
     # Iniciar el bucle de eventos de la ventana
# Nota: La función abrir_ventana() se puede llamar desde el botón correspondiente en el módulo principal.
# Esto asegura que la ventana de conversión de longitud se abra correctamente.



