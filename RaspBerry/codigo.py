#__universidad del Valle de Guatemala
#__HCI
#__Marcos Gutierrez
#__David Valenzuela
#__carlos Chew
#__Mario Sarmientos
#__Fernando Hengstenberg
#__maquina de latas


#__importamos la libreria tkinter
#__interfaz Grafica
from tkinter import *

#__variable de ejemplo para los codigos
ejemplo="4dgasff5asefdd5e5"



#__creamos la raiz
raiz=Tk()

#__titulo de la ventana
raiz.title("codigo")

#__no ose puede redimencionar la ventana
raiz.resizable(0,0)

#__figura del icono
raiz.iconbitmap("icono.ico")

#__tamanio de la ventana
raiz.geometry("700x500")

#__color de fondo
raiz.config(bg="white")

#__creamos el frame
frame=Frame()

#__empaquetamos el frame
frame.pack()

#__tamanio al frame
frame.config(width="700",height="500")

#__instrucciones de la ventana.
#__titulo
nombre =Label(frame,text="Tu codigo es:",fg="black", font=("Comic Sans MS",12)).place(x=30,y=50)


#__instrucciones de la ventana.
#__titulo
codigo =Label(frame,text=ejemplo,fg="forestgreen", font=("Comic Sans MS",50)).place(x=30,y=100)


#__informacion_parrafo
imformacion_parrafo=Label(frame,text="Gracias por ayudar a salvar nuestro planeta esperamos que regreses pronto.",fg="black", font=("Comic Sans MS",12),wraplength=700,anchor="center").place(x=25,y=230)


#__imagen de latas
imagen_latas=PhotoImage(file="latas.png")

#__lugar de imagen_latas
lblImagen2=Label(raiz,image=imagen_latas).place(x=330,y=350)




#__cargamos la primer imagen
imagen_reciclar=PhotoImage(file="reciclar.png")

#__lugar de la imagen_reciclar
lblImagen=Label (raiz,image=imagen_reciclar).place(x=0,y=350)


#__loop de la ventana
raiz.mainloop()
