from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

# Creamos un indice global para que cada numero que pongamos este al lado del otro
i = 0

# Entrada de texto
e_texto = Entry(ventana, font = 'Calibri 20')
e_texto.grid(row = 0, column=0, columnspan= 4, padx = 5, pady = 5)

# Funcionalidad de los botones
def click_boton(valor):
    # Traemos la variable global
    global i
    # el primer parametro del insert es el indice donde queremos insertar el valor
    e_texto.insert(i, valor)
    # Aumentamos el indice global en 1 para que los numeros que vayamos ingresando se posicionen a la derecha del anterior puesto
    i += 1

def borrar():
    # Esto es para borrar en caso de apretar el boton borrar, desde el indice 0 hasta el final
    e_texto.delete(0, END)
    # Ahora reseteamos el indice 0
    i = 0

# Para las operaciones en si nos apoyamos de la funcion "eval" que viene en python
def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    borrar()
    e_texto.insert(0, resultado)


# Botones numericos
boton1 = Button(ventana, text = "1", width=5, height=2, command= lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width=5, height=2, command= lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width=5, height=2, command= lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width=5, height=2, command= lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width=5, height=2, command= lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width=5, height=2, command= lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width=5, height=2, command= lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width=5, height=2, command= lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width=5, height=2, command= lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width=13, height=2, command= lambda: click_boton(0))

# Botones especiales
boton_borrar = Button(ventana, text = "AC", width=5, height=2, command= lambda: borrar())
boton_parentesis1 = Button(ventana, text = "(", width=5, height=2, command= lambda: click_boton('('))
boton_parentesis2 = Button(ventana, text = ")", width=5, height=2, command= lambda: click_boton(')'))
boton_punto = Button(ventana, text = ".", width=5, height=2, command= lambda: click_boton('.'))

# Botones aritmeticos
boton_div = Button(ventana, text = "/", width=5, height=2, command= lambda: click_boton('/'))
boton_mult = Button(ventana, text = "*", width=5, height=2, command= lambda: click_boton('*'))
boton_sum = Button(ventana, text = "+", width=5, height=2, command= lambda: click_boton('+'))
boton_rest = Button(ventana, text = "-", width=5, height=2, command= lambda: click_boton('-'))
boton_igual = Button(ventana, text = "=", width=5, height=2, command= lambda: hacer_operacion())

# Posiicionar botones en la pantalla/interfaz
# Fila 1
boton_borrar.grid(row= 1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row= 1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row= 1, column=2, padx=5, pady=5)
boton_div.grid(row= 1, column=3, padx=5, pady=5)

# Fila 2
boton7.grid(row= 2, column=0, padx=5, pady=5)
boton8.grid(row= 2, column=1, padx=5, pady=5)
boton9.grid(row= 2, column=2, padx=5, pady=5)
boton_mult.grid(row= 2, column=3, padx=5, pady=5)

# Fila 3
boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)

# Fila 4
boton1.grid(row = 4, column=0, padx=5, pady=5)
boton2.grid(row = 4, column=1)
boton3.grid(row = 4, column=2, padx=5, pady=5)
boton_rest.grid(row = 4, column=3, padx=5, pady=5)

# Fila 5
boton0.grid(row = 5, column = 0, padx=5, pady=5, columnspan=2)
boton_punto.grid(row = 5, column = 2, padx=5, pady=5)
boton_igual.grid(row = 5, column = 3, padx=5, pady=5)







ventana.mainloop()