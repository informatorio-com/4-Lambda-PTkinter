import tkinter as tk




conversiones_masa = {
    "kilogramos": 1.0,
    "gramos": 0.001,
    "miligramos": 0.000001,
    "toneladas": 1000.0,
    "libras": 0.453592,
    "onzas": 0.0283495
}

def convertir_masa(valor, unidad_origen, unidad_destino):
    # Paso 1: Convertir a la unidad base (metros)
    valor_en_kilogramos = valor * conversiones_masa[unidad_origen]

    # Paso 2: Convertir desde metros a la unidad destino
    resultado = valor_en_kilogramos / conversiones_masa[unidad_destino]

    return resultado





def abrir_ventana():
    ventana = tk.Toplevel()
    ventana.title("Conversión de Masa")
    ventana.geometry("300x420")


    tk.Label(ventana, text="Conversión de Masa", font=("Arial", 14)).pack(pady=10)
    tk.Label(ventana, text="Valor:").pack(pady=5)
    valor_entry = tk.Entry(ventana)
    valor_entry.pack(pady=5)
    tk.Label(ventana, text="Unidad de origen:").pack(pady=5)
    unidad_origen_var = tk.StringVar(ventana) # Crear una variable StringVar para la unidad de origen
    unidad_origen_var.set("gramos")  # Valor por defecto
    unidades_origen = list(conversiones_masa.keys()) # Obtener las claves del diccionario de conversiones
    unidad_origen_menu = tk.OptionMenu(ventana, unidad_origen_var, *unidades_origen) # Crear un menú desplegable con las unidades de origen.
    unidad_origen_menu.pack(pady=5)
    tk.Label(ventana, text="Unidad de destino:").pack(pady=5)
    unidad_destino_var = tk.StringVar(ventana)
    unidad_destino_var.set("kilogramos")  # Valor por defecto
    unidades_destino = list(conversiones_masa.keys())
    unidad_destino_menu = tk.OptionMenu(ventana, unidad_destino_var, *unidades_destino)
    unidad_destino_menu.pack(pady=5)
    resultado_label = tk.Label(ventana, text="Resultado: ")
    resultado_label.pack(pady=10)
    def realizar_conversion():
        try:
            valor = float(valor_entry.get())
            unidad_origen = unidad_origen_var.get()
            unidad_destino = unidad_destino_var.get()
            resultado = convertir_masa(valor, unidad_origen, unidad_destino) # Llamar a la función de conversión
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
