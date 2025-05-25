import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        self.root.minsize(300, 400)

        # Variables
        self.entrada = tk.StringVar()
        self.resultado = tk.StringVar()
        self.modo_actual = tk.StringVar(value="Oscuro")
        
        # Configuración de estilos
        self.estilo = ttk.Style()
        self.configurar_tema_oscuro()
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Pantalla
        self.entrada_campo = ttk.Entry(
            self.main_frame, 
            textvariable=self.entrada,
            font=("Arial", 24),
            justify='right'
        )
        self.entrada_campo.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
        
        # Botones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        
        for (texto, fila, col) in botones:
            boton = ttk.Button(
                self.main_frame,
                text=texto,
                command=lambda t=texto: self.click_boton(t),
                style='Calc.TButton' if texto in '0123456789.' else 'Op.TButton'
            )
            boton.grid(row=fila, column=col, sticky='nsew', padx=2, pady=2)
            if texto == '=':
                boton.grid(columnspan=2)
        
        # Botón de modo
        self.boton_modo = ttk.Button(
            self.main_frame,
            text="Cambiar Modo",
            command=self.cambiar_modo,
            style='Mode.TButton'
        )
        self.boton_modo.grid(row=5, column=1, columnspan=3, sticky='nsew', padx=2, pady=2)
        
        # Hacer que los botones se expandan
        for i in range(6):
            self.main_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.main_frame.grid_columnconfigure(i, weight=1)

        # Vincular el evento de cambio de tamaño
        self.root.bind("<Configure>", self.ajustar_fuente)

    def configurar_tema_oscuro(self):
        self.root.configure(bg='#1a1a1a')
        self.estilo.configure('TFrame', background='#1a1a1a')
        self.estilo.configure('TButton', font=('Arial Black', 14, 'bold'))
        self.estilo.configure('Calc.TButton', background='#141414', foreground='#FF69B4')
        self.estilo.configure('Op.TButton', background='#141414', foreground='#00BFFF', font=('Arial', 14))
        self.estilo.configure('Mode.TButton', background='#141414', foreground='#32CD32', font=('Arial', 14))
        self.estilo.configure('TEntry', fieldbackground='#333333', foreground='#FF69B4')

    def configurar_tema_claro(self):
        self.root.configure(bg='#FFFFFF')
        self.estilo.configure('TFrame', background='#FFFFFF')
        self.estilo.configure('TButton', font=('Arial Black', 14, 'bold'))
        self.estilo.configure('Calc.TButton', background='#F0F8FF', foreground='#FF1493')
        self.estilo.configure('Op.TButton', background='#F0F8FF', foreground='#1E90FF', font=('Arial', 14))
        self.estilo.configure('Mode.TButton', background='#F0F8FF', foreground='#228B22', font=('Arial', 14))
        self.estilo.configure('TEntry', fieldbackground='white', foreground='#FF1493')

    def click_boton(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.entrada.get())
                self.entrada.set(str(resultado))
            except:
                self.entrada.set('Error')
        elif valor == 'C':
            self.entrada.set('')
        else:
            self.entrada.set(self.entrada.get() + valor)

    def cambiar_modo(self):
        if self.modo_actual.get() == "Oscuro":
            self.configurar_tema_claro()
            self.modo_actual.set("Claro")
        else:
            self.configurar_tema_oscuro()
            self.modo_actual.set("Oscuro")

    def ajustar_fuente(self, event):
        # Ajustar tamaño de fuente basado en el tamaño de la ventana
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        size = min(width // 20, height // 25)  # Aumentado el tamaño relativo
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, tk.Button):
                if widget['text'] in '0123456789.':
                    widget.configure(font=("Arial Black", size, "bold"))  # Números más gordos
                else:
                    widget.configure(font=("Arial", size))  # Operadores normales

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Calculadora()
    app.iniciar()