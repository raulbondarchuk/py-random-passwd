# recursos 
# https://skillbox.ru/media/code/pishem-desktopprilozhenie-na-python-s-pomoshchyu-tkinter/

import functions # importar los ficheros con functions para dividir interface y def
import tkinter as tk # import de biblioteca Tkinter para poder usarla

from tkinter import * # Cargar los metodos de tkinter y usarlas sin necesidad de llamarlas con los enlaces
from tkinter import messagebox # import de metodo messagebox para evitar codigo duplicado

# Resto de codigo es igual

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


# FUNCTION OF BTN NUEVA CONTRASEÑA ºººººººººººººººººººººººººººººººººººººººººººººººº

# Создаем новый LabelFrame для ввода значения количества символов в новом пароле
frameInput = LabelFrame(text="Introduce valor:")
frameInput.pack(side=TOP, padx=10, pady=10)
frameInput.pack_forget()

# Создаем новый Label для текста "Valor de caracteres de nueva contraseña"
lblValorCaracteres = Label(frameInput, text="Valor de caracteres de nueva contraseña:")
lblValorCaracteres.pack(side=LEFT, padx=10, pady=10)

# Создаем новый TextBox для ввода значения количества символов в новом пароле
txtValorCaracteres = Entry(frameInput)
valueCaracteres = Entry(frameInput).get()
txtValorCaracteres.pack(side=LEFT, padx=10, pady=10)

# Создаем новую кнопку для сохранения значения количества символов в новом пароле
btnGuardar = tk.Button(frameInput, text="Guardar", bg="grey", fg="white")
btnGuardar.pack(side=LEFT, padx=10, pady=10)

# Создаем новую кнопку для отмены ввода значения количества символов в новом пароле
btnCancelar = tk.Button(frameInput, text="Cancelar", bg="grey", fg="white")
btnCancelar.pack(side=LEFT, padx=10, pady=10)

# Создаем функцию для отображения нового LabelFrame и скрытия старого
def mostrar_frame_input():
    frameInput.pack(side=TOP, padx=10, pady=10)
    btnNewPasswd.config(state="disabled", bg="white", fg="black")

    btnChangePasswd.config(state="disabled")
    btnDropPasswd.config(state="disabled")
    btnShowPasswd.config(state="disabled")
    #frameBtns.pack_forget()

# Создаем функцию для скрытия нового LabelFrame и отображения старого
def ocultar_frame_input():
    frameInput.pack_forget()
    btnNewPasswd.config(state="normal", bg="grey", fg="white")

    btnChangePasswd.config(state="normal")
    btnDropPasswd.config(state="normal")
    btnShowPasswd.config(state="normal")
    #frameBtns.pack(side=TOP, padx=10, pady=10)

# Привязываем функцию к нажатию кнопки "Generar nueva contraseña"
btnNewPasswd.config(command=mostrar_frame_input)
# Привязываем функцию к нажатию кнопки "Guardar"
btnGuardar.config(command=ocultar_frame_input)
btnGuardar.config(functions.newPasswd(valueCaracteres))
# Привязываем функцию к нажатию кнопки "Cancelar"
btnCancelar.config(command=ocultar_frame_input)

# BTN NUEVA CONTRASEÑA FIN ºººººººººººººººººººººººººººººººººººººººººººººººº

window.mainloop() # Programa no se cierre sola, usuario tiene que cerrarla 

