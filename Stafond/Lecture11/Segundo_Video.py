"""
Aqui voy a crear una animacion de una bola que rebota
"""

import tkinter, time

ancho_pantalla=800
alto_pantalla=600
tamano_ovalo=70

def main():
    canvas = make_canvas(ancho_pantalla, alto_pantalla, 'Mover Cuadrado')
    ovalo=canvas.create_oval(0,0,tamano_ovalo,tamano_ovalo, fill="red")

    cambio_x=3
    cambio_y=6

    while True:
        
        #Actualizar mundo
        canvas.move(ovalo,cambio_x,cambio_y)
        canvas.update()

        if si_golpea_y_abajo(canvas,ovalo) or si_golpea_y_arriba(canvas,ovalo):
            cambio_y = cambio_y * -1

        if si_golpea_x_izquierda(canvas,ovalo) or si_golpea_x_derecha(canvas,ovalo):
            cambio_x=cambio_x * -1

        # Pausa
        time.sleep(1/50) 

    canvas.mainloop()

#Funciones para saber si chocar
def si_golpea_y_abajo(canvas,ovalo):
    ball_top_y=obtener_izquierda_y_abajo(canvas,ovalo)
    return ball_top_y > alto_pantalla - tamano_ovalo

def si_golpea_y_arriba(canvas,ovalo):
    ball_top_y=obtener_izquierda_y_arriba(canvas,ovalo)
    return ball_top_y <= 0 + tamano_ovalo

def si_golpea_x_izquierda(canvas,ovalo):
    ball_top_y=obtener_x_izquierda(canvas,ovalo)
    return ball_top_y >= ancho_pantalla - tamano_ovalo

def si_golpea_x_derecha(canvas,ovalo):
    ball_top_y=obtener_x_derecha(canvas,ovalo)
    return ball_top_y <= 0 + tamano_ovalo

#Conocer Puntos
def obtener_x_izquierda(canvas,object):
    return canvas.coords(object)[0]

def obtener_x_derecha(canvas,object):
    return canvas.coords(object)[2]

def obtener_izquierda_y_abajo(canvas,object):
    return canvas.coords(object)[1]

def obtener_izquierda_y_arriba(canvas,object):
    return canvas.coords(object)[3]

#Funcion de Canvas
def make_canvas(width, height, title=None):
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  
    canvas.yview_scroll(8, 'units')  
    return canvas

if __name__ == '__main__':
    main()
