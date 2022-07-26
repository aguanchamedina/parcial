
import tkinter as tk
from tkinter import Canvas, messagebox

lista_datos=[]

def borrar():
    x1.set("")
    x2.set("")
    y1.set("")
    y2.set("")
    at_resultados.delete("1.0","end")
def salir():
    ventana_principal.destroy()

def graficar():
    frameCanvas= Canvas(width=250, height=250)
    frameCanvas.create_line(0,125,250,125)
    frameCanvas.create_line(125,0,125,250)
    frameCanvas.create_line(125+x1.get()*5,125-y1.get()*5,125+x2.get()*5,125-y2.get()*5,fill="red")
    frameCanvas.place(x=350,y=60)

    at_resultados.delete("1.0","end")
    at_resultados.insert(tk.INSERT, "")
    pass

def borrar_datos():
    lista_datos= []
    at_resultados.delete("1.0","end")
    at_resultados.insert(tk.INSERT, f"""\nDatos del usuario:
     {lista_datos}""")
    pass
def hallar():
    at_resultados.insert("1. x=" +str(x1.get()))
    at_resultados.insert("1. x=" +str(x1.get()))
    at_resultados.insert("1. x=" +str(x1.get()))
    at_resultados.insert("1. x=" +str(x1.get()))
    valor= (y1.get()-y2.get()) / (x1.get() - x2.get())
    at_resultados.insert("El valor de la pendiande es= y1 . y2/ x1 - x2 =" + valor)
    
    pass

ventana_principal = tk.Tk()
ventana_principal.title("GRAFICADOR")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")


# Frame de entrada de datos
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg="white", width=640, height=360)
frame_entrada.pack(fill=tk.BOTH)
# Frame para operaciones
frame_2 = tk.Frame(ventana_principal)
frame_2.config(bg="white", width=480, height=100)
frame_2.pack(fill=tk.BOTH)
frame_2.columnconfigure(0, weight=1)
frame_2.columnconfigure(1, weight=1)
frame_2.columnconfigure(2, weight=1)
frame_2.rowconfigure(0,weight=1)
# Frame para resultados
frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=100)
frame_resultados.pack(fill=tk.BOTH, padx=10,pady = 10 )
frame_resultados.columnconfigure(0, weight=1)
frame_resultados.columnconfigure(1, weight=1)
frame_resultados.rowconfigure(0,weight=1)
frame_resultados.rowconfigure(1,weight=1)

x1= tk.IntVar()
x2= tk.IntVar()
y1= tk.IntVar()
y2= tk.IntVar()


# Etiqueta de titulo
titulo = tk.Label(frame_entrada,text=" GRAFICADOR ")
titulo.config(bg="white", fg= "black" , font=("Berlin Sans FB Demi", 32))
titulo.place(x=45,y=20)
# Etiqueta x
label_x = tk.Label(frame_entrada, text="valor X:")
label_x.config(bg="white",fg="black", font=("Arial", 14))
label_x.place(x=45,y=80)

# Etiqueta y
label_dir = tk.Label(frame_entrada, text="Valor Y:")
label_dir.config(bg="white",fg="black", font=("Arial", 14))
label_dir.place(x=45,y=120)

# Etiqueta x
label_x = tk.Label(frame_entrada, text="valor X:")
label_x.config(bg="white",fg="black", font=("Arial", 14))
label_x.place(x=45,y=160)

# Etiqueta y
label_dir = tk.Label(frame_entrada, text="Valor Y:")
label_dir.config(bg="white",fg="black", font=("Arial", 14))
label_dir.place(x=45,y=200)

#etiqueta Info
label_info = tk.Label(frame_resultados, text="REGISTRO")
label_info.config(bg="white",fg="black", font=("Arial", 14))
label_info.grid(row=0,column=0)


# Caja de texto x
entry_x1 = tk.Entry(frame_entrada,textvariable=x1)
entry_x1.config(font=("Arial",),width=15)
entry_x1.focus_set()
entry_x1.place(x=145,y=83)

# Caja de texto y
entry_y1 = tk.Entry(frame_entrada,textvariable=y1)
entry_y1.config(font=("Arial",12), width=15)
entry_y1.focus_set()
entry_y1.place(x=145,y=123)

# Caja de texto x
entry_x2 = tk.Entry(frame_entrada,textvariable=x2)
entry_x2.config(font=("Arial",),width=15)
entry_x2.focus_set()
entry_x2.place(x=145,y=163)

# Caja de texto y
entry_y2 = tk.Entry(frame_entrada,textvariable=y2)
entry_y2.config(font=("Arial",12), width=15)
entry_y2.focus_set()
entry_y2.place(x=145,y=203)

#Boton guardar
boton_graficar = tk.Button(frame_2, text="Graficar", command=graficar, font=("Arial", 14))
boton_graficar.config(bg="red")
boton_graficar.place(x=45, y=20)
#Boton Pendiente
boton_borrar = tk.Button(frame_2, text="Pendiente",font=("Arial",14),command=hallar)
boton_borrar.config(bg="red")
boton_borrar.place(x=140, y=20)
# Boton borrar
boton_borrar = tk.Button(frame_2, text="Borrar",font=("Arial",14),command=borrar)
boton_borrar.config(bg="red")
boton_borrar.place(x=255, y=20)
# Boton salir
boton_salir = tk.Button(frame_2, text="Salir",command=salir,font=("Arial",22))
boton_salir.config(bg="red")
boton_salir.place(x=520, y=15)

# areas resultado 

at_resultados = tk.Text(frame_resultados, width=50, height=6)
at_resultados.grid(row=1, column=0)
sb_resultados = tk.Scrollbar(frame_resultados, command=at_resultados.yview)
sb_resultados.config(width=30)
sb_resultados.place(x=470, y=50)


ventana_principal.mainloop()