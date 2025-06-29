import tkinter as tk

# Importamos los módulos de cada integrante del equipo
import longitud
from temperatura import abrir_ventana_temp
from tiempo import abrir_ventana_tiempo
import masa

def main():
    root = tk.Tk()
    root.title("Conversor de Unidades")
    root.geometry("400x300")
    
    tk.Label(root, text="Conversor de Unidades", font=("Arial", 16)).pack(pady=10)

    # Botones para abrir cada submódulo
    tk.Button(root, text="Conversión de Longitud", command=longitud.abrir_ventana).pack(pady=10)

    tk.Button(root, text="Conversión de Masa", command=masa.abrir_ventana).pack(pady=10)
    
    tk.Button(root, text="Conversión de Temperatura", command=abrir_ventana_temp).pack(pady=10)

    tk.Button(root, text="Conversión de tiempo", command=abrir_ventana_tiempo).pack(pady=10)


    tk.Label(root, text="© Proyecto para el Informatorio", font=("Arial", 10)).pack(side="bottom", pady=10)

    

    root.mainloop()

if __name__ == "__main__":
    main()