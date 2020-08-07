from tkinter import *
from tkinter import font
import os
import os.path


# ------------------ Logica del Programa (Funciones y Clases)-----------------
def eliminar_cadena():
    url = rutaC.get()
    m = textoE.get()    
    #print("ruta = "+ rutaC.get())
    
    if len(m)>0 and m != " " and len(url)>0 and url != " ":
        try:
            archivos = os.listdir(url)
            for x in archivos:
                indice_inicial=x.find(m)
                if indice_inicial!=-1:
                    ruta_archivo = url+"\\"+x
                    cadena_nueva=x.replace(m,textoR.get())
                    cadena_nueva = url + "\\" +cadena_nueva
                    os.rename(ruta_archivo,cadena_nueva)
            label_advertencia.config(text="Operacion realizada con exito.")
            label_advertencia.config(fg="green")
            pass
        except:
            #print ("Unexpected error:"+ e)
            label_advertencia.config(text="La carpeta no existe :( o nombres archivo duplicados")
            label_advertencia.config(fg="red")
            pass        
        pass       
    else:
        label_advertencia.config(text="Debe Ingreserar una Frase a Eliminar y una Direccion Valida")
        label_advertencia.config(fg="red")
        pass

def agregar_cadena():
    #print("Hola mundo"+ variable_tk.get())
    lugarI = variable_tk.get()
    cadenaA = textoA.get()
    url = rutaC.get()

    if len(cadenaA)>0 and cadenaA != " " and len(url)>0 and url != " ":
        try:
            archivos=os.listdir(url)
            for x in archivos:
                ruta_original = url +"\\"+ x
                nombreNuevo = ""
                if os.path.isfile(ruta_original):
                    indice = x.rfind(".") # encuentra el ultimo indice del punto
                    extension = x[indice:]
                    nombre = x[0:indice]
                    #aqui comprobaremos si es al inicio o al final la insercion
                    if lugarI =="Inicio":
                        nombreNuevo = cadenaA + nombre + extension
                        pass
                    else:
                        nombreNuevo = nombre + cadenaA + extension
                        pass
                    pass
                else:
                    if lugarI =="Inicio":
                        nombreNuevo = cadenaA + x
                        pass
                    else:
                        nombreNuevo = x + cadenaA
                        pass
                    pass  
                os.rename(ruta_original, url+'\\'+nombreNuevo)
            label_advertencia2.config(text="Operacion realizada con exito.")
            label_advertencia2.config(fg="green")
            pass
        except:
            label_advertencia2.config(text="Error! Debe Ingreserar una direccion de carpeta Valida")
            label_advertencia2.config(fg="red")
            pass
        
        pass
    else:
        label_advertencia2.config(text="Debe Ingreserar una Frase a Agregar y una Direccion Valida")
        label_advertencia2.config(fg="red")
        pass
    pass

# ------------------ Configuracion de Raiz ---------------------
raiz = Tk()
raiz.title("Anres Software")
raiz.iconbitmap("logo.ico")

# ------------------- Definicion Tipografias a Utilizar ------
tipografia_titulo = font.Font(family='Helvetica', size=12, weight='bold')

# ------------------- Configuracion de Frame -------------------
miFrame = Frame(raiz,width="650",height="400")
miFrame.config(bg="#E7DBAA")
miFrame.pack(fill="both", expand="true") 

# ------------------ Elementos de la ventana -----------
# ***** Seccion Reemplazar Cadenas de los Nombres ****
titulo = Label(miFrame, text="Remplazar Frases de los Nombres")
titulo.grid(pady=5, row=0, column=0, columnspan=2)
titulo.config(bg="#E7DBAA", font=tipografia_titulo)

Label(miFrame, text="Ruta de Carpeta:", bg="#E7DBAA").grid(pady=5, row=1, column=0)
Label(miFrame, text="Texto a Eliminar:", bg="#E7DBAA").grid(pady=5, row=2, column=0)
Label(miFrame, text="Texto (Remplazo):", bg="#E7DBAA").grid(pady=5, row=3, column=0)

rutaC = Entry(miFrame, width=40)
rutaC.grid(padx=5, row=1, column=1)
textoE = Entry(miFrame, width=40)
textoE.grid(padx=5, row=2, column=1)
textoR = Entry(miFrame, width=40)
textoR.grid(padx=5, row=3, column=1)

label_advertencia = Label(miFrame, text="", bg="#E7DBAA")
label_advertencia.grid(pady=5, row=4, column=0, columnspan=2)

Button(miFrame, text="Reemplazar Cadena", width=50, command=eliminar_cadena).grid(padx=10, pady=10, row=5, column=0, columnspan=2)

# ***** Seccion Agregar Cadenas a los Nombres ****
titulo2 = Label(miFrame, text="Agregar Frases a los Nombres", bg="#E7DBAA", font=tipografia_titulo)
titulo2.grid(pady=5, row=6, column=0, columnspan=2)

Label(miFrame, text="Texto a Agregar:", bg="#E7DBAA").grid(pady=5, row=7, column=0)
textoA = Entry(miFrame, width=40)
textoA.grid(padx=5, row=7, column=1)
# select
Label(miFrame, text="Posicion al Insertar:", bg="#E7DBAA").grid(pady=5, row=8, column=0)
variable_tk= StringVar(raiz) #crear una variable de tkinter para obtener el valor de la entrada
variable_tk.set("Inicio") # establecer un valor por defecto
lista_opciones = { 'Inicio','Fin'}
select = OptionMenu(miFrame, variable_tk, *lista_opciones)
select.grid(padx=5, row=8, column=1)
select.config(width=30)

label_advertencia2 = Label(miFrame, text="", bg="#E7DBAA")
label_advertencia2.grid(pady=5, row=9, column=0, columnspan=2)

Button(miFrame, text="Agregar Cadena", width=50, command=agregar_cadena).grid(padx=10, pady=10, row=10, column=0, columnspan=2)


# (Renderiza la ventana en bucle) se mantiene imprimiendo en pantalla el objeto raiz en espera a eventos
raiz.mainloop()