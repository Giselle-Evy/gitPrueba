import tkinter as tk
from tkinter import ttk

# Función para realizar las operaciones
def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except Exception as e:
        resultado.set("Error")

# Función para cambiar entre modos oscuro y claro
def cambiar_modo():
    if estilo_actual.get() == "Oscuro":
        root.configure(bg="white")
        estilo.configure("TButton", background="white", foreground="black")
        estilo.configure("TLabel", background="white", foreground="black")
        estilo_actual.set("Claro")
    else:
        root.configure(bg="black")
        estilo.configure("TButton", background="black", foreground="white")
        estilo.configure("TLabel", background="black", foreground="white")
        estilo_actual.set("Oscuro")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")

# Variables
entrada = tk.StringVar()
resultado = tk.StringVar()
estilo_actual = tk.StringVar(value="Oscuro")

# Estilo
estilo = ttk.Style()
root.configure(bg="black")
estilo.configure("TButton", background="black", foreground="white")
estilo.configure("TLabel", background="black", foreground="white")

# Entrada
entrada_campo = ttk.Entry(root, textvariable=entrada, font=("Arial", 20))
entrada_campo.pack(pady=10, padx=10, fill="x")

# Botón de calcular
boton_calcular = ttk.Button(root, text="Calcular", command=calcular)
boton_calcular.pack(pady=10)

# Resultado
resultado_label = ttk.Label(root, textvariable=resultado, font=("Arial", 20))
resultado_label.pack(pady=10)

# Botón para cambiar de modo
boton_modo = ttk.Button(root, text="Cambiar Modo", command=cambiar_modo)
boton_modo.pack(pady=10)

root.mainloop()