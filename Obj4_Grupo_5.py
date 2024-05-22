from tkinter import *
from tkinter import messagebox

def crear_ventana_login():
    root = Tk()
    root.title("Login grupo 5")
    root.geometry("300x130")
    root.resizable(0,0)
    #root.iconbitmap("icono.ico")
    root.config(bg="steelblue")
    return root

def crear_frame(root):
    frame = Frame(root)
    frame.configure(bg="steelblue")
    frame.pack(fill="both")
    return frame

def crear_label(contenedor, texto, fila, columna, padx=0, pady=0, posicion=""):
    label = Label(contenedor ,text=texto)
    label.grid(row=fila, column=columna, padx=padx, pady=pady, sticky=posicion)
    return label

def crear_input(contenedor, fila, columna, padx=0, pady=0, posicion="", texto_a_mostrar=""):
    input = Entry(contenedor, show=texto_a_mostrar)
    input.grid(row=fila, column=columna, padx=padx, pady=pady, sticky=posicion)
    return input

def crear_boton(contenedor, texto, funcion, fila, columna, padx=0, pady=0, posicion=""):
    boton = Button(contenedor, text=texto, command=funcion)
    boton.grid(row=fila, column=columna, padx=padx, pady=pady, sticky=posicion)
    return boton


def obtener_usuarios_claves():
    ALUMNOS = {'Valentin' : "1234", 'Omar': "2030", 'Agustina': "4321", 'Patricio' : "0000", 'Joel': "7777"}
    return ALUMNOS


def validacion_datos(key, clave):
    ALUMNOS = obtener_usuarios_claves()
    datos_validos = True

    try: 
        contraseña = ALUMNOS[key]
        if contraseña != clave:
            datos_validos = False
    except KeyError:
        datos_validos = False

    return datos_validos


def mostrar_mensaje(booleano):
    if booleano:
        messagebox.showinfo("Exito","Usuario y Clave Correctos")
    else:
        messagebox.showerror("Error","Alguno de los datos ingresados es incorrecto")

def verificar(usuario, clave):
    datos_validos= validacion_datos(usuario, clave)
    mostrar_mensaje(datos_validos)


def main():
    root = crear_ventana_login()
    login_frame = crear_frame(root)

    label_user = crear_label(login_frame, "Usuario Alumno:", fila=0, columna=0, padx=5, pady=5, posicion="w")
    input_user = crear_input(login_frame, fila=0, columna=1, padx=5, pady=5)

    label_clave = crear_label(login_frame, "Clave:", fila=1, columna=0, padx=5, pady=5, posicion="w")
    input_clave = crear_input(login_frame, fila=1, columna=1, padx=5, pady=5, texto_a_mostrar="*")

    boton_enviar = crear_boton(login_frame, fila=2, columna=1, pady= 30, texto="Ingresar", funcion= lambda: verificar(input_user.get(), input_clave.get()))
    boton_enviar.config(bg="lightblue", cursor="hand2")

    root.mainloop()

main()

