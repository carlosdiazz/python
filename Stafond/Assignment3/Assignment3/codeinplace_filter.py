
from simpleimage import SimpleImage


def cambiar_color(pixel):
    Red = pixel.red
    Green = pixel.green
    Blue = pixel.blue

    pixel.red=Red*1.5
    pixel.green=Green*0.7
    pixel.blue=Blue*1.5

def main():

    imagen=str(input("Ingrese el nombre de la imagen: "))
    imagen='images/'+imagen

    image = SimpleImage(imagen)
    image.show()

    for y in range(image.height):
        for x in range(image.width):
            pixel=image.get_pixel(x,y)
            cambiar_color(pixel)
    image.show()

if __name__ == '__main__':
    main()