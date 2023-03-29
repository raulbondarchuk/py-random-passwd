# recursos 
# https://skillbox.ru/media/code/pishem-desktopprilozhenie-na-python-s-pomoshchyu-tkinter/

import functions # importar los ficheros con functions para dividir interface y def
import tkinter as tk # import de biblioteca Tkinter para poder usarla

from tkinter import * # Cargar los metodos de tkinter y usarlas sin necesidad de llamarlas con los enlaces
from tkinter import messagebox # import de metodo messagebox para evitar codigo duplicado

window = Tk() # crear la ventana de aplicacion
window.title("Password Generator") # Nombre de la aplicacion

# Tamaños DISPLAY
weightDisplay = window.winfo_screenwidth() # devuelve ancho del display pc 
heightDisplay = window.winfo_screenheight() # devuelve alto del display pc

# Tamaños VENTANA
weightWindow = weightDisplay // 1.5
heightWindow = heightDisplay // 1.5

x = int((weightDisplay - weightWindow) // 2) # Calcular la posición para centrar la ventana
y = int((heightDisplay - heightWindow) // 2 )# Calcular la posición para centrar la ventana

window.geometry("{}x{}+{}+{}".format(int(weightWindow), int(heightWindow), x, y)) # Fin de centrarnos la ventana

# crear el contenedor
frameBtns = LabelFrame(text="Gestión de la contraseña", width = (weightWindow * 0.95), height = (heightWindow * 0.15))
frameBtns.pack(side=TOP) # Alinear LabelFrame vertical

# Crear Buttons
btnNewPasswd = tk.Button(frameBtns, text="Generar nueva contraseña", bg="grey",fg="white")
btnChangePasswd = tk.Button(frameBtns, text="Cambiar la contraseña", bg="grey",fg="white")
btnDropPasswd = tk.Button(frameBtns,text="Borrar la contraseña", bg="grey",fg="white")
btnShowPasswd = tk.Button(frameBtns, text="Mostrar la contraseña actual", bg="grey",fg="white")

# Centrar HORIZONTAL
btnNewPasswd.pack(side=tk.LEFT, padx=10, pady=10, ipadx=10, ipady=5)
btnChangePasswd.pack(side=tk.LEFT, padx=10, pady=10, ipadx=10, ipady=5)
btnDropPasswd.pack(side=tk.LEFT, padx=10, pady=10, ipadx=10, ipady=5)
btnShowPasswd.pack(side=tk.LEFT, padx=10, pady=10, ipadx=10, ipady=5)



window.mainloop() #Programa no se cierre sola, usuario tiene que cerrarla 