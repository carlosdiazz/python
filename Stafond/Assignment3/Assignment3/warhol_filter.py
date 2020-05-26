
from simpleimage import SimpleImage

def make_recolored(rojo,verde,azul,pixel):

    Red = pixel.red
    Green = pixel.green
    Blue = pixel.blue

    pixel.red=Red*rojo
    pixel.green=Green*verde
    pixel.blue=Blue*azul

def transformar(imagen,rojo,verde,azul):

    image = SimpleImage(imagen)
    for y in range(image.height):
        for x in range(image.width):
            pixel=image.get_pixel(x,y)
            make_recolored(rojo,verde,azul,pixel)

    return image


def unir(imagen,image):

    alto = image.height
    ancho = image.width

    foto_1 = transformar(imagen, 1.3, 0, 1.3)
    foto_2 = transformar(imagen, 0.5, 1, 0.5)
    foto_3 = transformar(imagen, 2, 2, 2)
    foto_4 = transformar(imagen, 1.5, 1.5, 0.5)
    foto_5 = transformar(imagen, 1, 1, 1)
    foto_6 = transformar(imagen, 0.4, 0.4, 1.7)

    completa = SimpleImage.blank(ancho * 3, alto * 2)

    for y in range(alto):
        for x in range(ancho):
            pixel = foto_1.get_pixel(x, y)
            completa.set_pixel(x, y, pixel)

            pixel = foto_2.get_pixel(x, y)
            completa.set_pixel(x + (ancho*1), y, pixel)

            pixel = foto_3.get_pixel(x, y)
            completa.set_pixel(x + (ancho*2), y, pixel)

            pixel = foto_4.get_pixel(x, y)
            completa.set_pixel(x, y + (alto*1), pixel)

            pixel = foto_5.get_pixel(x, y)
            completa.set_pixel(x + (ancho*1), y + (alto*1), pixel)

            pixel = foto_6.get_pixel(x, y)
            completa.set_pixel(x + (ancho*2), y + (alto*1), pixel)

    return completa

def main():

    imagen='images/simba-sq.jpg'
    image=SimpleImage(imagen)
    image.show()


    ok=unir(imagen,image)
    ok.show()

if __name__ == '__main__':
    main()