"""
Aqui ene ste codigo,k solo dibuja un cuadrado en el centro y luego lo mueve a la mitad de pantalla

"""

import tkinter, time

ancho_pantalla=600
alto_pantalla=600
tamano_cuadro=50

def main():
    canvas = make_canvas(ancho_pantalla, alto_pantalla, 'Mover Cuadrado')
    inicio_y=ancho_pantalla/2 - tamano_cuadro/2
    final_y=inicio_y+tamano_cuadro
    cuadrado=canvas.create_rectangle(0,inicio_y,tamano_cuadro,final_y, fill="red")

    while este_cuadrado_esta_centrado(canvas,cuadrado):
        
        #Actualizar mundo
        canvas.move(cuadrado,1,0)
        canvas.update()

        # Pausa
        time.sleep(1/50) 

    canvas.mainloop()

def este_cuadrado_esta_centrado(canvas,cuadrado):
    antes_x=obtener_izquierda_x(canvas,cuadrado)
    max_x=ancho_pantalla/2 - tamano_cuadro/2
    print(antes_x,max_x)
    return antes_x <= max_x

def obtener_izquierda_x(canvas,object):
    return canvas.coords(object)[0]

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
