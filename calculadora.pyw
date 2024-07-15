import tkinter as tk
from tkinter import ttk

def calcular():
    try:
        cantidad_estribos = int(entry_cantidad.get())
        medida1 = float(entry_medida1.get())
        medida2 = float(entry_medida2.get())
        medida3 = float(entry_medida3.get())

        suma_medidas = medida1 + medida2 + medida3
        resultado_medidas = suma_medidas / 100

        label_resultado_medidas.config(text=f"Suma de medidas es: {resultado_medidas:.2f}")

        PxC = cantidad_estribos * resultado_medidas
        label_PxC.config(text=f"{resultado_medidas:.2f} x {cantidad_estribos:.2f}: {PxC:.2f}")

        v12 = 0.888
        v10 = 0.617
        v8 = 0.395

        resultado_v12 = PxC * v12
        resultado_v10 = PxC * v10
        resultado_v8 = PxC * v8

        label_resultado_v12.config(text=f"{PxC:.2f} * v12 (0.888): {resultado_v12:.2f}")
        label_resultado_v10.config(text=f"{PxC:.2f} * v10 (0.617): {resultado_v10:.2f}")
        label_resultado_v8.config(text=f"{PxC:.2f} * v8 (0.395): {resultado_v8:.2f}")
    except ValueError:
        label_resultado_medidas.config(text="Por favor ingrese valores válidos.")

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

def enter_key(event):
    calcular()

# Crear la ventana principal
root = tk.Tk()
root.title("Cálculo de Estribos")

# Definir una fuente más grande
font_large = ("Arial", 14)

# Crear los widgets de entrada
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Cantidad de Estribos:", font=font_large).grid(column=0, row=0, sticky=tk.W)
entry_cantidad = ttk.Entry(frame, width=10, font=font_large)
entry_cantidad.grid(column=1, row=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Primera Medida:", font=font_large).grid(column=0, row=1, sticky=tk.W)
entry_medida1 = ttk.Entry(frame, width=10, font=font_large)
entry_medida1.grid(column=1, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Segunda Medida:", font=font_large).grid(column=0, row=2, sticky=tk.W)
entry_medida2 = ttk.Entry(frame, width=10, font=font_large)
entry_medida2.grid(column=1, row=2, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Tercera Medida:", font=font_large).grid(column=0, row=3, sticky=tk.W)
entry_medida3 = ttk.Entry(frame, width=10, font=font_large)
entry_medida3.grid(column=1, row=3, sticky=(tk.W, tk.E))

# Crear botón para calcular
button_calcular = ttk.Button(frame, text="Calcular", command=calcular)
button_calcular.grid(column=1, row=4, sticky=tk.W)

# Crear etiquetas para mostrar los resultados
label_resultado_medidas = ttk.Label(frame, text="", font=font_large)
label_resultado_medidas.grid(column=0, row=5, columnspan=2, sticky=(tk.W, tk.E))

label_PxC = ttk.Label(frame, text="", font=font_large)
label_PxC.grid(column=0, row=6, columnspan=2, sticky=(tk.W, tk.E))

label_resultado_v12 = ttk.Label(frame, text="", font=font_large)
label_resultado_v12.grid(column=0, row=7, columnspan=2, sticky=(tk.W, tk.E))

label_resultado_v10 = ttk.Label(frame, text="", font=font_large)
label_resultado_v10.grid(column=0, row=8, columnspan=2, sticky=(tk.W, tk.E))

label_resultado_v8 = ttk.Label(frame, text="", font=font_large)
label_resultado_v8.grid(column=0, row=9, columnspan=2, sticky=(tk.W, tk.E))

# Configurar el redimensionamiento de las columnas
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Vincular la tecla Enter a cada campo de entrada
entry_cantidad.bind("<Return>", focus_next_widget)
entry_medida1.bind("<Return>", focus_next_widget)
entry_medida2.bind("<Return>", focus_next_widget)
entry_medida3.bind("<Return>", focus_next_widget)

# Vincular la tecla Enter al botón Calcular
button_calcular.bind("<Return>", enter_key)
root.bind("<Return>", enter_key)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()