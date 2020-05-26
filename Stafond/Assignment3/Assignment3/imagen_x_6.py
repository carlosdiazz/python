
from simpleimage import SimpleImage



def main():

    imagen='images/simba.jpg'
    image=SimpleImage(imagen)
    image.show()

    alto=image.height
    ancho=image.width




    completa = SimpleImage.blank(ancho, alto)
    completa.show()

    for y in range(alto):
        for x in range(ancho):

            pixel = image.get_pixel(x,y)

            completa.set_pixel(x, y, pixel)



    completa.show()

if __name__ == '__main__':
    main()