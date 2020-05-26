

from simpleimage import SimpleImage

def oscuro(archivo):

    image= SimpleImage(archivo)

    for pixel in image:
        pixel.red=pixel.red//2
        pixel.green=pixel.green//2
        pixel.blue=pixel.blue//2
    return  image

def canal_rojo(archivo):
    image = SimpleImage(archivo)
    for pixel in image:
        pixel.green=0
        pixel.blue=0
    return  image

def pantalla_roja(archivo,archivo2):
    inte = 1.6

    image = SimpleImage(archivo)
    back = SimpleImage(archivo2)
    for pixel in image:
        prome = (pixel.red + pixel.green + pixel.blue) // 3

        if pixel.red >= prome * inte:
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, back.get_pixel(x, y))
    return image

def imagen_doble():
    print(" ")

def espejo_image(imagen):

    image=SimpleImage(imagen)
    ancho=image.width
    alto=image.height

    espejo=SimpleImage.blank(ancho*2,alto)

    for y in range(alto):
        for x in range(ancho):
            pixel=image.get_pixel(x,y)
            espejo.set_pixel(x,y,pixel)
            espejo.set_pixel((ancho*2)-(x+1),y,pixel)

    return  espejo

def main():

    #espejo_normal=SimpleImage('images/ok.jpg')
    #espejo_normal.show()

    Mostrar_espejo=espejo_image('images/burrito.jpg')
    Mostrar_espejo.show()


    foto_original=SimpleImage('images/flower.png')
    foto_original.show()

    foto_oscura=oscuro('images/flower.png')
    foto_oscura.show()

    foto_Rojo=canal_rojo('images/flower.png')
    foto_Rojo.show()

    foto_ori=SimpleImage('images/stop.png')
    foto_ori.show()

    foto_ori2=SimpleImage('images/leaves.png')
    foto_ori2.show()

    foto_sinfondo=pantalla_roja('images/stop.png', 'images/leaves.png')
    foto_sinfondo.show()

if __name__ == '__main__':
    main()
