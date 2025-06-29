import tkinter as tk

# Definimos los diferentes calculos de valores...
def segundos_a_minutos(segundos):
    return segundos / 60

def minutos_a_horas(minutos):
    return minutos / 60

def horas_a_dias(horas):
    return horas / 24

def dias_a_semanas(dias):
    return dias / 7

def dias_a_anios(dias):
    return dias / 365

# Convertimos el resultado segun la opción elejida...
def convertir():
  try:

    valor = float(entrada.get())
    resultado = ""
    if unidad.get() == "Segundos a Minutos":
        resultado = f"{valor} segundos son {segundos_a_minutos(valor):.2f} minutos"
    elif unidad.get() == "Minutos a Horas":
        resultado = f"{valor} minutos son {minutos_a_horas(valor):.2f} horas"
    elif unidad.get() == "Horas a Días":
        resultado = f"{valor} horas son {horas_a_dias(valor):.2f} días"
    elif unidad.get() == "Días a Semanas":
        resultado = f"{valor} días son {dias_a_semanas(valor):.2f} semanas"
    elif unidad.get() == "Días a Años":
        resultado = f"{valor} días son {dias_a_anios(valor):.2f} años"
    
  except:ValueError
  etiqueta_resultado.config(text="ERROR: Debe ingresar un número")
  etiqueta_resultado.config(text=resultado)

def abrir_ventana_tiempo():
    global entrada, etiqueta_resultado, unidad
    ventana = tk.Toplevel()
    ventana.title("Conversión de Tiempo")
    ventana.geometry("300x200")

    tk.Label(ventana, text="Ingrese un valor:").pack()
    entrada = tk.Entry(ventana)
    entrada.pack()

    unidad = tk.StringVar(ventana)
    unidad.set("Segundos a Minutos")
    opciones = tk.OptionMenu(
        ventana, unidad, 
        "Segundos a Minutos", "Minutos a Horas", "Horas a Días", 
        "Días a Semanas", "Días a Años"
    )
    opciones.pack()

    # Definimos un botón para borrar los campos ingresados... 
    def borrar():
        entrada.delete(0, tk.END)
        etiqueta_resultado.config(text="")

    boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
    boton_convertir.pack()
    tk.Button(ventana, text="Borrar",command=borrar).pack()
    tk.Button(ventana, text="Salir", command=ventana.destroy).pack(pady=5) # botón de salir...

    etiqueta_resultado = tk.Label(ventana, text="")
    etiqueta_resultado.pack()